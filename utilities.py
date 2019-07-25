from selenium import webdriver
import requests

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

def testAllLinks(driver):
    linkArray = storeLinks(driver)

    for link in linkArray:
        
        response = requests.get(link)
        status = response.status_code
        category = "The request category is: "

        if status >= 100 and status < 200:
            print("Link: " + link)
            print("status code for this link: " + str(status))
            print(category + " Informational")
            print("No issues/n")

        if status >= 200 and status < 300:
            print("Link: " + link)
            print("status code for this link: " + str(status))
            print(category + " Successful")
            print("Request successfully received\n")

        if status >= 300 and status < 400:
            print("Link: " + link)
            print("status code for this link: " + str(status))
            print(category + " Redirection")
            print("Further action needed to navigate here\n")

        if status >= 400 and status < 500:
            print("Link: " + link)
            print("status code for this link: " + str(status))
            print(category + " Client Error")
            print("Broken Link\n")

        if status >= 500 and status < 600:
            print("Link: " + link)
            print("status code for this link: " + str(status))
            print(category + " Server Error")
            print("Broken Link\n")

# Prints all the links in the page
def printLinks(driver):
    links = driver.find_elements_by_xpath("//a[@href]")
    index = 0

    for link in links:
        index += 1

        print(link.get_attribute("href") + "\n")

    print("Number of links: " + str(index))

def getTitle(driver):
    return driver.title


