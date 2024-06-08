import pandas as pd
test1_path = "C:/Users/funny/Desktop/test1.csv"
test2_path = "C:/Users/funny/Desktop/test2.csv"
df1 = pd.read_csv("test1_path")
df2 = pd.read_csv("test2_path")
merged_df = pd.merge(df1, df2, on = "pixel", suffixes = ("_test1", "_test2"))
merged_df["intensity_diff"] = merged_df["intensity_test1"]-merged_df["intensity_test2"]
result_df = merged_df[["pixel", "intensity_diff"]]
result_df.to_csv("result.csv", index = False)