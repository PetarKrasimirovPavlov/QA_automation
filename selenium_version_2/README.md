# QA Automation Challenge



## 🔧 Selenium Version 2

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

   This will execute all tests in the `selenium_version_2/` folder with all fixtures and generate a self-contained HTML report with a timestamp inside `selenium_version_2/reports/`. No overwriting - reports history. When you run run_tests.py, you'll be prompted to enter the base URL (environment) to test on.
   This gives you flexibility to test against different environments (e.g. staging, production, local).

   ```bash
   python run_tests.py
   ```

   or for detach mode (for testing purposes)(PowerShell):
   ```bash
   $env:DETACH = "true"
   python run_tests.py
   ```

   or headless mode (PowerShell):
   ```bash
   $env:HEADLESS = "true"
   python run_tests.py
   ```

   ✅ To run only specific scenarios without generating report use:

     ```bash
     pytest -m scenario1
     ```

     ```bash
     pytest -m scenario2
     ```
5. ### Issues discovered during testing:

- The active_option UI element sometimes fails(in low resolution most frequently) to update consistently during tests, causing assertion failures.
- The postal code input field accepts input consisting of letters only. This suggests missing or weak validation, as no country uses postal codes made up entirely of letters — most use either numeric or alphanumeric formats.