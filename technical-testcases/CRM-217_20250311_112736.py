""" 
Title: Automated Test Case for Password Reset Feature
Environment Variables: N/A
Notes: This test case automates the password reset process and verifies each step of the user story. Ensure to replace 'https://your-application-url.com' with the actual application URL and adjust element locators as necessary.
Assignee: pranav
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

# Initialize the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Navigate to the login page
    try:
        driver.get('https://your-application-url.com/login')
        logging.info('Navigated to the login page.')
    except Exception as e:
        logging.error(f'Error navigating to login page: {e}')

    # Step 2: Click on 'Forgot Password' link
    try:
        forgot_password_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Forgot Password')))
        forgot_password_link.click()
        logging.info('Clicked on Forgot Password link.')
    except Exception as e:
        logging.error(f'Error clicking Forgot Password link: {e}')

    # Step 3: Enter registered email address
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email')))
        email_input.send_keys('user@example.com')
        logging.info('Entered registered email address.')
    except Exception as e:
        logging.error(f'Error entering email address: {e}')

    # Step 4: Submit the form
    try:
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'submit')))
        submit_button.click()
        logging.info('Submitted the form.')
    except Exception as e:
        logging.error(f'Error submitting the form: {e}')

    # Step 5: Check for success message
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'success-message')))
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

    # Step 6: Simulate user clicking the link in the email and setting a new password
    try:
        driver.get('https://your-application-url.com/reset-password?token=sampletoken')
        new_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'new_password')))
        new_password_input.send_keys('NewPassword123!')
        confirm_password_input = driver.find_element(By.NAME, 'confirm_password')
        confirm_password_input.send_keys('NewPassword123!')
        reset_button = driver.find_element(By.ID, 'reset')
        reset_button.click()
        logging.info('Reset password form submitted.')
    except Exception as e:
        logging.error(f'Error resetting password: {e}')

    # Step 7: Check for confirmation message
    try:
        confirmation_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'confirmation-message')))
        assert confirmation_message.is_displayed(), 'Confirmation message not displayed'
        logging.info('Confirmation message displayed.')
    except Exception as e:
        logging.error(f'Error checking confirmation message: {e}')

    # Step 8: Log in with the new password
    try:
        driver.get('https://your-application-url.com/login')
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email')))
        email_input.send_keys('user@example.com')
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys('NewPassword123!')
        login_button = driver.find_element(By.ID, 'login')
        login_button.click()
        logging.info('Logged in with new password.')
    except Exception as e:
        logging.error(f'Error logging in with new password: {e}')

    # Step 9: Check for successful login
    try:
        dashboard = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'dashboard')))
        assert dashboard.is_displayed(), 'Dashboard not displayed, login failed'
        logging.info('Dashboard displayed, login successful.')
    except Exception as e:
        logging.error(f'Error checking dashboard: {e}')

finally:
    # Close the driver
    driver.quit()