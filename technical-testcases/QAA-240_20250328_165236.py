""" 
Title: User logs in successfully
Environment Variables: valid_username=your_username
valid_password=your_password
Notes: This test case verifies that a user can log in successfully and is redirected to the Candidate Profile page. Ensure to replace 'valid_username' and 'valid_password' with actual credentials for testing.
Assignee: Ritesh Gond
"""

import time
from playwright.sync_api import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    try:
        # Navigate to the login page
        print("Navigating to the login page...")
        page.goto('https://example.com/login')
    except Exception as e:
        print(f"Error navigating to login page: {e}")

    try:
        # Enter valid credentials
        print("Entering valid credentials...")
        page.fill('input[name="username"]', 'valid_username')
        page.fill('input[name="password"]', 'valid_password')
    except Exception as e:
        print(f"Error entering credentials: {e}")

    try:
        # Click the login button
        print("Clicking the login button...")
        page.click('button[type="submit"]')
    except Exception as e:
        print(f"Error clicking login button: {e}")

    try:
        # Wait for navigation to the Candidate Profile page
        print("Waiting for navigation to the Candidate Profile page...")
        page.wait_for_navigation()
    except Exception as e:
        print(f"Error waiting for navigation: {e}")

    try:
        # Check if redirected to the Candidate Profile page
        assert page.url == 'https://example.com/candidate-profile', "User was not redirected to the Candidate Profile page"
        print("Successfully redirected to the Candidate Profile page.")
    except AssertionError as e:
        print(e)

    try:
        # Check if the profile elements are displayed
        assert page.is_visible('h1:has-text("Candidate Profile")'), "Candidate Profile header is not displayed"
        print("Candidate Profile header is displayed.")
    except AssertionError as e:
        print(e)

    # Close the browser
    print("Closing the browser...")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)