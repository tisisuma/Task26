from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import Data.data
import Locators.locators


class imdb:
    def __init__(self, url):

        self.url = url

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def booting_function(self):
        try:
            self.driver.maximize_window()
            self.driver.get(Data.data.url)

            return True
        except:
            print("ERROR : Unable to run the code !")
            return False

    def shutdown(self):
        self.driver.quit()

    def search(self):
        self.driver.find_element(by=By.XPATH, value=Locators.locators.input_locator).send_keys(Data.data.moviename)
        self.driver.find_element(by=By.XPATH, value=Locators.locators.search_locator).click()


execute = imdb()
execute.booting_function()
execute.search()
execute.shutdown()
