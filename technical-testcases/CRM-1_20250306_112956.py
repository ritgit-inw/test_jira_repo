""" 
Title: Test summary content of CRM
Environment Variables: Python 3.12, Selenium, Chrome
Notes: This test case checks for JavaScript load errors and noscript errors on the CRM page.
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
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to the CRM page
    driver.get('https://akademe.atlassian.net/browse/CRM-1')

    try:
        # Check for JavaScript load error message
        js_load_error = driver.find_element(By.ID, 'javaScriptLoadError')
        if js_load_error.is_displayed():
            logging.info('JavaScript load error is displayed.')
        else:
            logging.info('No JavaScript load error.')
    except Exception as e:
        logging.error('Error checking JavaScript load error: %s', e)

    try:
        # Check for noscript error message
        noscript_error = driver.find_element(By.CLASS_NAME, 'scriptLoadError')
        if noscript_error.is_displayed():
            logging.info('No JavaScript is enabled error is displayed.')
        else:
            logging.info('JavaScript is enabled.')
    except Exception as e:
        logging.error('Error checking noscript error: %s', e)

finally:
    # Clean up and close the browser
    driver.quit()