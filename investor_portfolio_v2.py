################################################################################
# Step 1 - Financial tax information:
# Import personal tax information from 'financial_information.py' (or whatever the file is called) script into the file "investor_portfolio"
# which contains code for Investor Portfolio's customer interface in order to add wallet operations to the
# application. We will provide the investors account information to the application.

# Step 2 - Crypto wallet:
# Within the Streamlit sidebar section of code, create a variable named `account`. Set this variable equal to a call on the `generate_account`
# function. This function will create the Investor Portfolio customer's account and will contain their wallet information. Additionally within
# this section, there will be an `st.sidebar.write` function that will display the balance of the customer’s account.

################################################################################
# Imports
import hvplot.pandas
import matplotlib as plt
import pandas_datareader as pdr
import alpaca_trade_api as alpaca
from dotenv import load_dotenv
import requests
import json
import urllib.request
import calendar
import yesg
import streamlit as st
from dataclasses import dataclass
import plotly.figure_factory as ff
from datetime import datetime
import os
import matplotlib.pyplot as plt
import numpy as np
from typing import Any, List
import pandas as pd
import urllib.request
import plotly.express as px
munis = pd.read_csv('municipal_bonds.csv')
treas = pd.read_csv('treasury_bonds.csv')



# Importing the functions for other .py files
#from crypto_wallet_information import generate_crypto_account, get_balance
#from tax import investor_tax_rate

st.title("Investor Portfolio")
st.markdown("### Financial areas recommended to invest in based on your financial background.")
st.sidebar.write('Welcome!')
st.sidebar.image("Images/stock_image_pixabay.jpg")

# Creating the drop down menu options located on the sidebar. If/else will used to choose either "Tax Portfolio", "Sentiment Analysis Model" or "Twitter Sentiment Analysis".

drop_down = ["Tax Portfolio", "Sentiment Analysis Model", "Twitter Sentiment Analysis"]
options = st.sidebar.selectbox("Select from the following options:", drop_down)

# Creating the interactive buttons for name, age, and income

if options == 'Tax Portfolio':
    st.sidebar.success("2021 Tax Portfolio Summary")
    st.write('Here is a brief summary of your 2021 Tax Portfolio.')

    investor_input = st.text_input("Enter your name:", " ")
    if(st.button('Submit')):
        result = investor_input.title()
        st.success(result)

    age_response= st.number_input("Enter your age:" , 0 , 100)
    if(st.button('Submit', key = 0)):
        result_age = age_response
        st.success(result_age)

    income_response = st.number_input("Enter your annual income (if married, please respond the joint annual income):", 0, 10000000)
    if(st.button('Submit', key = 1)):
        result_income = income_response
        st.success(result_income)

    if not investor_input:
        pass

# Creating the drop down menu options if 'Tax Portfolio' is selected. If/else will used to choose either 'Breakdown of Portfolio' or 'Portfolio Plot'.

    else:
        st.markdown('Select from the drop down menu:')
        selected_options = st.selectbox("", options=['Select an option','Breakdown of Portfolio', 'Portfolio Plot'], index=0)
        if selected_options == 'Breakdown of Portfolio':
            st.write('Information of the investor will be displayed here!')

