""" 
Title: Implement username Reset Feature
Environment Variables: Selenium WebDriver, Chrome, Python 3.12
Notes: Ensure that the email used is registered in the system and that the reset link is valid.
Assignee: Malini Sharma
"""

import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def reset_password():
    # Initialize the Chrome driver
    try:
        driver = webdriver.Chrome()
        logging.info('Chrome driver initialized successfully.')
    except Exception as e:
        logging.error(f'Error initializing Chrome driver: {e}')
        return

    try:
        # Navigate to the password reset page
        driver.get('http://example.com/reset-password')
        logging.info('Navigated to the password reset page.')

        # Locate the email input field and enter a registered email address
        try:
            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'email'))
            )
            email_input.send_keys('user@example.com')
            logging.info('Entered email address.')
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f'Error locating email input: {e}')

        # Locate and click the reset password button
        try:
            reset_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'reset-button'))
            )
            reset_button.click()
            logging.info('Clicked the reset password button.')
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f'Error clicking reset button: {e}')

        # Wait for the confirmation message to appear
        try:
            confirmation_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'confirmation-message'))
            )
            assert confirmation_message.is_displayed(), 'Confirmation message not displayed'
            logging.info('Confirmation message displayed.')
        except (TimeoutException, AssertionError) as e:
            logging.error(f'Error with confirmation message: {e}')

        # Simulate clicking the link in the email
        driver.get('http://example.com/reset-password/confirm?token=valid_token')
        logging.info('Navigated to the confirmation link.')

        # Locate the new password input field and enter a new password
        try:
            new_password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'new-password'))
            )
            new_password_input.send_keys('NewPassword123!')
            logging.info('Entered new password.')
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f'Error locating new password input: {e}')

        # Locate and click the submit button to set the new password
        try:
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'submit-button'))
            )
            submit_button.click()
            logging.info('Clicked the submit button.')
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f'Error clicking submit button: {e}')

        # Wait for the success message to appear
        try:
            success_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'success-message'))
            )
            assert success_message.is_displayed(), 'Success message not displayed'
            logging.info('Success message displayed.')
        except (TimeoutException, AssertionError) as e:
            logging.error(f'Error with success message: {e}')

    finally:
        # Close the browser
        driver.quit()
        logging.info('Browser closed.')

# Run the password reset function
reset_password()