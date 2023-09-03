from flightscrape import scrape_city
from listofcities import popular_cities
import pandas as pd
import json
import time

dictionary = {}
visited = []
for city in popular_cities:
    print(city)
    if city in visited:
        continue
    visited.append(city)
    dictionary[city] = scrape_city('London,UK', city, popular_cities.index(city))

with open("flightprices3.json", "w") as outfile:
    json.dump(dictionary, outfile)

time.sleep(10)

jsonfile = open(r'C:\Users\mjasb\PycharmProjects\FlightScrape\flightprices3.json')
flights = json.load(jsonfile)

flights_df = pd.DataFrame(columns=['City', 'Country', 'Month', 'Day', 'Price'])

for key in flights:
    for index in range(len(flights[key])):
        city = flights[key][index][0]
        country = flights[key][index][1]
        month = flights[key][index][2]
        day = flights[key][index][3]
        price = flights[key][index][4]
        details = [city, country, month, day, price]
        flights_df.loc[len(flights_df)] = details

flights_df.to_excel("flightprices3.xlsx",
             sheet_name='flights')


