""" 
Title: Implement Password Reset Feature
Environment Variables: Selenium WebDriver, Chrome, Python 3.12
Notes: This test case covers the password reset functionality including email validation and password creation.
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome driver
try:
    driver = webdriver.Chrome()
    print('Chrome driver initialized successfully.')
except Exception as e:
    print('Error initializing Chrome driver:', e)
    exit(1)

# Function to log messages
def log(message):
    print(message)

# Test case 1: Navigate to the password reset page
try:
    driver.get('https://example.com/password-reset')
    log('Navigated to password reset page.')

    # Enter the registered email address
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'email'))
    )
    email_input.send_keys('user@example.com')
    log('Entered email address.')

    # Click the reset password button
    reset_button = driver.find_element(By.ID, 'reset-button')
    reset_button.click()
    log('Clicked reset password button.')

    # Wait for the email validation message
    email_error = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email-error'))
    )
    if email_error.is_displayed():
        log('Email validation error displayed: ' + email_error.text)
    else:
        log('Email validation passed, check your inbox for the reset link.')

except Exception as e:
    log('Error during password reset email process: ' + str(e))

# Test case 2: Simulate clicking the reset link in the email
try:
    driver.get('https://example.com/reset-link')
    log('Navigated to reset link page.')

    # Enter a new password
    new_password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'new-password'))
    )
    new_password_input.send_keys('NewPassword123!')
    log('Entered new password.')

    # Confirm the new password
    confirm_password_input = driver.find_element(By.NAME, 'confirm-password')
    confirm_password_input.send_keys('NewPassword123!')
    log('Confirmed new password.')

    # Click the submit button
    submit_button = driver.find_element(By.ID, 'submit-button')
    submit_button.click()
    log('Clicked submit button.')

    # Wait for the success message
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'success-message'))
    )
    if success_message.is_displayed():
        log('Password reset successful: ' + success_message.text)
    else:
        log('Password reset failed.')

except Exception as e:
    log('Error during password reset process: ' + str(e))

finally:
    # Close the browser
    driver.quit()
    log('Browser closed.')