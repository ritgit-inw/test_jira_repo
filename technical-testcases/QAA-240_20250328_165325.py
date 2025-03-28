""" 
Title: User updates personal information
Environment Variables: path/to/cv.pdf
Notes: This test case covers the user story of updating personal information and validating the success message after saving the profile.
Assignee: Ritesh Gond
"""

import time
from playwright.sync_api import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    try:
        # Navigate to the login page
        print("Navigating to the login page...")
        page.goto('https://example.com/login')
    except Exception as e:
        print(f"Error navigating to login page: {e}")

    try:
        # Log in as a job seeker
        print("Logging in as a job seeker...")
        page.fill('input[name="username"]', 'jobseeker@example.com')
        page.fill('input[name="password"]', 'password123')
        page.click('button[type="submit"]')
    except Exception as e:
        print(f"Error logging in: {e}")

    try:
        # Wait for navigation to profile page
        print("Waiting for navigation to profile page...")
        page.wait_for_navigation()
    except Exception as e:
        print(f"Error waiting for navigation: {e}")

    try:
        # Navigate to the profile page
        print("Navigating to the profile page...")
        page.goto('https://example.com/profile')
    except Exception as e:
        print(f"Error navigating to profile page: {e}")

    try:
        # Update required fields
        print("Updating required fields...")
        page.fill('input[name="first_name"]', 'John')
        page.fill('input[name="last_name"]', 'Doe')
        page.fill('input[name="phone"]', '1234567890')
        page.fill('input[name="address"]', '123 Main St')
    except Exception as e:
        print(f"Error updating required fields: {e}")

    try:
        # Add academic education
        print("Adding academic education...")
        page.fill('input[name="education"]', 'Bachelor of Science in Computer Science')
    except Exception as e:
        print(f"Error adding academic education: {e}")

    try:
        # Upload CV
        print("Uploading CV...")
        page.set_input_files('input[name="cv_upload"]', 'path/to/cv.pdf')
    except Exception as e:
        print(f"Error uploading CV: {e}")

    try:
        # Click save
        print("Clicking save...")
        page.click('button[type="submit"]')
    except Exception as e:
        print(f"Error clicking save: {e}")

    try:
        # Wait for success message
        print("Waiting for success message...")
        time.sleep(2)  # Adjust as necessary for the application response time
    except Exception as e:
        print(f"Error waiting for success message: {e}")

    try:
        # Validate success message
        print("Validating success message...")
        assert page.locator('text="Candidate Profile saved successfully"').is_visible()
        print("Success message is visible.")
    except Exception as e:
        print(f"Error validating success message: {e}")

    finally:
        # Close browser
        print("Closing browser...")
        context.close()
        browser.close()


with sync_playwright() as playwright:
    run(playwright)