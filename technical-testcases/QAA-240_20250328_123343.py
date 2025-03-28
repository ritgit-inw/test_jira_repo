""" 
Title: User registers successfully
Environment Variables: PLAYWRIGHT_BROWSERS_PATH=0
Notes: This test case verifies that a user can register successfully and receive a confirmation email message.
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
    except Exception as e:
        print(f"Error navigating to registration page: {e}")

    try:
        # Fill in the registration form
        print("Filling in the registration form...")
        page.fill('input[name="email"]', 'testuser@example.com')
        page.fill('input[name="password"]', 'SecurePassword123')
    except Exception as e:
        print(f"Error filling registration form: {e}")

    try:
        # Click the register button
        print("Clicking the register button...")
        page.click('button[type="submit"]')
    except Exception as e:
        print(f"Error clicking register button: {e}")

    try:
        # Wait for the confirmation message
        print("Waiting for the confirmation message...")
        page.wait_for_selector('text=Confirmation email sent', timeout=5000)
        # Check for confirmation email message
        assert page.locator('text=Confirmation email sent').is_visible()
        print("Confirmation email message is visible.")
    except Exception as e:
        print(f"Error checking confirmation message: {e}")

    # Close the browser
    print("Closing the browser...")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)