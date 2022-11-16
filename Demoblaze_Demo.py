import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

src = Service(r"C:\Users\user\PycharmProjects\pythonProject\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=src)
mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception])
driver.get("https://demoblaze.com/index.html")
#Phone
phone = mywait.until(EC.presence_of_element_located((By.XPATH,"//div[@id='contcont']//a[2]")))
phone.click()
Mobile = mywait.until(EC.presence_of_element_located((By.XPATH,'//a[text()="Samsung galaxy s6"]')))
Mobile.click()
addtocart = mywait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='Add to cart']")))
addtocart.click()
time.sleep(2)
alt=driver.switch_to.alert
alt_text=alt.text
print("Alert text is:",alt_text)
alt.accept()

home = driver.find_element(By.XPATH,"(//a[@class='nav-link'])[1]")
home.click()
#Laptop
laptop = driver.find_element(By.XPATH,'//a[text()="Laptops"]')
laptop.click()
dell = mywait.until(EC.presence_of_element_located((By.LINK_TEXT,"Dell i7 8gb")))
dell.click()
addtocart1 = mywait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='Add to cart']")))
addtocart1.click()
time.sleep(2)
alt1=driver.switch_to.alert
alt1.accept()

home1 = driver.find_element(By.XPATH,"(//a[@class='nav-link'])[1]")
home1.click()
#Monitor
monitor = mywait.until(EC.presence_of_element_located((By.LINK_TEXT,"Monitors")))
monitor.click()
asus = mywait.until(EC.presence_of_element_located((By.LINK_TEXT,"ASUS Full HD")))
asus.click()
addtocart2 = mywait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='Add to cart']")))
addtocart2.click()
time.sleep(2)
alt2=driver.switch_to.alert
alt2.accept()

cart = mywait.until(EC.presence_of_element_located((By.XPATH,"//a[@id='cartur']")))
cart.click()
Product_prices = []
#Cart Details
dellprice = mywait.until(EC.presence_of_element_located((By.XPATH,"//table[@class='table table-bordered table-hover table-striped']//tr[1]//td[3]"))).text
print("Dell price is:",dellprice)
DP = int(dellprice)
print(type(DP))
Product_prices.append(DP)
Mob_price = mywait.until(EC.presence_of_element_located((By.XPATH,"//table[@class='table table-bordered table-hover table-striped']//tr[2]//td[3]"))).text
print("Mobile price is:",Mob_price)
MP = int(Mob_price)
print(type(MP))
Product_prices.append(MP)
AsusPrice = mywait.until(EC.presence_of_element_located((By.XPATH,"//table[@class='table table-bordered table-hover table-striped']//tr[3]//td[3]"))).text
print("Asus price is:",AsusPrice)
AP = int(AsusPrice)
print(type(AP))
Product_prices.append(AP)
print("Product_prices is :", Product_prices)
Totalcost = mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()=1290]"))).text
print("Total cost is:",Totalcost)
TC = int(Totalcost)
print(type(TC))
time.sleep(3)
print("Product_prices after sort :", Product_prices.sort())

# Sum of product prices

Total_Sum = 0
for i in Product_prices:
    Total_Sum = Total_Sum+i
print("Total sum of prices is :",Total_Sum)

# Compare both prices
if TC == Total_Sum:
    print("Both Amount matched perfectly...")
else:
    print("Both amount does not matched...")

# Place order

placeOrder = mywait.until(EC.presence_of_element_located((By.XPATH,'//button[text()="Place Order"]')))
placeOrder.click()
time.sleep(1)
#FORM
name = mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='name']")))
name.send_keys("ABCD")
country = mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='country']")))
country.send_keys("india")
city = mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='city']")))
city.send_keys("pune")
card = mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='card']")))
card.send_keys("123456789")
month = mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='month']")))
month.send_keys("2704")
year = mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='year']")))
year.send_keys("2022")
driver.save_screenshot(r"C:\Users\user\PycharmProjects\pythonProject\Practice2\img1.png")
purchase = mywait.until(EC.presence_of_element_located((By.XPATH,'//button[text()="Purchase"]')))
purchase.click()
time.sleep(2)
#popup
id = mywait.until(EC.presence_of_element_located((By.XPATH,"//p[contains(@class,'lead text-muted')]"))).text
print(" Order ID is:",id)
driver.save_screenshot(r"C:\Users\user\PycharmProjects\pythonProject\Practice2\img2.png")
driver.close()