### *** FROM tax.ipynb *** Calculating tax-yield and annual return for the portfolio ###

            if income_response >= 0 and income_response <= 10275:
                tax_rate = .10
            elif income_response >= 10275 and income_response < 41775:
                tax_rate = .12
            elif income_response >= 41775 and income_response < 89075:
                tax_rate = .22
            elif income_response >= 89075 and income_response < 170050:
                tax_rate = .24
            elif income_response >= 170050 and income_response < 215950:
                tax_rate = .32
            elif income_response >= 215950 and income_response < 539900:
                tax_rate = .35
            elif income_response >= 539900:
                tax_rate = .37

            st.write("Here is your tax rate:", tax_rate)

            treas_tax_equivalet_yield = (munis['Coupon']) / (1-tax_rate)
            munis_vs_treas = pd.DataFrame(treas_tax_equivalet_yield)
            munis_vs_treas = pd.DataFrame(munis[['Issuer Name', 'CUSIP', 'Coupon']])

            munis_vs_treas['treasury_equivalet_yield'] = treas_tax_equivalet_yield
            st.write("Here is a DataFrame created based on your tax rate to calculate your tax-equivalent yield:", munis_vs_treas)


        # Getting the treas_weight and muni_weight from the tax_rate

            treas_weight = 0
            muni_weight = 0

            if tax_rate == .10 or tax_rate == .12:
                treas_weight = .100
                muni_weight = 0
            if tax_rate == .22 or tax_rate == .24 or tax_rate == .32:
                treas_weight = .50
                muni_weight = .50
            if tax_rate == .35 or tax_rate == .37:
                treas_weight = 0
                muni_weight = .100

            st.write("The portfolio weight for treasury bonds should be",
                     treas_weight * 100, "% since your income tax rate is:", tax_rate)
            st.write("The portfolio weight for municipal bonds should be",
                     muni_weight * 100, "% since your income tax rate is:", tax_rate)


        # Getting the equity_allocation, fixed_income_allocation and fixed_return

            equity_allocation = 100 - age_response
            st.write("Equity allocation:", equity_allocation)

            fixed_allocation = 100 - equity_allocation
            st.write("Fixed income allocation:", fixed_allocation)

            treas_yield_chosen = np.mean(munis_vs_treas['treasury_equivalet_yield'])
            muni_yield_chosen = np.mean(munis_vs_treas['Coupon'])

            fixed_allocation_return = (
                treas_weight * treas_yield_chosen) + (muni_weight * muni_yield_chosen)
            st.write("Fixed return:", fixed_allocation_return)

            equity_annual_return = .27

        # Getting the annual_return

            portfolio_annual_return = (equity_allocation / 100) * equity_annual_return + (
                fixed_allocation/100) * ((fixed_allocation_return * 2)/100)
            st.write("Your annual portfolio return is:",
                     portfolio_annual_return)

### *** FROM tax.ipynb *** Calculating tax-yield and annual return for the portfolio ###

        elif selected_options == 'Portfolio Plot':
            # Sample data from https://docs.streamlit.io/library/api-reference/charts/st.plotly_chart
            
            equity_allocation = 100 - age_response
            fixed_allocation = 100 - equity_allocation
            equity_annual_return = .27

            # Add allocation data
            x1 = equity_allocation
            x2 = fixed_allocation
  
            # Group data together
            pie_data = [x1, x2]
            group_labels = ['Equity Allocation','Fixed Allocation']

            # Pie Chart Plot of test Tickers
            pie_chart = px.pie( values=pie_data, names=group_labels, title='Pie Chart of Allocations')
            st.plotly_chart(pie_chart, use_container_width=True)



elif options == 'Sentiment Analysis Model':
    st.sidebar.success("Trending Stocks or Coins")
    st.write('Here is a fundamental analysis for the following selected stock or coin.')
    #investor_input = ''
    
    st.markdown('Type in the ** Ticker Symbol ** for the given ** Stock** or ** Coin **')
    investor_input = st.text_input('')     
    if(st.button('Submit', key=4)):
        result_ticker_symbol = investor_input
        st.success(result_ticker_symbol)
    
    if not investor_input:
            pass
    else: 
        st.markdown('Select from the drop down menu if the ticker symbol is a stock or coin:')    
        selected_options = st.selectbox("", options = ['Select an option','Stock', 'Crypto'], index=0)
        if selected_options == 'Stock':
            st.markdown('Displayed **Stock** Information')
            st.write('Select a ** timeframe ** for the selected ** stock ** to get a fundamental analysis breakdown.')
            st.markdown('Select a Start Date:')
            start_date = st.date_input("", datetime(2020, 1, 1))
            st.write('Selected date:', start_date)


### *** FROM ESG_DATA.ipynb *** Downloads historic ESG ratings and returns it as a dataframe (7 years) ###

            sp_500 = pd.read_csv('sandp500.csv')
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/50.0.2661.102 Safari/537.36'}

            response = requests.get('https://query2.finance.yahoo.com/v1/finance/esgChart', params={"symbol": investor_input},
                        headers=headers)

            try:
                df = pd.DataFrame(
                    response.json()["esgChart"]["result"][0]["symbolSeries"])
                df["Date"] = pd.to_datetime(df["timestamp"], unit="s")

                df = df.rename(columns={"esgScore": "Total-Score", "environmentScore": "E-Score", "socialScore": "S-Score",
                                        "governanceScore": "G-Score"})
                df["Ticker"] = investor_input
                
                st.write('DataFrame for Total Score and ESG Scores from the past 7 years:', investor_input)
                st.write(df[['Date', 'Total-Score', 'E-Score', 'S-Score', 'G-Score', 'Ticker']].set_index('Date'))

            except:
                st.write('An error has occurred. The ticker symbol might be wrong or you might need to wait to continue.')

           

