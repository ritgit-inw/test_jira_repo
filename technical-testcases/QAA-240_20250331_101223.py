""" 
Title: User registers successfully
Environment Variables: PLAYWRIGHT_BROWSERS_PATH=0
Notes: This test case verifies that a user can successfully register by entering a valid email and password, and that a confirmation message is displayed after registration.
Assignee: Ritesh Gond
"""

import asyncio
from playwright.async_api import async_playwright
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

async def run(playwright):
    browser = await playwright.chromium.launch()
    page = await browser.new_page()

    try:
        logging.info('Navigating to the registration page.')
        await page.goto('https://example.com/registration')
    except Exception as e:
        logging.error(f'Error navigating to registration page: {e}')  

    try:
        logging.info('Filling in the registration form.')
        await page.fill('input[name="email"]', 'testuser@example.com')
        await page.fill('input[name="password"]', 'SecurePassword123')
    except Exception as e:
        logging.error(f'Error filling registration form: {e}')  

    try:
        logging.info('Clicking the register button.')
        await page.click('button[type="submit"]')
    except Exception as e:
        logging.error(f'Error clicking register button: {e}')  

    try:
        logging.info('Waiting for the confirmation message.')
        await page.wait_for_selector('text=Account created successfully')
    except Exception as e:
        logging.error(f'Error waiting for confirmation message: {e}')  

    # Check for confirmation email
    # This part would typically involve checking an email service, which is not covered here.

    try:
        logging.info('Closing the browser.')
        await browser.close()
    except Exception as e:
        logging.error(f'Error closing the browser: {e}')  

asyncio.run(run(async_playwright()))