""" 
Title: Technical Test Case for Google Authentication Login
Environment Variables: N/A
Notes: This test case automates the login process using Google authentication. Ensure to replace the placeholder URLs and elements with actual values from your application.
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

# Initialize the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Navigate to the login page
    logging.info('Navigating to the login page.')
    driver.get('https://your-app-login-url.com')  # Replace with the actual login URL

    # Step 2: Click on 'Login with Google'
    try:
        logging.info('Clicking on the Login with Google button.')
        google_login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Login with Google"]'))
        )
        google_login_button.click()
    except Exception as e:
        logging.error(f'Error clicking Login with Google button: {e}')  

    # Step 3: Wait for the Google authentication page to load
    logging.info('Waiting for the Google authentication page to load.')
    WebDriverWait(driver, 10).until(EC.title_contains("Google"))

    # Step 4: Check if redirected to Google authentication page
    assert "Google" in driver.title, "Not redirected to Google authentication page"
    logging.info('Successfully redirected to Google authentication page.')

    # Step 5: Simulate successful authentication (this part will depend on your testing setup)
    # You may need to enter credentials here or use a test account
    # Example:
    # driver.find_element('id', 'identifierId').send_keys('your-email@gmail.com')
    # driver.find_element('id', 'identifierNext').click()
    # time.sleep(2)
    # driver.find_element('name', 'password').send_keys('your-password')
    # driver.find_element('id', 'passwordNext').click()

    # Step 6: Wait for redirection back to the app
    logging.info('Waiting for redirection back to the app.')
    WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))

    # Step 7: Verify successful login
    assert "Dashboard" in driver.title, "Login failed, not redirected to Dashboard"
    logging.info('Successfully logged in and redirected to Dashboard.')

    # Step 8: Check for any error messages
    try:
        error_message = driver.find_element(By.ID, 'error-message')  # Adjust the selector as necessary
        if error_message.is_displayed():
            logging.warning(f'Error message displayed: {error_message.text}')  # Log the error message if displayed
    except Exception as e:
        logging.info('No error message displayed or element not found.')
        logging.error(f'Error checking for error message: {e}')

finally:
    # Close the driver
    logging.info('Closing the driver.')
    driver.quit()