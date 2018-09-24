import requests
from bs4 import BeautifulSoup

quote_page = 'https://idebate.org/debatabase/culture-media/should-airbrushing-womens-bodies-be-banned'
page = requests.get(quote_page).text

output = open('output.csv', 'w')

soup = BeautifulSoup(page, 'html.parser')
points_for = soup.find('div', {'id': 'debatabase-points-1'})
points_for = points_for.find('div', {'class': 'field-items'})
all_points = points_for.find_all('div', {'class': 'field-item'})
for point in all_points:
    text = point.find('div', {'class': 'field-item'})
    if text is not None:
        print(text.get_text())
        output.write('pro,' + text.get_text() + '\n')

points_against = soup.find('div', {'id': 'debatabase-points-2'})
points_against = points_against.find('div', {'class': 'field-items'})
all_points = points_against.find_all('div', {'class': 'field-item'})
for point in all_points:
    text = point.find('div', {'class': 'field-item'})
    if text is not None:
        print(text.get_text())
        output.write('con,' + text.get_text() + '\n')

output.close()

