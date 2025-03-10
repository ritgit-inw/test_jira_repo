""" 
Title: Implement Password Reset Feature
Environment Variables: Python 3.12, Selenium, Chrome
Notes: This test case automates the password reset feature, including navigating to the reset page, submitting the email, and verifying the success message. It also tests setting a new password and logging in with it.
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

# Initialize the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Navigate to the password reset page
    try:
        logging.info('Navigating to the password reset page.')
        driver.get('https://yourapp.com/password-reset')  # Replace with actual URL
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
    except Exception as e:
        logging.error(f'Error navigating to password reset page: {e}')

    # Step 2: Enter registered email address
    try:
        logging.info('Entering registered email address.')
        email_input = driver.find_element(By.NAME, 'email')  # Adjust selector as needed
        email_input.send_keys('user@example.com')  # Replace with actual email
    except Exception as e:
        logging.error(f'Error entering email address: {e}')

    # Step 3: Submit the password reset request
    try:
        logging.info('Submitting the password reset request.')
        submit_button = driver.find_element(By.ID, 'submit')  # Adjust selector as needed
        submit_button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'success-message')))
    except Exception as e:
        logging.error(f'Error submitting password reset request: {e}')

    # Step 4: Check for success message
    try:
        logging.info('Checking for success message.')
        success_message = driver.find_element(By.ID, 'success-message')  # Adjust selector as needed
        assert success_message.is_displayed(), "Success message not displayed"
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

    # Step 5: Simulate user clicking the link in the email and setting a new password
    try:
        logging.info('Navigating to the reset password page.')
        driver.get('https://yourapp.com/reset-password?token=exampletoken')  # Replace with actual URL
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'new_password')))
        logging.info('Setting a new password.')
        new_password_input = driver.find_element(By.NAME, 'new_password')  # Adjust selector as needed
        new_password_input.send_keys('NewPassword123!')  # Replace with actual new password
        confirm_password_input = driver.find_element(By.NAME, 'confirm_password')  # Adjust selector as needed
        confirm_password_input.send_keys('NewPassword123!')  # Replace with actual new password
        reset_button = driver.find_element(By.ID, 'reset-button')  # Adjust selector as needed
        reset_button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login')))
    except Exception as e:
        logging.error(f'Error resetting password: {e}')

    # Step 6: Check for login success with new password
    try:
        logging.info('Navigating to the login page.')
        driver.get('https://yourapp.com/login')  # Replace with actual URL
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
        logging.info('Logging in with new password.')
        login_email_input = driver.find_element(By.NAME, 'email')  # Adjust selector as needed
        login_email_input.send_keys('user@example.com')  # Replace with actual email
        login_password_input = driver.find_element(By.NAME, 'password')  # Adjust selector as needed
        login_password_input.send_keys('NewPassword123!')  # Use new password
        login_button = driver.find_element(By.ID, 'login-button')  # Adjust selector as needed
        login_button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'welcome-message')))
        assert driver.find_element(By.ID, 'welcome-message').is_displayed(), "Login failed, welcome message not displayed"
    except Exception as e:
        logging.error(f'Error during login: {e}')

finally:
    logging.info('Quitting the driver.')
    driver.quit()