""" 
Title: User updates personal information
Environment Variables: path/to/cv.pdf
Notes: Ensure that the user is already registered and the CV file path is correct.
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


def test_update_profile(setup):
    page = setup
    try:
        logging.info("Navigating to login page...")
        page.goto("https://example.com/login")
        logging.info("Filling in login credentials...")
        page.fill("#username", "testuser")
        page.fill("#password", "password123")
        page.click("#login-button")
        page.wait_for_navigation()

        logging.info("Navigating to profile page...")
        page.goto("https://example.com/profile")

        logging.info("Updating profile fields...")
        page.fill("#first-name", "John")
        page.fill("#last-name", "Doe")
        page.fill("#email", "john.doe@example.com")
        page.fill("#education", "Bachelor's in Computer Science")
        page.set_input_files("#cv-upload", "path/to/cv.pdf")

        logging.info("Clicking save button...")
        page.click("#save-button")

        logging.info("Waiting for success message...")
        page.wait_for_selector("#success-message")

        logging.info("Validating success message...")
        assert page.locator("#success-message").is_visible()
        assert page.locator("#success-message").inner_text() == "Candidate Profile saved successfully"
        logging.info("Profile updated successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
