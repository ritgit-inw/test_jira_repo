""" 
Title: User accesses the login page
Environment Variables: N/A
Notes: This test case covers the user login functionality, including form visibility and error message handling.
Assignee: Malini Sharma
"""

import time
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        # Navigate to the login page
        print('Navigating to the login page...')
        page.goto('https://example.com/login')

        # Check if the login form is displayed
        if page.locator('form#login').is_visible():
            print('Login form is displayed.')
        else:
            print('Login form is not displayed.')
            return

        # Fill in the registration form
        print('Filling in the login form...')
        page.fill('input[name="username"]', 'testuser')
        page.fill('input[name="password"]', 'password123')

        # Click the login button
        print('Clicking the login button...')
        page.click('button[type="submit"]')

        # Wait for navigation after login
        print('Waiting for navigation after login...')
        page.wait_for_navigation()

        # Check if the user is redirected to the profile page
        if page.url == 'https://example.com/profile':
            print('User is redirected to the profile page.')
        else:
            print('User is not redirected to the profile page.')

        # Check for any error messages
        if page.locator('.error-message').is_visible():
            print('Error message displayed:', page.locator('.error-message').inner_text())
        else:
            print('No error messages displayed.')

    except Exception as e:
        print('An error occurred:', e)
    finally:
        # Close the browser
        print('Closing the browser...')
        browser.close()

with sync_playwright() as playwright:
    run(playwright)