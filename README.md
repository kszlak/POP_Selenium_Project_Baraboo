*This is a small project that was created during post-graduate studies.*

*Project subject:*
#### Test case automation using Selenium WebDriver and Page Object Pattern ####


* **Title:**  Checking the correctness of booking a restaurant table using the correct data
* **ID:** 1.1
* **Environment:** Chrome 73.0.3683.103, Ubuntu 18.04.1 LTS
* **Prerequisite:** Chrome browser installed
* **Steps:**


1. Open the browser
2. Go to the website http://www.baraboo.pl/
3. Click "WYBIERZ LOKAL"
4. Choose "KATOWICE MARIACKA"
5. Click "REZERWACJA"
6. Add name
7. Add surname
8. Add the e-mail address
9. Add the phone number
10. Add the number of people
11. Add the start time
12. Add the ending time
13. Select the current date
14. Click REZERWUJ


* **Expected result:** Displays the booking confirmation page with the "Potwierdź dane i rezerwuj" button.


* **Final remarks:**
Automation of the test case was successful. The case hasn't been deliberately finished not to generate artificial booking. After making a small change and ending the test case with the full booking, the case could be used as part of the regression tests - checking if one of the basic functions (table booking) is going correctly.
