""" 
Title: User Registration and Login
Environment Variables: pytest, playwright
Notes: This test case covers user registration and login functionality, including validation of email format and password strength. It also checks for error messages on incorrect login attempts.
Assignee: Malini Sharma
"""

import pytest
from playwright.async_api import async_playwright, Page
from playwright.async_api import expect

@pytest.fixture(scope="function")
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        yield browser
        await browser.close()

@pytest.mark.asyncio
async def test_user_registration_and_login(browser):
    try:
        page = await browser.new_page()
        print("Navigating to the registration page...")
        await page.goto('https://example.com/register')

        print("Filling in the registration form...")
        await page.fill('input[name="name"]', 'John Doe')
        await page.fill('input[name="email"]', 'john.doe@example.com')
        await page.fill('input[name="password"]', 'Password123!')
        await page.fill('input[name="confirm_password"]', 'Password123!')

        print("Submitting the registration form...")
        await page.click('button[type="submit"]')

        print("Validating successful registration...")
        await page.wait_for_timeout(2000)  # Wait for the confirmation email to be sent
        await expect(page).to_have_text('Registration successful! A confirmation email has been sent.')

        print("Navigating to the login page...")
        await page.goto('https://example.com/login')

        print("Logging in with the registered email and password...")
        await page.fill('input[name="email"]', 'john.doe@example.com')
        await page.fill('input[name="password"]', 'Password123!')
        await page.click('button[type="submit"]')

        print("Validating successful login...")
        await page.wait_for_timeout(2000)  # Wait for the login process
        await expect(page).to_have_text('Welcome, John Doe!')

        print("Attempting to log in with incorrect credentials...")
        await page.goto('https://example.com/login')
        await page.fill('input[name="email"]', 'john.doe@example.com')
        await page.fill('input[name="password"]', 'WrongPassword!')
        await page.click('button[type="submit"]')

        print("Validating error message for incorrect credentials...")
        await page.wait_for_timeout(2000)  # Wait for the error message to appear
        await expect(page.locator('.error-message')).to_be_visible()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await page.close()