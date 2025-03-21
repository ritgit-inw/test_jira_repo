""" 
Title: Implement Password Reset Feature
Environment Variables: Selenium WebDriver, Chrome, Python 3.12
Notes: This test case covers the password reset feature as per the user story and acceptance criteria.
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

# Initialize the Chrome driver with options
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode if needed
driver = webdriver.Chrome(options=options)

try:
    # Step 1: Navigate to the login page
    try:
        driver.get('http://example.com/login')
        logging.info('Navigated to the login page.')
    except Exception as e:
        logging.error(f'Error navigating to login page: {e}')

    # Step 2: Click on the 'Forgot Password' link
    try:
        forgot_password_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Forgot Password')))
        forgot_password_link.click()
        logging.info('Clicked on the Forgot Password link.')
    except Exception as e:
        logging.error(f'Error clicking Forgot Password link: {e}')

    # Step 3: Enter the registered email address
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email')))
        email_input.send_keys('user@example.com')
        email_input.send_keys(Keys.RETURN)
        logging.info('Entered email address and submitted.')
    except Exception as e:
        logging.error(f'Error entering email address: {e}')

    # Step 4: Check for email existence validation message
    try:
        email_error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'email-error')))
        if email_error_message.is_displayed():
            logging.info('Email validation error displayed.')
        else:
            logging.info('Email sent for password reset.')
    except Exception as e:
        logging.error(f'Error checking email validation message: {e}')

    # Step 5: Simulate clicking the reset link from the email
    try:
        driver.get('http://example.com/reset-password?token=valid_token')
        logging.info('Navigated to the reset password page.')
    except Exception as e:
        logging.error(f'Error navigating to reset password page: {e}')

    # Step 6: Set a new password
    try:
        new_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'new_password')))
        new_password_input.send_keys('NewPassword123!')
        confirm_password_input = driver.find_element(By.NAME, 'confirm_password')
        confirm_password_input.send_keys('NewPassword123!')
        confirm_password_input.send_keys(Keys.RETURN)
        logging.info('Entered new password and confirmed.')
    except Exception as e:
        logging.error(f'Error setting new password: {e}')

    # Step 7: Check for confirmation message
    try:
        confirmation_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'confirmation-message')))
        if confirmation_message.is_displayed():
            logging.info('Password reset successful.')
        else:
            logging.info('Password reset failed.')
    except Exception as e:
        logging.error(f'Error checking confirmation message: {e}')

finally:
    # Close the browser
    driver.quit()
    logging.info('Browser closed.')