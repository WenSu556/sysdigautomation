<span style="font-size:1em; opacity:0.5">Homework for sysdigautomation readme </span>

## Overview
**Project structure**
All the code are under **webdriver** folder, under webdriver folder, there are following subfolder
- **drivers** : the folder contains the Selenium browser driver
- **ElementLocators** : Wrapper class to find releated elements in the page
- **logs**: Test logs folder, for debugging and analyze results
- **Pages**: All the actions related to the page
- **TestCases**: All the real test cases in json format
- **Tests**: All the test driver which will use the cases under TestCases Folder to run the tests
- **utils**: Help funcitons like parse json 

**Test Configuration**
- Four regions(EU, US East, US West, AP)
- Different browsers(Firefox, Edge), can be extended to other browsers with the new Selenium driver installed

**Features covered in the test cases in the code**
- Different Email + password log in(As required, "Log in" button is not clicked)
- "Forgot your password" 
- Log in with Google
- Switch to four regions

## How to use the test cases
**How to use the automation script**
- Please run command from "automation" folder. Script use absolute path. Command can be: "python -m webdriver.Tests.TestLogin"
- Unittest is used to drive automation testing

## Potential improvements
**Possible improvements on the tests**
*Because 2 hours is suggested to do the work, there are places can be improved in my mind as below*:
- Implement a test driver/test suite that can drive all the cases (and new cases)
- Cover other functions in login page
- Add more functional and force error test inputs combination, I didn't put all as I don't have the valid test data to make sure using minimum cases to cover most scearions
- Better automation result report
- Use a defined logger class to do logging 

**Possible improvements on the login page itself:**
*During writing the cases, I found there can be some improvements for the login page to help deliver better customer experience*
- Detect user region by the access IP address, and after user input the email adderss, detect if the user is in travel scenario or not, auto-redirect user to the right site
- For "AP" region, hide "Google" in "Log in with" because "Google OAuth is not enabled"
- Left part of login page seems a little blank, can add some simple information there
- I experienced some performance issue, that is why I put waituntil in the code to improve the test reliability, not sure if this is related to my home network or service.
