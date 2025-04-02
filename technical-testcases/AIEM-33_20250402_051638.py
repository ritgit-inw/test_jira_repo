""" 
Title: User registers successfully
Environment Variables: N/A
Notes: This test case verifies that a user can successfully register with a valid email and password. It checks for the confirmation message after registration.
Assignee: Malini Sharma
"""

import asyncio
from playwright.async_api import async_playwright
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

async def run(playwright):
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()

    try:
        # Navigate to the registration page
        logging.info('Navigating to the registration page.')
        await page.goto('https://example.com/register')
    except Exception as e:
        logging.error(f'Error navigating to registration page: {e}')

    try:
        # Enter valid email and password
        logging.info('Filling in the email and password.')
        await page.fill('input[name="email"]', 'testuser@example.com')
        await page.fill('input[name="password"]', 'SecurePassword123')
    except Exception as e:
        logging.error(f'Error filling in email and password: {e}')

    try:
        # Click the register button
        logging.info('Clicking the register button.')
        await page.click('button[type="submit"]')
    except Exception as e:
        logging.error(f'Error clicking the register button: {e}')

    try:
        # Wait for the confirmation message
        logging.info('Waiting for the confirmation message.')
        await page.wait_for_selector('text=Account created successfully')
    except Exception as e:
        logging.error(f'Error waiting for confirmation message: {e}')

    # Check for confirmation email
    # This part would typically involve checking an email service, which is not covered here.

    try:
        # Close the browser
        logging.info('Closing the browser.')
        await browser.close()
    except Exception as e:
        logging.error(f'Error closing the browser: {e}')

asyncio.run(run(async_playwright()))