""" 
Title: Login with Google Authentication
Environment Variables: N/A
Notes: This test case verifies the login functionality using Google authentication. Ensure that the app URL is correctly set in the code.
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
        logging.error(f'Error clicking Login with Google button: {e}')

    try:
        # Wait for the Google authentication page to load
        page.wait_for_url('https://accounts.google.com/*')
        logging.info('Redirected to Google authentication page.')
    except Exception as e:
        logging.error(f'Error waiting for Google authentication page: {e}')

    try:
        # Simulate successful login (this part may vary based on your app's flow)
        page.fill('input[type="email"]', 'your-email@example.com')
        logging.info('Filled in email address.')
        page.click('button[type="submit"]')
        logging.info('Clicked on submit button for email.')
        page.fill('input[type="password"]', 'your-password')
        logging.info('Filled in password.')
        page.click('button[type="submit"]')
        logging.info('Clicked on submit button for password.')
    except Exception as e:
        logging.error(f'Error during login process: {e}')

    try:
        # Check if the user is logged in by verifying a specific element is visible
        if page.is_visible('text=Logout'):
            logging.info('User is logged in successfully.')
        else:
            logging.warning('User is not logged in.')
    except Exception as e:
        logging.error(f'Error checking login status: {e}')

    try:
        # Logout process
        page.click('text=Logout')
        logging.info('Clicked on Logout button.')
    except Exception as e:
        logging.error(f'Error clicking Logout button: {e}')

    # Close the browser
    context.close()
    browser.close()