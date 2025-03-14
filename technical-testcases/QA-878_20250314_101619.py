""" 
Title: Implement Password Reset Feature
Environment Variables: Selenium WebDriver, Chrome, Python 3.12
Notes: Ensure that the email sending functionality is mocked or tested in a controlled environment.
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the login page
    try:
        driver.get('http://example.com/login')
        logging.info('Navigated to login page.')
    except Exception as e:
        logging.error(f'Error navigating to login page: {e}')

    # Step 2: Click on the 'Forgot Password?' link
    try:
        forgot_password_link = driver.find_element(By.LINK_TEXT, 'Forgot Password?')
        forgot_password_link.click()
        logging.info('Clicked on Forgot Password link.')
    except Exception as e:
        logging.error(f'Error clicking Forgot Password link: {e}')

    # Step 3: Enter the registered email address
    try:
        email_input = driver.find_element(By.NAME, 'email')
        email_input.send_keys('user@example.com')
        logging.info('Entered registered email address.')
    except Exception as e:
        logging.error(f'Error entering email address: {e}')

    # Step 4: Submit the password reset request
    try:
        submit_button = driver.find_element(By.NAME, 'submit')
        submit_button.click()
        logging.info('Submitted password reset request.')
    except Exception as e:
        logging.error(f'Error submitting password reset request: {e}')

    # Step 5: Wait for the confirmation message
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'success-message')))
        logging.info('Confirmation message is present.')
    except Exception as e:
        logging.error(f'Error waiting for confirmation message: {e}')

    # Step 6: Check for success message
    try:
        success_message = driver.find_element(By.ID, 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

    # Step 7: Simulate clicking the password reset link from the email
    try:
        driver.get('http://example.com/reset-password?token=valid_token')
        logging.info('Navigated to password reset link.')
    except Exception as e:
        logging.error(f'Error navigating to password reset link: {e}')

    # Step 8: Enter a new password
    try:
        new_password_input = driver.find_element(By.NAME, 'new_password')
        new_password_input.send_keys('NewPassword@123')
        logging.info('Entered new password.')
    except Exception as e:
        logging.error(f'Error entering new password: {e}')

    # Step 9: Confirm the new password
    try:
        confirm_password_input = driver.find_element(By.NAME, 'confirm_password')
        confirm_password_input.send_keys('NewPassword@123')
        logging.info('Confirmed new password.')
    except Exception as e:
        logging.error(f'Error confirming new password: {e}')

    # Step 10: Submit the new password
    try:
        reset_button = driver.find_element(By.NAME, 'reset')
        reset_button.click()
        logging.info('Submitted new password.')
    except Exception as e:
        logging.error(f'Error submitting new password: {e}')

    # Step 11: Check for success message after password reset
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'reset-success-message')))
        logging.info('Password reset success message is present.')
    except Exception as e:
        logging.error(f'Error waiting for password reset success message: {e}')

    # Step 12: Attempt to log in with the new password
    try:
        driver.get('http://example.com/login')
        email_input = driver.find_element(By.NAME, 'email')
        email_input.send_keys('user@example.com')
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys('NewPassword@123')
        login_button = driver.find_element(By.NAME, 'login')
        login_button.click()
        logging.info('Attempted to log in with new password.')
    except Exception as e:
        logging.error(f'Error attempting to log in: {e}')

    # Step 13: Check for successful login
    try:
        WebDriverWait(driver, 10).until(EC.url_to_be('http://example.com/dashboard'))
        logging.info('Login successful, user redirected to dashboard.')
    except Exception as e:
        logging.error(f'Error checking successful login: {e}')

finally:
    # Close the browser
    driver.quit()