### *** FROM ESG_DATA.ipynb *** Downloads historic ESG ratings and returns it as a dataframe (7 years) ###


### *** FROM portfolio analysis v2.ipynb *** Gives the portfolio annual return, portfolio annual SD, portfolio sharpe ratio, total ESG score  ###

            st.write('Insert test or using Twitter Sentiment DataFrame:')
    
            test = [['JPM', 50], ['SBAC', 12], ['GOOGL', 39], ['TSLA', 100], ['GPN', 22]]
            df_test = pd.DataFrame(test, columns=['Ticker', 'Sentiment'])
            #st.write(df_test)

            # Insert test or twitter  sentiment dataframe
            df_portfolio = df_test[['Ticker', 'Sentiment']]
            df_portfolio = df_portfolio.sort_values(by=['Sentiment'], ascending=False)
            df_portfolio = df_portfolio.reset_index()
            df_portfolio = df_portfolio.drop(['index'], axis=1)

            # Calculate the total number of sentiments
            sentiment_sum = df_portfolio['Sentiment'].sum()
            st.write('Total number of Sentiments:', sentiment_sum)

            # Calculate the weights for each ticker
            df_portfolio['weights'] = df_portfolio['Sentiment']/sentiment_sum


            # Pie Chart Plot of test Tickers
            pie_chart = px.pie(data_frame=df_portfolio, values= 'weights', names='Ticker', title='Pie Chart of Sentiments')
            st.plotly_chart(pie_chart, use_container_width=True)

            # Naming tickers
            df_portfolio['weights'].sum()

            ticker_0 = df_portfolio.loc[0, 'Ticker']
            ticker_1 = df_portfolio.loc[1, 'Ticker']
            ticker_2 = df_portfolio.loc[2, 'Ticker']
            ticker_3 = df_portfolio.loc[3, 'Ticker']
            ticker_4 = df_portfolio.loc[4, 'Ticker']

            #Set start and end date for the API calls
            start_date = pd.Timestamp('2010-08-01', tz='America/New_York').isoformat()
            end_date = pd.Timestamp('2021-11-23', tz='America/New_York').isoformat()

            # INDEX 0: Make API call and populate dataframe with Close, and Daily Return info
            df_0 = pdr.DataReader(ticker_0, 'yahoo', start_date, end_date)
            df_0 = df_0['Close']
            df_0 = pd.DataFrame(df_0)
            df_0['Daily Return'] = df_0['Close'].pct_change()
            df_0 = df_0.dropna()

            #INDEX 0: Calculate annual return, annual standard deviation and Sharpe Ratio

            # META NOTE: Because Facebook changed their name, the ticker META doesn't have
            #the same amount of historical data

            df_0['Annual Return'] = df_0['Daily Return'].rolling(window=252).mean()
            df_0['Annual SD'] = df_0['Daily Return'].rolling(window=252).std()*np.sqrt(252)
            df_0['Sharpe Ratio'] = (df_0['Annual Return']-.02)/df_0['Annual SD']
            df_0 = df_0.dropna()
            

            # INDEX 1: Make API call and populate dataframe with Close, and Daily Return info
            df_1 = pdr.DataReader(ticker_1, 'yahoo', start_date, end_date)
            df_1 = df_1['Close']
            df_1 = pd.DataFrame(df_1)
            df_1['Daily Return'] = df_1['Close'].pct_change()
            df_1 = df_1.dropna()

            #INDEX 1: Calculate annual return, annual standard deviation and Sharpe Ratio
            df_1['Annual Return'] = df_1['Daily Return'].rolling(window=252).mean()*252
            df_1['Annual SD'] = df_1['Daily Return'].rolling(window=252).std()*np.sqrt(252)
            df_1['Sharpe Ratio'] = (df_1['Annual Return']-.02)/df_1['Annual SD']
            df_1 = df_1.dropna()

            # INDEX 2: Make API call and populate dataframe with Close, and Daily Return info
            df_2 = pdr.DataReader(ticker_2, 'yahoo', start_date, end_date)
            df_2 = df_2['Close']
            df_2 = pd.DataFrame(df_2)
            df_2['Daily Return'] = df_2['Close'].pct_change()
            df_2 = df_2.dropna()
            
            #INDEX 2: Calculate annual return, annual standard deviation and Sharpe Ratio
            df_2['Annual Return'] = df_2['Daily Return'].rolling(window=252).mean()*252
            df_2['Annual SD'] = df_2['Daily Return'].rolling(window=252).std()*np.sqrt(252)
            df_2['Sharpe Ratio'] = (df_2['Annual Return']-.02)/df_2['Annual SD']
            df_2 = df_2.dropna()

            # INDEX 3: Make API call and populate dataframe with Close, and Daily Return info
            df_3 = pdr.DataReader(ticker_3, 'yahoo', start_date, end_date)
            df_3 = df_3['Close']
            df_3 = pd.DataFrame(df_3)
            df_3['Daily Return'] = df_3['Close'].pct_change()
            df_3 = df_3.dropna()

            #INDEX 3: Calculate annual return, annual standard deviation and Sharpe Ratio
            df_3['Annual Return'] = df_3['Daily Return'].rolling(window=252).mean()*252
            df_3['Annual SD'] = df_3['Daily Return'].rolling(window=252).std()*np.sqrt(252)
            df_3['Sharpe Ratio'] = (df_3['Annual Return']-.02)/df_3['Annual SD']
            df_3 = df_3.dropna()
            

            # INDEX 4: Make API call and populate dataframe with Close, and Daily Return info
            df_4 = pdr.DataReader(ticker_4, 'yahoo', start_date, end_date)
            df_4 = df_4['Close']
            df_4 = pd.DataFrame(df_4)
            df_4['Daily Return'] = df_4['Close'].pct_change()
            df_4 = df_4.dropna()
            
            
            #INDEX 4: Calculate annual return, annual standard deviation and Sharpe Ratio
            df_4['Annual Return'] = df_4['Daily Return'].rolling(window=252).mean()*252
            df_4['Annual SD'] = df_4['Daily Return'].rolling(window=252).std()*np.sqrt(252)
            df_4['Sharpe Ratio'] = (df_4['Annual Return']-.02)/df_4['Annual SD']
            df_4 = df_4.dropna()

            # Add annual return for each ticker to portfolio dataframe

            df_portfolio.loc[0, 'Annual Return'] = df_0.loc['2021-11-23', 'Annual Return']
            df_portfolio.loc[1, 'Annual Return'] = df_1.loc['2021-11-23', 'Annual Return']
            df_portfolio.loc[2, 'Annual Return'] = df_2.loc['2021-11-23', 'Annual Return']
            df_portfolio.loc[3, 'Annual Return'] = df_3.loc['2021-11-23', 'Annual Return']
            df_portfolio.loc[4, 'Annual Return'] = df_4.loc['2021-11-23', 'Annual Return']
            

            # Add annual standard deviation for each ticker to portfolio dataframe

            df_portfolio.loc[0, 'Annual SD'] = df_0.loc['2021-11-23', 'Annual SD']
            df_portfolio.loc[1, 'Annual SD'] = df_1.loc['2021-11-23', 'Annual SD']
            df_portfolio.loc[2, 'Annual SD'] = df_2.loc['2021-11-23', 'Annual SD']
            df_portfolio.loc[3, 'Annual SD'] = df_3.loc['2021-11-23', 'Annual SD']
            df_portfolio.loc[4, 'Annual SD'] = df_4.loc['2021-11-23', 'Annual SD']
            

            # Add the Sharpe Ratio for each ticker to portfolio dataframe

            df_portfolio.loc[0, 'Sharpe Ratio'] = df_0.loc['2021-11-23', 'Sharpe Ratio']
            df_portfolio.loc[1, 'Sharpe Ratio'] = df_1.loc['2021-11-23', 'Sharpe Ratio']
            df_portfolio.loc[2, 'Sharpe Ratio'] = df_2.loc['2021-11-23', 'Sharpe Ratio']
            df_portfolio.loc[3, 'Sharpe Ratio'] = df_3.loc['2021-11-23', 'Sharpe Ratio']
            df_portfolio.loc[4, 'Sharpe Ratio'] = df_4.loc['2021-11-23', 'Sharpe Ratio']
            
            # Create a dataframe to store the weighted values of each firm
            metric_weights = pd.DataFrame(df_portfolio['Ticker'])
            metric_weights['weights'] = df_portfolio['weights']
            metric_weights['Weighted Annual Return'] = df_portfolio['weights'] * \
                df_portfolio['Annual Return']
            metric_weights['Weighted Annual SD'] = df_portfolio['weights'] * \
                df_portfolio['Annual SD']
            metric_weights['Weighted Sharpe Ratio'] = df_portfolio['weights'] * \
                df_portfolio['Sharpe Ratio']

            # Create a dataframe of portfolio metrics
            portfolio_metrics = pd.DataFrame(columns=['', 'Metric'])

            portfolio_metrics.loc[0] = 'Portfolio Annual Return'
            portfolio_metrics.loc[0,
                                'Metric'] = metric_weights['Weighted Annual Return'].sum()

            portfolio_metrics.loc[1] = 'Portfolio Annual SD'
            portfolio_metrics.loc[1, 'Metric'] = metric_weights['Weighted Annual SD'].sum()

            portfolio_metrics.loc[2] = 'Portfolio Sharpe Ratio'
            portfolio_metrics.loc[2, 'Metric'] = ((portfolio_metrics.loc[0, 'Metric']-.02)
                                                / portfolio_metrics.loc[1, 'Metric'])

            portfolio_metrics = portfolio_metrics.set_index('')
            
            portfolio_metrics['SP 500 Benchmark'] = np.nan

            # Make a dataframe for the SP 500 to use as a benchmark for the Twitter portfolio
            sp_500 = pdr.DataReader('^GSPC', 'yahoo', start_date, end_date)
            sp_500 = sp_500['Close']
            sp_500 = pd.DataFrame(sp_500)
            sp_500['Daily Return'] = sp_500['Close'].pct_change()
            sp_500 = sp_500.dropna()

            # Calculate metrics for the SP 500
            sp_500['Annual Return'] = sp_500['Daily Return'].rolling(window=252).mean()*252
            sp_500['Annual SD'] = sp_500['Daily Return'].rolling(
                window=252).std()*np.sqrt(252)
            sp_500['Sharpe Ratio'] = (sp_500['Annual Return']-.02)/sp_500['Annual SD']
            sp_500 = sp_500.dropna()

            # Put the SP 500 metrics into the portfolio metrics dataframe

            portfolio_metrics.loc['Portfolio Annual Return',
                                'SP 500 Benchmark'] = sp_500.loc['2021-11-23', 'Annual Return']
            portfolio_metrics.loc['Portfolio Annual SD',
                                'SP 500 Benchmark'] = sp_500.loc['2021-11-23', 'Annual SD']
            portfolio_metrics.loc['Portfolio Sharpe Ratio',
                                'SP 500 Benchmark'] = sp_500.loc['2021-11-23', 'Sharpe Ratio']

            # Import the csv file of ESG data

            esg = pd.read_csv('ESG_data.csv', parse_dates=True)

            # INDEX 0: Create ESG dataframe for each ticker in portfolio by selecting rows that contain the specific Ticker
            ticker_0_esg = esg[esg['Ticker'].str.contains(ticker_0)]
            ticker_0_esg['Date'] = pd.to_datetime(ticker_0_esg['Date'])
            ticker_0_esg = ticker_0_esg.set_index('Date')
            ticker_0_esg = ticker_0_esg.dropna()

            # INDEX 1: Create ESG dataframe for each ticker in portfolio by selecting rows that contain the specific Ticker
            ticker_1_esg = esg[esg['Ticker'].str.contains(ticker_1)]
            ticker_1_esg['Date'] = pd.to_datetime(ticker_1_esg['Date'])
            ticker_1_esg = ticker_1_esg.set_index('Date')
            ticker_1_esg = ticker_1_esg.dropna()

            # INDEX 2: Create ESG dataframe for each ticker in portfolio by selecting rows that contain the specific Ticker
            ticker_2_esg = esg[esg['Ticker'].str.contains(ticker_2)]
            ticker_2_esg['Date'] = pd.to_datetime(ticker_2_esg['Date'])
            ticker_2_esg = ticker_2_esg.set_index('Date')
            ticker_2_esg = ticker_2_esg.dropna()

            # INDEX 3: Create ESG dataframe for each ticker in portfolio by selecting rows that contain the specific Ticker
            ticker_3_esg = esg[esg['Ticker'].str.contains(ticker_3)]
            ticker_3_esg['Date'] = pd.to_datetime(ticker_3_esg['Date'])
            ticker_3_esg = ticker_3_esg.set_index('Date')
            ticker_3_esg = ticker_3_esg.dropna()

            # INDEX 4: Create ESG dataframe for each ticker in portfolio by selecting rows that contain the specific Ticker
            ticker_4_esg = esg[esg['Ticker'].str.contains(ticker_4)]
            ticker_4_esg['Date'] = pd.to_datetime(ticker_4_esg['Date'])
            ticker_4_esg = ticker_4_esg.set_index('Date')
            ticker_4_esg = ticker_4_esg.dropna()

        # Calculate the mean scores for the last available 12 months of ESG data to smooth out potential outliers

            yearly_esg_0 = ticker_0_esg.resample('Y').mean()
            yearly_esg_1 = ticker_1_esg.resample('Y').mean()
            yearly_esg_2 = ticker_2_esg.resample('Y').mean()
            yearly_esg_3 = ticker_3_esg.resample('Y').mean()
            yearly_esg_4 = ticker_4_esg.resample('Y').mean()

            #yearly_esg_4.iloc[-1:]

            df_portfolio['Total ESG'] = np.nan
            

            # Add the ESG scores to the portfolio dataframe

            df_portfolio.loc[0,'Total ESG'] = yearly_esg_0.loc['2021-12-31', 'Total-Score']
            df_portfolio.loc[1,'Total ESG'] = yearly_esg_1.loc['2021-12-31', 'Total-Score']
            df_portfolio.loc[2,'Total ESG'] = yearly_esg_2.loc['2021-12-31', 'Total-Score']
            df_portfolio.loc[3,'Total ESG'] = yearly_esg_3.loc['2021-12-31', 'Total-Score']
            df_portfolio.loc[4,'Total ESG'] = yearly_esg_4.loc['2021-12-31', 'Total-Score']


            # Apply the ESG scores to the metric weights dataframe

            metric_weights['Weighted Total ESG']= df_portfolio['weights']*df_portfolio['Total ESG']
            st.write('Portfolio Summary:', metric_weights)

            # Add the ESG metric to the portfolio metrics dataframe
            esg_row = pd.Series(['', ''])
            esg_row_df = pd.DataFrame([esg_row], index = ['Total ESG Score'], columns=['Metric','SP 500 Benchmark'])

            esg_row_df.loc['Total ESG Score','Metric'] = metric_weights['Weighted Total ESG'].sum()

            portfolio_metrics = pd.concat([portfolio_metrics, esg_row_df])

            
            st.write('Portfolio Summary:', portfolio_metrics)


### *** FROM portfolio analysis v2.ipynb *** Gives the portfolio annual return, portfolio annual SD, portfolio sharpe ratio, total ESG score  ###

        # TODO: Need to import a line graph (1 year) for the selected stock using an API

        elif selected_options == 'Crypto':
            st.markdown('Displayed ** Coin ** Information')
            st.write('Select a ** timeframe ** for the selected ** coin ** to get a fundamental analysis breakdown.')
            st.markdown('Select a Start Date')
            start_date = st.date_input("", datetime(2020, 1, 1))
            st.write('Selected date:', start_date)



        # TODO: Need to import ESG score from the ESG_Data.file
        # TODO: Need to import a line graph (1 year) for the selected stock using an API
        

elif options == 'Twitter Sentiment Analysis':
    st.write('Using information from Twitter to understand how to format our sharpe, calmar, sortino, treynor ratios for market evaluations.')
    st.sidebar.success("Trending on Twitter")

# Need to import information from TwitterSentimentAnalysis.ipynb and import the pie charts for this file here. 
