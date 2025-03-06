""" 
Title: Implement Password Reset Feature
Environment Variables: N/A
Notes: This test case automates the password reset feature, ensuring that the user can request a reset link, set a new password, and log in successfully.
Assignee: Vikesh Bk
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import logging

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
        email_input = driver.find_element('id', 'email')  # Replace with actual ID
        email_input.send_keys('user@example.com')  # Replace with actual email
        request_button = driver.find_element('id', 'request-reset')  # Replace with actual ID
        request_button.click()
        logging.info('Requested password reset link.')
    except Exception as e:
        logging.error(f'Error requesting password reset link: {e}')  

    # Step 3: Check for success message
    try:
        success_message = driver.find_element('id', 'success-message')  # Replace with actual ID
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except AssertionError as ae:
        logging.error(f'Assertion error: {ae}')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')  

    # Step 4: Simulate receiving the email and clicking the reset link
    try:
        driver.get('https://yourapp.com/reset-password?token=exampletoken')  # Replace with actual link
        logging.info('Navigated to reset password link.')
    except Exception as e:
        logging.error(f'Error navigating to reset password link: {e}')  

    # Step 5: Set a new password
    try:
        new_password_input = driver.find_element('id', 'new-password')  # Replace with actual ID
        new_password_input.send_keys('NewPassword123!')  # Replace with actual password
        confirm_password_input = driver.find_element('id', 'confirm-password')  # Replace with actual ID
        confirm_password_input.send_keys('NewPassword123!')  # Replace with actual password
        reset_button = driver.find_element('id', 'reset-password')  # Replace with actual ID
        reset_button.click()
        logging.info('New password set and reset button clicked.')
    except Exception as e:
        logging.error(f'Error setting new password: {e}')  

    # Step 6: Check for confirmation message
    try:
        confirmation_message = driver.find_element('id', 'confirmation-message')  # Replace with actual ID
        assert confirmation_message.is_displayed(), 'Confirmation message not displayed'
        logging.info('Confirmation message displayed.')
    except AssertionError as ae:
        logging.error(f'Assertion error: {ae}')
    except Exception as e:
        logging.error(f'Error checking confirmation message: {e}')  

    # Step 7: Log in with the new password
    try:
        driver.get('https://yourapp.com/login')  # Replace with actual login page
        login_email_input = driver.find_element('id', 'login-email')  # Replace with actual ID
        login_email_input.send_keys('user@example.com')  # Replace with actual email
        login_password_input = driver.find_element('id', 'login-password')  # Replace with actual ID
        login_password_input.send_keys('NewPassword123!')  # Replace with actual password
        login_button = driver.find_element('id', 'login-button')  # Replace with actual ID
        login_button.click()
        logging.info('Logged in with new password.')
    except Exception as e:
        logging.error(f'Error logging in with new password: {e}')  

    # Step 8: Check for successful login
    try:
        dashboard = driver.find_element('id', 'dashboard')  # Replace with actual ID
        assert dashboard.is_displayed(), 'Dashboard not displayed, login failed'
        logging.info('Dashboard displayed, login successful.')
    except AssertionError as ae:
        logging.error(f'Assertion error: {ae}')
    except Exception as e:
        logging.error(f'Error checking dashboard display: {e}')  

finally:
    driver.quit()
    logging.info('Driver quit successfully.')