# QA Automation Challenge



## 🔧 Version 2 

- Version 1 Implemented as base
- Add an ability to filter tests for the test execution
- Add custom HTML report for the test execution
- Tests will be executed on multiple environments (dev, testing, staging, etc..), add necessary configurations.
- Chrome and Firefox should be supported browsers
- Tests support different browser resolutions

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

   ✅ To run only specific scenarios without generating report use:

     ```bash
     pytest -m scenario1
     ```

     ```bash
     pytest -m scenario2
     ```