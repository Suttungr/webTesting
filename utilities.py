from selenium import webdriver
import requests
from requests.exceptions import InvalidSchema

# Function that just gets the title of Chrome home page
def getChromeTitle():
    driverDict = getDriver()

    chromedriver = driverDict.get("chromedriver")

    driver = webdriver.Chrome(chromedriver)

    driver.get("https://google.com")

    title = driver.title
    print("The title is: " + title)

# Function that returns a dict for all executable drivers, see below
# Make sure to change your path based on your machine
def getDriver():
    chromePath = "C:\\Users\\vws2\Documents\\Testing\\WebDriver\\chromedriver.exe"
    firefoxPath = "C:\\Users\\vws2\Documents\\Testing\\WebDriver\\geckodriver.exe"
    operaPath = "C:\\Users\\vws2\Documents\\Testing\\WebDriver\\operdriver.exe"
    edgePath = "C:\\Users\\vws2\Documents\\Testing\\WebDriver\\msedgedriver.exe"

    driverDict = {
        "chromedriver": chromePath,
        "geckodriver": firefoxPath,
        "operadriver": operaPath,
        "edgedriver": edgePath
    }

    return driverDict

# Stores all links in the page as an array
def storeLinks(driver):
    links = driver.find_elements_by_xpath("//a[@href]")
    linkArray = []

    for link in links:
        indexLink = link.get_attribute("href")
        linkArray.append(indexLink)

    return linkArray  

# Prints all the links in the page
def printLinks(driver):
    links = driver.find_elements_by_xpath("//a[@href]")
    index = 0

    for link in links:
        index += 1

        print(link.get_attribute("href") + "\n")

    print("Number of links: " + str(index))

def testForGoodLinks(driver):
    allLinks = storeLinks(driver)
    linkNumber = 0

    for link in allLinks:
        try:
            response = requests.get(link)
            status = response.status_code

            if status >= 100 and status < 300:
                print("The link is: " + link)
                print("This link is okay")
                print("Actual status code is: " + str(status) + "\n\n")

        except InvalidSchema as schemaErr:
            print("link: " + link)
            print("This is either an email or a telephone, there is no HTTP status code\n\n")

def testAllLinks(driver):
    allLinks = storeLinks(driver)

    for link in allLinks:
        try:
            response = requests.get(link)

        except InvalidSchema as schemaErr:
            print("link: " + link)
            print("This is either an email or a telephone, there is no HTTP status code\n\n")

        else:
            status = response.status_code

            print("The link is: " + link)
            print("The status code is: " + str(status) + "\n")
