""" 
Title: User accesses the login page
Environment Variables: N/A
Notes: This test case verifies that the user is redirected to the login page when they click the 'View Profile' button on the homepage.
Assignee: Malini Sharma
"""

import logging
from playwright.sync_api import sync_playwright

# Configure logging
logging.basicConfig(level=logging.INFO)

def test_user_accesses_login_page():
    try:
        logging.info('Starting test: User accesses the login page')
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            # Navigate to the application portal homepage
            logging.info('Navigating to the application portal homepage')
            page.goto('https://your-application-portal-url.com')

            # Click on the 'View Profile' button
            logging.info('Clicking on the View Profile button')
            page.click('text=View Profile')

            # Expect to be redirected to the login page
            logging.info('Expecting to be redirected to the login page')
            assert page.url == 'https://your-application-portal-url.com/login'

            # Check for the presence of an error message if applicable
            logging.info('Checking for the presence of an error message')
            error_message = page.locator('.error-message')  # Adjust the selector as needed
            assert error_message.is_visible()

            logging.info('Test completed successfully')
    except Exception as e:
        logging.error(f'Test failed with error: {e}')
    finally:
        browser.close()

# Run the test
if __name__ == '__main__':
    test_user_accesses_login_page()