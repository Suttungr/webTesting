from selenium import webdriver

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

    for link in links:
        print(link.get_attribute("href"))

def getTitle(driver):
    return driver.title


