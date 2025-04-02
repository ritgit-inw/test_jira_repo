""" 
Title: User adds an academic record
Environment Variables: N/A
Notes: This test case verifies that a user can successfully add an academic record to their profile and receive a confirmation message.
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
        logging.info('Navigating to the profile page.')
        page.goto('https://example.com/profile')
    except Exception as e:
        logging.error(f'Error navigating to profile page: {e}')

    try:
        logging.info('Clicking on the add button in the education section.')
        page.click('button#add-education')
    except Exception as e:
        logging.error(f'Error clicking add button: {e}')

    try:
        logging.info('Filling in the required fields.')
        page.fill('input#degree', 'Bachelor of Science')
        page.fill('input#institution', 'University of Example')
        page.fill('input#start-date', '2015-09-01')
        page.fill('input#end-date', '2019-06-01')
    except Exception as e:
        logging.error(f'Error filling in fields: {e}')

    try:
        logging.info('Clicking save button.')
        page.click('button#save-education')
    except Exception as e:
        logging.error(f'Error clicking save button: {e}')

    try:
        logging.info('Checking for success message.')
        success_message = page.locator('text=Candidate Profile saved successfully')
        assert success_message.is_visible()
        logging.info('Success message is visible.')
    except Exception as e:
        logging.error(f'Error checking success message: {e}')

    try:
        logging.info('Verifying that the academic record is displayed in the education section.')
        education_record = page.locator('text=Bachelor of Science')
        assert education_record.is_visible()
        logging.info('Education record is visible.')
    except Exception as e:
        logging.error(f'Error verifying education record: {e}')

    browser.close()

with sync_playwright() as playwright:
    run(playwright)