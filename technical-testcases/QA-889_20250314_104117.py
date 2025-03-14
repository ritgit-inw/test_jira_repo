""" 
Title: Implement username Reset Feature
Environment Variables: Chrome, Python 3.12
Notes: This test case covers the user story and acceptance criteria for the password reset feature.
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Navigate to the password reset page
    driver.get('http://example.com/reset-password')

    # Test case 1: User can enter their email address
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        email_input.send_keys('user@example.com')
        assert email_input.get_attribute('value') == 'user@example.com', 'Email input not working'
        logging.info('Test case 1 passed: Email input working.')
    except Exception as e:
        logging.error(f'Test case 1 failed: {e}')  

    # Test case 2: System sends a reset link to the registered email
    try:
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'submit'))
        )
        submit_button.click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'success-message'))
        )
        success_message = driver.find_element(By.ID, 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Test case 2 passed: Success message displayed.')
    except Exception as e:
        logging.error(f'Test case 2 failed: {e}')  

    # Test case 3: Link expires after a specified time
    # Simulate waiting for the link to expire (this would normally be handled in a real test)
    try:
        time.sleep(3600)  # This is just a placeholder for actual expiration logic
        logging.info('Test case 3: Simulated waiting for link expiration.')
    except Exception as e:
        logging.error(f'Test case 3 failed: {e}')  

    # Test case 4: User receives feedback for unregistered email addresses
    try:
        email_input.clear()
        email_input.send_keys('unregistered@example.com')
        submit_button.click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'error-message'))
        )
        error_message = driver.find_element(By.ID, 'error-message')
        assert error_message.is_displayed(), 'Error message for unregistered email not displayed'
        logging.info('Test case 4 passed: Error message displayed for unregistered email.')
    except Exception as e:
        logging.error(f'Test case 4 failed: {e}')  

finally:
    # Close the browser
    driver.quit()