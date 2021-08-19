import unittest
from selenium import webdriver


class OrganizzeSiteTestCase(unittest.TestCase):

    def test_access_organizze_site(self):

        driver = webdriver.Chrome()
        driver.get("http://www.organizze.com.br")
        assert "Controle financeiro pessoal online, fácil de usar e seguro." in driver.title
        driver.maximize_window()
        assert driver.find_element_by_class_name("fadeIn").text == "Controle suas finanças\nde forma fácil"
        driver.close()

    def test_creating_account(self):
        driver = webdriver.Chrome()
        driver.get("http://www.organizze.com.br")
        driver.maximize_window()
        driver.find_element_by_xpath("/html/body/main/header/div/div[2]/div[2]/a[2]").click()
        email_input = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[1]/input")
        password_input = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[2]/div[1]/input")
        password_confirm_input = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[2]/div[2]/input")
        terms_of_use = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[3]/div/input")
        submit_button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/button")
        email_input.send_keys("treinamentoft@ft.com")
        password_input.send_keys("123456")
        password_confirm_input.send_keys("123456")
        terms_of_use.click()
        submit_button.click()
        driver.implicitly_wait(5)
        success_message = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/h3")
        self.assertEqual(success_message, "Parabéns! O Organizze já está preparado para você!")
        driver.close()



if __name__ == "__main__":
    unittest.main()