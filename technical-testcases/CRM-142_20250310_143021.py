""" 
Title: Implement Password Reset Feature
Environment Variables: N/A
Notes: This test case automates the password reset feature, ensuring that the user can reset their password and log in successfully.
Assignee: Malini Sharma
"""

import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run headless Chrome
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Setup Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Function to perform login

def login(email, password):
    try:
        driver.get('https://your-application-url.com/login')
        logging.info('Navigated to login page.')
        email_input = driver.find_element('name', 'email')
        email_input.send_keys(email)
        password_input = driver.find_element('name', 'password')
        password_input.send_keys(password)
        login_button = driver.find_element('id', 'login')
        login_button.click()
        logging.info('Clicked login button.')
    except Exception as e:
        logging.error(f'Error during login: {e}')

# Function to reset password

def reset_password(email):
    try:
        driver.get('https://your-application-url.com/login')
        logging.info('Navigated to login page.')
        forgot_password_link = driver.find_element('link text', 'Forgot Password')
        forgot_password_link.click()
        logging.info('Clicked on Forgot Password link.')

        email_input = driver.find_element('name', 'email')
        email_input.send_keys(email)
        logging.info('Entered registered email address.')

        submit_button = driver.find_element('id', 'submit')
        submit_button.click()
        logging.info('Submitted the form.')

        success_message = driver.find_element('id', 'success-message')
        assert success_message.is_displayed(), 'Success message not displayed'
        logging.info('Success message displayed.')

        # Simulate clicking the reset link from email (this would be a separate test)
        new_password_input = driver.find_element('name', 'new_password')
        new_password_input.send_keys('NewPassword123!')
        confirm_password_input = driver.find_element('name', 'confirm_password')
        confirm_password_input.send_keys('NewPassword123!')
        reset_button = driver.find_element('id', 'reset')
        reset_button.click()
        logging.info('Clicked reset button.')

        confirmation_message = driver.find_element('id', 'confirmation-message')
        assert confirmation_message.is_displayed(), 'Confirmation message not displayed'
        logging.info('Confirmation message displayed.')
    except Exception as e:
        logging.error(f'Error during password reset: {e}')

# Main execution
try:
    reset_password('user@example.com')
    login('user@example.com', 'NewPassword123!')
    dashboard = driver.find_element('id', 'dashboard')
    assert dashboard.is_displayed(), 'Dashboard not displayed, login failed'
    logging.info('Dashboard displayed, login successful.')
finally:
    driver.quit()