import json
import csv
import sys
from dateutil import parser
from typing import Any, Dict
import statsmodels.api as sm
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import datetime

def download_stock_data(company: str):
    # Create Ticker variable
    ticker = yf.Ticker(company)
    # Set the time range
    start_date = datetime.datetime(2015, 1, 1)
    end_date = datetime.datetime.today()
    # Download stock history
    hist_data = ticker.history(start=start_date, end=end_date)
    # Save to CSV file
    filename = f"{company}_stock_data.csv"
    hist_data.to_csv(filename)
    print(f"Stock data saved to {filename}")
    return hist_data

def plot_stock_data(data, company):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.title(f"{company} Stock Close Price")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.legend()

def sarima_forecast(data, steps):
    # Fit SARIMA model
    model = sm.tsa.statespace.SARIMAX(data['Close'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    results = model.fit()
    # Forecast
    forecast = results.get_forecast(steps=steps)
    forecast_index = pd.date_range(start=data.index[-1], periods=steps+1, closed='right')
    forecast_data = pd.DataFrame(forecast.predicted_mean.values, index=forecast_index[1:], columns=['Forecast'])
    return forecast_data

def main(company):
    # Download stock data
    stock_data = download_stock_data(company)
    # Plot stock data
    plot_stock_data(stock_data, company)
    # Forecast next 30 days using SARIMA model
    forecast_data = sarima_forecast(stock_data, steps=30)
    plt.plot(forecast_data, label='Forecast', color='red')  # Set forecast plot color to red
    plt.legend()
    plt.show()

    # Forecast next 15 days
    forecast_15_days = sarima_forecast(stock_data, steps=15)
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label='Close Price', color='blue')
    plt.plot(forecast_15_days, label='Forecast', color='red')  # Set forecast plot color to red
    plt.title(f"{company} Stock Close Price and 15-day Forecast")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.legend()
    plt.show()
    plt.savefig(f"{company} Stock Close Price_tseries.png")

if __name__ == "__main__":
    company = "NVDA"
    main(company)
 