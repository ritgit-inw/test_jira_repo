""" 
Title: User accesses the login page
Environment Variables: N/A
Notes: This test case covers the user login functionality, including error message display. Ensure that the Playwright library is installed and configured properly.
Assignee: Malini Sharma
"""

from playwright.sync_api import sync_playwright
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to run the test case
def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        try:
            logging.info('Navigating to the login page')
            page.goto('https://example.com/login')

            logging.info('Checking if the login form is displayed')
            login_form = page.locator('#login-form')
            assert login_form.is_visible()

            logging.info('Filling in the login form')
            page.fill('#username', 'testuser')
            page.fill('#password', 'password123')

            logging.info('Submitting the form')
            page.click('#login-button')

            logging.info('Checking for error message if login fails')
            error_message = page.locator('#error-message')
            assert error_message.is_visible()

            logging.info('Checking if the user is redirected to the profile page after successful login')
            assert page.url == 'https://example.com/profile'

        except Exception as e:
            logging.error(f'An error occurred: {e}')

        finally:
            logging.info('Closing the browser')
            browser.close()

# Run the test
if __name__ == '__main__':
    run_test()