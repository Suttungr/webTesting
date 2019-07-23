from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def main():
    chromedriver = "C:\\Users\\vws2\Documents\\Testing\\WebDriver\\chromedriver.exe"

    driver = webdriver.Chrome(chromedriver)

    driver.get("https://google.com")
    
    title = driver.title
    print("The title is: " + title)

if __name__ == "__main__":
    main()
