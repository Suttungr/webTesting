from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


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

# Prints all the links in the page
def printLinks(driver):
    links = driver.find_elements_by_xpath("//a[@href]")

    for link in links:
        print(link.get_attribute("href"))

def testAllLinks(driver):
    links = driver.find_elements_by_xpath("//a[@href]")

    # Send HTTP request and read it
    
    # Check if the code is valid or broken

    # Loop through this

    pass

def getTitle(driver):
    return driver.title
