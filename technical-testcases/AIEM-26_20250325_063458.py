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
logging.basicConfig(level=logging.INFO)

def register_user(driver):
    try:
        logging.info('Navigating to the registration page.')
        driver.get('http://example.com/register')

        logging.info('Filling in the registration form.')
        driver.find_element(By.NAME, 'username').send_keys('testuser')
        driver.find_element(By.NAME, 'email').send_keys('testuser@example.com')
        driver.find_element(By.NAME, 'password').send_keys('Password123')
        driver.find_element(By.NAME, 'confirm_password').send_keys('Password123')
        driver.find_element(By.NAME, 'submit').click()

        logging.info('Registration form submitted.')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login')))
    except Exception as e:
        logging.error(f'Registration failed: {e}')


def login_user(driver):
    try:
        logging.info('Navigating to the login page.')
        driver.get('http://example.com/login')

        logging.info('Filling in the login form.')
        driver.find_element(By.NAME, 'username').send_keys('testuser')
        driver.find_element(By.NAME, 'password').send_keys('Password123')
        driver.find_element(By.NAME, 'submit').click()

        logging.info('Login form submitted.')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'logout')))
        assert driver.find_element(By.ID, 'logout').is_displayed(), 'Logout button is not displayed, login may have failed.'
    except Exception as e:
        logging.error(f'Login failed: {e}')


def update_profile(driver):
    try:
        logging.info('Navigating to the profile page.')
        driver.get('http://example.com/profile')

        logging.info('Updating profile bio.')
        driver.find_element(By.NAME, 'bio').send_keys('This is my bio.')
        driver.find_element(By.NAME, 'submit').click()

        logging.info('Profile updated.')
    except Exception as e:
        logging.error(f'Profile update failed: {e}')


def add_education(driver):
    try:
        logging.info('Navigating to the education page.')
        driver.get('http://example.com/education')

        logging.info('Adding academic education.')
        driver.find_element(By.NAME, 'degree').send_keys('Bachelor of Science')
        driver.find_element(By.NAME, 'institution').send_keys('University of Example')
        driver.find_element(By.NAME, 'submit').click()

        logging.info('Education added.')
    except Exception as e:
        logging.error(f'Adding education failed: {e}')


def upload_cv(driver):
    try:
        cv_path = '/path/to/cv.pdf'
        if not os.path.exists(cv_path):
            logging.error('CV file does not exist.')
            return

        logging.info('Navigating to the upload page.')
        driver.get('http://example.com/upload')

        logging.info('Uploading CV.')
        driver.find_element(By.NAME, 'cv').send_keys(cv_path)
        driver.find_element(By.NAME, 'submit').click()

        logging.info('CV uploaded.')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'success')))
        assert driver.find_element(By.ID, 'success').is_displayed(), 'Success message is not displayed after CV upload.'
    except Exception as e:
        logging.error(f'CV upload failed: {e}')


def main():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    try:
        register_user(driver)
        login_user(driver)
        update_profile(driver)
        add_education(driver)
        upload_cv(driver)
    finally:
        logging.info('Closing the browser.')
        driver.quit()

if __name__ == '__main__':
    main()