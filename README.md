# 📊 Stock Portfolio Tracker

A simple Python program to track your stock portfolio.  
It allows you to enter stock symbols, quantities, and then calculates the total value of your investments.  
Finally, it generates a **CSV report** of your portfolio.

---

## 🚀 Features
- Predefined stock prices for popular companies (AAPL, TSLA, GOOGL, MSFT, AMZN).
- Add multiple stock entries interactively.
- Portfolio summary with total value.
- Exports data to **Portfolio_Summary.csv**.
- Beginner-friendly Python code.

---

## 📂 Project Structure
📁 Stock-Portfolio-Tracker
┣ 📄 portfolio.py # Main Python script
┣ 📄 Portfolio_Summary.csv (generated after running)
┣ 📄 README.md # Project documentation


---

## 🛠️ Requirements
- Python 3.x
- No external libraries required (only uses built-in `csv` module).

---

## ▶️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Stock-Portfolio-Tracker.git
2. Navigate into the folder:
   cd Stock-Portfolio-Tracker
3. Run the Python script:
    python portfolio.py
4. 📋 Example Usage
   ------------------------------------------------------------
Welcome to Stock Portfolio Tracker
Available Stocks: AAPL, TSLA, GOOGL, MSFT, AMZN
------------------------------------------------------------
Enter stock symbol (or type 'done' to finish): AAPL
Enter the quantity of stock: AAPL: 5
5 shares of AAPL added
Enter stock symbol (or type 'done' to finish): TSLA
Enter the quantity of stock: TSLA: 3
3 shares of TSLA added
Enter stock symbol (or type 'done' to finish): done
----------------------------------------
YOUR PORTFOLIO SUMMARY
----------------------------------------
AAPL : 5 shares | value = 1273.15
TSLA : 3 shares | value = 1334.16
----------------------------------------
The total is: 2607.31
----------------------------------------


   ##💡 Future Improvements

Fetch real-time stock prices using an API.

Add user authentication for saving multiple portfolios.

Create a web version with Flask or Django.
   
   

   
   

