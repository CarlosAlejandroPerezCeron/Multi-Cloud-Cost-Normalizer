import pandas as pd
from utils import log

def normalize_aws(path):
    log("Normalizing AWS cost data...")
    df = pd.read_csv(path)

    df_norm = pd.DataFrame({
        "provider": "AWS",
        "account_id": df.get("lineItem_UsageAccountId", ""),
        "service": df.get("product_ProductName", ""),
        "region": df.get("product_region", ""),
        "date": pd.to_datetime(df["lineItem_UsageStartDate"]).dt.date,
        "cost": df["lineItem_UnblendedCost"].astype(float),
        "tags": df.get("resourceTags", "")
    })

    log(f"AWS records processed: {len(df_norm)}")
    return df_norm
