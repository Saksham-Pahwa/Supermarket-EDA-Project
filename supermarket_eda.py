import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_csv("D:\\python_datascience\\data sets\\supermarket_sales - Sheet1.csv")


df.sample(3)


df.shape


# **observation**:
# - This Dataset has 1000 rows and 17 columns 


df.info()


# **observation:**
# from above output , all columns are in appropriate type except date and time so we need to convert into datetime for better analysis
# - and also the column invoice id is seems irrelavant wrt to EDA so we will drop it later.


df.columns


# ##### - Column Description
# 
# - Invoice id: Computer generated sales slip invoice identification number
# 
# - Branch: Branch of supercenter (3 branches are available identified by A, B and C).
# 
# - City: Location of supercenters
# 
# - Customer type: Type of customers, recorded by Members for customers using member card and Normal for without member card.
# 
# - Gender: Gender type of customer
# 
# - Product line: General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel
# - Unit price: Price of each product in $
# 
# - Quantity: Number of products purchased by customer
# 
# - Tax: 5% tax fee for customer buying
# 
# - Total: Total price including tax
# 
# - Date: Date of purchase (Record available from January 2019 to March 2019)
# 
# - Time: Purchase time (10am to 9pm)
# 
# - Payment: Payment used by customer for purchase (3 methods are available – Cash, Credit card and Ewallet)
# 
# - COGS: Cost of goods sold
# 
# - Gross margin percentage: Gross margin percentage
# - Gross income: Gross income
# 
# - Rating: Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)


df.isnull().sum().to_frame().rename(columns={0:"missing values count"}).T


# #### **OBSERVATION** : 
# There is no missing values in the data, so data seems simple


df.duplicated().sum()


# ** OBSERVATION** : There is no duplicacy in the data


# since the invoice id is irrelavant column so we drop  and also we are dropping the Branch column since each  branch maps to each city as below:
# 
# - Mandalay     [B]
# - Naypyitaw    [C]
# - Yangon       [A]


df.drop(columns=["Invoice ID","Branch"],inplace=True)


# verifying the result
df.shape


# ## checking the inconsitency or invalid value  in the columns

# **First seggregating the data into object and numeric types and check the inconsitency accordingly**


df_obj=df.select_dtypes(include="object")
for col in df_obj.columns:
    print(col,"-----------------",df[col].unique(),"has ",df[col].nunique(),'values',"\n\n")


df_numeric=df.select_dtypes(exclude="object")
for col in df_numeric.columns:
    for i in df[col] :
        if i<0:
            print("invalid value")


# #  feature engineering column extraction 


df["Date"]=pd.to_datetime(df["Date"])
df["Time"]=pd.to_datetime(df["Time"])


df.dtypes


from datetime import datetime as dt


df["month"]=df.Date.dt.month_name()
df["day_name"]=df.Date.dt.day_name()
df["day"]=df.Date.dt.day
df["year"]=df.Date.dt.year
df["Hour"]=df.Time.dt.hour


# ## Insights 


df.columns


df.describe().T


df.describe().T.iloc[:-3]


cols=df.describe().T[:-3].index
cols


pos=1
plt.figure(figsize=(16,10))
for col in cols:
    plt.subplot(2,4,pos)
    sns.boxplot(x=col,data=df,color="yellow")
    plt.title(f"outlier detection in {col}")
    pos=pos+1


pos=1
plt.figure(figsize=(16,10))
for col in cols:
    plt.subplot(2,4,pos)
    sns.distplot(df[col])
    plt.title(f"distribution {col}")
    pos=pos+1


plt.figure(figsize=(10,7))
sns.heatmap(df[cols].corr(),annot=True,cmap="rainbow")


# **observation:**:
#         - There is perfect positive relation found between 
#         Total, gross income, tax 5% , cogs
#         - There is sort of positive relation between Total, quantity 
#         - There is no correlation between rating and quantity and total


df.drop(columns=["Tax 5%","cogs","gross income","gross margin percentage"],inplace=True)


df.head(2)


# since the total column is the main column under this eda so we do the univariate analysis


plt.figure(figsize=(15,4),facecolor="pink")
plt.subplot(1,2,1)
sns.distplot(df["Total"])
plt.title("distribution of Total Sale")
plt.subplot(1,2,2)
sns.boxplot(df["Total"])
plt.title("outliers in Total Sale");


