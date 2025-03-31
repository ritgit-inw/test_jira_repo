""" 
Title: User registers successfully
Environment Variables: Playwright installed, Python 3.12
Notes: Ensure that the email used for registration is valid and not already in use. Adjust the URL and selectors as per the actual application.
Assignee: Malini Sharma
"""

import time
from playwright.sync_api import sync_playwright

# Test case for user registration

def test_user_registration():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            # Navigate to the registration page
            print('Navigating to the registration page...')
            page.goto('https://example.com/registration')
            
            # Enter valid email and password
            print('Filling in the registration form...')
            page.fill('input[name="email"]', 'testuser@example.com')
            page.fill('input[name="password"]', 'SecurePassword123')
            
            # Click the register button
            print('Clicking the register button...')
            page.click('button[type="submit"]')
            
            # Wait for the confirmation message
            print('Waiting for the confirmation message...')
            page.wait_for_selector('text=Account created successfully!')
            
            # Check for confirmation email message
            assert page.is_visible('text=Account created successfully!')
            print('Registration successful, confirmation message is visible.')
        except Exception as e:
            print(f'An error occurred: {e}')
        finally:
            # Close the browser
            print('Closing the browser...')
            browser.close()

# Run the test case
if __name__ == '__main__':
    test_user_registration()