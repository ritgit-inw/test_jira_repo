""" 
Title: Automated Test Case for Password Reset Feature
Environment Variables: Python 3.12, Selenium, Chrome
Notes: This test case automates the password reset process and verifies each step of the flow.
Assignee: Aswin Suresh
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
        driver.get('https://id-frontend.prod-east.frontend.public.atl-paas.net/')
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

    # Step 3: Enter email address and submit
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email')))
        email_input.send_keys('user@example.com')  # Replace with a valid email
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()
        logging.info('Entered email and submitted the form.')
    except Exception as e:
        logging.error(f'Error entering email and submitting: {e}')

    # Wait for email to be sent (this should be replaced with a more robust wait)
    time.sleep(5)

    # Step 4: Check for success message
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.success-message')))
        assert success_message.is_displayed(), "Success message not displayed"
        logging.info('Success message displayed.')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

    # Step 5: Simulate clicking the link in the email and setting a new password
    try:
        new_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'new_password')))
        new_password_input.send_keys('NewPassword123!')  # Replace with a valid new password
        confirm_password_input = driver.find_element(By.NAME, 'confirm_password')
        confirm_password_input.send_keys('NewPassword123!')
        reset_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        reset_button.click()
        logging.info('New password set and form submitted.')
    except Exception as e:
        logging.error(f'Error setting new password: {e}')

    # Step 6: Check for confirmation message
    try:
        confirmation_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.confirmation-message')))
        assert confirmation_message.is_displayed(), "Confirmation message not displayed"
        logging.info('Confirmation message displayed.')
    except Exception as e:
        logging.error(f'Error checking confirmation message: {e}')

    # Step 7: Log in with the new password
    try:
        driver.get('https://id-frontend.prod-east.frontend.public.atl-paas.net/login')
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'username')))
        username_input.send_keys('user@example.com')  # Replace with the same email
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys('NewPassword123!')  # Use the new password
        login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        login_button.click()
        logging.info('Logged in with new password.')
    except Exception as e:
        logging.error(f'Error logging in with new password: {e}')

    # Step 8: Check for successful login
    try:
        dashboard_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.dashboard')))
        assert dashboard_element.is_displayed(), "Login failed, dashboard not displayed"
        logging.info('Dashboard displayed, login successful.')
    except Exception as e:
        logging.error(f'Error checking dashboard display: {e}')

finally:
    driver.quit()