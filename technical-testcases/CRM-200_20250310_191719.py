""" 
Title: Implement Password Reset Feature
Environment Variables: N/A
Notes: This test case automates the password reset feature, including requesting a reset link, resetting the password, and logging in with the new password.
Assignee: Anand Pv
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

# Initialize the Chrome driver
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

    # Step 3: Enter email address to request password reset
    try:
        logging.info('Entering email address for password reset.')
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email')))
        email_input.send_keys('user@example.com')
        request_button = driver.find_element(By.ID, 'request-reset')
        request_button.click()
    except Exception as e:
        logging.error(f'Error entering email address: {e}')  

    # Wait for email to be sent
    logging.info('Waiting for email to be sent.')
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'success-message')))

    # Step 4: Check for success message
    try:
        logging.info('Checking for success message.')
        success_message = driver.find_element(By.ID, 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')  

    # Step 5: Simulate receiving the email and clicking the reset link
    try:
        logging.info('Navigating to the reset password page.')
        driver.get('https://yourapp.com/reset-password?token=sampletoken')
    except Exception as e:
        logging.error(f'Error navigating to reset password page: {e}')  

    # Step 6: Set a new password
    try:
        logging.info('Setting a new password.')
        new_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'new_password')))
        new_password_input.send_keys('NewPassword123!')
        confirm_password_input = driver.find_element(By.NAME, 'confirm_password')
        confirm_password_input.send_keys('NewPassword123!')
        reset_button = driver.find_element(By.ID, 'reset-password')
        reset_button.click()
    except Exception as e:
        logging.error(f'Error setting new password: {e}')  

    # Step 7: Check for confirmation message
    try:
        logging.info('Checking for confirmation message.')
        confirmation_message = driver.find_element(By.ID, 'confirmation-message')
        assert confirmation_message.is_displayed(), 'Confirmation message not displayed'
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')
    except Exception as e:
        logging.error(f'Error checking confirmation message: {e}')  

    # Step 8: Log in with the new password
    try:
        logging.info('Logging in with the new password.')
        driver.get('https://yourapp.com/login')
        email_input = driver.find_element(By.NAME, 'email')
        email_input.send_keys('user@example.com')
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys('NewPassword123!')
        login_button = driver.find_element(By.ID, 'login-button')
        login_button.click()
    except Exception as e:
        logging.error(f'Error logging in: {e}')  

    # Step 9: Check for successful login
    try:
        logging.info('Checking for successful login.')
        dashboard = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'dashboard')))
        assert dashboard.is_displayed(), 'Dashboard not displayed after login'
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')
    except Exception as e:
        logging.error(f'Error checking dashboard: {e}')  

finally:
    # Close the driver
    logging.info('Closing the driver.')
    driver.quit()