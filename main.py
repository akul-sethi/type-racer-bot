from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time




website = input("Enter challange link: ")

# https://play.typeracer.com?rt=11atn1uvp1
service = Service(executable_path="/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get(website)
driver.implicitly_wait(1)

button = driver.find_element(By.XPATH, "//*[contains(text(), 'Join race')]")
button.click()
start = time.time()

input_panel = driver.find_element(By.CLASS_NAME, "inputPanel")
tbody = input_panel.find_element(By.TAG_NAME, "tbody")
field = tbody.find_element(By.CLASS_NAME, "txtInput")


while field.get_attribute("disabled"):
    time.sleep(0.03)

field.click()

table = tbody.find_elements(By.TAG_NAME, "tr")[0].find_element(By.TAG_NAME, "td").find_element(By.TAG_NAME, "table")
tbody = table.find_element(By.TAG_NAME, "tbody")
div = tbody.find_element(By.TAG_NAME, "tr").find_element(By.TAG_NAME, "td").find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, "div")

text = ""
spans = div.find_elements(By.TAG_NAME, "span")

for span in spans:
    text += span.get_attribute("innerText")

for letter in text:
    try:
        field.send_keys(letter)
        time.sleep(0.03)
    except:
        end = time.time()
        print(letter)
        print(len(text.split(" ")) / ((end - start) / 60))


time.sleep(120)
    



