
require 'set'

def parse_input(file_name)
  beacons_per_scanner = []
  File.open(file_name, 'r') do |file|
    file.each_line do |line|
      if line.include?('scanner')
        beacons_per_scanner << []
      elsif line.include?(',')
        beacons_per_scanner.last << line.split(',').map(&:to_i)
      end
    end
  end
  beacons_per_scanner
end

def rotation_matrix(x, y, z)
  [
    [
      (Math.cos(x) * Math.cos(y)).to_i,
      (Math.cos(x) * Math.sin(y) * Math.sin(z) - Math.sin(x) * Math.cos(z)).to_i,
      (Math.cos(x) * Math.sin(y) * Math.cos(z) + Math.sin(x) * Math.sin(z)).to_i,
    ],
    [
      (Math.sin(x) * Math.cos(y)).to_i,
      (Math.sin(x) * Math.sin(y) * Math.sin(z) + Math.cos(x) * Math.cos(z)).to_i,
      (Math.sin(x) * Math.sin(y) * Math.cos(z) - Math.cos(x) * Math.sin(z)).to_i,
    ],
    [
      -Math.sin(y).to_i,
      (Math.cos(y) * Math.sin(z)).to_i,
      (Math.cos(y) * Math.cos(z)).to_i,
    ],
  ]
end

def rotation_matrices
  angles = [0, Math::PI / 2, Math::PI]
  angles.flat_map do |x|
    angles.flat_map do |y|
      angles.map do |z|
        rotation_matrix(x, y, z)
      end
    end
  end
end

def apply_matrix_to_vector(m, v)
  v.length.times.map do |i|
    v.length.times.sum do |j|
      m[i][j] * v[j]
    end
  end
end

def translate_matrix(m, v)
  m.map do |row|
    row.each_with_index.map do |entry, j|
      entry + v[j]
    end
  end
end

def get_squared_distances(m)
  result = []
  m.each_with_index do |p1, i|
    m.each_with_index do |p2, j|
      next if j >= i
      x1, y1, z1 = p1
      x2, y2, z2 = p2
      dist = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
      result << [p1, p2, dist]
      result << [p2, p1, dist]
    end
  end
  result.sort_by {|x| x[2]}
end

def offset_with_max_overlaps(scanners_a, scanners_b)
  dist_a = get_squared_distances(scanners_a)
  dist_b = get_squared_distances(scanners_b)
  i = 0
  j = 0
  return if (dist_a.map {|d| d[2]} & dist_b.map {|d| d[2]}).length < 12
  while i < dist_a.length && j < dist_b.length
    i += 1 if dist_a[i][2] < dist_b[j][2]
    j += 1 if dist_a[j][2] < dist_b[i][2]
    break unless (i < dist_a.length && j < dist_b.length)
    offset = [
      dist_a[j][0][0] - dist_b[i][0][0],
      dist_a[j][0][1] - dist_b[i][0][1],
      dist_a[j][0][2] - dist_b[i][0][2],
    ]
    m = translate_matrix(scanners_b, offset)
    if (m & scanners_a).length >= 12
      return scanners_a | m
    end
    i += 1
    j += 1
  end
end

def run(beacons_per_scanner)
  rotations = rotation_matrices

  # Run all above logic to coalesce a map for the 1st -> last scanner
  already_checked = Hash.new {|d, k| d[k] = Set.new}
  already_rotated = {}
  map = beacons_per_scanner[1..beacons_per_scanner.length-1]
  while map.length > 1
    map.each_with_index do |scanner_a, i|
      map.each_with_index do |scanner_b, j|
        if i < j && !already_checked[scanner_a]&.include?(scanner_b)
          found = false
          rotations.each do |rotation|
            next if found
            already_checked[scanner_a] << scanner_b
            already_checked[scanner_b] << scanner_a
            if !already_rotated[[scanner_b, rotation]]
              already_rotated[[scanner_b, rotation]] = scanner_b.map {|beacon| apply_matrix_to_vector(rotation, beacon)}
            end

            remapped_points = offset_with_max_overlaps(scanner_a, already_rotated[[scanner_b, rotation]])
            if remapped_points
              map.delete(scanner_a)
              map.delete(scanner_b)
              map << remapped_points
              found = true
            end
          end
        end
      end
    end
  end
  full_map = map[0]

  # Need one last loop to combine the 0th scanner with the results from the rest,
  # since we want to use the co-ordinate system of the 0th (so this is how we
  # guarantee we process the 0th scanner last)
  rotations.each do |rotation|
    scanner_rotated = full_map.map {|beacon| apply_matrix_to_vector(rotation, beacon)}
    remapped_points = offset_with_max_overlaps(beacons_per_scanner.first, scanner_rotated)
    if remapped_points
      full_map = remapped_points
    end
  end

  full_map
end

if $0 == __FILE__
  file_name = ARGV[0]
  beacons_per_scanner = parse_input(file_name)
  result = run(beacons_per_scanner)
  puts(result.length)
end
