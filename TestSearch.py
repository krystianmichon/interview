from selenium import webdriver
import random
import string



driver = webdriver.Chrome(executable_path=r"C:\Users\Hiro\PycharmProjects\Test_interview\chromedriver\chromedriver.exe")
driver.implicitly_wait(15)
driver.get(r'https://www.rossmann.pl/')
driver.maximize_window()
driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]").click()
search = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/header[1]/section[1]/div[3]/div[1]/input[1]")
search.click()
search.send_keys(random.choice(string.ascii_uppercase+string.digits)*10)
searchButton = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/header[1]/section[1]/div[3]/div[1]/button[1]/i[1]")
searchButton.click()
if driver.find_element_by_xpath("//div[@class='col-12 text-center']").is_displayed():
    print('PASS')
else:
    print("FAIL")


driver.quit()
