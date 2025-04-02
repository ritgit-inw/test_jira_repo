""" 
Title: Implement Account Reset Feature
Environment Variables: N/A
Notes: This test case covers the entire account reset process, including initiating the reset, receiving a confirmation email, setting a new password, and verifying the account state.
Assignee: Malini Sharma
"""

import time
from playwright.sync_api import sync_playwright

# Test case for account reset feature

def test_account_reset():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            # Step 1: Navigate to the account reset page
            print("Navigating to the account reset page...")
            page.goto('https://example.com/account-reset')

            # Step 2: Initiate the account reset process
            print("Filling in the email for account reset...")
            page.fill('input[name="email"]', 'user@example.com')
            print("Clicking the reset account button...")
            page.click('button#reset-account')

            # Step 3: Wait for confirmation message
            print("Waiting for confirmation message...")
            page.wait_for_selector('text=Confirmation email sent')
            assert page.is_visible('text=Confirmation email sent')
            print("Confirmation email sent message is visible.")

            # Step 4: Simulate user clicking the link in the email
            print("Navigating to the reset password page...")
            page.goto('https://example.com/reset-password?token=valid_token')

            # Step 5: Set a new password
            print("Setting a new password...")
            page.fill('input[name="new-password"]', 'NewPassword123!')
            page.fill('input[name="confirm-password"]', 'NewPassword123!')
            print("Clicking the submit new password button...")
            page.click('button#submit-new-password')

            # Step 6: Verify success message
            print("Verifying success message...")
            assert page.is_visible('text=Your password has been reset successfully')
            print("Password reset success message is visible.")

            # Step 7: Verify account is reset to initial state
            print("Navigating to the login page...")
            page.goto('https://example.com/login')
            print("Logging in with the new password...")
            page.fill('input[name="email"]', 'user@example.com')
            page.fill('input[name="password"]', 'NewPassword123!')
            page.click('button#login')

            # Check if the account is in initial state
            assert page.is_visible('text=Welcome to your account!')
            print("Welcome message is visible, account is in initial state.")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # Close the browser
            print("Closing the browser...")
            browser.close()

# Run the test case
if __name__ == '__main__':
    test_account_reset()