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
    try:
        driver.get('https://yourapp.com/password-reset')
        logging.info('Navigated to password reset page.')
    except Exception as e:
        logging.error(f'Error navigating to password reset page: {e}')

    # Step 2: Request a password reset link
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        email_input.send_keys('user@example.com')
        request_button = driver.find_element(By.ID, 'request-reset')
        request_button.click()
        logging.info('Requested password reset link.')
    except Exception as e:
        logging.error(f'Error requesting password reset link: {e}')

    # Wait for email to be sent (this should be replaced with a proper wait)
    time.sleep(5)

    # Step 3: Check for success message
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'success-message'))
        )
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

    # Step 4: Simulate receiving the email and clicking the reset link
    try:
        driver.get('https://yourapp.com/reset-password?token=valid_token')
        logging.info('Navigated to reset password link.')
    except Exception as e:
        logging.error(f'Error navigating to reset password link: {e}')

    # Step 5: Set a new password
    try:
        new_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'new_password'))
        )
        new_password_input.send_keys('NewPassword123!')
        confirm_password_input = driver.find_element(By.NAME, 'confirm_password')
        confirm_password_input.send_keys('NewPassword123!')
        reset_button = driver.find_element(By.ID, 'reset-password')
        reset_button.click()
        logging.info('Set a new password.')
    except Exception as e:
        logging.error(f'Error setting new password: {e}')

    # Step 6: Check for confirmation message
    try:
        confirmation_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'confirmation-message'))
        )
        assert confirmation_message.is_displayed(), 'Confirmation message not displayed'
        logging.info('Confirmation message displayed.')
    except Exception as e:
        logging.error(f'Error checking confirmation message: {e}')

    # Step 7: Log in with the new password
    try:
        driver.get('https://yourapp.com/login')
        email_input = driver.find_element(By.NAME, 'email')
        email_input.send_keys('user@example.com')
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys('NewPassword123!')
        login_button = driver.find_element(By.ID, 'login')
        login_button.click()
        logging.info('Logged in with new password.')
    except Exception as e:
        logging.error(f'Error logging in with new password: {e}')

    # Step 8: Check for successful login
    try:
        dashboard = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'dashboard'))
        )
        assert dashboard.is_displayed(), 'Dashboard not displayed, login failed'
        logging.info('Dashboard displayed, login successful.')
    except Exception as e:
        logging.error(f'Error checking successful login: {e}')

finally:
    driver.quit()