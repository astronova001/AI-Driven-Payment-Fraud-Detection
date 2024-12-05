# AI-Driven Payment Fraud Detection

This project is a web-based application designed to detect potential fraudulent transactions in payment systems. By analyzing key parameters such as transaction type, amount, and balances, the system predicts whether a transaction is fraudulent or not. The application includes a user-friendly interface with validation to ensure data accuracy.

---

## Features

- **Transaction Prediction**: Detects potential fraud using a machine learning model.
- **User-Friendly Interface**: Input form with real-time validation for transaction data.
- **Dropdown for Transaction Types**: Includes options for `PAYMENT`, `CASH_IN`, `DEBIT`, `CASH_OUT`, and `TRANSFER`.
- **Input Validation**: Ensures all inputs fall within predefined ranges.
- **Custom Warnings**: Alerts users when invalid data is entered.

---

## Types of Transactions

1. **PAYMENT (0)**: Payments for bills or purchases.
2. **CASH_IN (1)**: Deposits into an account.
3. **DEBIT (2)**: Money withdrawn from an account for payments or purchases.
4. **CASH_OUT (3)**: Withdrawal of physical cash.
5. **TRANSFER (4)**: Funds transferred between accounts.

Fraudulent Transactions: Fraud has been observed more frequently in the TRANSFER and CASH_OUT transaction types, with these types being more likely to involve fraudulent activities based on Exploratory Data Analysis (EDA).

---

## Technologies Used

- **Frontend**: HTML, CSS (custom styles for a polished interface).
- **Backend**: Flask (Python web framework).
- **Machine Learning**: A predictive model for fraud detection.
- **Version Control**: Git and GitHub for project management.

---

## Installation

### Prerequisites

- Python 3.7 or later
- `pip` (Python package manager)
- Git

### Steps

1. Clone the repository:
    ```bash
    git clone 
    ```
2. Navigate to the project directory:
    ```bash
    cd payment-fraud-detection
    ```

4. Activate the virtual environment:
    - On Windows:
        ```bash
        env\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source env/bin/activate
        ```
5. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Run the application:
    ```bash
    python app.py
    ```
7. Open the application in your browser at `http://127.0.0.1:5000`.

---

## Usage

1. Navigate to the prediction page.
2. Enter the required transaction details:
    - **Step**: Enter a step value between 1 and 744.
    - **Type**: Choose a transaction type from the dropdown.
    - **Amount**: Enter a transaction amount within the valid range.
    - **Senders Old Balance**: Input the origin account's balance.
    - **Receiver's Old Balance**: Input the destination account's balance.
3. Click **Predict** to see the fraud detection result.

---
## Demo
<img src="" width="500" />

---

## Screenshots

### Home Page


### Prediction Form


### Preticted Fraud


### Predicted Non-Fraud


---

## Key Findings from EDA

### Fraudulent Transactions tend to have:

-Transaction Type: Primarily TRANSFER and CASH_OUT.
-Amount: Higher amounts, typically above 1,467,967.30.
-Sender's Balance: Lower balances, typically below 1,649,667.61.
-Receiver's Balance: Can vary, but often lower balances, typically below 544,249.62.

### Non-Fraudulent Transactions tend to have:

-Transaction Type: Primarily PAYMENT and CASH_IN.
-Amount: Lower amounts, typically below 178,197.04.
-Sender's Balance: Higher balances, typically above 832,828.71.
-Receiver's Balance: Higher balances, typically above 1,101,420.87.

---

## Acknowledgments

- Machine learning model development inspired by financial fraud datasets.
- Frontend design contributions by the team.
