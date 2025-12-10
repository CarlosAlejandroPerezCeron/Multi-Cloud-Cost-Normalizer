import pandas as pd
from utils import log

def normalize_azure(path):
    log("Normalizing Azure cost data...")
    df = pd.read_csv(path)

    df_norm = pd.DataFrame({
        "provider": "Azure",
        "account_id": df.get("SubscriptionId", ""),
        "service": df["Service"],
        "region": df.get("Region", ""),
        "date": pd.to_datetime(df["Date"]).dt.date,
        "cost": df["Cost"].astype(float),
        "tags": df.get("TagKey", "")
    })

    log(f"Azure records processed: {len(df_norm)}")
    return df_norm
