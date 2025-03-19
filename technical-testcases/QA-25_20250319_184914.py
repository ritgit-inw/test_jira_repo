""" 
Title: Technical Test Case for Google Authentication Login
Environment Variables: Python 3.12, Selenium, Chrome, WebDriver Manager
Notes: This test case automates the login process using Google authentication and verifies the redirection and successful login.
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
        logging.info('Navigated to login page.')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Login with Google"]')))
    except Exception as e:
        logging.error('Failed to navigate to login page: %s', e)

    # Step 2: Click on 'Login with Google'
    try:
        google_login_button = driver.find_element(By.XPATH, '//button[text()="Login with Google"]')
        google_login_button.click()
        logging.info('Clicked on Login with Google button.')
        WebDriverWait(driver, 10).until(EC.url_contains('accounts.google.com'))
    except Exception as e:
        logging.error('Failed to click on Google login button: %s', e)

    # Step 3: Verify redirection to Google authentication page
    try:
        assert "accounts.google.com" in driver.current_url, "Not redirected to Google authentication page"
        logging.info('Successfully redirected to Google authentication page.')
    except AssertionError as e:
        logging.error(e)

    # Step 4: Simulate successful authentication (this part may vary based on your setup)
    # Uncomment and implement the following lines if needed:
    # driver.find_element(By.ID, 'identifierId').send_keys('your-email@gmail.com')
    # driver.find_element(By.ID, 'identifierNext').click()
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
    # driver.find_element(By.NAME, 'password').send_keys('your-password')
    # driver.find_element(By.ID, 'passwordNext').click()
    # WebDriverWait(driver, 10).until(EC.url_contains('your-app-dashboard-url.com'))

    # Step 5: Verify successful login
    try:
        assert "your-app-dashboard-url.com" in driver.current_url, "Login failed, not redirected to dashboard"
        logging.info('Successfully logged in and redirected to dashboard.')
    except AssertionError as e:
        logging.error(e)

    # Optional: Check for error messages if login fails
    try:
        error_message = driver.find_element(By.ID, 'error-message-id')  # Replace with actual error message ID
        if error_message.is_displayed():
            logging.warning("Error message displayed: %s", error_message.text)
    except Exception as e:
        logging.info('No error message displayed or element not found: %s', e)

finally:
    driver.quit()
    logging.info('Driver quit successfully.')