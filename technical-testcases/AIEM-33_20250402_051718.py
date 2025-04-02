""" 
Title: User accesses the login page
Environment Variables: N/A
Notes: This test case verifies that the user is redirected to the login page when clicking the 'View Profile' button on the homepage.
Assignee: Malini Sharma
"""

import logging
from playwright.sync_api import sync_playwright

# Configure logging
logging.basicConfig(level=logging.INFO)

def run_tests():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        try:
            logging.info('Navigating to the application portal homepage.')
            page.goto('https://your-application-portal.com')

            logging.info('Clicking the View Profile button.')
            page.click('text=View Profile')

            logging.info('Expecting to be redirected to the login page.')
            assert page.url == 'https://your-application-portal.com/login'

            logging.info('Checking for the presence of an error message.')
            error_message = page.locator('.error-message')
            assert not error_message.is_visible(), 'Error message should not be displayed.'

        except Exception as e:
            logging.error(f'An error occurred: {e}')

        finally:
            logging.info('Closing the browser.')
            browser.close()

if __name__ == '__main__':
    run_tests()