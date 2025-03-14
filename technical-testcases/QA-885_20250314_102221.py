""" 
Title: Implement username Reset Feature
Environment Variables: Selenium WebDriver, Chrome, Python 3.12
Notes: Ensure that the email used is registered and the new username is unique.
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Navigate to the username reset page
    driver.get('http://example.com/reset-username')
    logging.info('Navigated to the username reset page.')

    # Step 1: Enter registered email address
    try:
        email_input = driver.find_element(By.ID, 'email')
        email_input.send_keys('user@example.com')
        email_input.send_keys(Keys.RETURN)
        logging.info('Entered registered email address.')
    except Exception as e:
        logging.error(f'Error entering email address: {e}')  

    # Wait for the email to be processed
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'success-message')))

    # Step 2: Check for success message
    try:
        success_message = driver.find_element(By.ID, 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')  

    # Step 3: Simulate clicking the reset link in the email
    driver.get('http://example.com/reset-username-link')
    logging.info('Navigated to the reset username link.')

    # Step 4: Enter new username
    try:
        new_username_input = driver.find_element(By.ID, 'new-username')
        new_username_input.send_keys('new_username')
        new_username_input.send_keys(Keys.RETURN)
        logging.info('Entered new username.')
    except Exception as e:
        logging.error(f'Error entering new username: {e}')  

    # Wait for the username to be processed
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'error-message')))

    # Step 5: Check for error message if username is not unique
    try:
        error_message = driver.find_element(By.ID, 'error-message')
        assert error_message.is_displayed(), 'Error message not displayed for non-unique username'
        logging.info('Error message displayed for non-unique username.')
    except Exception as e:
        logging.error(f'Error checking error message: {e}')  

    # Step 6: Enter a unique username
    try:
        new_username_input.clear()
        new_username_input.send_keys('unique_username')
        new_username_input.send_keys(Keys.RETURN)
        logging.info('Entered unique username.')
    except Exception as e:
        logging.error(f'Error entering unique username: {e}')  

    # Wait for the username to be processed
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'success-message')))

    # Step 7: Check for success message
    try:
        success_message = driver.find_element(By.ID, 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed after username reset'
        logging.info('Success message displayed after username reset.')
    except Exception as e:
        logging.error(f'Error checking success message after username reset: {e}')  

finally:
    # Close the browser
    driver.quit()
    logging.info('Browser closed.')