# ## Total  and average sale  of the company 


df["Total"].agg(["mean","sum"])


# since the some products are expensive means they are considered as outliers so we find median since the above avg sale does give the genuine insight 


df["Total"].median()


# ## Observation:
# 
# - Total sale of the company is approx 322966 dollar
# - Average sale of the company is approx 322 dollar


# ## Which city is more crowed ?


sns.countplot(x="City",data=df,palette="Set2")
plt.title("crowded city")


## insight : yangon


# ## Total and average sale of each City 


plt.figure(figsize=(15,4),facecolor="pink")
plt.subplot(1,2,1)
sns.barplot(x="City",y="Total",data=df)
plt.title("Average sale of each City")
plt.subplot(1,2,2)
sns.barplot(x="City",y="Total",data=df,estimator=sum)
plt.title("Total sale of each City")


# # Insight :
# 
# althogh there is no much significant difference  between each city but still we can observe 
# **Naypyitaw** is found to be hot selling city

# **Insight:**
# 
# - Though the crowded city was yangon but hot selling city found to be Naypitaw
#     There is not much significant differeence between three supermarts in each city but still the city name Naypitaw is found to  be hot selling city 


# ## Find the Highest sale in naypyitaw  on any day


df_n=df[df["City"]=="Naypyitaw"]
df_n[df_n["Total"]==df_n["Total"].max()]


# ## Find the lowest sale in naypyitaw  on any day


df_n=df[df["City"]=="Naypyitaw"]
df_n[df_n["Total"]==df_n["Total"].min()]


# ## Root cause analysis of Hot selling City


df.head(2)


# ## Taking factor customer type 


sns.countplot(x="City",data=df,hue="Customer type")


sns.barplot(x="City",y="Rating",data=df)


df[df["Unit price"]==df["Unit price"].max()]


df.groupby(["City"])["Product line"].agg(["value_counts"])


# there is not a specific cause behind the hot selling branch / city this could be due to natural factor  


df.head(2)


# ### Find  the highest business revenue  month  of the company


df.groupby(["month"])["Total"].agg(["sum"])


plt.figure(figsize=(15,4))
plt.subplot(1,2,1)
sns.barplot(x="month",y="Total",data=df,estimator=sum,palette="Set2")
plt.title("Highest business revenue month",fontsize=12,color="Red",fontweight="bold")
plt.subplot(1,2,2)
plt.pie(df.groupby(["month"])["Total"].agg(["sum"])["sum"],labels=df.groupby(["month"])["Total"].agg(["sum"]).index,autopct="%.2f%%",colors=sns.color_palette('Set2'))
plt.title("Hot selling Month of the company ",fontsize=12,color="Red",fontweight="bold")


# ## find the highest business revenue of month of  each City/Branch and also sale pattern 


plt.figure(figsize=(15,4),facecolor="pink")
plt.subplot(1,2,1)
sns.barplot(x="City",y="Total",data=df,estimator=sum,palette="Set2",hue="month");
plt.title("Average sale of each city in each month ",fontsize=15,color="brown",fontweight="bold")
plt.subplot(1,2,2)
sns.boxplot(x="City",y="Total",data=df,palette="Set2",hue="month");
plt.title("sale pattern of each city in each month",fontsize=15,color="brown",fontweight="bold");


# ## Sale trend of company over the three months


plt.figure(figsize=(15,5))
sns.relplot(x="Date",y="Total",data=df,kind="line",color="purple",estimator=sum,ci=False)
plt.xlabel("date")
plt.title(" Company Sale trend over the  3 months ",fontsize=10,color="red",fontweight="bold")
plt.xticks(rotation=90);


# ## Sale trend of each city 


df_n=df[df["City"]=="Naypyitaw"]
df_y=df[df["City"]=="Yangon"]
df_m=df[df["City"]=="Mandalay"]


cities=[df_y,df_n,df_m]


city_name=["Yangon", 'Naypyitaw', 'Mandalay']
pos=1
plt.figure(figsize=(14,5))
for city in cities:
    plt.subplot(1,3,pos)
    sns.lineplot(x="Date",y="Total",data=city,estimator=sum,ci=False)
    plt.title(f"the trend of city {city_name[pos-1]}")
    plt.xticks(rotation=90)
    pos=pos+1


