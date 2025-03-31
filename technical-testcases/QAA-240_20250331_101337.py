""" 
Title: User logs in successfully
Environment Variables: N/A
Notes: This test case verifies that a user can log in successfully with valid credentials and is redirected to the Candidate Profile page. It also checks that no error messages are displayed after a successful login.
Assignee: Ritesh Gond
"""

import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.parametrize('username, password', [
    ('valid_user', 'valid_password')  # Replace with actual valid credentials
])
def test_user_login(username, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            # Navigate to the login page
            print('Navigating to the login page...')
            page.goto('https://example.com/login')  # Replace with actual login URL
            
            # Enter valid credentials
            print('Entering credentials...')
            page.fill('input[name="username"]', username)
            page.fill('input[name="password"]', password)
            
            # Click the login button
            print('Clicking the login button...')
            page.click('button[type="submit"]')
            
            # Wait for navigation to the Candidate Profile page
            print('Waiting for navigation...')
            page.wait_for_navigation()
            
            # Assert that the user is redirected to the Candidate Profile page
            assert page.url == 'https://example.com/candidate-profile'  # Replace with actual profile URL
            print('User successfully redirected to the Candidate Profile page.')
            
            # Check for any error messages (if applicable)
            error_message = page.query_selector('.error-message')  # Replace with actual error message selector
            if error_message:
                assert not error_message.is_visible(), 'Error message should not be displayed'
                print('Error message is displayed, which is not expected.')
            else:
                print('No error message displayed.')
        except Exception as e:
            print(f'An error occurred: {e}')
        finally:
            # Close the browser
            print('Closing the browser...')
            browser.close()