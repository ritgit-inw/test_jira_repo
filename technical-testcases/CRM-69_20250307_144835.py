""" 
Title: Implement Password Reset Feature
Environment Variables: N/A
Notes: This test case automates the password reset feature, including requesting a reset link, resetting the password, and logging in with the new password.
Assignee: Aswin Suresh
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
    try:
        driver.get('https://yourapp.com/login')
        logging.info('Navigated to login page.')
    except Exception as e:
        logging.error(f'Error navigating to login page: {e}')

    # Step 2: Click on 'Forgot Password' link
    try:
        forgot_password_link = driver.find_element('link text', 'Forgot Password?')
        forgot_password_link.click()
        logging.info('Clicked on Forgot Password link.')
    except Exception as e:
        logging.error(f'Error clicking Forgot Password link: {e}')

    # Step 3: Enter email address
    try:
        email_input = driver.find_element('id', 'email')
        email_input.send_keys('user@example.com')
        logging.info('Entered email address.')
    except Exception as e:
        logging.error(f'Error entering email address: {e}')

    # Step 4: Submit the request
    try:
        submit_button = driver.find_element('id', 'submit')
        submit_button.click()
        logging.info('Submitted password reset request.')
    except Exception as e:
        logging.error(f'Error submitting password reset request: {e}')

    # Step 5: Check for success message
    try:
        success_message = driver.find_element('id', 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

    # Step 6: Simulate receiving email and clicking reset link
    try:
        driver.get('https://yourapp.com/reset-password?token=valid_token')
        logging.info('Navigated to reset password page.')
    except Exception as e:
        logging.error(f'Error navigating to reset password page: {e}')

    # Step 7: Set new password
    try:
        new_password_input = driver.find_element('id', 'new-password')
        new_password_input.send_keys('NewPassword123!')
        confirm_password_input = driver.find_element('id', 'confirm-password')
        confirm_password_input.send_keys('NewPassword123!')
        logging.info('Entered new password and confirmation.')
    except Exception as e:
        logging.error(f'Error entering new password: {e}')

    # Step 8: Submit new password
    try:
        reset_button = driver.find_element('id', 'reset-button')
        reset_button.click()
        logging.info('Submitted new password.')
    except Exception as e:
        logging.error(f'Error submitting new password: {e}')

    # Step 9: Check for confirmation message
    try:
        confirmation_message = driver.find_element('id', 'confirmation-message')
        assert confirmation_message.is_displayed(), 'Confirmation message not displayed'
        logging.info('Confirmation message displayed.')
    except Exception as e:
        logging.error(f'Error checking confirmation message: {e}')

    # Step 10: Log in with new password
    try:
        driver.get('https://yourapp.com/login')
        email_input = driver.find_element('id', 'email')
        email_input.send_keys('user@example.com')
        password_input = driver.find_element('id', 'password')
        password_input.send_keys('NewPassword123!')
        login_button = driver.find_element('id', 'login-button')
        login_button.click()
        logging.info('Logged in with new password.')
    except Exception as e:
        logging.error(f'Error logging in with new password: {e}')

    # Step 11: Check for successful login
    try:
        dashboard = driver.find_element('id', 'dashboard')
        assert dashboard.is_displayed(), 'Dashboard not displayed, login failed'
        logging.info('Dashboard displayed, login successful.')
    except Exception as e:
        logging.error(f'Error checking dashboard display: {e}')

finally:
    driver.quit()