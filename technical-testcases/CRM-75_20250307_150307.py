""" 
Title: Implement Password Reset Feature
Environment Variables: Python 3.12, Selenium, Chrome
Notes: This test case automates the password reset feature, including requesting a reset link, resetting the password, and logging in with the new password.
Assignee: Aditya Jena
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
    try:
        driver.get('https://yourapp.com/login')
        logging.info('Navigated to login page.')
    except Exception as e:
        logging.error(f'Error navigating to login page: {e}')

    # Step 2: Click on 'Forgot Password' link
    try:
        forgot_password_link = driver.find_element(By.LINK_TEXT, 'Forgot Password?')
        forgot_password_link.click()
        logging.info('Clicked on Forgot Password link.')
    except Exception as e:
        logging.error(f'Error clicking Forgot Password link: {e}')

    # Step 3: Enter email address
    try:
        email_input = driver.find_element(By.NAME, 'email')
        email_input.send_keys('user@example.com')
        logging.info('Entered email address.')
    except Exception as e:
        logging.error(f'Error entering email address: {e}')

    # Step 4: Submit the request
    try:
        submit_button = driver.find_element(By.ID, 'submit')
        submit_button.click()
        logging.info('Submitted the password reset request.')
    except Exception as e:
        logging.error(f'Error submitting password reset request: {e}')

    # Step 5: Wait for the email to be sent
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'success-message')))
        logging.info('Email sent successfully.')
    except Exception as e:
        logging.error(f'Error waiting for email to be sent: {e}')

    # Step 6: Check for success message
    try:
        success_message = driver.find_element(By.ID, 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

    # Step 7: Simulate clicking the link in the email
    try:
        driver.get('https://yourapp.com/reset-password?token=valid_token')
        logging.info('Navigated to reset password page.')
    except Exception as e:
        logging.error(f'Error navigating to reset password page: {e}')

    # Step 8: Enter new password
    try:
        new_password_input = driver.find_element(By.NAME, 'new_password')
        new_password_input.send_keys('NewPassword123!')
        logging.info('Entered new password.')
    except Exception as e:
        logging.error(f'Error entering new password: {e}')

    # Step 9: Confirm new password
    try:
        confirm_password_input = driver.find_element(By.NAME, 'confirm_password')
        confirm_password_input.send_keys('NewPassword123!')
        logging.info('Confirmed new password.')
    except Exception as e:
        logging.error(f'Error confirming new password: {e}')

    # Step 10: Submit new password
    try:
        reset_button = driver.find_element(By.ID, 'reset')
        reset_button.click()
        logging.info('Submitted new password.')
    except Exception as e:
        logging.error(f'Error submitting new password: {e}')

    # Step 11: Check for success message after reset
    try:
        reset_success_message = driver.find_element(By.ID, 'reset-success-message')
        assert reset_success_message.is_displayed(), 'Reset success message not displayed'
        logging.info('Reset success message displayed.')
    except Exception as e:
        logging.error(f'Error checking reset success message: {e}')

    # Step 12: Log in with new password
    try:
        driver.get('https://yourapp.com/login')
        email_input = driver.find_element(By.NAME, 'email')
        email_input.send_keys('user@example.com')
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys('NewPassword123!')
        login_button = driver.find_element(By.ID, 'login')
        login_button.click()
        logging.info('Logged in with new password.')
    except Exception as e:
        logging.error(f'Error logging in with new password: {e}')

    # Step 13: Check for successful login
    try:
        dashboard = driver.find_element(By.ID, 'dashboard')
        assert dashboard.is_displayed(), 'Dashboard not displayed, login failed'
        logging.info('Dashboard displayed, login successful.')
    except Exception as e:
        logging.error(f'Error checking dashboard display: {e}')

finally:
    driver.quit()