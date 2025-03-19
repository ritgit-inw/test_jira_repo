""" 
Title: Technical Test Case for Google Authentication Login
Environment Variables: N/A
Notes: This test case automates the login process using Google authentication. Ensure to replace the placeholder URLs and element selectors with actual values from your application.

 Github commit: a0bfca7fcda954d2b789c718feee583d12d97e51
 Github link: https://github.com/ritgit-inw/test_jira_repo/blob/main/technical-testcases/QA-25_20250319_111029.py
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run headless Chrome
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Navigate to the login page
    logging.info('Navigating to the login page.')
    driver.get('https://your-app-login-url.com')  # Replace with the actual login URL

    # Step 2: Click on 'Login with Google'
    try:
        logging.info('Clicking on the Login with Google button.')
        login_with_google_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Login with Google"]'))
        )
        login_with_google_button.click()
    except Exception as e:
        logging.error(f'Error clicking Login with Google button: {e}')  

    # Step 3: Wait for the Google authentication page to load
    logging.info('Waiting for the Google authentication page to load.')
    WebDriverWait(driver, 10).until(
        EC.title_contains("Google")
    )

    # Step 4: Check if redirected to Google authentication page
    assert "Google" in driver.title, "Not redirected to Google authentication page"

    # Step 5: Simulate successful authentication (this part may vary based on your app's flow)
    # Uncomment and replace with actual selectors if needed
    # logging.info('Entering email and password for authentication.')
    # email_input = driver.find_element('id', 'identifierId')
    # email_input.send_keys('your-email@gmail.com')
    # email_input.submit()
    # time.sleep(2)
    # password_input = driver.find_element('name', 'password')
    # password_input.send_keys('your-password')
    # password_input.submit()

    # Step 6: Wait for redirection back to the app
    logging.info('Waiting for redirection back to the app.')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//h1[text()="Welcome"]'))
    )

    # Step 7: Verify successful login
    logging.info('Verifying successful login.')
    assert "Welcome" in driver.page_source, "Login failed"

    # Step 8: Check for any error messages
    try:
        error_message = driver.find_element(By.ID, 'error-message')  # Replace with actual error message element
        assert not error_message.is_displayed(), "Error message is displayed"
    except Exception as e:
        logging.info('No error message element found or it is not displayed.')

finally:
    # Clean up and close the browser
    logging.info('Closing the browser.')
    driver.quit()