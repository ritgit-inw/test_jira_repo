""" 
Title: Implement Password Reset Feature
Environment Variables: Python 3.12, Selenium, Chrome
Notes: This test case automates the password reset feature, including requesting a reset link, setting a new password, and logging in with the new password.
Assignee: Vikesh Bk
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
    # Step 1: Navigate to the password reset page
    logging.info('Navigating to the password reset page.')
    driver.get('https://yourapp.com/password-reset')

    # Step 2: Request a password reset link
    try:
        logging.info('Requesting a password reset link.')
        email_input = driver.find_element(By.NAME, 'email')
        email_input.send_keys('user@example.com')
        request_button = driver.find_element(By.ID, 'request-reset')
        request_button.click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'success-message')))
        logging.info('Password reset link requested successfully.')
    except Exception as e:
        logging.error(f'Error requesting password reset link: {e}')  

    # Step 3: Check for success message
    try:
        success_message = driver.find_element(By.ID, 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')

    # Simulate user clicking the link in the email
    driver.get('https://yourapp.com/reset-password?token=valid_token')

    # Step 4: Set a new password
    try:
        logging.info('Setting a new password.')
        new_password_input = driver.find_element(By.NAME, 'new_password')
        new_password_input.send_keys('NewPassword123!')
        confirm_password_input = driver.find_element(By.NAME, 'confirm_password')
        confirm_password_input.send_keys('NewPassword123!')
        reset_button = driver.find_element(By.ID, 'reset-password')
        reset_button.click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'confirmation-message')))
        logging.info('New password set successfully.')
    except Exception as e:
        logging.error(f'Error setting new password: {e}')  

    # Step 5: Check for confirmation message
    try:
        confirmation_message = driver.find_element(By.ID, 'confirmation-message')
        assert confirmation_message.is_displayed(), 'Confirmation message not displayed'
        logging.info('Confirmation message displayed.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')

    # Step 6: Log in with the new password
    try:
        logging.info('Logging in with the new password.')
        driver.get('https://yourapp.com/login')
        email_input = driver.find_element(By.NAME, 'email')
        email_input.send_keys('user@example.com')
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys('NewPassword123!')
        login_button = driver.find_element(By.ID, 'login')
        login_button.click()
        WebDriverWait(driver, 10).until(EC.url_to_be('https://yourapp.com/dashboard'))
        logging.info('Login successful, user redirected to dashboard.')
    except Exception as e:
        logging.error(f'Error during login: {e}')  

finally:
    driver.quit()