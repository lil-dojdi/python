import pandas as pd
import matplotlib.pyplot as plt
import os



file_path = "python/lab7/orders.csv"
base_dir = os.path.dirname(file_path)

 
# 1. ЗАГРУЗКА И ИССЛЕДОВАНИЕ ДАННЫХ
 

df = pd.read_csv(file_path)

df["order_date"] = pd.to_datetime(df["order_date"], format="%d/%m/%Y %H:%M")

print("=== MISSING VALUES ===")
print(df.isna().sum())

print("\n=== DATA TYPES ===")
print(df.dtypes)


 
# 2. ОЧИСТКА ДАННЫХ
 

df_clean = df[(df["quantity"] > 0) & (df["unit_price"] > 0)].copy()
df_clean = df_clean[(df_clean["discount"] >= 0) & (df_clean["discount"] <= 0.5)]

# отдельные таблицы по статусам
completed_df = df_clean[df_clean["status"] == "Completed"].copy()
returned_df = df_clean[df_clean["status"] == "Returned"].copy()
canceled_df = df_clean[df_clean["status"] == "Canceled"].copy()


 
# 3. НОВЫЕ СТОЛБЦЫ
 

df_clean["gross"] = df_clean["unit_price"] * df_clean["quantity"]
df_clean["net"] = df_clean["gross"] * (1 - df_clean["discount"])
df_clean["is_valid_sale"] = df_clean["status"] == "Completed"


 
# 4. БИЗНЕС-АНАЛИЗ
 

# общий доход
total_income = completed_df["unit_price"].mul(completed_df["quantity"]) \
    .mul(1 - completed_df["discount"]).sum()

# пересчёт net для completed
completed_df["net"] = completed_df["unit_price"] * completed_df["quantity"] * (1 - completed_df["discount"])

# топ-5 продуктов
top_products = (
    completed_df
    .groupby("product")["net"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# категория
category_report = (
    completed_df
    .groupby("category")
    .agg({
        "net": "sum",
        "quantity": "sum",
        "discount": "mean"
    })
)

# возвраты
returned = returned_df.groupby("country").size()
completed = completed_df.groupby("country").size()

return_rate = (returned / (returned + completed)).fillna(0)


 
# 5. ОТЧЁТЫ
 

# месячный отчёт
monthly_report = (
    completed_df
    .groupby(completed_df["order_date"].dt.to_period("M").dt.to_timestamp())["net"]
    .sum()
    .sort_index()
)

# сохранение CSV В ПАПКУ orders.csv
category_report.to_csv(os.path.join(base_dir, "report_category.csv"))
monthly_report.to_csv(os.path.join(base_dir, "report_monthly.csv"))

summary = pd.DataFrame({
    "total_income": [total_income],
    "top_category": [category_report["net"].idxmax()],
    "highest_return_country": [return_rate.idxmax()],
    "top_product": [top_products.idxmax()]
})

summary.to_csv(os.path.join(base_dir, "final_report.csv"), index=False)


 
# 6. ГРАФИК
 

df_clean["day"] = df_clean["order_date"].dt.date

daily_report = (
    completed_df
    .groupby(df_clean["day"])["net"]
    .sum()
    .sort_index()
)

plt.figure(figsize=(12, 5))

plt.plot(
    daily_report.index,
    daily_report.values,
    marker="o",
    linewidth=2
)

plt.title("Daily Revenue (Completed Orders)")
plt.xlabel("Date")
plt.ylabel("Net Revenue")

plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()


 
# 7. ВЫВОД РЕЗУЛЬТАТОВ
 

print("\n=== TOTAL INCOME ===")
print(total_income)

print("\n=== TOP PRODUCTS ===")
print(top_products)

print("\n=== CATEGORY REPORT ===")
print(category_report)

print("\n=== RETURN RATE ===")
print(return_rate)