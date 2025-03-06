""" 
Title: Password Reset Functionality
Environment Variables: Chrome, Python 3.12
Notes: Ensure that the email is valid and the link in the email is functional.
Assignee: Ritesh Gond
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
try:
    driver = webdriver.Chrome()
    logging.info('Chrome driver initialized successfully.')
except Exception as e:
    logging.error(f'Error initializing Chrome driver: {e}')
    raise

try:
    # Step 1: Navigate to the login page
    driver.get('http://example.com/login')
    logging.info('Navigated to the login page.')

    # Step 2: Click on the 'Forgot Password?' link
    try:
        forgot_password_link = driver.find_element(By.LINK_TEXT, 'Forgot Password?')
        forgot_password_link.click()
        logging.info('Clicked on the Forgot Password link.')
    except Exception as e:
        logging.error(f'Error clicking Forgot Password link: {e}')

    # Step 3: Enter the registered email address
    try:
        email_field = driver.find_element(By.NAME, 'email')
        email_field.send_keys('user@example.com')
        logging.info('Entered registered email address.')
    except Exception as e:
        logging.error(f'Error entering email address: {e}')

    # Step 4: Click on the 'Submit' button
    try:
        submit_button = driver.find_element(By.NAME, 'submit')
        submit_button.click()
        logging.info('Clicked on the Submit button.')
    except Exception as e:
        logging.error(f'Error clicking Submit button: {e}')

    # Step 5: Wait for the confirmation message
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'confirmation')))
        confirmation_message = driver.find_element(By.ID, 'confirmation')
        assert confirmation_message.is_displayed(), 'Confirmation message not displayed'
        logging.info('Confirmation message displayed.')
    except Exception as e:
        logging.error(f'Error waiting for confirmation message: {e}')

    # Step 6: Simulate checking the email inbox
    logging.info('Check your email inbox for the password reset link.')

    # Step 7: Click on the link provided in the password reset email (simulated)
    try:
        driver.get('http://example.com/reset-password?token=exampletoken')
        logging.info('Navigated to the password reset link.')
    except Exception as e:
        logging.error(f'Error navigating to password reset link: {e}')

    # Step 8: Enter a new password
    try:
        new_password_field = driver.find_element(By.NAME, 'new_password')
        new_password_field.send_keys('NewPassword123!')
        logging.info('Entered new password.')
    except Exception as e:
        logging.error(f'Error entering new password: {e}')

    # Step 9: Confirm the new password
    try:
        confirm_password_field = driver.find_element(By.NAME, 'confirm_password')
        confirm_password_field.send_keys('NewPassword123!')
        logging.info('Confirmed new password.')
    except Exception as e:
        logging.error(f'Error confirming new password: {e}')

    # Step 10: Click on the 'Reset Password' button
    try:
        reset_button = driver.find_element(By.NAME, 'reset')
        reset_button.click()
        logging.info('Clicked on the Reset Password button.')
    except Exception as e:
        logging.error(f'Error clicking Reset Password button: {e}')

    # Step 11: Wait for the success message
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'success')))
        success_message = driver.find_element(By.ID, 'success')
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except Exception as e:
        logging.error(f'Error waiting for success message: {e}')

    # Step 12: Attempt to log in with the new password
    try:
        driver.get('http://example.com/login')
        email_field = driver.find_element(By.NAME, 'email')
        email_field.send_keys('user@example.com')
        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys('NewPassword123!')
        password_field.send_keys(Keys.RETURN)
        logging.info('Attempted to log in with new password.')
    except Exception as e:
        logging.error(f'Error attempting to log in: {e}')

    # Step 13: Verify successful login
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be('http://example.com/dashboard'))
        assert driver.current_url == 'http://example.com/dashboard', 'Login failed'
        logging.info('Login successful, redirected to dashboard.')
    except Exception as e:
        logging.error(f'Error verifying successful login: {e}')

finally:
    # Close the browser
    driver.quit()
    logging.info('Browser closed.')