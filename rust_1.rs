use std::io;

fn main() {
    let mut guess = String::new();
    io::stdin().read_line(&mut guess).expect("Failed to read line!");
    let guess: u32 = guess.trim().parse().expect("Please type a number!");
}
