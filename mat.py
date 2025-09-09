import pandas as pd

df = pd.read_csv("restaurants_dataset.csv")
print(df)


print(df.info())
print(df.isnull().sum())

print(df.groupby("Restaurant")["Rating"].max())

print()
print("HIGH RATING RESTAURANT")
top_rest = df.loc[df["Rating"].idxmax()]
print(top_rest)

#print(df.loc[df["Rating"].idxmax()])

print()
print("AVG RATING BY CUISINE")
avg_rate = df.groupby("Cuisine")["Rating"].mean()
print(avg_rate)
#print(df.groupby("Cuisine")["Rating"].mean())

print()

print("AVG COST BY LOCATION")
avg_cost = df.groupby("Location")["Avg_Cost"].mean()
print(avg_cost)

top_rest = df.sort_values(by="Restaurant", ascending=False).head(5)
print(top_rest)

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

avg_rating = df.groupby("Cuisine")["Rating"].mean()

plt.bar(avg_rating.index,avg_rating.values,color="gold")
plt.xlabel("cuisine")
plt.ylabel("average rating")
plt.title("AVG RATING BY CUISINE")
plt.xticks(rotation=45,ha="right")
plt.grid(linestyle=':',color="gray")
plt.tight_layout()
plt.savefig("restaurants_avg_rating.png",dpi=300)
plt.show()


plt.bar(df["Restaurant"],df["Rating"],color="purple",label="top restaurants")
plt.xlabel("RESTAURANT")
plt.ylabel("RATING")
plt.title("TOP RESTAURANT BY RATING")
plt.xticks(rotation=45,ha="right")
plt.legend(loc="upper left",fontsize=10)
plt.tight_layout()
plt.savefig("TOP RESTAURANT BY RATING.png",dpi=300)
plt.show()


avg_cost = df.groupby("Location")["Avg_Cost"].mean().sort_values()
plt.plot(avg_cost.index,avg_cost.values,marker="o",color="orange",linestyle="--",label="Average Cost")
plt.xlabel("LOCATION")
plt.ylabel("AVERAGE COST")
plt.title("AVG COST BY LOCATION")
plt.xticks(rotation=45,ha="right")
plt.legend(loc="upper left",fontsize=10)
plt.tight_layout()
plt.savefig("AVG COST BY LOCATION.png",dpi=300)
plt.show()


cuisine = df["Cuisine"].value_counts().head(5)

plt.pie(cuisine,labels=cuisine.index,autopct="%1.1f%%",startangle=90)
plt.title("CUISINE COUNT")
plt.tight_layout()
plt.savefig("CUISINE COUNT.png",dpi=300)
plt.show()


#SUBPLOT
plt.figure(figsize=(20,12))

plt.subplot(2,2,1)
plt.bar(avg_rating.index,avg_rating.values,color="gold")
plt.ylabel("average rating",fontweight="bold",fontsize=10)
plt.title("AVG RATING BY CUISINE")
plt.xticks(rotation=45,ha="right",fontsize=10,fontweight="bold")
plt.grid(linestyle=':',color="gray")

plt.subplot(2,2,2)
plt.bar(df["Restaurant"],df["Rating"],color="purple",label="top restaurants")
plt.ylabel("RATING",fontweight="bold",fontsize=10)
plt.title("TOP RESTAURANT BY RATING")
plt.xticks(rotation=45,ha="right",fontsize=10,fontweight="bold")
plt.legend(loc="upper left",fontsize=10)

plt.subplot(2,2,3)
plt.plot(avg_cost.index,avg_cost.values,marker="o",color="orange",linestyle="--",label="Average Cost")
plt.xlabel("LOCATION")
plt.ylabel("AVERAGE COST",fontsize=10,fontweight="bold")
plt.title("AVG COST BY LOCATION")
plt.xticks(rotation=45,ha="right",fontsize=10,fontweight="bold")
plt.yticks(fontsize=12,fontweight="bold")
plt.legend(loc="upper left",fontsize=10)


plt.subplot(2,2,4)
plt.pie(cuisine,labels=cuisine.index,autopct="%1.1f%%")
plt.title("CUISINE COUNT",fontsize=10,fontweight="bold")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.suptitle("RESTAURANT DATA ANALYSIS",fontsize=14,fontweight="bold")
#plt.subplots_adjust(hspace=0.5, wspace=0.4)
#plt.subplots_adjust(bottom=0.2)

plt.savefig("RESTAURANT ANALYSIS",dpi=300)
plt.show()

