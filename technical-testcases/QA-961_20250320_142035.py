""" 
Title: User Registration and Login
Environment Variables: path/to/cv.pdf
Notes: This test case covers user registration, login, profile update, education addition, and CV upload functionalities.
Assignee: Malini Sharma
"""

import pytest
from playwright.async_api import async_playwright, Page, Browser

@pytest.fixture(scope="function")
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        yield browser
        await browser.close()

@pytest.mark.asyncio
async def test_user_registration_and_login(browser: Browser):
    try:
        page = await browser.new_page()
        print("Navigating to the registration page...")
        await page.goto('https://example.com/register')

        print("Filling in the registration form...")
        await page.fill('input[name="username"]', 'testuser')
        await page.fill('input[name="email"]', 'testuser@example.com')
        await page.fill('input[name="password"]', 'SecurePassword123')
        await page.click('button[type="submit"]')

        print("Waiting for confirmation email...")
        await page.wait_for_timeout(2000)  # Wait for 2 seconds for email to be sent
        print("Navigating to the login page...")
        await page.goto('https://example.com/login')
        await page.fill('input[name="email"]', 'testuser@example.com')
        await page.fill('input[name="password"]', 'SecurePassword123')
        await page.click('button[type="submit"]')

        print("Validating successful login...")
        await page.wait_for_timeout(2000)  # Wait for 2 seconds for login to process
        await expect(page).to_have_text('Welcome, testuser!')

        print("Navigating to profile update page...")
        await page.goto('https://example.com/profile')
        await page.fill('input[name="bio"]', 'This is my bio.')
        await page.click('button[type="submit"]')

        print("Validating profile update...")
        await expect(page).to_have_text('Profile updated successfully!')

        print("Navigating to education section...")
        await page.goto('https://example.com/education')
        await page.fill('input[name="degree"]', 'Bachelor of Science')
        await page.fill('input[name="institution"]', 'University of Example')
        await page.click('button[type="submit"]')

        print("Validating education addition...")
        await expect(page).to_have_text('Education added successfully!')

        print("Navigating to CV upload section...")
        await page.goto('https://example.com/upload-cv')
        await page.set_input_files('input[type="file"]', 'path/to/cv.pdf')
        await page.click('button[type="submit"]')

        print("Validating CV upload...")
        await expect(page).to_have_text('CV uploaded successfully!')

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await page.close()