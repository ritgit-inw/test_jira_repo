""" 
Title: Technical Test Case for Google Authentication Login
Environment Variables: Python 3.12, Selenium, Chrome, WebDriver Manager
Notes: Ensure that the Google login button and error message element IDs are correctly referenced in the code.
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

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Setup Chrome options
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
        driver.get('https://your-app-login-url.com')  # Replace with actual login URL
        logging.info('Navigated to login page.')
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
        logging.error(f'Error clicking Login with Google button: {e}')

    # Step 3: Wait for Google authentication page to load
    time.sleep(5)  # Adjust sleep time as necessary

    # Step 4: Check if redirected to Google authentication page
    try:
        assert "Google" in driver.title, "Not redirected to Google authentication page"
        logging.info('Redirected to Google authentication page.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')

    # Step 5: Simulate successful authentication (this part may vary based on your app's flow)
    # Here you would typically enter credentials and submit the form
    # For example:
    # try:
    #     driver.find_element(By.ID, 'identifierId').send_keys('your-email@gmail.com')
    #     driver.find_element(By.ID, 'identifierNext').click()
    #     time.sleep(2)
    #     driver.find_element(By.NAME, 'password').send_keys('your-password')
    #     driver.find_element(By.ID, 'passwordNext').click()
    #     logging.info('Simulated successful authentication.')
    # except Exception as e:
    #     logging.error(f'Error during authentication: {e}')

    # Step 6: Wait for redirection back to the app
    time.sleep(5)  # Adjust sleep time as necessary

    # Step 7: Verify successful login
    try:
        assert "Welcome" in driver.page_source, "Login failed, welcome message not found"
        logging.info('Login successful, welcome message found.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')

    # Step 8: Check for any error messages
    try:
        error_message = driver.find_element(By.ID, 'error-message-id')  # Replace with actual error message element ID
        assert not error_message.is_displayed(), "Error message is displayed"
        logging.info('No error messages displayed.')
    except Exception as e:
        logging.error(f'Error checking for error messages: {e}')

finally:
    # Close the driver
    driver.quit()
    logging.info('Driver closed.')