""" 
Title: Test summary content of CRM
Environment Variables: Python 3.12, WebSelenium, Chrome
Notes: This test case checks for the presence of JavaScript load error messages on the CRM page.
Assignee: Prakhar Soni
"""

import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run headless Chrome
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())

def main():
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        # Navigate to the CRM page
        url = 'https://akademe.atlassian.net/browse/CRM-1'
        logging.info(f'Navigating to {url}')
        driver.get(url)

        # Check for error messages
        try:
            error_message = driver.find_element(By.ID, 'javaScriptLoadError')
            if error_message.is_displayed():
                logging.error('JavaScript load error is displayed.')
            else:
                logging.info('No JavaScript load error.')
        except Exception as e:
            logging.error('Error checking for JavaScript load error: %s', e)

    except Exception as e:
        logging.error('An error occurred during the main execution: %s', e)
    finally:
        # Close the driver
        driver.quit()
        logging.info('Driver closed.')

if __name__ == '__main__':
    main()