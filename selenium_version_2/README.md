# QA Automation Challenge



## 🔧 Selenium Version 2 -

## Implemented Functionalities

- **Multi-browser support:**  
  Tests run on both Chrome and Firefox browsers with browser-specific options (incognito/private modes).

- **Responsive testing:**  
  Tests run across multiple screen resolutions (1920x1080, 1366x768, 375x667) to simulate desktop and mobile devices.

- **Parameterized fixtures:**  
  Used `pytest` fixtures with parameters to manage different browser and resolution combinations.

- **Parallel test execution:**  
  Enabled parallel test runs using `pytest-xdist` to speed up test suite execution.

- **Explicit waits:**  
  Applied Selenium explicit waits (`WebDriverWait`) to handle dynamic web elements reliably.

- **Assertions with visibility waits:**  
  Asserted UI elements and text presence with visibility waits to avoid flaky tests.

- **Environment configuration:**  
  Supported dynamic environment URLs through environment variables.

- **HTML reporting:**  
  Generated detailed HTML test reports with timestamps for easier result tracking.

- **Headless mode setup:**  
  (Optional) Supported headless browser runs to speed up tests without UI rendering.

---

## 🚀 How to Run the Tests

1. ### Create a virtual environment:

   ```bash
   python -m venv venv
2. ### Activate the environment:

   ```bash
   venv\Scripts\activate.ps1
3. ### Install dependencies:

   ```bash
   pip install -r requirements.txt

4. ### Run tests:

   ✅ To run all tests with a custom HTML report (timestamped).

   This will execute all tests in the `selenium_version_2/` folder and generate a self-contained HTML report with a timestamp inside `selenium_version_2/reports/`. No overwriting - reports history.

   ```bash
   python run_tests.py
   ```

   or for detach and headless mode (PowerShell):
   ```bash
   $env:HEADLESS = "true"
   $env:DETACH = "true"
   python run_tests.py
   ```


   ✅ To run only specific scenarios without generating report use:

     ```bash
     pytest -m scenario1
     ```

     ```bash
     pytest -m scenario2
     ```