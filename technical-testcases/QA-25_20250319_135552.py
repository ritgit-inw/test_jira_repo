""" 
Title: Technical Test Case for Google Authentication Login
Environment Variables: N/A
Notes: This test case automates the login process using Google authentication and checks for successful login and error messages.
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run headless Chrome
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Navigate to the login page
    try:
        driver.get('https://your-app-login-url.com')  # Replace with the actual login URL
        print("Navigated to login page.")
    except Exception as e:
        print(f"Failed to navigate to login page: {e}")

    # Step 2: Click on 'Login with Google'
    try:
        google_login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Login with Google"]'))
        )
        google_login_button.click()
        print("Clicked on 'Login with Google' button.")
    except Exception as e:
        print(f"Failed to click 'Login with Google': {e}")

    # Step 3: Wait for the Google authentication page to load
    time.sleep(5)  # Adjust sleep time as necessary

    # Step 4: Check if redirected to Google authentication page
    try:
        assert "Google" in driver.title, "Not redirected to Google authentication page"
        print("Successfully redirected to Google authentication page.")
    except AssertionError as e:
        print(e)

    # Step 5: Simulate successful authentication (this part will depend on your testing setup)
    # You may need to fill in the email and password fields here

    # Step 6: Check if logged into the app
    time.sleep(5)  # Wait for the app to log in
    try:
        assert "Welcome" in driver.page_source, "User not logged in"
        print("User successfully logged in.")
    except AssertionError as e:
        print(e)

    # Step 7: Check for any error messages
    try:
        error_message = driver.find_element(By.ID, 'error-message-id')  # Replace with actual error message ID
        if error_message.is_displayed():
            print("Error message displayed:", error_message.text)
        else:
            print("No error message displayed")
    except Exception as e:
        print(f"Error checking for error message: {e}")

finally:
    # Close the driver
    driver.quit()
    print("Driver closed.")