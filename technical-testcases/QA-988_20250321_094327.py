""" 
Title: Implement username Reset Feature
Environment Variables: Selenium WebDriver, Chrome, Python 3.12
Notes: This test case automates the process of resetting a username and verifies the confirmation message. Ensure that the email sending and receiving functionalities are mocked or tested separately.
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the login page
    try:
        driver.get('http://example.com/login')
        logging.info('Navigated to the login page.')
    except Exception as e:
        logging.error(f'Error navigating to login page: {e}')

    # Step 2: Request a username reset
    try:
        reset_link = driver.find_element(By.LINK_TEXT, 'Forgot Username?')
        reset_link.click()
        logging.info('Clicked on the Forgot Username link.')
    except Exception as e:
        logging.error(f'Error clicking Forgot Username link: {e}')

    # Step 3: Enter the registered email address
    try:
        email_input = driver.find_element(By.NAME, 'email')
        email_input.send_keys('user@example.com')
        email_input.send_keys(Keys.RETURN)
        logging.info('Entered email address and submitted.')
    except Exception as e:
        logging.error(f'Error entering email address: {e}')

    # Step 4: Wait for the email to be sent (mocking this step)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email_sent_confirmation')))
        logging.info('Email sent confirmation received.')
    except Exception as e:
        logging.error(f'Error waiting for email sent confirmation: {e}')

    # Step 5: Simulate clicking the reset link in the email
    try:
        driver.get('http://example.com/reset-username?token=valid_token')
        logging.info('Navigated to the reset username page.')
    except Exception as e:
        logging.error(f'Error navigating to reset username page: {e}')

    # Step 6: Enter a new username
    try:
        new_username_input = driver.find_element(By.NAME, 'new_username')
        new_username_input.send_keys('new_username')
        new_username_input.send_keys(Keys.RETURN)
        logging.info('Entered new username and submitted.')
    except Exception as e:
        logging.error(f'Error entering new username: {e}')

    # Step 7: Check for confirmation message
    try:
        confirmation_message = driver.find_element(By.ID, 'confirmation')
        assert confirmation_message.is_displayed(), 'Confirmation message not displayed'
        logging.info('Confirmation message displayed successfully.')
    except Exception as e:
        logging.error(f'Error checking confirmation message: {e}')

    # Step 8: Check for email confirmation (mocking this step)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email_confirmation_received')))
        logging.info('Email confirmation received.')
    except Exception as e:
        logging.error(f'Error waiting for email confirmation: {e}')

finally:
    # Close the browser
    driver.quit()
    logging.info('Browser closed.')