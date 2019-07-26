from selenium import webdriver
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
    testURL = "https://google.com/"

    driver.get(testURL)

    getAllGoodLinks(driver)
    getAllRedirects(driver)
    getAllBrokenLinks(driver)

    # Closes the browser window
    driver.close()
