from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

import Data.data
import Locators.locators


class Test_imdb:

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        yield
        self.driver.close()

    def test_imdb(self, booting_function):
        try:
            self.driver.get(Data.data.url)
            self.driver.implicitly_wait(30)
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, Locators.locators.dropdown)))
            element.click()
            self.driver.find_element(by=By.XPATH, value=Locators.locators.dropdownvalues_locator).click()
            self.driver.find_element(by=By.XPATH, value=Locators.locators.input_locator).send_keys(Data.data.moviename)
            self.driver.find_element(by=By.XPATH, value=Locators.locators.search_locator).click()
        except NoSuchElementException as e:
            print("Error : ", e)
