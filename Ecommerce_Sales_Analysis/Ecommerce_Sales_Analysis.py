# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("ecommerce_sales.csv")
print(df.head())

print("\nNumber of rows and columns:")
print(df.shape)
print("\nColumn names:")
print(df.columns)
print("\nDataset information:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())

df["Price"] = df["Price"].fillna(df["Price"].median())
df["Region"] = df["Region"].fillna(df["Region"].mode()[0])
print("\nMissing values after cleaning:")
print(df.isnull().sum())

df["Order_Date"] = pd.to_datetime(df["Order_Date"])
print("\nData types after conversion:")
print(df.dtypes)

df["Sales"] = df["Quantity"] * df["Price"]
print("\nDataset with Sales:")
print(df.head())

total_sales = df["Sales"].sum()
print("\nTotal Sales:")
print(total_sales)

total_quantity = df["Quantity"].sum()
print("\nTotal Quantity Sold:")
print(total_quantity)

average_order_value = df["Sales"].mean()
print("\nAverage Order Value:")
print(average_order_value)

product_sales = df.groupby("Product")["Sales"].sum()
print("\nSales by Product:")
print(product_sales)

product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Product:")
print(product_sales)

best_product = product_sales.idxmax()
print("\nBest-Selling Product:")
print(best_product)

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Category:")
print(category_sales)

best_category = category_sales.idxmax()
print("\nBest-Selling Category:")
print(best_category)

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Region:")
print(region_sales)

best_region = region_sales.idxmax()
print("\nBest-Performing Region:")
print(best_region)

df["Month"] = df["Order_Date"].dt.to_period("M")
print("\nDataset with Month:")
print(df[["Order_Date", "Month", "Sales"]].head())

monthly_sales = df.groupby("Month")["Sales"].sum()
print("\nMonthly Sales:")
print(monthly_sales)

best_month = monthly_sales.idxmax()
print("\nBest Sales Month:")
print(best_month)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(category_sales.index, category_sales.values)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(region_sales.index, region_sales.values)
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

top_products = product_sales.head(10)
plt.figure(figsize=(10, 5))
plt.bar(top_products.index, top_products.values)
plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o"
)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
for i, value in enumerate(monthly_sales.values):
    plt.text(i, value, str(int(value)), ha="center", va="bottom")
plt.show()

product_quantity = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print("\nQuantity Sold by Product:")
print(product_quantity)
most_sold_product = product_quantity.idxmax()
print("\nMost Sold Product by Quantity:")
print(most_sold_product)

plt.figure(figsize=(10, 5))
plt.bar(product_quantity.index, product_quantity.values)
plt.title("Quantity Sold by Product")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.show()

lowest_region = region_sales.idxmin()
print("\nLowest-Performing Region:")
print(lowest_region)
print("\nLowest Region Sales:")
print(region_sales.min())

plt.figure(figsize=(8, 5))
plt.bar(region_sales.index, region_sales.values)
plt.title("Sales Performance by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
for i, value in enumerate(region_sales.values):
    plt.text(i, value, str(int(value)), ha="center", va="bottom")
plt.show()

print("\n========== E-COMMERCE SALES ANALYSIS ==========")

print("\nTotal Sales:")
print(total_sales)
print("\nTotal Quantity Sold:")
print(total_quantity)
print("\nAverage Order Value:")
print(round(average_order_value, 2))
print("\nBest-Selling Product:")
print(best_product)
print("\nMost Sold Product by Quantity:")
print(most_sold_product)
print("\nBest-Selling Category:")
print(best_category)
print("\nBest-Performing Region:")
print(best_region)
print("\nLowest-Performing Region:")
print(lowest_region)
print("\nBest Sales Month:")
print(best_month)

print("\n===============================================")