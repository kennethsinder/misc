import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Constants for term start-months, which are used by adm.uwaterloo
WINTER = 1
SPRING = WINTER + 4
FALL = SPRING + 4


def lookup_course_data(department, catalog_number, year, term):
    # so that year=2019,term=9 becomes sess='1199':
    sess = '1{}{}'.format(str(year)[-2:], term)

    BASE_URL = 'http://www.adm.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?level=under&sess={}&subject={}&cournum={}'
    url = BASE_URL.format(sess, department, catalog_number)
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_num_enrolled(department, catalog_number, year, term):
    soup = lookup_course_data(department, catalog_number, year, term)
    table_rows = soup.find_all('tr')
    # We'll choose the first "class type" (e.g. LEC) as the one over which
    # we want to sum enrollment counts.
    canonical_class_type = None
    enrolled_count = 0
    for row in table_rows:
        try:
            tds = row.find_all('td')
            class_type = tds[1].text.split(' ')[0]
        except:
            continue

        if class_type not in ['LEC', 'TUT', 'LAB', 'SEM']:
            continue
        if not canonical_class_type:
            canonical_class_type = class_type

        enrl_tot = int(tds[7].text)
        if class_type == canonical_class_type:
            enrolled_count += enrl_tot
    return enrolled_count


if __name__ == '__main__':
    CLASSES = [
        ('SE', 101, FALL, 2015, '1A'),
        ('SE', 102, WINTER, 2016, '1B'),
        ('SE', 201, FALL, 2016, '2A'),
        ('SE', 202, SPRING, 2017, '2B'),
        ('SE', 301, WINTER, 2018, '3A'),
        ('SE', 302, FALL, 2018, '3B'),
        ('SE', 401, SPRING, 2019, '4A'),
    ]
    num_enrolled = []
    for department, catalog_number, term, year, _ in CLASSES:
        num_enrolled.append(get_num_enrolled(
            department, catalog_number, year, term))
    plt.plot([x[-1] for x in CLASSES], num_enrolled)
    plt.title('Enrollment in SE Seminar vs. term')
    plt.show()
