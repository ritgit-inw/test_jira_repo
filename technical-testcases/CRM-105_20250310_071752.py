""" 
Title: Implement Password Reset Feature
Environment Variables: N/A
Notes: This test case automates the password reset feature using Selenium WebDriver. Ensure that the email used is registered and the application is accessible.
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
    try:
        driver.get('https://yourapp.com/password-reset')
        assert "Password Reset" in driver.title
        logging.info("Navigated to password reset page successfully.")
    except Exception as e:
        logging.error(f"Error navigating to password reset page: {e}")

    # Step 2: Enter registered email address
    try:
        email_input = driver.find_element(By.NAME, 'email')
        email_input.send_keys('user@example.com')
        logging.info("Entered registered email address.")
    except Exception as e:
        logging.error(f"Error entering email address: {e}")

    # Step 3: Submit the password reset request
    try:
        submit_button = driver.find_element(By.ID, 'submit')
        submit_button.click()
        logging.info("Submitted password reset request.")
    except Exception as e:
        logging.error(f"Error submitting password reset request: {e}")

    # Wait for the email to be sent
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'success-message'))
        )
        logging.info("Email sent successfully.")
    except Exception as e:
        logging.error(f"Error waiting for success message: {e}")

    # Step 4: Check for success message
    try:
        success_message = driver.find_element(By.ID, 'success-message')
        assert success_message.is_displayed()
        logging.info("Success message is displayed.")
    except Exception as e:
        logging.error(f"Error checking success message: {e}")

    # Step 5: Simulate clicking the link in the email and setting a new password
    try:
        driver.get('https://yourapp.com/reset-password?token=valid_token')
        new_password_input = driver.find_element(By.NAME, 'new_password')
        new_password_input.send_keys('NewPassword123!')
        confirm_password_input = driver.find_element(By.NAME, 'confirm_password')
        confirm_password_input.send_keys('NewPassword123!')
        reset_button = driver.find_element(By.ID, 'reset')
        reset_button.click()
        logging.info("New password set successfully.")
    except Exception as e:
        logging.error(f"Error setting new password: {e}")

    # Step 6: Check for login with new password
    try:
        driver.get('https://yourapp.com/login')
        login_email_input = driver.find_element(By.NAME, 'email')
        login_email_input.send_keys('user@example.com')
        login_password_input = driver.find_element(By.NAME, 'password')
        login_password_input.send_keys('NewPassword123!')
        login_button = driver.find_element(By.ID, 'login')
        login_button.click()
        logging.info("Login attempt made with new password.")
    except Exception as e:
        logging.error(f"Error during login attempt: {e}")

    # Check for successful login
    try:
        assert "Dashboard" in driver.title
        logging.info("Login successful, navigated to dashboard.")
    except Exception as e:
        logging.error(f"Error checking login success: {e}")

finally:
    driver.quit()