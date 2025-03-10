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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
    driver.get('https://your-application-url.com/login')
    logging.info('Navigated to login page.')

    # Step 2: Click on 'Forgot Password' link
    try:
        forgot_password_link = driver.find_element(By.LINK_TEXT, 'Forgot Password?')
        forgot_password_link.click()
        logging.info('Clicked on Forgot Password link.')
    except Exception as e:
        logging.error(f'Error clicking Forgot Password link: {e}')  

    # Step 3: Enter email address to request password reset
    try:
        email_input = driver.find_element(By.NAME, 'email')
        email_input.send_keys('user@example.com')
        request_reset_button = driver.find_element(By.ID, 'request-reset')
        request_reset_button.click()
        logging.info('Requested password reset for user@example.com.')
    except Exception as e:
        logging.error(f'Error requesting password reset: {e}')  

    # Step 4: Wait for email to be sent
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'success-message')))
        logging.info('Email sent successfully.')
    except Exception as e:
        logging.error(f'Error waiting for email to be sent: {e}')  

    # Step 5: Check for success message
    try:
        success_message = driver.find_element(By.ID, 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')  

    # Step 6: Simulate clicking the link in the email
    try:
        driver.get('https://your-application-url.com/reset-password?token=sampletoken')
        logging.info('Navigated to reset password page.')
    except Exception as e:
        logging.error(f'Error navigating to reset password page: {e}')  

    # Step 7: Set a new password
    try:
        new_password_input = driver.find_element(By.NAME, 'new_password')
        new_password_input.send_keys('NewPassword123!')
        confirm_password_input = driver.find_element(By.NAME, 'confirm_password')
        confirm_password_input.send_keys('NewPassword123!')
        reset_password_button = driver.find_element(By.ID, 'reset-password')
        reset_password_button.click()
        logging.info('New password set and reset password button clicked.')
    except Exception as e:
        logging.error(f'Error setting new password: {e}')  

    # Step 8: Check for confirmation message
    try:
        confirmation_message = driver.find_element(By.ID, 'confirmation-message')
        assert confirmation_message.is_displayed(), 'Confirmation message not displayed'
        logging.info('Confirmation message displayed.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')
    except Exception as e:
        logging.error(f'Error checking confirmation message: {e}')  

    # Step 9: Log in with the new password
    try:
        driver.get('https://your-application-url.com/login')
        email_input = driver.find_element(By.NAME, 'email')
        email_input.send_keys('user@example.com')
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys('NewPassword123!')
        login_button = driver.find_element(By.ID, 'login')
        login_button.click()
        logging.info('Logged in with new password.')
    except Exception as e:
        logging.error(f'Error logging in with new password: {e}')  

    # Step 10: Check for successful login
    try:
        dashboard = driver.find_element(By.ID, 'dashboard')
        assert dashboard.is_displayed(), 'Dashboard not displayed, login failed'
        logging.info('Dashboard displayed, login successful.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')
    except Exception as e:
        logging.error(f'Error checking dashboard display: {e}')  

finally:
    driver.quit()