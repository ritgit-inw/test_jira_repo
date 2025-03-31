""" 
Title: User updates personal information
Environment Variables: BASE_URL=https://example.com
Notes: Ensure that the user is logged in before running this test. The CV file path should be valid and accessible.
Assignee: Malini Sharma
"""

import logging
from playwright.sync_api import sync_playwright

# Configure logging
logging.basicConfig(level=logging.INFO)

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    try:
        logging.info('Navigating to the login page.')
        page.goto('https://example.com/login')

        logging.info('Logging in as a job seeker.')
        page.fill('input[name="username"]', 'jobseeker@example.com')
        page.fill('input[name="password"]', 'password123')
        page.click('button[type="submit"]')

        logging.info('Waiting for navigation to the profile page.')
        page.wait_for_navigation()

        logging.info('Navigating to the profile page.')
        page.goto('https://example.com/profile')

        logging.info('Updating required fields.')
        page.fill('input[name="first_name"]', 'John')
        page.fill('input[name="last_name"]', 'Doe')
        page.fill('input[name="education"]', 'Bachelor of Science in Computer Science')
        page.set_input_files('input[type="file"]', 'path/to/cv.pdf')

        logging.info('Clicking save button.')
        page.click('button[type="submit"]')

        logging.info('Validating the success message.')
        success_message = page.locator('text=Candidate Profile saved successfully')
        assert success_message.is_visible()
        logging.info('Success message is visible.')
    except Exception as e:
        logging.error(f'An error occurred: {e}')
    finally:
        logging.info('Closing the browser.')
        browser.close()

with sync_playwright() as playwright:
    run(playwright)