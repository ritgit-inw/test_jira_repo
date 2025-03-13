""" 
Title: Technical Test Case for Google Authentication Login
Environment Variables: N/A
Notes: This test case automates the login process using Google authentication and verifies the redirection and successful login.
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run headless Chrome
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Function to log messages
def log(message):
    print(message)

try:
    # Step 1: Navigate to the login page
    log('Navigating to the login page...')
    driver.get('https://your-app-login-url.com')  # Replace with the actual login URL

    # Step 2: Click on 'Login with Google'
    try:
        log('Clicking on Login with Google button...')
        login_with_google_button = driver.find_element('xpath', '//button[text()="Login with Google"]')
        login_with_google_button.click()
    except Exception as e:
        log(f'Error clicking Login with Google button: {e}')  # Log the error

    # Step 3: Verify redirection to Google authentication page
    try:
        log('Verifying redirection to Google authentication page...')
        assert "accounts.google.com" in driver.current_url, "Not redirected to Google authentication page"
    except AssertionError as e:
        log(f'Assertion error: {e}')  # Log the assertion error

    # Step 4: Simulate successful authentication (this part may vary based on your app's flow)
    log('Simulating successful authentication...')
    # You may need to handle Google login here, which can be complex due to security measures.
    # For demonstration, we will assume successful login and redirect back to the app.

    # Step 5: Check if logged in by verifying an element on the app's homepage
    try:
        log('Checking if user is logged in...')
        home_page_element = driver.find_element('id', 'home_page_element_id')  # Replace with actual ID
        assert home_page_element.is_displayed(), "User is not logged in"
    except AssertionError as e:
        log(f'Assertion error: {e}')  # Log the assertion error
    except Exception as e:
        log(f'Error finding home page element: {e}')  # Log the error

except Exception as e:
    log(f'An unexpected error occurred: {e}')
finally:
    log('Quitting the driver...')
    driver.quit()