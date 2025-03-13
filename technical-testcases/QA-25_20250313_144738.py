""" 
Title: Technical Test Case for Google Authentication Login
Environment Variables: N/A
Notes: This test case automates the login process using Google authentication and verifies the redirection and successful login.
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
        logging.info('Navigated to the login page.')
    except Exception as e:
        logging.error(f'Error navigating to login page: {e}')

    # Step 2: Click on 'Login with Google'
    try:
        google_login_button = driver.find_element('xpath', '//button[text()="Login with Google"]')
        google_login_button.click()
        logging.info('Clicked on Login with Google button.')
    except NoSuchElementException:
        logging.error('Login with Google button not found.')
    except Exception as e:
        logging.error(f'Error clicking Login with Google button: {e}')

    # Step 3: Verify redirection to Google authentication page
    try:
        assert "accounts.google.com" in driver.current_url, "Not redirected to Google authentication page"
        logging.info('Successfully redirected to Google authentication page.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')

    # Step 4: Simulate successful authentication (this part may vary based on your app's flow)
    # You may need to handle the Google login process here, which could involve entering credentials.

    # Step 5: Verify successful login to the app
    try:
        assert driver.find_element('id', 'welcome-message').is_displayed(), "Login failed, welcome message not displayed"
        logging.info('Login successful, welcome message displayed.')
    except NoSuchElementException:
        logging.error('Welcome message not found after login.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')

finally:
    # Close the driver
    driver.quit()
    logging.info('Driver closed.')