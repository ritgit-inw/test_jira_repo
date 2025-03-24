""" 
Title: User registers successfully
Environment Variables: N/A
Notes: This test case verifies that a user can register successfully. It checks for the presence of a success message after registration.
Assignee: Malini Sharma
"""

import logging
from playwright.sync_api import sync_playwright

# Configure logging
logging.basicConfig(level=logging.INFO)


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    try:
        logging.info('Navigating to the registration page.')
        page.goto('https://example.com/register')

        logging.info('Filling in the registration form.')
        page.fill('input[name="username"]', 'testuser')
        page.fill('input[name="email"]', 'testuser@example.com')
        page.fill('input[name="password"]', 'SecurePassword123')
        page.fill('input[name="confirm_password"]', 'SecurePassword123')

        logging.info('Submitting the registration form.')
        page.click('button[type="submit"]')

        logging.info('Waiting for navigation to the login page.')
        page.wait_for_navigation()

        logging.info('Checking for successful registration message.')
        assert page.locator('text=Registration successful!').is_visible()
        logging.info('Registration successful!')
    except Exception as e:
        logging.error(f'An error occurred: {e}')
    finally:
        logging.info('Closing the browser.')
        context.close()
        browser.close()


with sync_playwright() as playwright:
    run(playwright)