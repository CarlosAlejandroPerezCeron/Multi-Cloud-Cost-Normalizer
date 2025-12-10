from merge_datasets import merge_all
from utils import log

def main():
    log("=== Multi-Cloud Cost Normalizer ===")
    merged = merge_all()

    summary = merged.groupby("provider")["cost"].sum().reset_index()
    log("Total cost per provider:")
    log(summary.to_string(index=False))

if __name__ == "__main__":
    main()
