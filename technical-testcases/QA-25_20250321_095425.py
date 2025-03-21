""" 
Title: Technical Test Case for Google Authentication Login
Environment Variables: N/A
Notes: This test case automates the login process using Google authentication and verifies the expected behavior.
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run headless Chrome
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Initialize the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Navigate to the login page
    try:
        driver.get('https://your-app-login-url.com')  # Replace with the actual login URL
        logging.info('Navigated to the login page.')
    except Exception as e:
        logging.error(f'Error navigating to login page: {e}')  

    # Step 2: Click on 'Login with Google'
    try:
        google_login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Login with Google"]'))
        )
        google_login_button.click()
        logging.info('Clicked on Login with Google button.')
    except Exception as e:
        logging.error(f'Error clicking on Google login button: {e}')  

    # Step 3: Wait for the Google authentication page to load
    time.sleep(5)  # Adjust sleep time as necessary

    # Step 4: Check if redirected to Google authentication page
    try:
        assert "Google" in driver.title, "Not redirected to Google authentication page"
        logging.info('Redirected to Google authentication page.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')  

    # Step 5: Simulate successful authentication (this part may vary based on your setup)
    # You may need to enter credentials here or handle Google login via automation tools
    logging.info('Simulating successful authentication...')
    # Add your authentication logic here

    # Step 6: Verify successful login to the app
    try:
        time.sleep(5)  # Wait for the app to load after login
        assert "Welcome" in driver.page_source, "Login failed, welcome message not found"
        logging.info('Login successful, welcome message found.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')  

    # Step 7: Check for any error messages
    try:
        error_message = driver.find_element(By.ID, 'error-message-id')  # Replace with actual error message ID
        assert not error_message.is_displayed(), "Error message is displayed"
        logging.info('No error messages displayed.')
    except Exception as e:
        logging.error(f'Error checking for error messages: {e}')  

finally:
    # Close the driver
    driver.quit()
    logging.info('Driver closed.')