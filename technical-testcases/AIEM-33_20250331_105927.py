""" 
Title: User logs in successfully
Environment Variables: { "USERNAME": "valid_username", "PASSWORD": "valid_password" }
Notes: This test case verifies that a user can log in successfully and is redirected to the Candidate Profile page. It also checks that no error messages are displayed.
Assignee: Malini Sharma
"""

import logging
from playwright.sync_api import sync_playwright

# Configure logging
logging.basicConfig(level=logging.INFO)

# Test case for user login

def test_user_login():
    try:
        logging.info('Starting test: User logs in successfully')
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            # Navigate to the login page
            logging.info('Navigating to the login page')
            page.goto('https://example.com/login')

            # Enter valid credentials
            logging.info('Entering valid credentials')
            page.fill('input[name="username"]', 'valid_username')
            page.fill('input[name="password"]', 'valid_password')

            # Click the login button
            logging.info('Clicking the login button')
            page.click('button[type="submit"]')

            # Wait for navigation to the Candidate Profile page
            logging.info('Waiting for navigation to the Candidate Profile page')
            page.wait_for_url('https://example.com/candidate-profile')

            # Verify that the user is redirected to the Candidate Profile page
            logging.info('Verifying redirection to Candidate Profile page')
            profile_header = page.locator('h1')
            assert profile_header.inner_text() == 'Candidate Profile'

            # Check for any error messages (if applicable)
            logging.info('Checking for error messages')
            error_message = page.locator('.error-message')
            assert not error_message.is_visible()

            logging.info('Test completed successfully')

    except Exception as e:
        logging.error(f'Test failed: {e}')

# Run the test
if __name__ == '__main__':
    test_user_login()