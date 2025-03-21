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

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Navigate to the password reset page
    try:
        driver.get('https://example.com/password-reset')
        logging.info('Navigated to password reset page.')
    except Exception as e:
        logging.error(f'Error navigating to password reset page: {e}')

    # Enter the registered email address
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        email_input.send_keys('user@example.com')
        logging.info('Entered email address.')
    except Exception as e:
        logging.error(f'Error entering email address: {e}')

    # Click the reset password button
    try:
        reset_button = driver.find_element(By.ID, 'reset-button')
        reset_button.click()
        logging.info('Clicked reset password button.')
    except Exception as e:
        logging.error(f'Error clicking reset password button: {e}')

    # Wait for the email validation message
    try:
        email_error = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'email-error'))
        )
        if email_error.is_displayed():
            logging.info('Email validation error displayed.')
        else:
            logging.info('Email validation passed, check your inbox for the reset link.')
    except Exception as e:
        logging.error(f'Error checking email validation message: {e}')

    # Simulate clicking the reset link in the email
    try:
        driver.get('https://example.com/reset-link')
        logging.info('Navigated to reset link.')
    except Exception as e:
        logging.error(f'Error navigating to reset link: {e}')

    # Enter a new password
    try:
        new_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'new-password'))
        )
        new_password_input.send_keys('NewSecurePassword123!')
        logging.info('Entered new password.')
    except Exception as e:
        logging.error(f'Error entering new password: {e}')

    # Confirm the new password
    try:
        confirm_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'confirm-password'))
        )
        confirm_password_input.send_keys('NewSecurePassword123!')
        logging.info('Entered confirm password.')
    except Exception as e:
        logging.error(f'Error entering confirm password: {e}')

    # Click the submit button
    try:
        submit_button = driver.find_element(By.ID, 'submit-button')
        submit_button.click()
        logging.info('Clicked submit button.')
    except Exception as e:
        logging.error(f'Error clicking submit button: {e}')

    # Wait for the success message
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'success-message'))
        )
        if success_message.is_displayed():
            logging.info('Password reset successful!')
        else:
            logging.info('Password reset failed.')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

finally:
    # Close the browser
    driver.quit()