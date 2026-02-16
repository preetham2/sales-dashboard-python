import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("Superstore.csv")
df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
df = df.dropna(subset=["OrderDate"])

# Create Revenue column
df["Revenue"] = df["Sales"] * df["Quantity"]

# 1) Monthly Revenue Trend
monthly = df.groupby(df["OrderDate"].dt.to_period("M"))["Revenue"].sum().reset_index()
monthly["OrderDate"] = monthly["OrderDate"].astype(str)

plt.figure()
plt.plot(monthly["OrderDate"], monthly["Revenue"])
plt.xticks(rotation=45)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("monthly_revenue_trend.png")
plt.close()

# 2) Profit by Region (bar chart)
profit_region = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)

plt.figure()
profit_region.plot(kind="bar")
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("profit_by_region.png")
plt.close()

# 3) Top Categories by Sales
sales_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure()
sales_category.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.close()

# 4) Loss-making items (negative profit)
loss_items = df[df["Profit"] < 0].groupby("SubCategory")["Profit"].sum().sort_values()
loss_items = loss_items.head(5)

plt.figure()
loss_items.plot(kind="bar")
plt.title("Top 5 Loss-Making SubCategories")
plt.xlabel("SubCategory")
plt.ylabel("Total Loss (Profit)")
plt.tight_layout()
plt.savefig("loss_making_subcategories.png")
plt.close()

print("Dashboard charts created ✅")
print("Saved files:")
print("- monthly_revenue_trend.png")
print("- profit_by_region.png")
print("- sales_by_category.png")
print("- loss_making_subcategories.png")
