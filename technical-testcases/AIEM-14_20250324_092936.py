""" 
Title: User accesses the login page
Environment Variables: BASE_URL=https://example.com
Notes: This test case covers user registration, login, profile update, and CV upload functionalities.
Assignee: Malini Sharma
"""

from playwright.sync_api import sync_playwright

# Function to run the test case
def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        try:
            # Navigate to the login page
            print('Navigating to the login page...')
            page.goto('https://example.com/login')

            # Check if the login form is displayed
            print('Checking if the login form is displayed...')
            login_form_visible = page.is_visible('#login-form')
            assert login_form_visible, 'Login form is not visible'

            # Fill in the registration form
            print('Filling in the registration form...')
            page.fill('#username', 'testuser')
            page.fill('#password', 'password123')
            page.fill('#email', 'testuser@example.com')
            page.click('#register-button')

            # Check for success message
            print('Checking for success message...')
            success_message_visible = page.is_visible('#success-message')
            assert success_message_visible, 'Success message is not visible'

        except Exception as e:
            print(f'Error during registration: {e}')

        try:
            # Log in with the registered user
            print('Logging in with the registered user...')
            page.fill('#username', 'testuser')
            page.fill('#password', 'password123')
            page.click('#login-button')

            # Check if the user is logged in
            print('Checking if the user is logged in...')
            profile_section_visible = page.is_visible('#profile-section')
            assert profile_section_visible, 'Profile section is not visible'

        except Exception as e:
            print(f'Error during login: {e}')

        try:
            # Update profile
            print('Updating profile...')
            page.click('#edit-profile')
            page.fill('#education', 'Bachelor of Science')
            page.click('#save-profile')

            # Check for profile update success message
            print('Checking for profile update success message...')
            update_message_visible = page.is_visible('#update-message')
            assert update_message_visible, 'Update message is not visible'

        except Exception as e:
            print(f'Error during profile update: {e}')

        try:
            # Upload CV
            print('Uploading CV...')
            file_input = page.locator('#cv-upload')
            file_input.set_input_files('path/to/cv.pdf')
            page.click('#upload-button')

            # Check for upload success message
            print('Checking for upload success message...')
            upload_message_visible = page.is_visible('#upload-message')
            assert upload_message_visible, 'Upload message is not visible'

        except Exception as e:
            print(f'Error during CV upload: {e}')

        # Close the browser
        browser.close()

# Run the test
if __name__ == '__main__':
    run_test()