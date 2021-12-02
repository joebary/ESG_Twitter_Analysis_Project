# Project_3_Team_1
The overall idea for this project is to create an online interactive portfolio. In addition, we will take in information from Twitter and other forms of media to understand how to format our sharpe, calmar, sortino, treynor ratios for market evaluations. Once we have the analysis, we will determine what daily return information we can get based on the standard deviation and other financial metrics. One feature we will try to incorporate for this project is to use federal and state taxes to provide a recommendation for how much a person should invest in fixed income (corporate bond vs municipal bond) based on their age and financial background. 

ESG Data:

Environmental, social, and governance scores are newly yet very quickly becoming essential factors in investing. Therefore, our group decided to include each company in the s&p 500s ESG scores in our portfolio analysis and allocation. We were able to do this through our python function that retrieves this data seven years back (2014-2021) and with a monthly frequency. Specifically, we were able to get our data through our historical ESG functions call to yahoo finance - under the sustainability tab.

Customized Bond Recommendation:

Through our streamlit application, we also included a tab that allows for a customized bond recommendation. It first asks a user to input their income. From that income amount, we know what their federal income tax rate is. It can be the case that an investor will make more from investing in a municipal bond that is tax-exempt versus a treasury or corporate bond that is not tax-exempt, as he or she may be a high net worth individual. Therefore, this person could be taxed more heavily on those coupon payments from treasury or corporate bonds so it is helpful to know which bond could be more profitable. As a result, we use an equation called the tax equivalent yield to calculate the differing bond types comparable yields. Depending on which yield is highest, we recommend that type of bond to the user. We also indicate what they can expect their average yield to be, their portfolio weights, and portfolio returns. Depending on the users age input, the younger they are the greater the portfolio weight goes towards fixed income since it could be more long term. Correspondingly, the older the user the more their portfolio weight goes towards equities. Note: all of this data on the yields and types of bonds we retrieved from Bloomberg terminal.


## Portfolio Analysis


For the portfolio analysis, we created test dataframes to replicate the Twitter data. Tickers were chosen at random from the ESG data and Sentiment values were also chosen at random. The sentiment weights were used to determine each individual equity's weights. 

<img width="159" alt="test2" src="https://user-images.githubusercontent.com/86026996/144332190-e40233fa-a097-46d8-8f7b-2b21d2a5e7a2.png">

Using indexing, the dataframe will dynamically respond to changes from the incoming Twitter dataframe. Individual stock information came from Yahoo Finance. 

<img width="147" alt="test1" src="https://user-images.githubusercontent.com/86026996/144332195-72a788e0-81dc-4044-b160-451d58987fa2.png">


<img width="510" alt="Portfolio_Metrics" src="https://user-images.githubusercontent.com/86026996/144332206-f5ec6595-6674-429f-8ce3-39893e94785e.png">

<img width="482" alt="ESG_slicer" src="https://user-images.githubusercontent.com/86026996/144332211-97d39dc4-5310-494f-8d31-da475a1470eb.png">
<img width="411" alt="ESG_sliced" src="https://user-images.githubusercontent.com/86026996/144332215-12b71ee2-a89a-49da-bf3a-712f16e1fbd8.png">

<img width="558" alt="ESG_metrics" src="https://user-images.githubusercontent.com/86026996/144332219-18f1f6eb-e91b-4b71-95fc-ca5e915d0925.png">





Team 1 members:

David Ingraham
Donna Salinas
Edward Foote
Gabby Giordano
Youssef Said
