""" 
Title: User adds an academic record
Environment Variables: PLAYWRIGHT_BROWSERS_PATH=0
Notes: This test case verifies that a user can successfully add an academic record to their profile and receive a success message.
Assignee: Ritesh Gond
"""

import logging
from playwright.sync_api import sync_playwright

# Configure logging
logging.basicConfig(level=logging.INFO)

# Test case for adding an academic record

def test_add_academic_record():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            logging.info('Navigating to the profile page...')
            page.goto('https://example.com/profile')

            logging.info('Clicking on the add button in the education section...')
            page.click('button#add-education')

            logging.info('Filling in the required fields...')
            page.fill('input#degree', 'Bachelor of Science')
            page.fill('input#institution', 'University of Example')
            page.fill('input#start-date', '2015-09-01')
            page.fill('input#end-date', '2019-06-01')

            logging.info('Clicking save...')
            page.click('button#save-education')

            logging.info('Checking for success message...')
            success_message = page.locator('text=Candidate Profile saved successfully')
            assert success_message.is_visible(), 'Success message not visible'
            logging.info('Success message is visible.')

            logging.info('Checking if the academic record is displayed in the education section...')
            education_record = page.locator('text=Bachelor of Science')
            assert education_record.is_visible(), 'Education record not visible'
            logging.info('Education record is visible.')

    except Exception as e:
        logging.error(f'An error occurred: {e}')
    finally:
        browser.close()

# Run the test
if __name__ == '__main__':
    test_add_academic_record()