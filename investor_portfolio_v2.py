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
import streamlit as st
from dataclasses import dataclass
import plotly.figure_factory as ff
from datetime import datetime
import os
import matplotlib.pyplot as plt
import numpy as np
from typing import Any, List

# From `financial_information.py' import the functions generate_account, get_age
#from financial_information import generate_account, get_age

# From `crypto_wallet.py' import the functions generate_account, get_balance
from crypto_wallet_information import generate_crypto_account, get_balance
# from tax import income_response

st.title("Investor Portfolio")
st.markdown("### Financial areas recommended to invest in based on your financial background.")

# Interactive drop down menu for the investor to select 
drop_down = ["Tax Portfolio", "Sentiment Analysis Model", "Twitter Sentiment Analysis"]
options = st.sidebar.selectbox("Select from the following options", drop_down)

if options == 'Tax Portfolio':
    st.sidebar.success("2021 Tax Portfolio Summary")
    st.write('Here is a brief summary of your 2021 Tax Portfolio.')

    investor_input = st.text_input("Enter your name:", " ")
    if(st.button('Submit')):
        result = investor_input.title()
        st.success(result)

    age_input = st.number_input("Enter your age:" , 0 , 100)
    if(st.button('Submit', key = 0)):
        result_age = age_input
        st.success(result_age)

    income_response = st.number_input(
        "Enter your annual income (if married, please respond the joint annual income):", 0, 10000000)
    if(st.button('Submit', key = 1)):
        result_income = income_response
        st.success(result_income)

    if not investor_input:
        pass

    else:
        st.markdown('Select from the drop down menu:')
        selected_options = st.selectbox("", options=['Breakdown of Portfolio', 'Portfolio Plot'], index=0)
        if selected_options == 'Breakdown of Portfolio':
            st.write('Information of the investor will be displayed here!')
            if(st.button('Submit' , key = 1)):
                st.text("Your income is {}".format())

        elif selected_options == 'Portfolio Plot':
            # Sample data from https://docs.streamlit.io/library/api-reference/charts/st.plotly_chart

            # Add histogram data
            x1 = np.random.randn(200) - 2
            x2 = np.random.randn(200)
            x3 = np.random.randn(200) + 2
            
            # Group data together
            hist_data = [x1, x2, x3]

            group_labels = ['Group 1', 'Group 2', 'Group 3']

            # Create distplot with custom bin_size
            fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])

            # Plot!
            st.plotly_chart(fig, use_container_width=True)


elif options == 'Sentiment Analysis Model':
    st.sidebar.success("Trending Stocks or Coins")
    st.write('Here is a fundamental analysis for the following selected stock or coin.')
    investor_input = ''
    st.markdown('Type in the ** Ticker Symbol ** for the given ** Stock** or ** Coin **')
    investor_input = st.text_input('')
    
    if not investor_input:
            pass
    else: 
        st.markdown('Select from the drop down menu if the ticker symbol is a stock or coin:')    
        selected_options = st.selectbox("", options = ['Stock', 'Crypto'], index=0)
        if selected_options == 'Stock':
            st.markdown('Displayed **Stock** Information')
            st.write('Select a ** timeframe ** for the selected ** stock ** to get a fundamental analysis breakdown.')
            st.markdown('Select a Start Date:')
            start_date = st.date_input("", datetime(2020, 1, 1))
            st.write('Selected date:', start_date)

            interactive_button = st.button('Display Stock Information:')

            if interactive_button:
                try:

                    with st.spinner('Gathering Data... '):
                        time.sleep(1)
                    print('Date - ', start_date)

                except:
                    st.markdown('')

        # Need to import ESG score from the ESG_Data.file 
        # Need to import a line graph (1 year) for the selected stock using an API

        elif selected_options == 'Crypto':
            st.markdown('Displayed ** Coin ** Information')
            st.write('Select a ** timeframe ** for the selected ** coin ** to get a fundamental analysis breakdown.')
            st.markdown('Select a Start Date')
            start_date = st.date_input("", datetime(2020, 1, 1))
            st.write('Selected date:', start_date)

            interactive_button = st.button('Display Coin Information:')
       
            if interactive_button:
                try:
                    
                    with st.spinner('Gathering Data... '):
                        time.sleep(1)
                    print('Date - ', start_date)

                except:
                    st.markdown('')

        # Need to import ESG score from the ESG_Data.file
        # Need to import a line graph (1 year) for the selected coin using an API
        

elif options == 'Twitter Sentiment Analysis':
    st.write('Using information from Twitter to understand how to format our sharpe, calmar, sortino, treynor ratios for market evaluations.')
    st.sidebar.success("Trending on Twitter")

# Need to import information from TwitterSentimentAnalysis.ipynb and import the pie charts for this file here. 
