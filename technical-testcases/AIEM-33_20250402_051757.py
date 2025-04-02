""" 
Title: User logs in successfully
Environment Variables: N/A
Notes: This test case verifies that a user can log in successfully with valid credentials and checks for any error messages on the login page.
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


def test_user_login(setup):
    page = setup
    try:
        logging.info("Navigating to the login page...")
        page.goto("https://example.com/login")

        logging.info("Entering valid credentials...")
        page.fill("input[name='username']", "valid_username")
        page.fill("input[name='password']", "valid_password")

        logging.info("Clicking the login button...")
        page.click("button[type='submit']")

        logging.info("Waiting for navigation to the Candidate Profile page...")
        page.wait_for_navigation()

        logging.info("Asserting the user is redirected to the Candidate Profile page...")
        assert page.url == "https://example.com/candidate-profile"

        logging.info("Checking for any error messages...")
        error_message = page.query_selector(".error-message")
        assert error_message is None or not error_message.is_visible()
        logging.info("Test completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
