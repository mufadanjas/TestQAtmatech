import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import pyautogui

# s = Service("C:\Program Files\chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_experimental_option("excludeSwitches", ["enable-logging"])
# op.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
# op.add_argument(
#     "user-data-dir=C:\\Users\\mufad\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
# browser = webdriver.Chrome(service=s, options=op)

browser = webdriver.Chrome(options=op)
browser.implicitly_wait(10)
browser.maximize_window()
browser.get("https://brand.netray.id/login?redirect=%2F")
time.sleep(5)

# User Mengisi Credential
browser.find_element(By.ID, "username").send_keys("fadli")
time.sleep(3)
browser.find_element(By.ID, "password").send_keys("password123")
time.sleep(3)
browser.find_element(By.ID, "loginButton").click()
time.sleep(5)

# Masuk ke halaman webnya dan Klik List Topik pada Banjir Jakarta
browser.find_element(
    By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div/div/ul').click()
time.sleep(5)

# Date and Sentiment Filter in Twitter Overview
pilih = Select(browser.find_element(
    By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/select'))
pilih.select_by_value("neutral")
time.sleep(5)
browser.find_element(
    By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/div/div[1]/a').click()
time.sleep(3)
browser.find_element(
    By.CSS_SELECTOR, "#datepickerQuickButtons > button:nth-child(5)").click()
time.sleep(5)
browser.execute_script("window.scrollTo(0, 1350)")
time.sleep(3)

# Click Function on Top Words in Twitter Overview
browser.find_element(
    By.CSS_SELECTOR, "#__layout > div > div > div.site-content > div > div > div:nth-child(4) > div:nth-child(2) > div > div > h5")
pyautogui.press('enter')
time.sleep(3)
browser.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[4]/div[2]/div/div/div/div/a[1]").click()
pyautogui.press('enter')
time.sleep(3)
browser.find_element(
    By.CSS_SELECTOR, "#viewWordCloudTweetModal___BV_modal_body_ > button").click()
time.sleep(2)

# Change Sentiment on Tweets List in Twitter Overview
browser.find_element(By.LINK_TEXT, "View all tweets").click()
time.sleep(3)
browser.find_element(
    By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/ol/li[1]/div[1]/div/header/div/input').click()
time.sleep(3)
browser.find_element(
    By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/ol/li[1]/div[1]/div/header/div/div/button').click()
time.sleep(3)
browser.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/ol/li[1]/div[1]/div/header/div/div/ul/li[1]/a").click()
time.sleep(3)
browser.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/ol/li[1]/div[2]/p[2]/button[1]").click()
time.sleep(3)

# Mark as Spam Function on Tweets List in Twitter Overview
browser.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[1]/button").click()
time.sleep(2)
browser.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[1]/ul/li[1]/a").click()
time.sleep(2)
browser.find_element(
    By.XPATH, '//*[@id="markAsSpamModal___BV_modal_footer_"]/button[2]').click()
time.sleep(2)
browser.back()

# Click Function on Top People
browser.execute_script("window.scrollTo(0, 1750)")
time.sleep(3)
browser.find_element(
    By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[4]/div[4]/div/div/div/div[1]/div[1]/p').click()
time.sleep(4)
browser.find_element(
    By.CSS_SELECTOR, "#viewEntityTweetModal___BV_modal_body_ > button").click()
time.sleep(2)

# Click Function on Top Organizations
browser.execute_script("window.scrollTo(0, 2200)")
time.sleep(3)
browser.find_element(
    By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[4]/div[5]/div/div/div/div[1]/div[1]/p').click()
time.sleep(4)
browser.find_element(
    By.CSS_SELECTOR, "#viewEntityTweetModal___BV_modal_body_ > button").click()
time.sleep(2)

# Click Function on Top Locations
browser.execute_script("window.scrollTo(0, 2600)")
time.sleep(3)
browser.find_element(
    By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[4]/div[8]/div/div/div/div[1]/div[1]/p').click()
time.sleep(4)
browser.find_element(
    By.CSS_SELECTOR, "#viewEntityTweetModal___BV_modal_body_ > button").click()
time.sleep(3)

# Click Function on Top Complaints
browser.find_element(
    By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[4]/div[7]/div/div/div/div[1]/div[1]/p').click()
time.sleep(4)
browser.find_element(
    By.CSS_SELECTOR, "#viewEntityTweetModal___BV_modal_body_ > button").click()
time.sleep(2)

# Logout dari WEB
browser.find_element(
    By.XPATH, '/html/body/div[1]/div/div/div/div[1]/header/nav/div[2]/button').click()
time.sleep(3)
browser.find_element(By.LINK_TEXT, "Logout").click()
time.sleep(3)
browser.quit()
print("Success")
