""" 
Title: User accesses the login page
Environment Variables: N/A
Notes: This test case verifies that the user can access the login page by clicking the 'View Profile' button on the homepage.
Assignee: Ritesh Gond
"""

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


def test_user_accesses_login_page(setup):
    page = setup
    try:
        # Navigate to the application portal homepage
        print("Navigating to the application portal homepage...")
        page.goto("https://example.com")  # Replace with the actual URL
        
        # Click the "View Profile" button
        print("Clicking the 'View Profile' button...")
        page.click("text=View Profile")
        
        # Assert that the user is redirected to the login page
        print("Asserting that the user is redirected to the login page...")
        assert page.url == "https://example.com/login"  # Replace with the actual login URL
        
        # Check for any error messages (if applicable)
        print("Checking for error messages...")
        error_message = page.locator(".error-message")  # Adjust the selector as needed
        assert not error_message.is_visible()  # Ensure no error message is displayed
    except Exception as e:
        print(f"An error occurred: {e}")

# Additional test cases can be added here with similar try-except structure and logging.