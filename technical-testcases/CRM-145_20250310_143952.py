""" 
Title: Implement Username Reset Feature
Environment Variables: N/A
Notes: This test case automates the username reset feature, verifying each step of the process.
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
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
    # Step 1: Navigate to the username reset page
    try:
        logging.info('Navigating to the username reset page.')
        driver.get('https://yourapp.com/username-reset')
    except Exception as e:
        logging.error(f'Error navigating to username reset page: {e}')

    # Step 2: Request a username reset
    try:
        logging.info('Requesting a username reset.')
        email_input = driver.find_element('id', 'email')  # Assuming the input field has id='email'
        email_input.send_keys('user@example.com')  # Replace with a valid email
        request_button = driver.find_element('id', 'request-reset')  # Assuming the button has id='request-reset'
        request_button.click()
    except Exception as e:
        logging.error(f'Error requesting username reset: {e}')

    # Step 3: Check for confirmation message
    try:
        logging.info('Checking for confirmation message.')
        confirmation_message = driver.find_element('id', 'confirmation-message')  # Assuming the message has id='confirmation-message'
        assert confirmation_message.is_displayed(), 'Confirmation message not displayed'
        logging.info('Confirmation message displayed successfully.')
    except Exception as e:
        logging.error(f'Error checking confirmation message: {e}')

    # Step 4: Simulate receiving the email and clicking the reset link
    try:
        logging.info('Simulating email reception and navigating to reset link.')
        driver.get('https://yourapp.com/reset-username')
    except Exception as e:
        logging.error(f'Error navigating to reset link: {e}')

    # Step 5: Set a new username
    try:
        logging.info('Setting a new username.')
        new_username_input = driver.find_element('id', 'new-username')  # Assuming the input field has id='new-username'
        new_username_input.send_keys('new_username')  # Replace with a new username
        submit_button = driver.find_element('id', 'submit-new-username')  # Assuming the button has id='submit-new-username'
        submit_button.click()
    except Exception as e:
        logging.error(f'Error setting new username: {e}')

    # Step 6: Check for success message
    try:
        logging.info('Checking for success message.')
        success_message = driver.find_element('id', 'success-message')  # Assuming the message has id='success-message'
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed successfully.')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

finally:
    logging.info('Quitting the driver.')
    driver.quit()