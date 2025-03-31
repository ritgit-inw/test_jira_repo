""" 
Title: User accesses the login page
Environment Variables: NODE_ENV=test
Notes: This test case verifies that the user can access the login page by clicking the 'View Profile' button on the homepage. Ensure that the application portal URL is correctly set in the code.
Assignee: Malini Sharma
"""

import { test, expect } from '@playwright/test';

# Test case for user accessing the login page from the application portal homepage
test('User accesses the login page', async ({ page }) => {
    try:
        # Navigate to the application portal homepage
        print('Navigating to the application portal homepage...')
        await page.goto('https://your-application-portal-url.com')

        # Click on the 'View Profile' button
        print('Clicking on the View Profile button...')
        await page.click('text=View Profile')

        # Expect to be redirected to the login page
        print('Expecting to be redirected to the login page...')
        await expect(page).toHaveURL('https://your-application-portal-url.com/login')

        # Check if the login form is visible
        print('Checking if the login form is visible...')
        login_form = await page.locator('form#login')
        assert await login_form.is_visible() == True, 'Login form is not visible'

        # Check for any error messages (if applicable)
        print('Checking for error messages...')
        error_message = await page.locator('.error-message')
        assert await error_message.is_visible() == False, 'Error message is displayed'
    except Exception as e:
        print(f'An error occurred: {e}')
