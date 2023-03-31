#selenium : internette manuel olarak yaptığımız aram,tıkladığımız siteyi vs. selenium ile yapıyoruz.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com.tr/?hl=tr")
sleep(2)
input = driver.find_element(By.NAME,"q")
input.send_keys("Kodlama.io")
searchButton = driver.find_element(By.NAME,"btnK")
sleep(2)
searchButton.click()
sleep(2)
firstResult = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a")
firstResult.click()
sleep(2)
# lastResult = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[5]/div/div[1]/a/div/div[2]")
# lastResult.click()

# web scraping ve
# data scraping örneği olmuş oldu 
listOfcourses = driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlama.io sitesinde şu anda {len(listOfcourses)} adet kurs var")

# sleep(10) # 10 saniye uykuda kalsın sonra kapansın yani çalışan ekran 10 sn ye sonra kapanır.
# input() == kullanıcı kapatmadan çalışan ekran kapanmaması için
while True:  # sonsuz döngü oluşturduğumuz için çalışan ekran kapanmicak
    continue
# HTML LOCARTORS

# full xpath
# /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a

#xpath
# //*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a
