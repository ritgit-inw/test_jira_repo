""" 
Title: Implement Password Reset Feature
Environment Variables: N/A
Notes: This test case automates the password reset feature, including requesting a reset link, setting a new password, and logging in with the new password.
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run headless Chrome
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Setup Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Navigate to the login page
    logging.info('Navigating to the login page.')
    driver.get('https://your-application-url.com/login')

    # Step 2: Click on 'Forgot Password' link
    try:
        logging.info('Clicking on the Forgot Password link.')
        forgot_password_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Forgot Password?')))
        forgot_password_link.click()
    except Exception as e:
        logging.error(f'Error clicking Forgot Password link: {e}')  

    # Step 3: Enter email address
    try:
        logging.info('Entering email address.')
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'email')))
        email_input.send_keys('user@example.com')
    except Exception as e:
        logging.error(f'Error entering email address: {e}')  

    # Step 4: Submit the request
    try:
        logging.info('Submitting the password reset request.')
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'submit')))
        submit_button.click()
    except Exception as e:
        logging.error(f'Error submitting password reset request: {e}')  

    # Step 5: Check for success message
    try:
        logging.info('Checking for success message.')
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'success-message')))
        assert success_message.is_displayed(), 'Success message not displayed'
    except Exception as e:
        logging.error(f'Error checking success message: {e}')  

    # Step 6: Simulate receiving the email and clicking the reset link
    try:
        logging.info('Navigating to the reset password link.')
        driver.get('https://your-application-url.com/reset-password?token=sampletoken')
    except Exception as e:
        logging.error(f'Error navigating to reset password link: {e}')  

    # Step 7: Set a new password
    try:
        logging.info('Setting a new password.')
        new_password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'new-password')))
        new_password_input.send_keys('NewPassword123!')
        confirm_password_input = driver.find_element(By.ID, 'confirm-password')
        confirm_password_input.send_keys('NewPassword123!')
    except Exception as e:
        logging.error(f'Error setting new password: {e}')  

    # Step 8: Submit the new password
    try:
        logging.info('Submitting the new password.')
        reset_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'reset-button')))
        reset_button.click()
    except Exception as e:
        logging.error(f'Error submitting new password: {e}')  

    # Step 9: Check for confirmation message
    try:
        logging.info('Checking for confirmation message.')
        confirmation_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'confirmation-message')))
        assert confirmation_message.is_displayed(), 'Confirmation message not displayed'
    except Exception as e:
        logging.error(f'Error checking confirmation message: {e}')  

    # Step 10: Log in with the new password
    try:
        logging.info('Logging in with the new password.')
        driver.get('https://your-application-url.com/login')
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'email')))
        email_input.send_keys('user@example.com')
        password_input = driver.find_element(By.ID, 'password')
        password_input.send_keys('NewPassword123!')
        login_button = driver.find_element(By.ID, 'login-button')
        login_button.click()
    except Exception as e:
        logging.error(f'Error logging in with new password: {e}')  

    # Step 11: Check for successful login
    try:
        logging.info('Checking for successful login.')
        WebDriverWait(driver, 10).until(
            EC.url_to_be('https://your-application-url.com/dashboard'))
    except Exception as e:
        logging.error(f'Error checking successful login: {e}')  

finally:
    logging.info('Quitting the driver.')
    driver.quit()