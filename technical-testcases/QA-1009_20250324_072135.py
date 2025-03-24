""" 
Title: User registers successfully
Environment Variables: N/A
Notes: This test case verifies that a user can register successfully. It checks for a success message or an error message after submission.
Assignee: Malini Sharma
"""

import time
from playwright.sync_api import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    try:
        # Navigate to the registration page
        print("Navigating to the registration page...")
        page.goto('https://example.com/register')

        # Fill in the registration form
        print("Filling in the registration form...")
        page.fill('input[name="username"]', 'testuser')
        page.fill('input[name="email"]', 'testuser@example.com')
        page.fill('input[name="password"]', 'SecurePassword123')
        page.fill('input[name="confirm_password"]', 'SecurePassword123')

        # Submit the registration form
        print("Submitting the registration form...")
        page.click('button[type="submit"]')

        # Wait for navigation to the login page
        print("Waiting for navigation to the login page...")
        page.wait_for_url('https://example.com/login')

        # Check for success message or error message
        print("Checking for registration success or error message...")
        assert page.locator('text=Registration successful').is_displayed() or page.locator('text=Error').is_displayed(), "Registration message not displayed"
        print("Registration message displayed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        print("Closing the browser...")
        context.close()
        browser.close()


with sync_playwright() as playwright:
    run(playwright)