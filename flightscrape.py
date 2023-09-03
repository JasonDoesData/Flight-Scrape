from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

hasAccepted = False


def scrape_city(start, destination, count):

    start_index = start.index(',')
    destination_index = destination.index(',')

    start_city = start[:start_index]
    start_country = start[start_index+1:]

    destination_city = destination[:destination_index]
    destination_country = destination[destination_index+2:]

    driver.get(f"https://www.google.com/search?q={start_city}+{start_country}+to+"
               f"{destination_city}+{destination_country}+flights")

    time.sleep(3)
    if count == 0:
        accept = driver.find_element(By.ID, "L2AGLb")
        accept.click()

    time.sleep(5)
    element = driver.find_element(By.XPATH, "//span[contains(., 'Show flights')]")
    element.click()
    time.sleep(3)
    set_date = driver.find_element(By.CLASS_NAME, 'oSuIZ.YICvqf.kStSsc.ieVaIb')
    set_date.click()
    time.sleep(3)
    reset_click = driver.find_element(By.XPATH, "//span[contains(., 'Reset')]")
    reset_click.click()
    time.sleep(5)
    by_week = driver.find_elements(By.CLASS_NAME, 'WhDFk.Io4vne')
    time.sleep(3)

    months = ['September', 'October', 'November', 'December', 'January', 'February',
              'March', 'April', 'May', 'June', 'July', 'August']
    count = -1
    cities_return = []
    for day in by_week:
        daynum = day.find_element(By.CLASS_NAME, 'eoY5cb.CylAxb.sLG56c.yCya5')
        day_of_month = int(daynum.get_attribute("innerText").strip())
        if day_of_month == 1:
            count += 1
            month = months[count]
        else:
            month = months[count]
        price = day.find_element(By.CLASS_NAME, 'CylAxb.n3qw7.UNMzKf.julK3b')
        if len(price.get_attribute("innerText")[1:]) > 0:
            price_for_day = int(price.get_attribute("innerText")[1:].replace(',', ''))
        else:
            price_for_day = price.get_attribute("innerText")

        if price_for_day:
            print(f'{destination_city} {month} {day_of_month} {price_for_day}')
            cities_return.append([destination_city, destination_country, month, day_of_month, price_for_day])

    return cities_return
