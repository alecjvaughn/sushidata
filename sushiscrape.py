import requests
from bs4 import BeautifulSoup
import re
import sys

class sushiRoll:

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.name}: {self.ingredients}"

url = 'https://www.thrillist.com/eat/nation/fattest-sushi-rolls-sushi-rolls-by-calorie'
copy = open("/Users/alecjvaughn/Developer/py/sushi/fattest-sushi-rolls-sushi-rolls-by-calorie.html")

# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

soup = BeautifulSoup(copy, "html.parser")

divs = soup.find_all('div', class_='paragraph')
sushiTable = {}
for div in divs:
    roll = div.find('h2')
    ingredients = div.find('em')
    if None in (roll, ingredients):
        continue
    mySushi = sushiRoll(roll.text, ingredients.text.split(","))
    for ingredient in ingredients.text.split(","):
        if ingredient not in sushiTable:
            sushiList = [str(mySushi.name)]
            sushiTable[ingredient] = sushiList
        else:
            sushiTable[ingredient].append(str(mySushi.name))
myFile = open('mySushiData.txt', 'w')
for key in sushiTable:
    myFile.writelines(f"{key}: {sushiTable[key]}\n\n")
print(sys.exit)


