""" 
Title: Implement Password Reset Feature
Environment Variables: Python 3.12, Selenium, Chrome
Notes: This test case automates the password reset feature, including requesting a reset link, setting a new password, and logging in with the new password.
Assignee: Prakhar Soni
"""

import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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
    # Step 1: Navigate to the password reset page
    try:
        driver.get('https://yourapp.com/password-reset')
        logging.info('Navigated to password reset page.')
    except Exception as e:
        logging.error(f'Error navigating to password reset page: {e}')

    # Step 2: Request a password reset link
    try:
        email_input = driver.find_element('name', 'email')
        email_input.send_keys('user@example.com')
        request_button = driver.find_element('id', 'request-reset')
        request_button.click()
        logging.info('Requested password reset link.')
    except Exception as e:
        logging.error(f'Error requesting password reset link: {e}')

    # Step 3: Check for success message
    try:
        success_message = driver.find_element('id', 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

    # Simulate receiving the email and clicking the reset link
    try:
        driver.get('https://yourapp.com/reset-link')
        logging.info('Navigated to reset link page.')
    except Exception as e:
        logging.error(f'Error navigating to reset link page: {e}')

    # Step 4: Set a new password
    try:
        new_password_input = driver.find_element('name', 'new_password')
        new_password_input.send_keys('NewPassword123!')
        confirm_password_input = driver.find_element('name', 'confirm_password')
        confirm_password_input.send_keys('NewPassword123!')
        reset_button = driver.find_element('id', 'reset-password')
        reset_button.click()
        logging.info('New password set.')
    except Exception as e:
        logging.error(f'Error setting new password: {e}')

    # Step 5: Check for confirmation message
    try:
        confirmation_message = driver.find_element('id', 'confirmation-message')
        assert confirmation_message.is_displayed(), 'Confirmation message not displayed'
        logging.info('Confirmation message displayed.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')
    except Exception as e:
        logging.error(f'Error checking confirmation message: {e}')

    # Step 6: Log in with the new password
    try:
        driver.get('https://yourapp.com/login')
        login_email_input = driver.find_element('name', 'email')
        login_email_input.send_keys('user@example.com')
        login_password_input = driver.find_element('name', 'password')
        login_password_input.send_keys('NewPassword123!')
        login_button = driver.find_element('id', 'login-button')
        login_button.click()
        logging.info('Logged in with new password.')
    except Exception as e:
        logging.error(f'Error logging in with new password: {e}')

    # Step 7: Check for successful login
    try:
        dashboard = driver.find_element('id', 'dashboard')
        assert dashboard.is_displayed(), 'Dashboard not displayed after login'
        logging.info('Dashboard displayed after login.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')
    except Exception as e:
        logging.error(f'Error checking dashboard display: {e}')

finally:
    driver.quit()
    logging.info('Driver quit.')