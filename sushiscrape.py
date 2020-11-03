import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://www.thrillist.com/eat/nation/fattest-sushi-rolls-sushi-rolls-by-calorie'
path = "/Users/alecjvaughn/Developer/py/sushi/fattest-sushi-rolls-sushi-rolls-by-calorie.json"

# response = requests.get(url)
response = requests.get(path)
print(response)

soup = BeautifulSoup(response.text, "html.parser")

divs = soup.find_all('div', class_='paragraph')
for div in divs:
    roll = div.find('h2')
    ingredients = div.find('em')
    # print(type(roll))
    # print(type(ingredients))
    if None in (roll, ingredients):
        continue
    print(roll)
    print(ingredients)


