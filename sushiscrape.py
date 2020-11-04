from bs4.element import SoupStrainer
import requests
import urllib.request
import time
from bs4 import BeautifulSoup


def sushiRoll(name, ingredients):
    name
    ingredients

url = 'https://www.thrillist.com/eat/nation/fattest-sushi-rolls-sushi-rolls-by-calorie'
copy = open("/Users/alecjvaughn/Developer/py/sushi/fattest-sushi-rolls-sushi-rolls-by-calorie.html")

# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

soup = BeautifulSoup(copy, "html.parser")

divs = soup.find_all('div', class_='paragraph')
sushiTable = {} # <ingredient, rolls>
for div in divs:
    roll = div.find('h2')
    ingredients = div.find('em')
    if None in (roll, ingredients):
        continue
    mySushi = sushiRoll(roll, ingredients)
    for ingredient in ingredients:
        sushiTable[ingredient] = list.append(mySushi)
print(sushiTable)


