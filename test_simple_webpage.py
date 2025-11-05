from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

def result_message(test_name, passed, error_msg=""):
    if passed:
        print(f"✅ PASS: {test_name}")
    else:
        print(f"❌ FAIL: {test_name} -- {error_msg}")

# ✅ Setup ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(r"file:///C:\Users\arjun\OneDrive\Desktop\stqa mini project\index.html")
driver.maximize_window()

# Give time for manual interaction
print("\n⚙️ Webpage opened. You can interact now.")
print("👉 Click, hover, or change elements. Tests will start in 15 seconds...\n")
time.sleep(15)

actions = ActionChains(driver)

# ✅ Test 1: Check main heading text
try:
    heading = driver.find_element(By.ID, "main-title")
    assert heading.text == "Hello, World!"
    result_message("Heading text is correct", True)
except Exception as e:
    result_message("Heading text is correct", False, str(e))

# ✅ Test 2: Check first button exists
try:
    button = driver.find_element(By.ID, "myButton")
    result_message("Button (Click Me) exists", True)
except Exception as e:
    result_message("Button (Click Me) exists", False, str(e))

# ✅ Test 3: Verify user clicked button (text change)
try:
    result = driver.find_element(By.ID, "result")
    assert result.text == "Button Clicked!"
    result_message("Button click registered correctly", True)
except Exception as e:
    result_message("Button click registered correctly", False, str(e))

# ✅ Test 4: Check hover button exists
try:
    hover_button = driver.find_element(By.ID, "hoverButton")
    result_message("Hover button exists", True)
except Exception as e:
    result_message("Hover button exists", False, str(e))

# ✅ Test 5: Detect hover text change
try:
    hover_result = driver.find_element(By.ID, "hover-result")
    assert hover_result.text == "Hover Detected!"
    result_message("Hover detected successfully", True)
except Exception as e:
    result_message("Hover detected successfully", False, str(e))

# ✅ Test 6: Check hover button color change
try:
    hover_button = driver.find_element(By.ID, "hoverButton")
    actions.move_to_element(hover_button).perform()
    time.sleep(1)
    color = hover_button.value_of_css_property("background-color")
    print("Detected color:", color)
    assert "255, 255, 0" in color or "144, 238, 144" in color
    result_message("Hover color changed correctly", True)
except Exception as e:
    result_message("Hover color changed correctly", False, str(e))

# ✅ Test 7: Verify page title
try:
    assert driver.title == "Simple Web Page"
    result_message("Page title is correct", True)
except Exception as e:
    result_message("Page title is correct", False, str(e))

# ✅ Test 8: Check if body font family is applied correctly
try:
    body = driver.find_element(By.TAG_NAME, "body")
    font = body.value_of_css_property("font-family").lower()
    assert "arial" in font
    result_message("Font family (Arial) is applied correctly", True)
except Exception as e:
    result_message("Font family (Arial) is applied correctly", False, str(e))

# ✅ Test 9: Check both buttons alignment (rough visual logic)
try:
    btn1 = driver.find_element(By.ID, "myButton").location['y']
    btn2 = driver.find_element(By.ID, "hoverButton").location['y']
    diff = abs(btn1 - btn2)
    assert diff < 50  # within same row approximately
    result_message("Buttons are aligned properly", True)
except Exception as e:
    result_message("Buttons are aligned properly", False, str(e))

# ✅ Test 10: Ensure paragraphs (<p>) are visible and readable
try:
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    assert len(paragraphs) >= 2
    for p in paragraphs:
        assert p.is_displayed()
    result_message("Paragraphs are visible and present", True)
except Exception as e:
    result_message("Paragraphs are visible and present", False, str(e))

print("\n🧾 All tests executed successfully!")
driver.quit()
