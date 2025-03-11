""" 
Title: Implement Password Reset Feature
Environment Variables: N/A
Notes: This test case automates the password reset feature, including requesting a reset link, resetting the password, and logging in with the new password.
Assignee: pranav
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Constants for the test
APPLICATION_URL = 'https://your-application-url.com'
EMAIL = 'user@example.com'
PASSWORD = 'NewPassword123!'

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
    driver.get(f'{APPLICATION_URL}/login')

    # Step 2: Click on 'Forgot Password' link
    try:
        logging.info('Clicking on the Forgot Password link.')
        forgot_password_link = driver.find_element('link text', 'Forgot Password?')
        forgot_password_link.click()
    except Exception as e:
        logging.error(f'Error clicking Forgot Password link: {e}')  

    # Step 3: Enter email address to request password reset
    try:
        logging.info('Entering email address for password reset.')
        email_input = driver.find_element('name', 'email')
        email_input.send_keys(EMAIL)
        request_reset_button = driver.find_element('id', 'request-reset')
        request_reset_button.click()
    except Exception as e:
        logging.error(f'Error requesting password reset: {e}')  

    # Step 4: Check for success message
    try:
        logging.info('Checking for success message.')
        success_message = driver.find_element('id', 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
    except Exception as e:
        logging.error(f'Error checking success message: {e}')  

    # Step 5: Simulate receiving the email and clicking the reset link
    logging.info('Navigating to the reset password page.')
    driver.get(f'{APPLICATION_URL}/reset-password?token=mock-token')

    # Step 6: Set a new password
    try:
        logging.info('Setting a new password.')
        new_password_input = driver.find_element('name', 'new_password')
        new_password_input.send_keys(PASSWORD)
        confirm_password_input = driver.find_element('name', 'confirm_password')
        confirm_password_input.send_keys(PASSWORD)
        reset_password_button = driver.find_element('id', 'reset-password')
        reset_password_button.click()
    except Exception as e:
        logging.error(f'Error setting new password: {e}')  

    # Step 7: Check for confirmation message
    try:
        logging.info('Checking for confirmation message.')
        confirmation_message = driver.find_element('id', 'confirmation-message')
        assert confirmation_message.is_displayed(), 'Confirmation message not displayed'
    except Exception as e:
        logging.error(f'Error checking confirmation message: {e}')  

    # Step 8: Log in with the new password
    try:
        logging.info('Logging in with the new password.')
        driver.get(f'{APPLICATION_URL}/login')
        email_input = driver.find_element('name', 'email')
        email_input.send_keys(EMAIL)
        password_input = driver.find_element('name', 'password')
        password_input.send_keys(PASSWORD)
        login_button = driver.find_element('id', 'login')
        login_button.click()
    except Exception as e:
        logging.error(f'Error logging in: {e}')  

    # Step 9: Check for successful login
    try:
        logging.info('Checking for successful login.')
        user_dashboard = driver.find_element('id', 'user-dashboard')
        assert user_dashboard.is_displayed(), 'User dashboard not displayed'
    except Exception as e:
        logging.error(f'Error checking user dashboard: {e}')  

finally:
    logging.info('Quitting the driver.')
    driver.quit()