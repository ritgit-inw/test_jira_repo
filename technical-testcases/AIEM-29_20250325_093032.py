""" 
Title: User updates personal information
Environment Variables: NODE_ENV=test
Notes: This test case covers user registration, login, profile update, education addition, and CV upload scenarios. Ensure that the selectors used in the code match the actual HTML elements on the web page.
Assignee: Malini Sharma
"""

import asyncio
from playwright.async_api import async_playwright, expect

async def run_tests():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        try:
            print('Navigating to registration page...')
            await page.goto('https://example.com/register')
            await page.fill('#username', 'testuser')
            await page.fill('#email', 'testuser@example.com')
            await page.fill('#password', 'Password123')
            await page.click('#register-button')
            print('Checking for success message...')
            assert await page.locator('#success-message').is_visible()
            print('User registration successful.')
        except Exception as e:
            print(f'User Registration Error: {e}')

        try:
            print('Navigating to login page...')
            await page.goto('https://example.com/login')
            await page.fill('#email', 'testuser@example.com')
            await page.fill('#password', 'Password123')
            await page.click('#login-button')
            print('Checking for welcome message...')
            assert await page.locator('#welcome-message').is_visible()
            print('User login successful.')
        except Exception as e:
            print(f'User Login Error: {e}')

        try:
            print('Navigating to profile page...')
            await page.goto('https://example.com/profile')
            await page.fill('#first-name', 'Test')
            await page.fill('#last-name', 'User')
            await page.click('#update-button')
            print('Checking for update success message...')
            assert await page.locator('#update-success').is_visible()
            print('User information updated successfully.')
        except Exception as e:
            print(f'User Update Error: {e}')

        try:
            print('Navigating to education page...')
            await page.goto('https://example.com/profile/education')
            await page.fill('#degree', 'Bachelor of Science')
            await page.fill('#institution', 'University of Example')
            await page.fill('#year', '2023')
            await page.click('#add-education-button')
            print('Checking for education success message...')
            assert await page.locator('#education-success').is_visible()
            print('Education details added successfully.')
        except Exception as e:
            print(f'Education Addition Error: {e}')

        try:
            print('Navigating to CV upload page...')
            await page.goto('https://example.com/profile/upload-cv')
            await page.set_input_files('#cv-upload', 'path/to/cv.pdf')
            await page.click('#upload-button')
            print('Checking for upload success message...')
            assert await page.locator('#upload-success').is_visible()
            print('CV uploaded successfully.')
        except Exception as e:
            print(f'CV Upload Error: {e}')

        await page.close()
        await browser.close()

asyncio.run(run_tests())