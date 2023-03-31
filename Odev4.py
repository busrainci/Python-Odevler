from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.common.action_chains import ActionChains

class Odev4:
    def __init__(self):
         self.driver = webdriver.Chrome(ChromeDriverManager().install())
         self.driver.maximize_window()
         self.driver.get("https://www.saucedemo.com/")
         sleep(10)
    
    def testEmptyLogin(self): 
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        sleep(4)
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password")
        sleep(4)

        usernameInput.send_keys()
        passwordInput.send_keys()
        
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click() 
        sleep(4)

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Test Sonucu : {testResult}")
        
    
    def testEmptyPassword(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password")
        
        usernameInput.send_keys("b")
        passwordInput.send_keys()
        
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Test Sonucu : {testResult}")
        

    def lockedOutUser(self):
        WebDriverWait (self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password")

        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce" )
       
        loginBtn = self.driver.find_element(By.ID,"login-button")

        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out." 
        print(f"Test Sonucu : {testResult}")
        

    def x_ikonu(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        sleep(4)
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password") 
        sleep(4)
        usernameInput.send_keys()
        passwordInput.send_keys()
    
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        iconFind = self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3 > button > svg > path")
        iconFind.click()
        
    def enterInventoryPage(self):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password")
        sleep(2)
       

        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce") 
      

        loginBtn = self.driver.find_element(By.ID,"login-button")
        
        loginBtn.click()
        sleep(2)
     

        invertoryList = self.driver.find_element(By.CLASS_NAME,"/inventory.html")
        print(f"Swag Labs da {len(invertoryList)}(6)adet ürün bulunmaktadır.")
        
        

        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        sleep(5)
        

        # usernameInput.send_keys("standard_user")
        # passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(20)
        
        


        
       



Class = Odev4()
Class.testEmptyLogin()
Class.testEmptyPassword()
Class.lockedOutUser()
Class.x_ikonu()
Class.enterInventoryPage()