#  ### sale  trend of each branch/City at each month


city_name=["Yangon", 'Naypyitaw', 'Mandalay']
pos=1
plt.figure(figsize=(14,5))
for city in cities:
    plt.subplot(1,3,pos)
    sns.lineplot(x="Date",y="Total",data=city,estimator=sum,ci=False,hue="month")
    plt.title(f"the trend of city {city_name[pos-1]}")
    plt.xticks(rotation=90)
    pos=pos+1


# ## Hot selling day of the company


plt.figure(figsize=(10,6))
sns.barplot(x="day",y="Total",data=df,estimator=sum,palette="Set2")
plt.xticks(rotation=90)
plt.title("Hot selling day");


# ## Hot selling day of each branch/city 


city_name=["Yangon", 'Naypyitaw', 'Mandalay']
pos=1
plt.figure(figsize=(14,15))
for city in cities:
    plt.subplot(3,1,pos)
    sns.barplot(x="day",y="Total",data=city,estimator=sum,ci=False)
    plt.title(f"the hot selling day of city {city_name[pos-1]}")
    plt.xticks(rotation=90)
    pos=pos+1


# #### Find Total weekdays sale and weekends sale


df["weekday/weeknd"]=df["day_name"].apply(lambda x: "weekend "if x=="Saturday" or x=="Sunday" else "weekday")


sns.barplot(x="weekday/weeknd",y="Total",data=df,estimator=sum,palette="pastel");


df.groupby(["weekday/weeknd"])["Total"].sum()


plt.pie(df.groupby(["weekday/weeknd"])["Total"].sum().values,labels=df.groupby(["weekday/weeknd"])["Total"].sum().index,autopct="%.2f%%");


# ## weekday and weekend sale of each city 


plt.figure(figsize=(10,4))
sns.barplot(x="City",y="Total",data=df,estimator=sum,palette="pastel",hue="weekday/weeknd")


# ## weekday and weekend sale of each branch/City of each month


df.groupby(["City","month","weekday/weeknd"])["Total"].agg(["sum"])


df.head(2)


# #### Find most populated product of the company/most demanding


sns.countplot(x="Product line",data=df,palette="pastel")
plt.xticks(rotation=90);


# #### Most populated product of the each City


plt.figure(figsize=(10,6))
sns.countplot(x="City",data=df,hue="Product line",palette="Set2")
plt.xticks(rotation=90);


# ## Find the most revenue generating product of the company


sns.barplot(x="Product line",y="Total",estimator=sum,data=df,palette="Set2")
plt.xticks(rotation=90);


plt.figure(figsize=(10,12))
sns.barplot(x="City",y="Total",estimator=sum,data=df,palette="Set2",hue="Product line",ci=None)
plt.xticks(rotation=90);


# #### Find city  and month wise demand of product detail


df.groupby(["City","month"])["Product line"].value_counts()


# #### Find the total number of Customers 


df.head(2)


print("total customers : ",df["Gender"].count())
sns.countplot(x="Gender",data=df)


# # Total male and female customers in each city


sns.countplot(x="City",data=df,hue="Gender")


# ## Which type of customer visiting most in each city


sns.countplot(x="City",data=df,hue="Customer type")


sns.barplot(x="City",y="Total",data=df,hue="Customer type")


df.columns


df["Payment"].value_counts()


plt.pie(df["Payment"].value_counts().values,labels=df["Payment"].value_counts().index,autopct="%.2f%%");


df_n["Payment"].value_counts()


df_y["Payment"].value_counts()


df_m["Payment"].value_counts()


cities


cities[0]


plt.figure(figsize=(12,5))
plt.subplot(1,3,1)
plt.pie(df_y["Payment"].value_counts().values,labels=df_y["Payment"].value_counts().index,autopct="%.2f%%")
plt.title("% of customers based on \nmode of payement of city yangon")
plt.subplot(1,3,2)
plt.pie(df_m["Payment"].value_counts().values,labels=df_m["Payment"].value_counts().index,autopct="%.2f%%")
plt.title("% of customers based on \n mode of payement of city mandalay")
plt.subplot(1,3,3)
plt.pie(df_n["Payment"].value_counts().values,labels=df_n["Payment"].value_counts().index,autopct="%.2f%%")
plt.title("% of customers based on\n mode of payement of city naypayitaw");


