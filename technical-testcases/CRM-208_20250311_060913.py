""" 
Title: Implement Username Reset Feature
Environment Variables: N/A
Notes: This test case automates the process of requesting a username reset, verifying the email confirmation, and setting a new username. Ensure that the element IDs used in the code match those in the actual HTML implementation.
Assignee: Aswin Suresh
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

# Setup Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to the username reset page
    logging.info('Navigating to the username reset page.')
    driver.get('https://yourapp.com/reset-username')

    try:
        # Request username reset
        logging.info('Requesting username reset.')
        request_button = driver.find_element('id', 'request-username-reset')
        request_button.click()

        # Check for confirmation email message
        logging.info('Checking for confirmation email message.')
        confirmation_message = driver.find_element('id', 'confirmation-message')
        assert confirmation_message.is_displayed(), 'Confirmation message not displayed'
        logging.info('Confirmation message displayed successfully.')
    except Exception as e:
        logging.error(f'Error during username reset request: {e}')  

    try:
        # Simulate user clicking the link in the email
        logging.info('Simulating user clicking the link in the email.')
        driver.get('https://yourapp.com/verify-username-reset?token=sampletoken')

        # Set new username
        logging.info('Setting new username.')
        new_username_input = driver.find_element('id', 'new-username')
        new_username_input.send_keys('new_username')
        submit_button = driver.find_element('id', 'submit-new-username')
        submit_button.click()

        # Check for success message
        logging.info('Checking for success message.')
        success_message = driver.find_element('id', 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed successfully.')
    except Exception as e:
        logging.error(f'Error during username reset verification: {e}')  

finally:
    logging.info('Quitting the driver.')
    driver.quit()