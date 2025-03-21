""" 
Title: User Registration and Login
Environment Variables: pytest, playwright
Notes: This test case covers both valid and invalid login scenarios, ensuring that the application behaves as expected.
Assignee: Malini Sharma
"""

import pytest
from playwright.sync_api import sync_playwright, expect
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Fixture for browser setup and teardown
@pytest.fixture(scope="function")
def browser_setup():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

# Test case for user login functionality
@pytest.mark.parametrize("username, password, expected_text, should_fail", [
    ("valid_user", "valid_password", "Welcome to your dashboard", False),
    ("invalid_user", "invalid_password", "Invalid username or password", True)
])
def test_user_login(browser, username, password, expected_text, should_fail):
    try:
        logging.info("Starting test for user login")
        page = browser.new_page()
        page.goto('https://example.com/login')

        # Check if username and password fields are present
        assert page.locator('input[name="username"]').is_visible()
        assert page.locator('input[name="password"]').is_visible()

        # Fill in the credentials
        page.fill('input[name="username"]', username)
        page.fill('input[name="password"]', password)
        page.click('button[type="submit"]')

        # Validate redirection and messages
        if not should_fail:
            page.wait_for_url('https://example.com/dashboard')
            expect(page).to_have_text(expected_text)
        else:
            expect(page.locator('.error-message')).to_be_visible()
            expect(page).to_have_text(expected_text)

        logging.info("Test completed successfully")
    except Exception as e:
        logging.error(f"Test failed: {e}")
    finally:
        page.close()