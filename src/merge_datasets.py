import pandas as pd
from utils import get_env, log
from normalize_aws import normalize_aws
from normalize_azure import normalize_azure
from normalize_gcp import normalize_gcp

def merge_all():
    aws = normalize_aws(get_env("AWS_COST_FILE"))
    azure = normalize_azure(get_env("AZURE_COST_FILE"))
    gcp = normalize_gcp(get_env("GCP_COST_FILE"))

    all_data = pd.concat([aws, azure, gcp], ignore_index=True)
    all_data["cost"] = all_data["cost"].round(2)
    all_data["date"] = pd.to_datetime(all_data["date"])
    all_data.sort_values(by=["date", "provider"], inplace=True)

    output_path = get_env("OUTPUT_FILE")
    all_data.to_csv(output_path, index=False)
    log(f"Unified dataset exported to {output_path}")

    return all_data
