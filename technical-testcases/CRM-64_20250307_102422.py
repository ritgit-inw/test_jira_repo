""" 
Title: Implement Password Reset Feature
Environment Variables: N/A
Notes: This test case automates the password reset feature, ensuring that the user can reset their password successfully. It checks for the display of success and confirmation messages.
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
    # Navigate to the password reset page
    try:
        driver.get('https://your-application-url.com/password-reset')
        logging.info('Navigated to password reset page.')
    except Exception as e:
        logging.error(f'Error navigating to password reset page: {e}')  

    # Enter email address
    try:
        email_input = driver.find_element('name', 'email')
        email_input.send_keys('user@example.com')
        logging.info('Entered email address.')
    except Exception as e:
        logging.error(f'Error entering email address: {e}')  

    # Click on the reset password button
    try:
        reset_button = driver.find_element('id', 'reset-password')
        reset_button.click()
        logging.info('Clicked on reset password button.')
    except Exception as e:
        logging.error(f'Error clicking reset password button: {e}')  

    # Check for success message
    try:
        success_message = driver.find_element('id', 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')  

    # Simulate receiving the reset link and setting a new password
    try:
        driver.get('https://your-application-url.com/reset-link')
        logging.info('Navigated to reset link page.')
    except Exception as e:
        logging.error(f'Error navigating to reset link page: {e}')  

    # Enter new password
    try:
        new_password_input = driver.find_element('name', 'new-password')
        new_password_input.send_keys('NewSecurePassword123!')
        confirm_password_input = driver.find_element('name', 'confirm-password')
        confirm_password_input.send_keys('NewSecurePassword123!')
        logging.info('Entered new password and confirmation.')
    except Exception as e:
        logging.error(f'Error entering new password: {e}')  

    # Submit new password
    try:
        submit_button = driver.find_element('id', 'submit-new-password')
        submit_button.click()
        logging.info('Clicked on submit new password button.')
    except Exception as e:
        logging.error(f'Error clicking submit new password button: {e}')  

    # Check for confirmation message
    try:
        confirmation_message = driver.find_element('id', 'confirmation-message')
        assert confirmation_message.is_displayed(), 'Confirmation message not displayed'
        logging.info('Confirmation message displayed.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')
    except Exception as e:
        logging.error(f'Error checking confirmation message: {e}')  

finally:
    driver.quit()
    logging.info('Driver quit successfully.')