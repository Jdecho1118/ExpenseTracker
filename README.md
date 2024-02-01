**Expense Tracker README:**

### Overview:
This Expense Tracker is a Python console application designed to help users manage their monthly income and expenses. It provides features such as setting credentials, logging in, inserting income, adding expenses, viewing expenses, saving data, and exiting the application.

### Dependencies:
- The application relies on the `bcrypt` library for securely hashing and verifying passwords. Ensure it is installed by running `pip install bcrypt` in your terminal.

### Usage:

1. **Initialization:**
   - The `ExpenseTracker` class is the core component, managing user data, income, expenses, and credentials.
   - Upon instantiation, it initializes with an empty expense dictionary, zero income, and no set username or password hash.

2. **Setting Credentials:**
   - Use option `1` to set a username and password.
   - The password is securely hashed using the `bcrypt` library and stored as a hash.

3. **Login:**
   - Option `2` allows users to log in using their set credentials.
   - Passwords are securely checked against the stored hash.

4. **Inserting Income:**
   - Option `3` enables users to input their monthly income.
   - Only non-negative numbers are accepted.

5. **Adding Expense:**
   - Option `4` allows users to add expenses by specifying a category and amount.
   - Categories must be non-empty strings, and amounts must be positive numbers.

6. **Viewing Expenses:**
   - Option `5` displays a summary of recorded expenses, total expenses, remaining income, and a warning if the user has exceeded their income.

7. **Saving Data:**
   - Option `6` saves the current state of the application, including expenses, income, username, and hashed password, to a JSON file (`expense_tracker_data.json` by default).

8. **Exiting:**
   - Option `7` exits the application.

### Data Persistence:
- User data is saved to and loaded from a JSON file (`expense_tracker_data.json` by default).
- Data is loaded at the start of the application, and any changes made during runtime are saved upon choosing option `6`.

### Logging:
- The application uses the Python `logging` module to log important events and errors.
- Logs are configured to include timestamps, logger names, log levels, and messages.

### Exception Handling:
- The code incorporates exception handling to capture and log errors during password hashing, invalid input, and file operations.

### Running the Application:
- Run the script in a Python environment.
- Follow the on-screen instructions to set credentials, log in, manage income and expenses, and save/exit the application.

### Note:
- Make sure to keep your credentials secure.
- For security reasons, avoid sharing your `expense_tracker_data.json` file and consider protecting it with appropriate permissions.

Feel free to explore, customize, and extend the functionality of the Expense Tracker as needed!
