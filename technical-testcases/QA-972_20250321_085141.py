""" 
Title: Implement Password Reset Feature
Environment Variables: Selenium WebDriver, Chrome, Python 3.12
Notes: Ensure that the ChromeDriver is installed and the path is set correctly. The example URLs and element IDs should be replaced with actual values from the application.
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
try:
    driver = webdriver.Chrome()
    logging.info('Chrome driver initialized successfully.')
except Exception as e:
    logging.error(f'Error initializing Chrome driver: {e}')
    raise

# Define the URL and credentials
login_url = 'http://example.com/login'
reset_url = 'http://example.com/reset-password?token=valid_token'
email = 'user@example.com'
new_password = 'NewPassword123!'

try:
    # Step 1: Navigate to the login page
    driver.get(login_url)
    logging.info('Navigated to the login page.')

    # Step 2: Click on the 'Forgot Password' link
    try:
        forgot_password_link = driver.find_element(By.LINK_TEXT, 'Forgot Password')
        forgot_password_link.click()
        logging.info('Clicked on the Forgot Password link.')
    except Exception as e:
        logging.error(f'Error clicking Forgot Password link: {e}')  

    # Step 3: Enter the registered email address
    try:
        email_input = driver.find_element(By.NAME, 'email')
        email_input.send_keys(email)
        email_input.send_keys(Keys.RETURN)
        logging.info('Entered email address and submitted.')
    except Exception as e:
        logging.error(f'Error entering email address: {e}')

    # Step 4: Check for email existence validation message
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'email-error')))
        email_error_message = driver.find_element(By.ID, 'email-error')
        if email_error_message.is_displayed():
            logging.info('Email validation error displayed.')
        else:
            logging.info('Email sent for password reset.')
    except Exception as e:
        logging.error(f'Error checking email validation message: {e}')

    # Step 5: Simulate clicking the reset link from the email
    try:
        driver.get(reset_url)
        logging.info('Navigated to the password reset page.')
    except Exception as e:
        logging.error(f'Error navigating to reset password page: {e}')  

    # Step 6: Set a new password
    try:
        new_password_input = driver.find_element(By.NAME, 'new_password')
        new_password_input.send_keys(new_password)
        new_password_input.send_keys(Keys.RETURN)
        logging.info('Entered new password and submitted.')
    except Exception as e:
        logging.error(f'Error entering new password: {e}')

    # Step 7: Check for success message
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'success-message')))
        success_message = driver.find_element(By.ID, 'success-message')
        if success_message.is_displayed():
            logging.info('Password reset successful.')
        else:
            logging.info('Password reset failed.')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

finally:
    # Close the browser
    driver.quit()
    logging.info('Browser closed.')