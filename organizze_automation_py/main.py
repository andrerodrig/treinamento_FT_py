from selenium import webdriver


driver = webdriver.Chrome()
driver.get("http://www.organizze.com.br")
assert "Controle financeiro" in driver.title
driver.maximize_window()
assert driver.find_element_by_class_name("fadeIn").text == "Controle suas finanças\nde forma fácil"
driver.close()