""" 
Title: Test summary content of CRM
Environment Variables: Python 3.12, Selenium, Chrome
Notes: This test case checks for the display of JavaScript load error messages on the CRM page.
Assignee: Prakhar Soni
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run headless Chrome
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Set up the Chrome driver
try:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    logging.info('Chrome driver initialized successfully.')
except Exception as e:
    logging.error('Failed to initialize Chrome driver: %s', e)
    driver = None

if driver:
    try:
        # Navigate to the CRM page
        url = 'https://akademe.atlassian.net/browse/CRM-1'
        driver.get(url)
        logging.info('Navigated to URL: %s', url)

        # Check for the presence of error messages
        try:
            error_message = driver.find_element(By.ID, 'javaScriptLoadError')
            if error_message.is_displayed():
                logging.info('JavaScript load error is displayed.')
            else:
                logging.info('No JavaScript load error.')
        except Exception as e:
            logging.warning('Error message not found: %s', e)
    finally:
        # Close the driver
        driver.quit()
        logging.info('Chrome driver closed.')