""" 
Title: Implement Username Reset Feature
Environment Variables: N/A
Notes: This test case automates the username reset feature, ensuring that the user can request a reset, receive a verification email, and set a new username successfully.
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
        driver.get('https://yourapp.com/reset-username')
    except Exception as e:
        logging.error(f'Error navigating to reset page: {e}')

    # Step 2: Request a username reset
    try:
        logging.info('Requesting a username reset.')
        email_input = driver.find_element('id', 'email')  # Assuming the input field has id='email'
        email_input.send_keys('user@example.com')  # Replace with a valid email
        request_button = driver.find_element('id', 'request-reset')  # Assuming the button has id='request-reset'
        request_button.click()
    except Exception as e:
        logging.error(f'Error requesting username reset: {e}')

    # Step 3: Check for verification email sent message
    try:
        logging.info('Checking for success message after requesting reset.')
        success_message = driver.find_element('id', 'success-message')  # Assuming the success message has id='success-message'
        assert success_message.is_displayed(), 'Success message not displayed'
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

    # Step 4: Simulate user clicking the link in the email and setting a new username
    try:
        logging.info('Navigating to set new username page.')
        driver.get('https://yourapp.com/set-new-username')  # Navigate to the new username page
        new_username_input = driver.find_element('id', 'new-username')  # Assuming the input field has id='new-username'
        new_username_input.send_keys('new_username')  # Replace with a new username
        set_username_button = driver.find_element('id', 'set-username')  # Assuming the button has id='set-username'
        set_username_button.click()
    except Exception as e:
        logging.error(f'Error setting new username: {e}')

    # Step 5: Check for confirmation message
    try:
        logging.info('Checking for confirmation message after setting new username.')
        confirmation_message = driver.find_element('id', 'confirmation-message')  # Assuming the confirmation message has id='confirmation-message'
        assert confirmation_message.is_displayed(), 'Confirmation message not displayed'
    except Exception as e:
        logging.error(f'Error checking confirmation message: {e}')

finally:
    # Close the driver
    logging.info('Closing the driver.')
    driver.quit()