from selenium import webdriver


try:
    browser = webdriver.Chrome()
    browser.get("https://shimo.im/login?from=home")
    browser.find_element_by_xpath('//input[@type="text"]').send_keys("email@google.com")
    browser.find_element_by_xpath('//input[@type="password"]').send_keys("password")
    browser.find_element_by_xpath('//button[@type="black"]').click()
except Exception as e:
    print(e)
finally:
    browser.close()
