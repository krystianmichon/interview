from selenium import webdriver


login = "krystian.michon90@gmail.com"
password = "oHeu6qo6WY"

driver = webdriver.Chrome(executable_path=r"C:\Users\Hiro\PycharmProjects\Test_interview\chromedriver\chromedriver.exe")
driver.implicitly_wait(10)
driver.get(r'https://www.rossmann.pl/')
driver.find_element_by_xpath("//span[contains(text(),'×')]").click()
accountCircle = driver.find_element_by_link_text("account_circle")
accountCircle.click()
loginInput = driver.find_element_by_xpath("//input[@name='login']")
loginInput.click()
loginInput.send_keys(login)
passwordInput = driver.find_element_by_xpath("(//input[@name='password'])[1]")
passwordInput.click()
passwordInput.send_keys(password)
logIn = driver.find_element_by_css_selector("button[class*='cart-step__btn-next']")
logIn.click()

title = driver.title
if ('Zaloguj się | Drogeria Rossmann.pl' == title):
    print("PASS")
else:
    print("FAIL")

driver.quit()
