'''
The purpose of this testmain.py file is to test cities to make sure they work properly in the webscrape
before putting them into the regular list of cities being used in the scrape.
'''
from flightscrape import scrape_city
from listofcities import test_city

dictionary = {}
visited = []
for city in test_city:
    print(city)
    if city in visited:
        continue
    visited.append(city)
    dictionary[city] = scrape_city('London,UK', city, test_city.index(city))

