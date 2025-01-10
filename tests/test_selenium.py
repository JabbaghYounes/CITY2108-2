from selenium import webdriver
from selenium.webdriver.common.by import By

def test_gui_simulation():
    driver = webdriver.Chrome()  # Ensure you have the Chrome WebDriver installed
    driver.get("file:///path/to/your/index.html")  # Use a test version of the application

    simulate_access_button = driver.find_element(By.ID, "simulateAccess")
    simulate_access_button.click()

    assert "Simulate Access" in driver.page_source, "Simulate Access window should open"

    driver.quit()
