import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
time.sleep(3)


driver.get("https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
driver.maximize_window()
time.sleep(5)

text_locator = driver.find_element(
    "xpath",
    "//h1[contains(normalize-space(), 'Dropdown Menu(s), Checkboxe(s) & Radio Button(s)')]"
)
actual_welcome_text = text_locator.text
print("------------------------>" + actual_welcome_text)

expected_text = "Dropdown Menu(s), Checkboxe(s) & Radio Button(s)"

# Normalize whitespace (replace multiple spaces/newlines with a single space)
def normalize(text):
    return re.sub(r'\s+', ' ', text).strip()

print(f"Actual text: {actual_welcome_text}")
assert normalize(actual_welcome_text) == normalize(expected_text), \
    f"Expected '{expected_text}', but got '{actual_welcome_text}'"

dropdown1_locator = driver.find_element(By.ID, "dropdown-menu-1")
dropdown1_locator.is_selected[1]

dropdown2_locator = driver.find_element(By.ID, "dropdown-menu-2")
dropdown2_locator.is_selected[1]

assert dropdown1_locator.is_selected[1], "Option 1 is not selected in dropdown 1"
assert dropdown2_locator.is_selected[2], "Option 1 is not selected in dropdown 2"


time.sleep(5)