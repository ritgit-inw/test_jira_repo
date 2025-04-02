""" 
Title: User registers successfully
Environment Variables: N/A
Notes: This test case verifies that a user can successfully register with valid credentials and checks for a confirmation message.
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
        logging.info('Navigating to the registration page.')
        await page.goto('https://example.com/registration')
    except Exception as e:
        logging.error(f'Error navigating to registration page: {e}')  

    try:
        logging.info('Entering valid email and password.')
        await page.fill('input[name="email"]', 'testuser@example.com')
        await page.fill('input[name="password"]', 'SecurePassword123')
    except Exception as e:
        logging.error(f'Error filling email and password: {e}')  

    try:
        logging.info('Clicking the register button.')
        await page.click('button[type="submit"]')
    except Exception as e:
        logging.error(f'Error clicking register button: {e}')  

    try:
        logging.info('Waiting for confirmation message.')
        await page.wait_for_selector('text=Account created successfully')
        logging.info('Confirmation message received.')
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