# # who contributed most in each city


sns.barplot(x="City",y="Total",data=df,estimator=sum,hue="Gender")


# # from which type customers revenue is generated high


sns.barplot(x="Branch",y="Total",data=df,hue="Customer type",estimator=sum);


sns.catplot(x="Branch",y="Total",data=df,hue="Customer type",estimator=sum,col="Gender",kind="bar");


df.columns


# #### Find the peak time of Customers visit at supermarket

# ## add hour for better analysis

# # hour


df.columns


df["Hour"]


plt.figure(figsize=(17,9))
sns.relplot(x="Hour",y="Total",data=df,estimator=sum,kind="line",ci=None)


# ## peak time for each city


city_name=["Yangon", 'Naypyitaw', 'Mandalay']
pos=1
plt.figure(figsize=(14,15))
for city in cities:
    plt.subplot(3,1,pos)
    sns.lineplot(x="Hour",y="Total",data=city,estimator=sum,ci=False)
    plt.title(f" hourly sale trend of {city_name[pos-1]}")
    plt.xticks(rotation=90)
    pos=pos+1


city_name


city=['Yangon', 'Naypyitaw', 'Mandalay']
pos=1
plt.figure(figsize=(25,15))
for i in cities:
    plt.subplot(3,1,pos)
    sns.lineplot(x="Hour",y="Total",data=i,estimator=sum,ci=None,hue="Product line")
    plt.title(f"peak time of branch {city[pos-1]}")
    plt.xticks(list(range(10,21)))
    pos=pos+1


# # rating

# #### Find Highest,lowest and average rating to the company


df["Rating"].agg(["max","min","mean"])


# #### How many customers had given 10 ratings ???


print(len(df[df["Rating"]==10.0]), "customers had given 10 rating")
print((len(df[df["Rating"]==10.0])*100)/df["Rating"].count(),"% customers had given 10 rating")


df["Rating"].unique()
len(df["Rating"].unique())


len(df["Rating"].value_counts())
df["Rating"].value_counts()


sns.countplot(x="Rating",data=df)


# #### How many customers had given 4 ratings ???


print(len(df[df["Rating"]==4.0]), "customers had given 4 rating")
print((len(df[df["Rating"]==4.0])*100)/df["Rating"].count(),"% customers had given 10 rating")


# #### How many customers had given below or equals 5 ratings ???


print(len(df[df["Rating"]<=5.0]), "customers had given below rating")
print((len(df[df["Rating"]<=5.0])*100)/df["Rating"].count(),"% customers had given below 5 rating")


# ####  Find  Ratings given by customers at each City


df.groupby(["City"])["Rating"].agg(["max","min","mean"])


# ## rating wrt each product


df.groupby(["Product line"])["Rating"].agg(["max","min","mean"])


df.groupby(["City","Product line"])["Rating"].agg(["max","min","mean"])


# #### or Visually we can plot as below


import seaborn as sns
plt.figure(figsize = (17,4))
a=df[(df["Branch"] =="A")]
plt.subplot(1,3,1)
plt.hist(a["Rating"],edgecolor="red",bins=[0,1,2,3,4,5,6,7,8,9,10,11])
plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
plt.title("Customer ratings at branch A")
b=df[(df["Branch"] =="B")]
plt.subplot(1,3,2)
plt.hist(b["Rating"],edgecolor="red",bins=7)
plt.xticks(rotation = 90)
plt.title("Customer ratings at Branch B")
c=df[(df["Branch"] =="C")]
plt.subplot(1,3,3)
plt.hist(c["Rating"],edgecolor="red",bins=7)
plt.xticks(rotation = 90)
plt.title("Customer ratings at Branch C")
plt.show()
print(" total customers at branch A is ",a["Customer type"].count())
print(" total customers at branch B is ",b["Customer type"].count())
print(" total customers at branch C is ",c["Customer type"].count())


# #### Insight:
# 
# At branch B 50 CUSTOMERS  had given the rating around 4 to 5 so it seems that some customers of branch B were not satisfied so business managers should provide proper feedback form to get the cause and improve the customer relationship  
