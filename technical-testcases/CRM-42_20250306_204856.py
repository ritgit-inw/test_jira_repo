""" 
Title: Implement Password Reset Feature
Environment Variables: Python 3.12, WebSelenium, Chrome
Notes: This test case automates the password reset feature, including requesting a reset link, setting a new password, and logging in with the new password.
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
    # Step 1: Navigate to the login page
    try:
        driver.get('https://your-application-url.com/login')
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

    # Step 3: Enter email address to request password reset
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'email')))
        email_input.send_keys('user@example.com')  # Replace with actual email
        request_reset_button = driver.find_element(By.ID, 'request-reset')  # Replace with actual ID
        request_reset_button.click()
        logging.info('Requested password reset.')
    except Exception as e:
        logging.error(f'Error requesting password reset: {e}')

    # Step 4: Check for success message
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'success-message')))
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

    # Step 5: Simulate receiving the email and clicking the reset link
    try:
        driver.get('https://your-application-url.com/reset-password?token=mock-token')  # Replace with actual token
        logging.info('Navigated to reset password page.')
    except Exception as e:
        logging.error(f'Error navigating to reset password page: {e}')

    # Step 6: Set a new password
    try:
        new_password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'new-password')))
        new_password_input.send_keys('NewPassword123!')  # Replace with actual password
        confirm_password_input = driver.find_element(By.ID, 'confirm-password')  # Replace with actual ID
        confirm_password_input.send_keys('NewPassword123!')  # Replace with actual password
        reset_password_button = driver.find_element(By.ID, 'reset-password')  # Replace with actual ID
        reset_password_button.click()
        logging.info('Password reset requested.')
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
            EC.visibility_of_element_located((By.ID, 'email')))
        email_input.send_keys('user@example.com')  # Replace with actual email
        password_input = driver.find_element(By.ID, 'password')  # Replace with actual ID
        password_input.send_keys('NewPassword123!')  # Replace with actual password
        login_button = driver.find_element(By.ID, 'login')  # Replace with actual ID
        login_button.click()
        logging.info('Logged in with new password.')
    except Exception as e:
        logging.error(f'Error logging in with new password: {e}')

    # Step 9: Check for successful login
    try:
        assert driver.current_url == 'https://your-application-url.com/dashboard', 'Login failed'
        logging.info('Login successful, redirected to dashboard.')
    except Exception as e:
        logging.error(f'Error checking login success: {e}')

finally:
    driver.quit()