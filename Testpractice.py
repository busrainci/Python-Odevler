from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date
timeout=5


class Test_practiceClass:

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        sleep(5)
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        sleep(5)
 


    def teardown_method(self):
        self.driver.quit()
    def waitForElementVisible(self,locator,timeout):
        WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located(locator))
          
    @pytest.mark.skip()
    def test_EmptyLogin(self):
        self.waitForElementVisible((By.ID,"user-name"),5)
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"),5)
        passwordInput = self.driver.find_element(By.ID,"password")

        usernameInput.send_keys()
        passwordInput.send_keys()
        
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click() 
        
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath} /test-EmptyLogin.png")  
        assert errorMessage.text == "Epic sadface: Username is required"

    
   
    @pytest.mark.skip()
    def test_EmptyPassword(self):
        self.waitForElementVisible((By.ID,"user-name"),5)
        # WebDriverWait (self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))  
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"),5)
        # WebDriverWait (self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password")
        
        usernameInput.send_keys("b")
        passwordInput.send_keys(" ")
        
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-EmptyPassword-{usernameInput}.png")
        assert errorMessage.text == "Epic sadface: Password is required"

    # @pytest.mark.skip()
    def test_lockedOutUser(self):
        self.waitForElementVisible((By.ID,"user-name"),3)
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"),2)
        passwordInput = self.driver.find_element(By.ID,"password")

        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce" )
       
        loginBtn = self.driver.find_element(By.ID,"login-button")

        loginBtn.click()  

        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-lockedOutUser-{usernameInput}-{passwordInput}.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out." 

    @pytest.mark.skip()
    def test_x_ikonu(self):
        self.waitForElementVisible((By.ID,"user-name"),3)
        usernameInput = self.driver.find_element(By.ID,"user-name")
        
        self.waitForElementVisible((By.ID,"password"),2)
        passwordInput = self.driver.find_element(By.ID,"password") 
        
        usernameInput.send_keys()
        passwordInput.send_keys()
    
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        iconFind = self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3 > button > svg > path")
        self.driver.save_screenshot(f"{self.folderPath}/test-x-ikonu.png")
        iconFind.click()
    @pytest.mark.skip()
    def test_enterInventoryPage(self):
        self.waitForElementVisible((By.ID,"user-name"),3)
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"),2)
        passwordInput = self.driver.find_element(By.ID,"password")
        sleep(5)

        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce") 
        sleep(5)
      
        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(5)
        self.driver.save_screenshot(f"{self.folderPath}/test-enterInventoryPage-{usernameInput}-{passwordInput}.png")       
        loginBtn.click()
        sleep(5)

        invertoryList = self.driver.find_element(By.CLASS_NAME,"/inventory.html")
        print(f"Swag Labs da {len(invertoryList)}(6)adet ürün bulunmaktadır.")
        
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        sleep(5)
        
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(20)
    
    # # @pytest.mark.skip()
    # @pytest.mark.parametrize("firstname,lastname,postalcode",[("yaser","Ulutürk","55000"),("Büşra","İnci","22000")])

    def test_payment_information(self):

        self.waitForElementVisible((By.ID,"user-name"),3)
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"),2)
        passwordInput = self.driver.find_element(By.ID,"password")
        sleep(5)

        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce") 
        sleep(5)
      
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(5)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        productBtn = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        productBtn.click()
        sleep(5)


        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"shopping_cart_container")))
        shoppingBtn = self.driver.find_element((By.XPATH,"shopping_cart_container"))
        shoppingBtn.click()
        sleep(5)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"checkout")))
        checkoutBtn = self.driver.find_element(By.ID,"checkout")
        checkoutBtn.click()
        sleep(5)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(By.ID,"first-name"))
        firstName = self.driver.find_element((By.ID,"first-name"))
        lastName = self.driver.find_element(By.ID,"last-name")
        postalCode = self.driver.find_element(By.ID,"postal-code")
        continueBtn = self.driver.find_element(By.ID,"continue")

        firstName.send_keys("Büşra")
        lastName.send_keys("İnci")
        postalCode.send_keys("34000")
        continueBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[4]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-payment-information.png")
        assert errorMessage.text == "Error: First Name is required"
        
        # self.driver.save_screenshot(f"{self.folderPath}/test-payment-information{firstnameInput}-{lastnameInput}-{postalcodeInput}.png")
        

    




        
    
    


   
    
     


        
        
        


