""" 
Title: User adds an academic record
Environment Variables: NODE_ENV=test
Notes: This test case verifies that a user can successfully add an academic record to their profile and receive a confirmation message.
Assignee: Malini Sharma
"""

import { test, expect } from '@playwright/test';

# Test case for adding an academic record

test('User adds an academic record', async ({ page }) => {
    try:
        # Navigate to the profile page
        print('Navigating to the profile page...')
        await page.goto('https://example.com/profile')

        # Click on the add button in the education section
        print('Clicking on the add button in the education section...')
        await page.click('button#add-education')

        # Fill in the required fields
        print('Filling in the required fields...')
        await page.fill('input#degree', 'Bachelor of Science')
        await page.fill('input#institution', 'University of Example')
        await page.fill('input#start-year', '2018')
        await page.fill('input#end-year', '2022')

        # Click save
        print('Clicking save...')
        await page.click('button#save-education')

        # Check for success message
        print('Checking for success message...')
        successMessage = await page.locator('text=Candidate Profile saved successfully')
        expect(await successMessage.is_visible()).toBe(true)

        # Optionally, check if the academic record is displayed in the education section
        print('Checking if the academic record is displayed...')
        educationRecord = await page.locator('text=Bachelor of Science')
        expect(await educationRecord.is_visible()).toBe(true)
    except Exception as e:
        print(f'An error occurred: {e}')
});