""" 
Title: User logs in successfully
Environment Variables: Chrome, Python 3.12
Notes: This test case covers user registration, login, profile update, education addition, and CV upload.
Assignee: Malini Sharma
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Step 1: Open the registration page
    try:
        driver.get('http://example.com/register')
        logging.info('Opened registration page.')
    except Exception as e:
        logging.error(f'Error opening registration page: {e}')

    # Step 2: Fill in the registration form
    try:
        driver.find_element(By.NAME, 'username').send_keys('testuser')
        driver.find_element(By.NAME, 'email').send_keys('testuser@example.com')
        driver.find_element(By.NAME, 'password').send_keys('Password123')
        driver.find_element(By.NAME, 'confirm_password').send_keys('Password123')
        driver.find_element(By.NAME, 'submit').click()
        logging.info('Registration form submitted.')
    except Exception as e:
        logging.error(f'Error filling registration form: {e}')

    # Wait for registration to complete
    WebDriverWait(driver, 10).until(EC.url_changes('http://example.com/register'))

    # Step 3: Open the login page
    try:
        driver.get('http://example.com/login')
        logging.info('Opened login page.')
    except Exception as e:
        logging.error(f'Error opening login page: {e}')

    # Step 4: Fill in the login form
    try:
        driver.find_element(By.NAME, 'email').send_keys('testuser@example.com')
        driver.find_element(By.NAME, 'password').send_keys('Password123')
        driver.find_element(By.NAME, 'submit').click()
        logging.info('Login form submitted.')
    except Exception as e:
        logging.error(f'Error filling login form: {e}')

    # Wait for login to complete
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'welcome-message')))

    # Step 5: Verify successful login
    try:
        assert driver.find_element(By.ID, 'welcome-message').is_displayed(), 'Login failed: Welcome message not displayed'
        logging.info('Login successful, welcome message displayed.')
    except Exception as e:
        logging.error(f'Error verifying login: {e}')

    # Step 6: Update profile
    try:
        driver.get('http://example.com/profile')
        driver.find_element(By.NAME, 'bio').send_keys('This is my bio.')
        driver.find_element(By.NAME, 'submit').click()
        logging.info('Profile updated.')
    except Exception as e:
        logging.error(f'Error updating profile: {e}')

    # Step 7: Add academic education
    try:
        driver.get('http://example.com/education')
        driver.find_element(By.NAME, 'degree').send_keys('Bachelor of Science')
        driver.find_element(By.NAME, 'institution').send_keys('University of Example')
        driver.find_element(By.NAME, 'submit').click()
        logging.info('Education added.')
    except Exception as e:
        logging.error(f'Error adding education: {e}')

    # Step 8: Upload CV
    try:
        cv_path = '/path/to/cv.pdf'
        if os.path.exists(cv_path):
            driver.get('http://example.com/upload')
            driver.find_element(By.NAME, 'cv').send_keys(cv_path)
            driver.find_element(By.NAME, 'submit').click()
            logging.info('CV uploaded.')
        else:
            logging.error('CV file does not exist.')
    except Exception as e:
        logging.error(f'Error uploading CV: {e}')

    # Wait for upload to complete
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'upload-success')))

    # Verify CV upload success
    try:
        assert driver.find_element(By.ID, 'upload-success').is_displayed(), 'Upload failed: Success message not displayed'
        logging.info('CV upload successful, success message displayed.')
    except Exception as e:
        logging.error(f'Error verifying CV upload: {e}')

finally:
    # Close the browser
    driver.quit()
    logging.info('Browser closed.')