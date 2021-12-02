# Project_3_Team_1
The overall idea for this project is to create an online interactive portfolio. In addition, we will take in information from Twitter and other forms of media to understand how to format our sharpe, calmar, sortino, treynor ratios for market evaluations. Once we have the analysis, we will determine what daily return information we can get based on the standard deviation and other financial metrics. One feature we will try to incorporate for this project is to use federal and state taxes to provide a recommendation for how much a person should invest in fixed income (corporate bond vs municipal bond) based on their age and financial background. 

Research Questions:

1. How will we filter certain keywords from Twitter/Reddit?
2. What relevant financial information (i.e, income, capital gains, etc.) would we need to incorporate in the tax portion of the code? Note: this is also important to ensure a person is eligible to invest.
3. How can we create an ESG metric as an additional feature to give investors the option whether they want to invest in a certain company? 


ESG Data:

Environmental, social, and governance scores are newly yet very quickly becoming essential factors in investing. Therefore, our group decided to include each company in the s&p 500s ESG scores in our portfolio analysis and allocation. We were able to do this through our python function that retrieves this data seven years back (2014-2021) and with a monthly frequency. Specifically, we were able to get our data through our historical ESG functions call to yahoo finance - under the sustainability tab.

Customized Bond Recommendation:

Through our streamlit application, we also included a tab that allows for a customized bond recommendation. It first asks a user to input their income. From that income amount, we know what their federal income tax rate is. It can be the case that an investor will make more from investing in a municipal bond that is tax-exempt versus a treasury or corporate bond that is not tax-exempt, as he or she may be a high net worth individual. Therefore, this person could be taxed more heavily on those coupon payments from treasury or corporate bonds so it is helpful to know which bond could be more profitable. As a result, we use an equation called the tax equivalent yield to calculate the differing bond types comparable yields. Depending on which yield is highest, we recommend that type of bond to the user. We also indicate what they can expect their average yield to be, their portfolio weights, and portfolio returns. Depending on the users age input, the younger they are the greater the portfolio weight goes towards fixed income since it could be more long term. Correspondingly, the older the user the more their portfolio weight goes towards equities. Note: all of this data on the yields and types of bonds we retrieved from Bloomberg terminal.


## Portfolio Analysis


For the portfolio analysis, we created test dataframes to replicate the Twitter data. Tickers were chosen at random from the ESG data and Sentiment values were also chosen at random. The sentiment weights were used to determine each individual equity's weights. 

<img width="159" alt="test2" src="https://user-images.githubusercontent.com/86026996/144332190-e40233fa-a097-46d8-8f7b-2b21d2a5e7a2.png">

<img width="147" alt="test1" src="https://user-images.githubusercontent.com/86026996/144332195-72a788e0-81dc-4044-b160-451d58987fa2.png">

Using indexing, the dataframe will dynamically respond to changes from the incoming Twitter dataframe. Individual stock information came from Yahoo Finance. We used it to calcualted the each equity's annual return, standard deviation and Sharpe ratio. Based on the weights of the five equity portfolio, we then calcuated the portfolio metrics. 


<img width="510" alt="Portfolio_Metrics" src="https://user-images.githubusercontent.com/86026996/144332206-f5ec6595-6674-429f-8ce3-39893e94785e.png">

The dataframe with the ESG data contains data on hundreds of different tickers. We created new ESG dataframes for each equity by capturing rows than contain their ticker.  

<img width="482" alt="ESG_slicer" src="https://user-images.githubusercontent.com/86026996/144332211-97d39dc4-5310-494f-8d31-da475a1470eb.png">
<img width="411" alt="ESG_sliced" src="https://user-images.githubusercontent.com/86026996/144332215-12b71ee2-a89a-49da-bf3a-712f16e1fbd8.png">

After adding all of the Total ESG Scores for each equity in df_portfolio, we were able to calculated the portfolio's Total ESG Score. 
<img width="558" alt="ESG_metrics" src="https://user-images.githubusercontent.com/86026996/144332219-18f1f6eb-e91b-4b71-95fc-ca5e915d0925.png">

## Twitter Analysis:
Markdown

1- Authentication.
2- Get CSV file with the top tickers from S&P500.
3- Get unique tickers in order for us to search tweets that relate to them on twitter.
4- Download the tweets that have those tickers.
5- Create a model that can classify those tweets into Positive/Negative.
6- Use the model to classify the downloaded tweets
7- get only the positive tweets.
8- Analysis.

![Screen Shot 2021-12-01 at 7 35 00 PM](https://user-images.githubusercontent.com/64050486/144336403-f38e166c-8305-4b66-8ef8-19f2bcd86c81.png)
After some problems with Twitter Keys and secret keys related to some changes in Twitter security policy. According to the situation we start to use this website these are the top ten ESG stocks on the market right now.

https://www.investors.com/news/esg-companies-list-best-esg-stocks-environmental-social-governance-values/

![Screen Shot 2021-12-01 at 7 38 00 PM](https://user-images.githubusercontent.com/64050486/144336681-192e2321-4e7d-4b1a-a7ef-81b4b5bf61b3.png)

## Fetching Tweets by Keyword
first get the amount to search per keyword

![Screen Shot 2021-12-01 at 7 39 21 PM](https://user-images.githubusercontent.com/64050486/144336776-e2957aa3-1982-4e1b-a0b9-694d18fba009.png)

## Query twitter.

In order to search for tweets we must specify the parameters.

Language is set to english.
start date and end date is set to 2021-10-01, 2021-12-01
the amount of tweets per keyword is 240.
the inner for loop just gets the corresponding ticker name, so we dont lose track of which tweet is talking about which ticker.
![Screen Shot 2021-12-01 at 7 40 16 PM](https://user-images.githubusercontent.com/64050486/144336862-61666984-8540-43e8-8d0d-d7d6ad84f9f3.png)

Creating dataframes to plot and review.
![Screen Shot 2021-12-01 at 7 41 11 PM](https://user-images.githubusercontent.com/64050486/144336923-0558db21-d50a-4d9c-bf3b-f77b50152c7c.png)
Visualize the top ten tickers in All tweets, postive tweets, negative tweets, neutral tweets.
![Screen Shot 2021-12-01 at 7 41 57 PM](https://user-images.githubusercontent.com/64050486/144336994-1b5fe2cb-44d7-4a6c-b84f-f38ae7b6b77e.png)



Team 1 members:

David Ingraham
Donna Salinas
Edward Foote
Gabby Giordano
Youssef Said
