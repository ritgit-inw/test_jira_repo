""" 
Title: Implement Password Reset Feature
Environment Variables: Selenium WebDriver, Chrome, Python 3.12
Notes: Ensure that the email used for testing is registered and can receive emails. The reset link should be valid for testing purposes.
Assignee: Malini Sharma
"""

import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the login page
    try:
        driver.get('https://example.com/login')
        logging.info('Navigated to the login page.')
    except Exception as e:
        logging.error(f'Error navigating to login page: {e}')

    # Step 2: Click on 'Forgot Password' link
    try:
        forgot_password_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Forgot Password')))
        forgot_password_link.click()
        logging.info('Clicked on the Forgot Password link.')
    except Exception as e:
        logging.error(f'Error clicking Forgot Password link: {e}')

    # Step 3: Enter registered email
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email')))
        email_input.send_keys('user@example.com')
        email_input.send_keys(Keys.RETURN)
        logging.info('Entered registered email and submitted.')
    except Exception as e:
        logging.error(f'Error entering email: {e}')

    # Step 4: Wait for the confirmation message
    time.sleep(2)  # Wait for the email to be sent

    # Step 5: Check for success message
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'success-message')))
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

    # Step 6: Simulate clicking the reset link from the email
    try:
        driver.get('https://example.com/reset-password?token=valid_token')
        logging.info('Navigated to the reset password page.')
    except Exception as e:
        logging.error(f'Error navigating to reset password page: {e}')

    # Step 7: Enter new password
    try:
        new_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'new_password')))
        new_password_input.send_keys('NewPassword@123')
        confirm_password_input = driver.find_element(By.NAME, 'confirm_password')
        confirm_password_input.send_keys('NewPassword@123')
        confirm_password_input.send_keys(Keys.RETURN)
        logging.info('Entered new password and confirmed.')
    except Exception as e:
        logging.error(f'Error entering new password: {e}')

    # Step 8: Wait for the confirmation message
    time.sleep(2)

    # Step 9: Check for success message after password reset
    try:
        reset_success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'reset-success-message')))
        assert reset_success_message.is_displayed(), 'Password reset success message not displayed'
        logging.info('Password reset success message displayed.')
    except Exception as e:
        logging.error(f'Error checking password reset success message: {e}')

finally:
    # Close the browser
    driver.quit()
    logging.info('Browser closed.')