# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set Streamlit page title
st.title('Imports & Exports Dataset Dashboard')

# Load the dataset
df = pd.read_csv("C:\\Users\\Rajiv Ranjan\\OneDrive\\Documents\\Imports_Exports_Dataset.csv")

# Generate a sample of 3001 records
my_sample = df.sample(n=3001, random_state=55017)

# Sidebar for filtering options
st.sidebar.title('Filter Options')
selected_customer = st.sidebar.selectbox('Select Customer:', my_sample['Customer'].unique())

# 1. Total transaction value by customer
st.subheader('Total Transaction Value by Customer')
total_transaction_value_by_customer = my_sample.groupby('Customer')['Value'].sum()

# Limit the number of customers for better readability
top_customers = total_transaction_value_by_customer.nlargest(15)  # Display top 15 customers only

# Plot Total Transaction Value by Customer
fig, ax = plt.subplots(figsize=(8, 6))
top_customers.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Top 15 Customers by Total Transaction Value')
ax.set_ylabel('Transaction Value')
ax.set_xlabel('Customer')
# Allow matplotlib to set x-axis ticks automatically
plt.xticks(rotation=45)
st.pyplot(fig)

# 2. Distribution of transaction values
st.subheader('Distribution of Transaction Values')
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(my_sample['Value'], bins=10, kde=True, color='purple', ax=ax)
ax.set_title('Distribution of Transaction Values')
ax.set_xlabel('Transaction Value')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# 3. Frequency of customs codes
st.subheader('Frequency of Customs Codes')
customs_code_count = my_sample['Customs_Code'].value_counts()

# Limit the number of customs codes for readability
top_customs_codes = customs_code_count.nlargest(15)

# Plot Frequency of Customs Codes
fig, ax = plt.subplots(figsize=(8, 6))
top_customs_codes.plot(kind='bar', color='orange', ax=ax)
ax.set_title('Top 15 Customs Codes by Frequency')
ax.set_ylabel('Frequency')
ax.set_xlabel('Customs Code')
# Let matplotlib automatically handle x-axis ticks
plt.xticks(rotation=45)
st.pyplot(fig)

# 4. Cumulative Transaction Value over Customers
st.subheader('Cumulative Transaction Value over Customers')
sorted_transaction_values = my_sample.groupby('Customer')['Value'].sum().sort_values(ascending=False).cumsum()

# Plot Cumulative Transaction Value over Customers
fig, ax = plt.subplots(figsize=(8, 6))
sorted_transaction_values[:15].plot(kind='line', marker='o', color='green', ax=ax)  # Limit to top 15 customers
ax.set_title('Cumulative Transaction Value over Top 15 Customers')
ax.set_ylabel('Cumulative Transaction Value')
ax.set_xlabel('Customer')
plt.xticks(rotation=45)
st.pyplot(fig)

# 5. Average Transaction Value per Customer
st.subheader('Average Transaction Value per Customer')
average_transaction_value_by_customer = my_sample.groupby('Customer')['Value'].mean()

# Limit the number of customers for readability
top_avg_customers = average_transaction_value_by_customer.nlargest(15)

# Plot Average Transaction Value per Customer
fig, ax = plt.subplots(figsize=(8, 6))
top_avg_customers.plot(kind='bar', color='salmon', ax=ax)
ax.set_title('Top 15 Customers by Average Transaction Value')
ax.set_ylabel('Average Transaction Value')
ax.set_xlabel('Customer')
plt.xticks(rotation=45)
st.pyplot(fig)

# Display dataset (optional)
st.subheader('Dataset Overview')
st.write(my_sample.head())
