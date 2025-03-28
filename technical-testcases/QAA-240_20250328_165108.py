""" 
Title: User registers successfully
Environment Variables: PLAYWRIGHT_BROWSERS_PATH=0
Notes: This test case verifies that a user can successfully register by entering a valid email and password, and checks for a success message after registration.
Assignee: Ritesh Gond
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

        # Enter valid email and password
        print("Filling in the registration form...")
        page.fill('input[name="email"]', 'testuser@example.com')
        page.fill('input[name="password"]', 'SecurePassword123')

        # Click the register button
        print("Clicking the register button...")
        page.click('button[type="submit"]')

        # Wait for the confirmation email (this is a placeholder, actual implementation may vary)
        print("Waiting for the confirmation email...")
        page.wait_for_timeout(5000)  # Adjust time as necessary for email confirmation

        # Check for success message or confirmation
        print("Checking for success message...")
        assert page.is_visible('text=Registration successful!'), "Success message not visible"
        print("Registration successful message is visible.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        print("Closing the browser...")
        context.close()
        browser.close()


with sync_playwright() as playwright:
    run(playwright)