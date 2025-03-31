""" 
Title: User updates personal information
Environment Variables: NODE_ENV=test
Notes: This test case covers the user story of updating personal information in the profile. Ensure that the Playwright environment is set up correctly and that the necessary selectors match the actual HTML elements on the page.
Assignee: Ritesh Gond
"""

import asyncio
from playwright.async_api import async_playwright, Page

async def run_test():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        try:
            # Navigate to the login page
            print('Navigating to the login page...')
            await page.goto('https://example.com/login')

            # Log in as a job seeker
            print('Filling in login credentials...')
            await page.fill('input[name="username"]', 'jobseeker@example.com')
            await page.fill('input[name="password"]', 'password123')
            await page.click('button[type="submit"]')

            # Wait for navigation to the profile page
            print('Waiting for navigation to the profile page...')
            await page.wait_for_navigation()

            # Navigate to the profile page
            print('Navigating to the profile page...')
            await page.goto('https://example.com/profile')

            # Update required fields
            print('Updating personal information...')
            await page.fill('input[name="first_name"]', 'John')
            await page.fill('input[name="last_name"]', 'Doe')
            await page.fill('input[name="email"]', 'john.doe@example.com')
            await page.fill('input[name="phone"]', '1234567890')

            # Click save
            print('Saving updated information...')
            await page.click('button[type="submit"]')

            # Validate the success message
            print('Validating success message...')
            success_message = await page.locator('text=Candidate Profile saved successfully')
            assert await success_message.is_visible(), 'Success message not visible'
            print('Success message is visible.')

        except Exception as e:
            print(f'An error occurred: {e}')

        finally:
            await browser.close()

if __name__ == '__main__':
    asyncio.run(run_test())