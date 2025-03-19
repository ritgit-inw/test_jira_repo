""" 
Title: Implement Password Reset Feature
Environment Variables: Selenium WebDriver, Chrome, Python 3.12
Notes: Ensure that the email used for testing is registered in the system and that the reset link is valid.
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
    # Navigate to the password reset page
    driver.get('https://example.com/password-reset')
    print('Navigated to password reset page.')

    try:
        # Enter the registered email address
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        email_input.send_keys('user@example.com')
        print('Entered email address.')

        # Click the reset password button
        reset_button = driver.find_element(By.ID, 'reset-button')
        reset_button.click()
        print('Clicked reset password button.')

        # Wait for the email validation message
        email_error = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'email-error'))
        )
        if email_error.is_displayed():
            print('Email validation error displayed: ', email_error.text)
        else:
            print('Email validation passed, check your inbox for the reset link.')
    except Exception as e:
        print('Error during email validation process:', e)

    try:
        # Simulate clicking the reset link in the email (this would normally be done in a real email client)
        driver.get('https://example.com/reset-link')
        print('Navigated to reset link.')

        # Enter a new password
        new_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'new-password'))
        )
        new_password_input.send_keys('NewPassword123!')
        print('Entered new password.')

        # Confirm the new password
        confirm_password_input = driver.find_element(By.NAME, 'confirm-password')
        confirm_password_input.send_keys('NewPassword123!')
        print('Confirmed new password.')

        # Click the submit button
        submit_button = driver.find_element(By.ID, 'submit-button')
        submit_button.click()
        print('Clicked submit button.')

        # Wait for the success message
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'success-message'))
        )
        if success_message.is_displayed():
            print('Password reset successful: ', success_message.text)
        else:
            print('Password reset failed.')
    except Exception as e:
        print('Error during password reset process:', e)

finally:
    # Close the browser
    driver.quit()
    print('Browser closed.')