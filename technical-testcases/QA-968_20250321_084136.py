""" 
Title: Implement Password Reset Feature
Environment Variables: Selenium WebDriver, Chrome, Python 3.12
Notes: Ensure that the email used for testing is registered in the system.
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the login page
    try:
        driver.get('http://example.com/login')
        print('Navigated to the login page.')
    except Exception as e:
        print(f'Error navigating to login page: {e}')

    # Step 2: Click on the 'Forgot Password' link
    try:
        forgot_password_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Forgot Password')))
        forgot_password_link.click()
        print('Clicked on the Forgot Password link.')
    except Exception as e:
        print(f'Error clicking Forgot Password link: {e}')

    # Step 3: Enter the registered email address
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email')))
        email_input.send_keys('user@example.com')
        email_input.send_keys(Keys.RETURN)
        print('Entered email address and submitted.')
    except Exception as e:
        print(f'Error entering email address: {e}')

    # Step 4: Check for email existence validation message
    try:
        time.sleep(2)  # Wait for the response
        email_error_message = driver.find_element(By.ID, 'email-error')
        if email_error_message.is_displayed():
            print('Email validation error displayed.')
        else:
            print('Email is valid, reset link sent.')
    except Exception as e:
        print(f'Error checking email validation message: {e}')

    # Step 5: Simulate clicking the reset link in the email
    try:
        driver.get('http://example.com/reset-password?token=valid_token')
        print('Navigated to the reset password page.')
    except Exception as e:
        print(f'Error navigating to reset password page: {e}')

    # Step 6: Set a new password
    try:
        new_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'new_password')))
        new_password_input.send_keys('NewP@ssw0rd')
        new_password_input.send_keys(Keys.RETURN)
        print('Entered new password and submitted.')
    except Exception as e:
        print(f'Error entering new password: {e}')

    # Step 7: Check for success message
    try:
        time.sleep(2)  # Wait for the response
        success_message = driver.find_element(By.ID, 'success-message')
        if success_message.is_displayed():
            print('Password reset successful.')
        else:
            print('Password reset failed.')
    except Exception as e:
        print(f'Error checking success message: {e}')

finally:
    # Close the browser
    driver.quit()
    print('Browser closed.')