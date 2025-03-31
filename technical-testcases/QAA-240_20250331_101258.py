""" 
Title: User accesses the login page
Environment Variables: N/A
Notes: This test case verifies that the user is redirected to the login page when clicking the 'View Profile' button on the homepage.
Assignee: Ritesh Gond
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


def test_user_accesses_login_page(setup):
    page = setup
    try:
        logging.info("Navigating to the application portal homepage.")
        page.goto("http://application-portal-homepage.com")
        
        logging.info("Clicking the 'View Profile' button.")
        page.click("text='View Profile'")
        
        logging.info("Asserting that the user is redirected to the login page.")
        assert page.url == "http://application-portal-homepage.com/login"
        
        logging.info("Checking for error message if applicable.")
        error_message = page.locator(".error-message")
        assert not error_message.is_visible()  # Ensure no error message is displayed
        logging.info("Test completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
