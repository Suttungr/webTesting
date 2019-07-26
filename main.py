from selenium import webdriver
import requests
from utilities import *

if __name__ == "__main__":
    driverDict = getDriver()

    chromedriver = driverDict.get("chromedriver")
    firefoxdriver = driverDict.get("geckodriver")
    edgedriver = driverDict.get("edgedriver")
    operadriver = driverDict.get("operadriver")

    # Change "Chrome" and "chromedriver" to respective browser when testing other than Chrome
    driver = webdriver.Chrome(chromedriver)

    # The URL to test
    testURL = "https://www.cefns.nau.edu/capstone/projects/CS/2019/GitOSSum-S19/index.html"

    driver.get(testURL)

    testForRedirects(driver)

    # Closes the browser window
    driver.close()
