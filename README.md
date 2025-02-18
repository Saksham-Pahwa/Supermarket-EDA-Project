# Supermarket-EDA-Project


## Table of Contents
- [Project Overview](#project-overview)
- [Data Description](#data-description)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
  - [Basic Information](#basic-information)
  - [Data Cleaning](#data-cleaning)
  - [Sales Analysis](#sales-analysis)
  - [Customer Analysis](#customer-analysis)
  - [Product Analysis](#product-analysis)
  - [Time-based Analysis](#time-based-analysis)
  - [Payment Method Analysis](#payment-method-analysis)
  - [Rating Analysis](#rating-analysis)
- [Conclusion](#conclusion)
- [Files](#files)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)

## Project Overview
The Supermarket EDA Project aims to provide detailed insights into the sales data of a supermarket across three branches located in different cities. By performing exploratory data analysis (EDA), we can uncover patterns, trends, and relationships within the data, which can help inform business decisions and strategies.

## Data Description
The dataset used in this project contains sales records from three supermarket branches over three months (January to March 2019). The dataset includes the following columns:

- **Invoice ID**: Unique identifier for each transaction
- **Branch**: Branch of the supermarket ('A', 'B', 'C')
- **City**: City where the branch is located
- **Customer type**: Type of customer (Member or Normal)
- **Gender**: Gender of the customer
- **Product line**: Category of the product
- **Unit price**: Price of each product
- **Quantity**: Number of products purchased
- **Tax 5%**: 5% tax on the total price
- **Total**: Total price including tax
- **Date**: Date of purchase
- **Time**: Time of purchase
- **Payment**: Payment method used (Cash, Credit card, Ewallet)
- **cogs**: Cost of goods sold
- **Gross margin percentage**: Gross margin percentage
- **Gross income**: Gross income
- **Rating**: Customer rating of their shopping experience

## Exploratory Data Analysis (EDA)

### Basic Information
The dataset contains **1000 rows** and **17 columns**. There are no missing values or duplicate records, ensuring that the data is complete and ready for analysis.

### Data Cleaning
Before delving into the analysis, we performed some data cleaning steps:
- Converted the 'Date' and 'Time' columns to datetime format for better analysis.
- Dropped the 'Invoice ID' and 'Branch' columns since they were not relevant to the analysis. Each branch maps to a specific city:
  - Mandalay (B)
  - Naypyitaw (C)
  - Yangon (A)

### Sales Analysis
- **Total sales**: The supermarket generated a total revenue of approximately **$322,966** over the three-month period.
- **Average sales per transaction**: The average sale per transaction was **$322**.
- **Median sales per transaction**: The median sale per transaction was **$253.53**, indicating that some transactions involved high-value purchases.
- **Highest sale**: The highest sale recorded was **$1042.65**.
- **Lowest sale**: The lowest sale recorded was **$10.96**.

### Customer Analysis
- **Total customers**: There were 1000 unique customers in the dataset.
- **Gender distribution**: The customers were almost evenly split by gender:
  - Male: 501
  - Female: 499
- **Customer type distribution**: The distribution between members and non-members was also nearly equal:
  - Member: 501
  - Normal: 499

### Product Analysis
- **Most popular product line**: The 'Fashion accessories' product line had the highest number of transactions.
- **Most revenue-generating product line**: The 'Health and beauty' product line generated the most revenue, with an average sale of **$726.48**.
- **Product line with highest average sales**: The 'Health and beauty' product line also had the highest average sales per transaction.

### Time-based Analysis
- **Most crowded city**: Yangon had the highest number of transactions.
- **Hot selling city**: Despite Yangon being the most crowded, Naypyitaw generated the highest sales revenue.
- **Highest business revenue month**: March was the highest revenue-generating month.
- **Highest business revenue day**: March 29th, 2019, recorded the highest sales.
- **Peak shopping hours**: The peak shopping hours were between 13:00 and 16:00.

### Payment Method Analysis
- **Payment method distribution**: The distribution of payment methods used by customers was as follows:
  - Ewallet: 345 transactions
  - Cash: 344 transactions
  - Credit card: 311 transactions

### Rating Analysis
- **Highest rating**: The highest customer rating was 10.
- **Lowest rating**: The lowest customer rating was 4.
- **Average rating**: The average customer rating was 7.1.
- **Number of customers who gave a rating of 10**: 106 customers gave a perfect rating of 10.
- **Number of customers who gave a rating of 4**: 5 customers gave a rating of 4.

## Conclusion
The EDA provided several valuable insights:
- Naypyitaw, although not the most crowded, was the top revenue-generating city.
- The 'Health and beauty' product line was the top performer in terms of revenue.
- The supermarket saw the highest sales in March, with a peak on March 29th.
- Ewallet and Cash were the most preferred payment methods.
- The average customer rating was positive, with most customers rating their experience at 7 or higher.

## Files
- **supermarket_sales.csv**: The dataset containing sales data.
- **supermarket_eda.py**: The Python script used for the exploratory data analysis.

