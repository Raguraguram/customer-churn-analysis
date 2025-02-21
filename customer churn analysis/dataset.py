import pandas as pd
import numpy as np

# Generate synthetic dataset
np.random.seed(42)
n_customers = 1000
data = {
    "CustomerID": range(1, n_customers + 1),
    "Tenure": np.random.randint(0, 60, n_customers),
    "LastRechargeDays": pd.date_range(start="2023-01-01", periods=1000, freq='D'),
    "ContractType": np.random.choice(["Retained", "Churned"], n_customers, p=[0.7, 0.3]),
    "plan_type": np.random.choice(["Prepaid", "Postpaid"], n_customers),
    "Churn": np.random.choice([0, 1], n_customers, p=[0.8, 0.2]),
    "Feedback": np.random.choice([
        "Service is too expensive",
        "Poor customer service",
        "Network issues",
        "Better offers from competitors",
        "Not satisfied with the plan",
        "Moving to a different location",
        "No specific reason"
    ], n_customers)
}
df = pd.DataFrame(data)

# Introduce some missing values
df.loc[np.random.choice(df.index, size=50, replace=False), "Tenure"] = np.nan
df.loc[np.random.choice(df.index, size=30, replace=False), "LastRechargeDays"] = np.nan

# Save to CSV file
csv_filename = "customer_churn_dataset.csv"
df.to_csv(csv_filename, index=False)

csv_filename