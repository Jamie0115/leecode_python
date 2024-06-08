import pandas as pd

# 讀取CSV檔案
df1 = pd.read_csv('test.csv')
df2 = pd.read_csv('test 2.csv')

# 確認兩個DataFrame有相同的結構
if df1.shape == df2.shape and all(df1.columns == df2.columns):
    # 數據相減
    df_result = df1 - df2

    # 將結果寫入新的CSV檔
    df_result.to_csv('result.csv', index=False)
else:
    print("兩個CSV檔案的結構不同，無法進行相減操作。")

print("數據相減操作完成，結果已寫入 'result.csv'")