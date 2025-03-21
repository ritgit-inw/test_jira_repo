""" 
Title: Implement Password Reset Feature
Environment Variables: Selenium WebDriver, Chrome, Python 3.12
Notes: Ensure that the email used for testing is registered in the system and that the reset link is valid.
Assignee: Malini Sharma
"""

import logging
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the Chrome driver with options
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Uncomment to run in headless mode

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Navigate to the password reset page
    try:
        driver.get('https://example.com/password-reset')
        logging.info('Navigated to password reset page.')
    except Exception as e:
        logging.error('Failed to navigate to password reset page: %s', e)

    # Enter the registered email address
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        email_input.send_keys('user@example.com')
        logging.info('Entered email address.')
    except Exception as e:
        logging.error('Failed to enter email address: %s', e)

    # Click the reset password button
    try:
        reset_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'reset-button'))
        )
        reset_button.click()
        logging.info('Clicked reset password button.')
    except Exception as e:
        logging.error('Failed to click reset password button: %s', e)

    # Wait for the email validation message
    try:
        email_error = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'email-error'))
        )
        if email_error.is_displayed():
            logging.warning('Email validation error displayed: %s', email_error.text)
        else:
            logging.info('Email validation passed, check your inbox for the reset link.')
    except Exception as e:
        logging.error('Failed to check email validation message: %s', e)

    # Simulate clicking the reset link in the email
    try:
        driver.get('https://example.com/reset-link')
        logging.info('Navigated to reset link.')
    except Exception as e:
        logging.error('Failed to navigate to reset link: %s', e)

    # Enter a new password
    try:
        new_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'new-password'))
        )
        new_password_input.send_keys('NewSecurePassword123!')
        logging.info('Entered new password.')
    except Exception as e:
        logging.error('Failed to enter new password: %s', e)

    # Confirm the new password
    try:
        confirm_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'confirm-password'))
        )
        confirm_password_input.send_keys('NewSecurePassword123!')
        logging.info('Confirmed new password.')
    except Exception as e:
        logging.error('Failed to confirm new password: %s', e)

    # Click the submit button
    try:
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'submit-button'))
        )
        submit_button.click()
        logging.info('Clicked submit button.')
    except Exception as e:
        logging.error('Failed to click submit button: %s', e)

    # Wait for the success message
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'success-message'))
        )
        if success_message.is_displayed():
            logging.info('Password reset successful: %s', success_message.text)
        else:
            logging.warning('Password reset failed.')
    except Exception as e:
        logging.error('Failed to check success message: %s', e)

finally:
    # Close the browser
    driver.quit()
    logging.info('Browser closed.')