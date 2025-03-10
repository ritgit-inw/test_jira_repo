""" 
Title: Automated Test Case for Username Reset Feature
Environment Variables: Python 3.12, Selenium, Chrome
Notes: This test case automates the process of resetting a username, including requesting a reset, verifying via email, and updating the username.
Assignee: Malini Sharma
"""

import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run headless Chrome
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Setup Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Navigate to the username reset page
    try:
        driver.get('https://yourapp.com/username-reset')
        logging.info('Navigated to the username reset page.')
    except Exception as e:
        logging.error(f'Error navigating to username reset page: {e}')

    # Step 2: Request a username reset
    try:
        email_input = driver.find_element('id', 'email')  # Assuming the input field has id='email'
        email_input.send_keys('user@example.com')  # Replace with a valid email
        request_button = driver.find_element('id', 'request-reset')  # Assuming the button has id='request-reset'
        request_button.click()
        logging.info('Requested a username reset.')
    except (NoSuchElementException, TimeoutException) as e:
        logging.error(f'Error requesting username reset: {e}')

    # Step 3: Check for verification email sent message
    try:
        success_message = driver.find_element('id', 'success-message')  # Assuming the success message has id='success-message'
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')
    except (NoSuchElementException, AssertionError) as e:
        logging.error(f'Error checking success message: {e}')

    # Step 4: Simulate clicking the link in the verification email
    try:
        driver.get('https://yourapp.com/username-reset/verify?token=valid_token')  # Replace with a valid token
        logging.info('Navigated to the verification link.')
    except Exception as e:
        logging.error(f'Error navigating to verification link: {e}')

    # Step 5: Set a new username
    try:
        new_username_input = driver.find_element('id', 'new-username')  # Assuming the input field has id='new-username'
        new_username_input.send_keys('new_username')  # Replace with a new username
        set_username_button = driver.find_element('id', 'set-username')  # Assuming the button has id='set-username'
        set_username_button.click()
        logging.info('Set a new username.')
    except (NoSuchElementException, TimeoutException) as e:
        logging.error(f'Error setting new username: {e}')

    # Step 6: Check for username update success message
    try:
        update_message = driver.find_element('id', 'update-message')  # Assuming the update message has id='update-message'
        assert update_message.is_displayed(), 'Update message not displayed'
        logging.info('Update message displayed.')
    except (NoSuchElementException, AssertionError) as e:
        logging.error(f'Error checking update message: {e}')

finally:
    driver.quit()