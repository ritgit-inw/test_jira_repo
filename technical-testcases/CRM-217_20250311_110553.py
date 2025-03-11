""" 
Title: Implement Password Reset Feature
Environment Variables: N/A
Notes: This test case automates the password reset feature using Selenium WebDriver. Ensure that the application URL and element identifiers are correct before running the test.
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
        forgot_password_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Forgot Password?')))
        forgot_password_link.click()
        logging.info('Clicked on Forgot Password link.')
    except Exception as e:
        logging.error(f'Error clicking Forgot Password link: {e}')

    # Step 3: Enter email to request password reset
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email')))
        email_input.send_keys('user@example.com')
        request_reset_button = driver.find_element(By.ID, 'request-reset')
        request_reset_button.click()
        logging.info('Requested password reset for user@example.com.')
    except Exception as e:
        logging.error(f'Error requesting password reset: {e}')

    # Wait for email to be sent (this should be replaced with a better wait)
    time.sleep(5)

    # Step 4: Check for success message
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'success-message')))
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

    # Simulate user clicking the link in the email (this part is usually manual)
    driver.get('https://yourapp.com/reset-password?token=exampletoken')

    # Step 5: Set new password
    try:
        new_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'new_password')))
        new_password_input.send_keys('NewPassword123!')
        confirm_password_input = driver.find_element(By.NAME, 'confirm_password')
        confirm_password_input.send_keys('NewPassword123!')
        reset_password_button = driver.find_element(By.ID, 'reset-password')
        reset_password_button.click()
        logging.info('Password reset successfully.')
    except Exception as e:
        logging.error(f'Error resetting password: {e}')

    # Step 6: Check for login success
    try:
        login_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'login-message')))
        assert login_message.is_displayed(), 'Login message not displayed'
        logging.info('Login message displayed.')
    except Exception as e:
        logging.error(f'Error checking login message: {e}')

finally:
    # Close the driver
    driver.quit()
    logging.info('Driver closed.')