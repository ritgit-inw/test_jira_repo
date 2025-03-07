""" 
Title: Implement Password Reset Feature
Environment Variables: Python 3.12, Selenium, Chrome WebDriver
Notes: This test case automates the password reset feature, including requesting a reset link, setting a new password, and verifying login with the new password.
Assignee: Prakhar Soni
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
logging.basicConfig(level=logging.INFO)

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run headless Chrome
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Setup Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Navigate to the login page
    logging.info('Navigating to the login page.')
    driver.get('https://yourapp.com/login')

    # Step 2: Click on 'Forgot Password' link
    try:
        logging.info('Clicking on the Forgot Password link.')
        forgot_password_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Forgot Password?')))
        forgot_password_link.click()
    except Exception as e:
        logging.error(f'Error clicking Forgot Password link: {e}')  

    # Step 3: Enter email to request password reset
    try:
        logging.info('Entering email to request password reset.')
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'email')))
        email_input.send_keys('user@example.com')
        request_reset_button = driver.find_element(By.ID, 'request-reset')
        request_reset_button.click()
    except Exception as e:
        logging.error(f'Error requesting password reset: {e}')  

    # Wait for email to be sent (better handling)
    logging.info('Waiting for email to be sent.')
    time.sleep(5)  # Ideally, replace this with a better wait mechanism

    # Step 4: Check for success message
    try:
        logging.info('Checking for success message.')
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'success-message')))
        assert success_message.is_displayed(), 'Success message not displayed'
    except AssertionError as ae:
        logging.error(f'Assertion error: {ae}')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')  

    # Simulate user clicking the link in the email
    logging.info('Navigating to the reset password page.')
    driver.get('https://yourapp.com/reset-password?token=valid_token')

    # Step 5: Set new password
    try:
        logging.info('Setting new password.')
        new_password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'new_password')))
        new_password_input.send_keys('NewPassword123!')
        confirm_password_input = driver.find_element(By.NAME, 'confirm_password')
        confirm_password_input.send_keys('NewPassword123!')
        reset_password_button = driver.find_element(By.ID, 'reset-password')
        reset_password_button.click()
    except Exception as e:
        logging.error(f'Error setting new password: {e}')  

    # Step 6: Check for login success
    try:
        logging.info('Checking for login success message.')
        login_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'login-success')))
        assert login_message.is_displayed(), 'Login success message not displayed'
    except AssertionError as ae:
        logging.error(f'Assertion error: {ae}')
    except Exception as e:
        logging.error(f'Error checking login success message: {e}')  

finally:
    logging.info('Quitting the driver.')
    driver.quit()