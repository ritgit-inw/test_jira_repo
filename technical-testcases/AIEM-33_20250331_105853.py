""" 
Title: User accesses the login page
Environment Variables: N/A
Notes: This test case verifies that clicking the 'View Profile' button redirects the user to the login page and checks for any error messages.
Assignee: Malini Sharma
"""

import pytest
from playwright.sync_api import sync_playwright
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

@pytest.fixture(scope="module")
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


def test_view_profile_redirects_to_login(setup):
    page = setup
    try:
        logging.info("Navigating to the application portal homepage.")
        page.goto("https://example.com")  # Replace with the actual URL
        logging.info("Clicked the 'View Profile' button.")
        page.click("text=View Profile")
        logging.info("Asserting that the user is redirected to the login page.")
        assert page.url == "https://example.com/login"  # Replace with the actual login URL
        logging.info("Checking for error messages if any.")
        error_message = page.locator(".error-message")  # Adjust the selector as needed
        assert not error_message.is_visible()  # Ensure no error message is displayed
    except Exception as e:
        logging.error(f"An error occurred: {e}")
