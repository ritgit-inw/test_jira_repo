""" 
Title: Implement Password Reset Feature
Environment Variables: N/A
Notes: This test case automates the password reset feature, including email submission and new password setting.
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
    logging.info('Navigating to the login page.')
    driver.get('https://your-application-url.com/login')

    # Step 2: Click on 'Forgot Password' link
    try:
        logging.info('Clicking on the Forgot Password link.')
        forgot_password_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Forgot Password')))
        forgot_password_link.click()
    except Exception as e:
        logging.error(f'Error clicking Forgot Password link: {e}')  

    # Step 3: Enter registered email address
    try:
        logging.info('Entering registered email address.')
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email')))
        email_input.send_keys('user@example.com')  # Replace with a valid email
    except Exception as e:
        logging.error(f'Error entering email address: {e}')  

    # Step 4: Submit the form
    try:
        logging.info('Submitting the form.')
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'submit')))
        submit_button.click()
    except Exception as e:
        logging.error(f'Error submitting the form: {e}')  

    # Wait for email to be sent
    logging.info('Waiting for email to be sent.')
    time.sleep(5)  # This should be replaced with a better wait

    # Step 5: Check for success message
    try:
        logging.info('Checking for success message.')
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'success-message')))
        assert success_message.is_displayed(), 'Success message not displayed'
    except Exception as e:
        logging.error(f'Error checking success message: {e}')  

    # Simulate user clicking the reset link in the email
    driver.get('https://your-application-url.com/reset-password?token=valid_token')  # Replace with actual token

    # Step 6: Set a new password
    try:
        logging.info('Setting a new password.')
        new_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'new_password')))
        new_password_input.send_keys('NewPassword123!')  # Replace with a valid password
    except Exception as e:
        logging.error(f'Error setting new password: {e}')  

    # Step 7: Confirm new password
    try:
        logging.info('Confirming new password.')
        confirm_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'confirm_password')))
        confirm_password_input.send_keys('NewPassword123!')  # Replace with a valid password
    except Exception as e:
        logging.error(f'Error confirming new password: {e}')  

    # Step 8: Submit the new password
    try:
        logging.info('Submitting the new password.')
        reset_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'reset-button')))
        reset_button.click()
    except Exception as e:
        logging.error(f'Error submitting new password: {e}')  

    # Wait for reset confirmation
    logging.info('Waiting for reset confirmation.')
    time.sleep(5)  

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
            EC.presence_of_element_located((By.NAME, 'email')))
        email_input.send_keys('user@example.com')
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password')))
        password_input.send_keys('NewPassword123!')
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'login-button')))
        login_button.click()
    except Exception as e:
        logging.error(f'Error logging in: {e}')  

    # Wait for login confirmation
    logging.info('Waiting for login confirmation.')
    time.sleep(5)  

    # Check for successful login
    try:
        assert driver.current_url == 'https://your-application-url.com/dashboard', 'Login failed'
        logging.info('Login successful.')
    except Exception as e:
        logging.error(f'Error checking login success: {e}')  

finally:
    logging.info('Quitting the driver.')
    driver.quit()