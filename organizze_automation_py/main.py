import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from properties import *

class OrganizzeSiteTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get(URL)
        self.driver.maximize_window()


    def test_access_organizze_site(self):
        
        assert TITLE in self.driver.title
        assert self.driver.find_element_by_class_name("fadeIn").text == "Controle suas finanças\nde forma fácil"

    def test_creating_account(self):
        self.driver.find_element_by_xpath("//a[contains(text(), 'Comece já')]").click()
        email_input = self.driver.find_element_by_id("email")
        password_input = self.driver.find_element_by_id("password")
        password_confirm_input = self.driver.find_element_by_id("passwordConfirmation")
        terms_of_use = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[3]/div/input")
        submit_button = self.driver.find_element_by_xpath("//button[text()='Começar a usar']")
        email_input.send_keys(EMAIL)
        password_input.send_keys(PASSWORD)
        password_confirm_input.send_keys(PASSWORD)
        terms_of_use.click()
        submit_button.click()
        try:
            success_message = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, "//h3[@class='signup__status-title mb-3']"))
            )
        finally:
            # success_message = driver.find_element_by_xpath("//h3[@class='signup__status-title mb-3']").text
            assert success_message.text == SUCCESS_MESSAGE

    def tearDown(self) -> None:
        self.driver.close()
        



if __name__ == "__main__":
    unittest.main()