""" 
Title: User logs in successfully
Environment Variables: N/A
Notes: This test case verifies that a user can log in successfully and is redirected to the Candidate Profile page without any error messages.
Assignee: Malini Sharma
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


def test_user_login(setup):
    page = setup
    try:
        # Navigate to the login page
        print("Navigating to the login page...")
        page.goto("https://example.com/login")

        # Enter valid credentials
        print("Entering valid credentials...")
        page.fill("input[name='username']", "valid_username")
        page.fill("input[name='password']", "valid_password")

        # Click the login button
        print("Clicking the login button...")
        page.click("button[type='submit']")

        # Wait for navigation to the Candidate Profile page
        print("Waiting for navigation to the Candidate Profile page...")
        page.wait_for_navigation()

        # Assert that the user is redirected to the Candidate Profile page
        assert page.url == "https://example.com/candidate-profile"
        print("User successfully redirected to the Candidate Profile page.")

        # Check for any error messages
        error_message = page.locator(".error-message")
        assert not error_message.is_visible()
        print("No error messages displayed.")
    except Exception as e:
        print(f"An error occurred during the test: {e}")