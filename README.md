*This is a small project that was created during post-graduate studies.*

Project subject:
#### Test case automation using Selenium WebDriver and Page Object Pattern ####


* **Title:**  Checking the correctness of booking a restaurant table using the correct data
* **ID:** 1.1
* **Environment:** Chrome 73.0.3683.103, Ubuntu 18.04.1 LTS
* **Prerequisite:** Chrome browser installed
* **Steps:**


1. Open the Chrome browser
2. Go to the website http://www.baraboo.pl/
3. Click "CHOOSE A LOCAL"
4. Choose "KATOWICE MARIACKA"
5. Click "RESERVATION"
6. Enter the name
7. Enter the name
8. Enter the e-mail address
9. Enter the phone
10. Enter the number of people
11. Enter the start time
12. Enter the ending time
13. Select the current date
14. Click RESERVE
Expected result: Displays the booking confirmation page with the "Confirm data and book" button visible.


* **Final remarks:**
Automation of the test case was successful. The case has not been deliberately finished by finalizing table reservations, so as not to generate artificial booking. After making a small change and ending the test with the booking, the case could be used as part of the regression tests - checking if one of the basic functions (table booking) is going correctly.
