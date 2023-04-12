import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 1 : Reading The CSV data From The CSv File
data = pd.read_csv("customer_segmentation.csv")
print("The Data For The Life Time Value is ")
print(data)

# 2 : Getting The Top Of The records
print("The top 10 Records Are ")
print(data.head(10))

# 3 : Getting The last 10 records
print("The Last 10 Records Are")
print(data.tail(10))

# 4 : Describing The Data
print(data.describe())

# Main Engineering Here :

# Part1 : 1 Feature Engineering

#converting the type of Invoice Date Field from string to datetime.
print("before Converting The invoice Date into the String Date time ")
print(data["InvoiceDate"])
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
print("after Converting The Invoice Date into the String date Time ")
print(data["InvoiceDate"])

#creating YearMonth field for the ease of reporting and visualization
data['InvoiceYearMonth'] = data['InvoiceDate'].map(lambda date: 100*date.year + date.month)

# Now Describing The data is
print(data.describe())

# Now Counting the Country
print("After Counting the value Of The Country is ")
print(data["Country"].value_counts())
print("Counting the Value Of The Customer Id  ")
print(data["CustomerID"].value_counts())

# Starting from this part, we will be focusing on UK data only (which has the most records).
# We can get the monthly active customers by counting unique CustomerIDs.
# The same analysis can be carried out for customers of other countries as well.

# Here We Are Going To use The United Kingdom Data Only
# we will be using only UK data and droping the Other Country Data
tx_uk = data.query("Country=='United Kingdom'").reset_index(drop=True)
print("After Dropping The Remaining Country Data  ")
print(tx_uk)

# Segmentation Techniques
#
# You can do many different segmentations according to what you are trying to achieve.
# If you want to increase retention rate, you can do a segmentation based on churn probability
# and take actions. But there are very common and useful segmentation methods as well. Now we are
# going to implement one of them to our business: RFM. RFM stands for Recency - Frequency - Monetary Value.
# Theoretically we will have segments like below:
#
# Low Value: Customers who are less active than others, not very frequent buyer/visitor and generates
# very low - zero - maybe negative revenue.
# Mid Value: In the middle of everything. Often using our platform (but not as much as our High Values),
# fairly frequent and generates moderate revenue.
# High Value: The group we don’t want to lose. High Revenue, Frequency and low Inactivity.
# As the methodology, we need to calculate Recency, Frequency and Monetary Value (we will call it
# Revenue from now on) and apply unsupervised machine learning to identify different groups (clusters) for each.
# Let’s jump into coding and see how to do RFM Clustering.
#
# 3. Recency

# To calculate recency, we need to find out most recent purchase date of each customer and see how many days
# they are inactive for. After having no. of inactive days for each customer, we will apply K-means*
# clustering to assign customers a recency score.
# Lets go ahead and calculate that.

# #create a generic user dataframe to keep CustomerID and new
# segmentation scores

tx_user = pd.DataFrame(data["CustomerID"].unique())
print("The Unique CustomerID is ")
print(tx_user)
tx_user.columns = ["CustomerID"]
print(tx_user.head())
print("The Head of The United kingdom is ")
print(tx_uk.head())

# Since we are calculating recency, we need to know when last the person bought something.
# Let us calculate the last date of transaction for a person.

#get the max purchase date for each customer and create a dataframe with it
tx_max_purchase = tx_uk.groupby('CustomerID').InvoiceDate.max().reset_index()
print("The Maximum & last purchase By the Person data from The Data Set is ")
print(tx_max_purchase)
tx_max_purchase.columns = ['CustomerID','MaxPurchaseDate']
print("The Last purchase of the person is ")
print(tx_max_purchase.head())

# Compare the last transaction of the dataset with last transaction dates of the individual customer IDs.
tx_max_purchase['Recency'] = (tx_max_purchase['MaxPurchaseDate'].max() - tx_max_purchase['MaxPurchaseDate']).dt.days
print("The Last Transaction With the Transactoon of The individual Customer id is ")
print(tx_max_purchase.head())

#merge this dataframe to our new user dataframe
tx_user = pd.merge(tx_user, tx_max_purchase[['CustomerID','Recency']], on='CustomerID')
print(tx_user)
print("merging The data With New user data Frame is ")
print(tx_user.head())

from sklearn.cluster import KMeans

sse={} # error
tx_recency = tx_user[['Recency']]
for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, max_iter=1000).fit(tx_recency)
    tx_recency["clusters"] = kmeans.labels_  #cluster names corresponding to recency values
    sse[k] = kmeans.inertia_ #sse corresponding to clusters
plt.figure()
plt.plot(list(sse.keys()), list(sse.values()))
plt.xlabel("Number of cluster")
plt.show()

#build 4 clusters for recency and add it to dataframe
kmeans = KMeans(n_clusters=4)
print("The k Means is ")
print(kmeans)
tx_user['RecencyCluster'] = kmeans.fit_predict(tx_user[['Recency']])
print("The Tx User RecencyCluster is ")
print(tx_user['RecencyCluster'])
print("The Head of The data is ")
print(tx_user.head())
print("After this Description is ")
print(tx_user.groupby('RecencyCluster')['Recency'].describe())

# 4. Frequency
# To create frequency clusters, we need to find total number orders for each customer.
# First calculate this and see  how frequency look like in our customer database

#get order counts for each user and create a dataframe with it
tx_frequency = tx_uk.groupby('CustomerID').InvoiceDate.count().reset_index()
tx_frequency.columns = ['CustomerID','Frequency']
print("The Tx Frequency is ")
print(tx_frequency)
print("The Tx frequency Column is ")
print(tx_frequency.columns)

#get order counts for each user and create a dataframe with it
tx_frequency = tx_uk.groupby('CustomerID').InvoiceDate.count().reset_index()
tx_frequency.columns = ['CustomerID','Frequency']
print("After Adding This user To The data Frame is ")
print(tx_frequency)

#calculate revenue for each customer
tx_uk['Revenue'] = tx_uk['UnitPrice'] * tx_uk['Quantity']
tx_revenue = tx_uk.groupby('CustomerID').Revenue.sum().reset_index()
print("The Revenue Of The Each Customer is ")
print(tx_revenue.head())


