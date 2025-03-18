""" 
Title: Implement Password Reset Feature
Environment Variables: Selenium WebDriver, Chrome, Python 3.12
Notes: Ensure that the email used for testing is registered in the system and that the reset link is valid.
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the password reset page
    try:
        driver.get('https://example.com/password-reset')
        logging.info('Navigated to password reset page.')
    except Exception as e:
        logging.error(f'Error navigating to password reset page: {e}')

    # Step 2: Enter the registered email address
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        email_input.send_keys('user@example.com')
        logging.info('Entered registered email address.')
    except Exception as e:
        logging.error(f'Error entering email address: {e}')

    # Step 3: Click the 'Send Reset Link' button
    try:
        reset_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'send-reset-link'))
        )
        reset_button.click()
        logging.info('Clicked the Send Reset Link button.')
    except Exception as e:
        logging.error(f'Error clicking Send Reset Link button: {e}')

    # Step 4: Wait for the confirmation message
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'success-message'))
        )
        logging.info('Confirmation message is displayed.')
    except Exception as e:
        logging.error(f'Error waiting for confirmation message: {e}')

    # Step 5: Check for success message
    try:
        success_message = driver.find_element(By.ID, 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message is displayed.')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

    # Step 6: Simulate receiving the email and clicking the reset link
    try:
        driver.get('https://example.com/reset-password?token=valid_token')
        logging.info('Navigated to reset password link.')
    except Exception as e:
        logging.error(f'Error navigating to reset password link: {e}')

    # Step 7: Enter a new password
    try:
        new_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'new_password'))
        )
        new_password_input.send_keys('NewPassword123!')
        logging.info('Entered new password.')
    except Exception as e:
        logging.error(f'Error entering new password: {e}')

    # Step 8: Confirm the new password
    try:
        confirm_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'confirm_password'))
        )
        confirm_password_input.send_keys('NewPassword123!')
        logging.info('Confirmed new password.')
    except Exception as e:
        logging.error(f'Error confirming new password: {e}')

    # Step 9: Click the 'Reset Password' button
    try:
        reset_password_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'reset-password'))
        )
        reset_password_button.click()
        logging.info('Clicked the Reset Password button.')
    except Exception as e:
        logging.error(f'Error clicking Reset Password button: {e}')

    # Step 10: Wait for the confirmation message
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'final-success-message'))
        )
        logging.info('Final confirmation message is displayed.')
    except Exception as e:
        logging.error(f'Error waiting for final confirmation message: {e}')

    # Step 11: Check for success message after password reset
    try:
        final_success_message = driver.find_element(By.ID, 'final-success-message')
        assert final_success_message.is_displayed(), 'Final success message not displayed'
        logging.info('Final success message is displayed.')
    except Exception as e:
        logging.error(f'Error checking final success message: {e}')

finally:
    # Close the browser
    driver.quit()
    logging.info('Browser closed.')