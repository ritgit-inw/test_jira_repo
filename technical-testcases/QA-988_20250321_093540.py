""" 
Title: Automated Test Case for Username Reset Feature
Environment Variables: Selenium WebDriver, Chrome, Python 3.12
Notes: Ensure that the email service is mocked or that the test environment can handle email sending.
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the login page
    try:
        driver.get('http://example.com/login')  # Replace with the actual login page URL
        logging.info('Navigated to the login page.')
    except Exception as e:
        logging.error(f'Error navigating to login page: {e}')

    # Step 2: Click on 'Forgot Username' link
    try:
        forgot_username_link = driver.find_element(By.LINK_TEXT, 'Forgot Username')
        forgot_username_link.click()
        logging.info('Clicked on the Forgot Username link.')
    except Exception as e:
        logging.error(f'Error clicking Forgot Username link: {e}')

    # Step 3: Enter the email address associated with the account
    try:
        email_input = driver.find_element(By.NAME, 'email')  # Adjust the selector as needed
        email_input.send_keys('user@example.com')  # Replace with a valid email
        email_input.send_keys(Keys.RETURN)
        logging.info('Entered email address and submitted.')
    except Exception as e:
        logging.error(f'Error entering email address: {e}')

    # Step 4: Wait for the confirmation message
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'confirmation-message')))
        confirmation_message = driver.find_element(By.ID, 'confirmation-message')
        assert confirmation_message.is_displayed(), 'Confirmation message not displayed'
        logging.info('Confirmation message displayed successfully.')
    except Exception as e:
        logging.error(f'Error waiting for confirmation message: {e}')

    # Simulate email link click (this would normally be done outside of this test)
    time.sleep(5)  # Wait for the email to be received (in a real scenario, you would check the email)
    driver.get('http://example.com/reset-username?token=valid_token')  # Replace with the actual reset link
    logging.info('Navigated to the reset username page.')

    # Step 5: Enter a new username
    try:
        new_username_input = driver.find_element(By.NAME, 'new_username')  # Adjust the selector as needed
        new_username_input.send_keys('new_username')  # Replace with a valid new username
        new_username_input.send_keys(Keys.RETURN)
        logging.info('Entered new username and submitted.')
    except Exception as e:
        logging.error(f'Error entering new username: {e}')

    # Step 6: Wait for the success message
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'success-message')))
        success_message = driver.find_element(By.ID, 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed successfully.')
    except Exception as e:
        logging.error(f'Error waiting for success message: {e}')

    # Step 7: Validate the uniqueness and format of the new username
    # This would typically involve checking the database or API, which is not covered in this test
    logging.info('Username validation step is not implemented.')

finally:
    # Close the browser
    driver.quit()
    logging.info('Browser closed.')