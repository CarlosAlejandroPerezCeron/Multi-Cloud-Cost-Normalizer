import pandas as pd
from utils import log

def normalize_gcp(path):
    log("Normalizing GCP cost data...")
    df = pd.read_csv(path)

    df_norm = pd.DataFrame({
        "provider": "GCP",
        "account_id": df["project_id"],
        "service": df["service"],
        "region": df.get("region", ""),
        "date": pd.to_datetime(df["date"]).dt.date,
        "cost": df["total_cost"].astype(float),
        "tags": ""
    })

    log(f"GCP records processed: {len(df_norm)}")
    return df_norm
