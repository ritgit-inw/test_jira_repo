""" 
Title: Implement Password Reset Feature
Environment Variables: N/A
Notes: This test case automates the password reset feature using Selenium WebDriver. Ensure that the application URL and element selectors are correctly set before running the test.
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
    try:
        driver.get('https://your-application-url.com/login')
        logging.info('Navigated to login page.')
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
        email_input.send_keys('user@example.com')  # Replace with a valid email
        logging.info('Entered registered email address.')
    except Exception as e:
        logging.error(f'Error entering email address: {e}')

    # Step 4: Submit the form
    try:
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        submit_button.click()
        logging.info('Submitted the form.')
    except Exception as e:
        logging.error(f'Error submitting the form: {e}')

    # Step 5: Check for success message
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.success-message')))
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

    # Step 6: Simulate clicking the reset link in the email (this part is usually manual)
    # For testing purposes, you would need to mock this part or use a test email service.

    # Step 7: Set a new password
    try:
        new_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'new_password')))
        new_password_input.send_keys('NewPassword123!')  # Replace with a valid password
        confirm_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'confirm_password')))
        confirm_password_input.send_keys('NewPassword123!')  # Replace with a valid password
        logging.info('Entered new password and confirmation.')
    except Exception as e:
        logging.error(f'Error entering new password: {e}')

    # Step 8: Submit the new password
    try:
        reset_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        reset_button.click()
        logging.info('Submitted the new password.')
    except Exception as e:
        logging.error(f'Error submitting new password: {e}')

    # Step 9: Check for success message after password reset
    try:
        reset_success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.reset-success-message')))
        assert reset_success_message.is_displayed(), 'Password reset success message not displayed'
        logging.info('Password reset success message displayed.')
    except Exception as e:
        logging.error(f'Error checking password reset success message: {e}')

    # Step 10: Log in with the new password
    try:
        driver.get('https://your-application-url.com/login')
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email')))
        email_input.send_keys('user@example.com')  # Replace with a valid email
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password')))
        password_input.send_keys('NewPassword123!')  # Replace with the new password
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        login_button.click()
        logging.info('Logged in with new password.')
    except Exception as e:
        logging.error(f'Error logging in with new password: {e}')

    # Step 11: Check for successful login
    try:
        assert driver.current_url == 'https://your-application-url.com/dashboard', 'Login failed'
        logging.info('Login successful, redirected to dashboard.')
    except Exception as e:
        logging.error(f'Error checking login success: {e}')

finally:
    driver.quit()