🧪 STQA Mini Project – Automated Webpage Testing using Selenium
📘 Overview

This project demonstrates automated software testing on a simple static webpage using Python (Selenium WebDriver).
It verifies UI elements, user interactions, and dynamic changes like button clicks and hover effects — reflecting practical STQA principles.

🧰 Technologies Used

Frontend: HTML, CSS

Testing Framework: Selenium (Python)

Automation Tool: Chrome WebDriver

Language: Python

Editor: Visual Studio Code

⚙️ Project Structure
stqa-mini-project/
│
├── index.html               # Simple webpage to be tested
├── style.css                # Styling for webpage elements
├── test_simple_webpage.py   # Selenium automation script
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

🌐 Webpage Description

A simple webpage built for automation testing with the following elements:

A main heading: “Hello, World!”

A Click Me button that updates text when clicked

A Hover Me button that changes color and text when hovered over

🧠 Test Scenarios (Automated via Selenium)
✅ Test Case	Description
1️⃣	Verify that the main heading text is correct
2️⃣	Check if “Click Me” button exists
3️⃣	Confirm text changes to “Button Clicked!” when button is clicked
4️⃣	Check if “Hover Me” button exists
5️⃣	Verify text changes to “Hover Detected!” on hover
6️⃣	Confirm background color change on hover
7️⃣	Verify correct page title
8️⃣	Ensure all elements are visible on page load
9️⃣	Check hover and click results persist visually
🔟	Validate that no JavaScript errors occur during interactions
🚀 How to Run the Project
1. Clone the Repository
git clone https://github.com/<your-username>/stqa-mini-project.git
cd stqa-mini-project

2. Install Dependencies
pip install -r requirements.txt

3. Run the Webpage

Simply open index.html in your browser.

4. Run the Selenium Tests
python test_simple_webpage.py


The script will open your local webpage, wait for your interactions (clicks, hover, etc.),
then automatically evaluate and print PASS/FAIL results for each test case in the terminal.

🧩 Key Features

Real-time testing feedback in terminal

Tests user-driven interactions (click, hover, visual response)

Uses ActionChains for hover simulation

Waits for manual or automated DOM updates

Demonstrates functional testing and UI validation

📸 Sample Output
⚙️ Webpage opened. You can interact now.
👉 Click, hover, or change elements. Tests will start in 15 seconds...

✅ PASS: Heading text is correct
✅ PASS: Button (Click Me) exists
✅ PASS: Button click registered correctly
✅ PASS: Hover button exists
✅ PASS: Hover detected successfully
✅ PASS: Hover color changed correctly
✅ PASS: Page title is correct

🧾 All tests executed.

