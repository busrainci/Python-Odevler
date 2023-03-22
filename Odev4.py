from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Odev4:
    def testEmptyLogin(self): 
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)

        usernameInput.send_keys()
        passwordInput.send_keys()
        sleep(2)

        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(2)

        loginBtn.click()
        sleep(2)

        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Test Sonucu : {testResult}")
        sleep(5)
    
    def testEmptyPassword(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)

        usernameInput.send_keys("b")
        passwordInput.send_keys()
        sleep(2)

        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(2)

        loginBtn.click()
        sleep(2)

        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Test Sonucu : {testResult}")
        sleep(5)

    def lockedOutUser(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)

        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce" )
        sleep(2)

        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(2)

        loginBtn.click()
        sleep(2)

        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out." 
        print(f"Test Sonucu : {testResult}")
        sleep(5)

    def x_ikonu(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)

        usernameInput.send_keys()
        passwordInput.send_keys()
        sleep(2)

        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)

        iconFind = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3 > button > svg > path")
        iconFind.click()
        sleep(3)

    def enterInventoryPage(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)

        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)

        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)

        invertoryList = driver.find_element(By.CLASS_NAME,"/inventory.html")
        print(f"Swag Labs da {len(invertoryList)}(6)adet ürün bulunmaktadır.")
        sleep(100)


        
       



Class = Odev4()
Class.testEmptyLogin()
Class.testEmptyPassword()
Class.lockedOutUser()
Class.x_ikonu()
Class.enterInventoryPage()
