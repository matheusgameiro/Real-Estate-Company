# Real Estate Company

Link to the app: https://real-estate-company-mg.herokuapp.com/

## **PREMISES:**

This project has the objective to answer business questions and find good propreties buying opportunities, this way, the Real Estate Company will be able to resell for a higher price and thus obtain a higher profit thanks to this.

Real Estate asked on the basis of two main questions:

1. What properties to buy and how much to sell them?

2. When is the best time to sell these properties?

In this way, this project has as premises to be able to answer these questions, and also to produce other relevant insights that may be able to have an impact in decision-making and, consequently, in the business itself.

## **Attributes List:**

| Attributtes     | Meaning                                                      |
| --------------- | ------------------------------------------------------------ |
| id              | Numeral Identification From Each House                       |
| date            | Sales Date From the Houses                                   |
| price           | Prices of Sales                                              |
| bedrooms        | Num of bedrooms                                              |
| bathrooms       | Num of bathrooms                                             |
| sqft_living     | Measured in square feet from the living room                 |
| sqft_lot        | Measured in square feet from the whole house                 |
| floors          | Number of floors                                             |
| waterfront      | Presence of view of water                                    |
| view            | Indicate the quality of view of the house                    |
| condition       | Indicate the condition of the house (1-5)                    |
| grade           | Indicate the quality of the house on grafic design.          |
| sqft_basement   | Measured in square feet from the basement                    |
| yr_built        | Year of built                                                |
| yr_renovated    | Year of renovated                                            |
| zipcode         | Zipcode from the house                                       |
| lat             | Latitude                                                     |
| long            | Longitude                                                    |
| sqft_livining15 | Measured in square feet of the inside of the house in relation with the 15 neighboors more close. |
| sqft_lot15      | Measured in square feet of the all house in relation with the 15 neighboors more close. |

## **Solution Plan:**

The solution plan can be understood with the following points:

Identify good buying opportunites: In this part, my objective with data manipulation was find the median price of properties with the same attributes,these attributes, which are more impacting on the price: zipcode, condition, sqft_lot_level, price. When the property is priced lower than properties with the same characteristics, then this propertie is considered a buying opportunity. Excellent offers are properties with condition equal or more than 4; Good Offers are properties with condition between 2 and 3. If the price was attractive but the condition attribute was equal to 1: not recommended buying
Best time for resale: As we can see below, the best moment to sell properties is the spring season and the best moment to buy these propertiesis in the winter season:

| Season     | Median Price  |
| ---------- | ------------- |
| Autumn     |  443,725.0000 |
| Spring     |  465,000.0000 |
| Summer     |  455,000.0000 |
| Winter     |  430,000.0000 |

Margin of profit to be able to sell: In this part, the profit's percentages varies according to the season:
If Winter: Sell Price = Buy Price * 1.07 (7% of profit)

If Autumn: Sell Price = Buy Price * 1.12 (12% of profit)

If Summer: Sell Price = Buy Price * 1.15 (15% of profit)

If Spring: Sell Price = Buy Price * 1.20 (20% of profit)

## **Validation of hypothesis - Insights Obtained**

9 hypotheses were taken, which were validated or devalued in the course of this project:

H1: Properties with waterview, are on avarage, more expensive.

H2: Properties built before 1955 are on average 15% cheaper.

H3: 30% of properties with a basement have been renovated at least once. 

H4: In terms of "floors", the most common type of properties are those with 1.0 floors.

H5: The buying reccomendations properties are found mostly in East Seattle. 

H6: The north has the highest priced houses.

H7: The annual growth in house prices is around 5%

H8: The monthly house price growth is somewhat linear, always maintaining price stability

H9: Houses before 1960 have a lower average price 

## **Financial Results**

If the company follows the strategy here described and buy the properties classified as buy opportunites, it is estimated that the annual profit around $ 400.896.000 (not included taxes), I believe it is possible to see an increase of about 15% ingross revenue.

## **Next Steps**

I suggest a implementation of a machine learning algorithm in order to help the company Real Estate Company make these analyzes and predictions faster. I reinforce that it is important to receive feedback from bussiness team which will consume this data product. I reiterate the importance of keeping the database accurate and up-to-date to maintain strategy's accuracy, turning possible to keep indicating good buying opportunities.

## **Conclusion**

With the help of this data product, the Real Estate Company will be able to gain productivity and address interesting purchase offers and make sales that are advantageous for it. I believe that the insights generated in the analysis will help the bussiness team open your mind to create new profit strategies.

## **Learns**

This was my first data science project where I learned the data analytics techniques and its libraries like matplotly and plotly, streamlit, pandas, folium and heroku.
