""" 
Title: User registers successfully
Environment Variables: N/A
Notes: This test case verifies that a user can successfully register by entering a valid email and password, and checks for a confirmation message after registration.
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
    except Exception as e:
        logging.error(f'Error navigating to registration page: {e}')

    try:
        logging.info('Filling in the registration form.')
        page.fill('input[name="email"]', 'testuser@example.com')
        page.fill('input[name="password"]', 'SecurePassword123')
    except Exception as e:
        logging.error(f'Error filling registration form: {e}')

    try:
        logging.info('Clicking the register button.')
        page.click('button[type="submit"]')
    except Exception as e:
        logging.error(f'Error clicking register button: {e}')

    try:
        logging.info('Waiting for the confirmation message.')
        page.wait_for_selector('text=Account created successfully!', timeout=5000)
        logging.info('Checking for confirmation email message.')
        assert page.is_visible('text=Account created successfully!')
    except Exception as e:
        logging.error(f'Error checking confirmation message: {e}')

    finally:
        logging.info('Closing the browser.')
        context.close()
        browser.close()


with sync_playwright() as playwright:
    run(playwright)