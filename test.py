import pandas as pd


df = pd.read_csv("dummy_job_dataset.csv")


filtered_df = df[df["category_confidence"] >= 4] #keeps the rows with confidence score of 4 or higher


grouped = filtered_df.groupby("canonical_title")


for category, group in grouped:
    print(f"\n=== {category.upper()} ===")

    sorted_group = group.sort_values(by="category_confidence", ascending=False)

    print(sorted_group[["job_title", "skills", "location", "category_confidence"]].to_string(index=False))

total_jobs = len(df)
kept_jobs = len(filtered_df)
print("\nSummary:")
print(f"Total jobs: {total_jobs}")
print(f"Jobs kept after filtering: {kept_jobs}")
print(f"Jobs removed: {total_jobs - kept_jobs}")

#gkgkgkgkgkjg
