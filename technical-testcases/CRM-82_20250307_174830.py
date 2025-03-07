""" 
Title: Implement Password Reset Feature
Environment Variables: Python 3.12, Selenium, ChromeDriver, WebDriver Manager
Notes: This test case automates the password reset feature, including requesting a reset link, resetting the password, and logging in with the new password.
Assignee: Prakhar Soni
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
    # Step 1: Navigate to the password reset page
    driver.get('https://yourapp.com/password-reset')
    logging.info('Navigated to password reset page.')

    # Step 2: Request a password reset link
    try:
        email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
        email_input.send_keys('user@example.com')
        request_button = driver.find_element(By.ID, 'request-reset')
        request_button.click()
        logging.info('Requested password reset link.')
    except Exception as e:
        logging.error(f'Error requesting password reset link: {e}')  

    # Wait for the email to be sent
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'success-message')))

    # Step 3: Check for success message
    try:
        success_message = driver.find_element(By.ID, 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')  

    # Simulate user clicking the reset link in the email
    driver.get('https://yourapp.com/reset-password?token=valid_token')
    logging.info('Navigated to reset password link.')

    # Step 4: Set a new password
    try:
        new_password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'new_password')))
        new_password_input.send_keys('NewPassword123!')
        confirm_password_input = driver.find_element(By.NAME, 'confirm_password')
        confirm_password_input.send_keys('NewPassword123!')
        reset_button = driver.find_element(By.ID, 'reset-password')
        reset_button.click()
        logging.info('New password set and reset button clicked.')
    except Exception as e:
        logging.error(f'Error setting new password: {e}')  

    # Wait for the password to be reset
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'reset-success-message')))

    # Step 5: Check for success message after reset
    try:
        reset_success_message = driver.find_element(By.ID, 'reset-success-message')
        assert reset_success_message.is_displayed(), 'Reset success message not displayed'
        logging.info('Reset success message displayed.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')
    except Exception as e:
        logging.error(f'Error checking reset success message: {e}')  

    # Step 6: Log in with the new password
    driver.get('https://yourapp.com/login')
    logging.info('Navigated to login page.')
    try:
        login_email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
        login_email_input.send_keys('user@example.com')
        login_password_input = driver.find_element(By.NAME, 'password')
        login_password_input.send_keys('NewPassword123!')
        login_button = driver.find_element(By.ID, 'login')
        login_button.click()
        logging.info('Login attempted with new password.')
    except Exception as e:
        logging.error(f'Error during login: {e}')  

    # Wait for login to complete
    WebDriverWait(driver, 10).until(EC.url_to_be('https://yourapp.com/dashboard'))

    # Check for successful login
    try:
        assert driver.current_url == 'https://yourapp.com/dashboard', 'Login failed: User not redirected to dashboard'
        logging.info('Login successful, redirected to dashboard.')
    except AssertionError as e:
        logging.error(f'Assertion error: {e}')
    except Exception as e:
        logging.error(f'Error checking login success: {e}')

finally:
    driver.quit()