""" 
Title: Technical Test Case for Google Authentication Login
Environment Variables: Python 3.12, WebSelenium, Chrome
Notes: This test case automates the login process using Google authentication. Ensure to replace placeholder URLs and credentials with actual values before running the test.
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        logging.error('Failed to navigate to the login page: %s', e)

    # Step 2: Click on 'Login with Google'
    try:
        google_login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Login with Google"]'))
        )
        google_login_button.click()
        logging.info('Clicked on Login with Google button.')
    except Exception as e:
        logging.error('Failed to click on Login with Google button: %s', e)

    # Step 3: Wait for the Google authentication page to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'identifier'))
        )
        logging.info('Google authentication page loaded.')
    except Exception as e:
        logging.error('Failed to load Google authentication page: %s', e)

    # Step 4: Perform Google login
    try:
        email_input = driver.find_element(By.NAME, 'identifier')
        email_input.send_keys('your-email@gmail.com')  # Replace with your email
        driver.find_element(By.ID, 'identifierNext').click()
        logging.info('Entered email and clicked next.')

        # Wait for password input
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_input.send_keys('your-password')  # Replace with your password
        driver.find_element(By.ID, 'passwordNext').click()
        logging.info('Entered password and clicked next.')
    except Exception as e:
        logging.error('Failed during Google login: %s', e)

    # Step 5: Verify successful login
    try:
        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://your-app-home-url.com')  # Replace with the actual home URL
        )
        logging.info('Login successful!')
    except Exception as e:
        logging.error('Login failed or took too long: %s', e)
        try:
            error_message = driver.find_element(By.XPATH, '//div[@class="error-message"]')  # Adjust the XPath as needed
            if error_message.is_displayed():
                logging.error('Error message displayed: %s', error_message.text)
        except Exception as e:
            logging.error('Failed to find error message: %s', e)

finally:
    driver.quit()
    logging.info('Driver quit.')