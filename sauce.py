from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  # bekleme işlemlerini(sleep 5 yerine mesela) ele alan yapı
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from constants import globalConstants 

class Test_sauce:
    
    def test_invalid_login(self): # kişinin doğru giriş yapmadığın da kullanıcıya şu mesajı göster,kırmızı yapılması gibi hususlar yapılır.
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name"))) # en fazla 5 saniye olacak şekilde user-name id li elementin görünmesini bekle
        usernameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password")
        
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        
        loginBtn = self.driver.find_element(By.ID,"login-button")
        
        loginBtn.click()
        
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Test Sonucu : {testResult}")
        
    def test_valid_login(self):
        self.driver.get(globalConstants.URL)
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password")
        

        #Action Chains
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        # usernameInput.send_keys("standart_user")
        # passwordInput.send_keys("secret_sauce")
        loginBtn =self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(25)



testClass = Test_sauce()
testClass.test_invalid_login()
testClass.test_valid_login()

print()
