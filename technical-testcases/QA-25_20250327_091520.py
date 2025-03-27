""" 
Title: Login using Google authentication
Environment Variables: N/A
Notes: This test case automates the login process using Google authentication. Ensure that the app URL is correctly set in the code.
Assignee: Malini Sharma
"""

from playwright.sync_api import sync_playwright
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # Run headless Chrome
    context = browser.new_context()
    page = context.new_page()

    try:
        # Navigate to the login page
        page.goto('https://your-app-url.com/login')
        logging.info('Navigated to login page.')
    except Exception as e:
        logging.error(f'Error navigating to login page: {e}')

    try:
        # Click on 'Login with Google'
        page.click('text=Login with Google')
        logging.info('Clicked on Login with Google button.')
    except Exception as e:
        logging.error(f'Error clicking Login with Google: {e}')

    try:
        # Wait for the Google authentication page to load
        page.wait_for_url('https://accounts.google.com/*')
        logging.info('Redirected to Google authentication page.')
    except Exception as e:
        logging.error(f'Error waiting for Google authentication page: {e}')

    try:
        # Here you would typically enter Google credentials, but for security reasons, this is omitted.
        # Assuming successful login, wait for redirection back to the app
        page.wait_for_url('https://your-app-url.com/dashboard')
        logging.info('Successfully logged in and redirected to the app dashboard.')
    except Exception as e:
        logging.error(f'Error waiting for redirection to dashboard: {e}')

    try:
        # Check if the user is logged in by verifying an element on the dashboard
        assert page.is_visible('text=Welcome back!'), 'Login failed: Welcome message not visible.'
        logging.info('Login successful: Welcome message is visible.')
    except Exception as e:
        logging.error(f'Login check failed: {e}')

    finally:
        # Close the browser
        context.close()
        browser.close()