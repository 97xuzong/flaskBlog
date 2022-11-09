import pandas as pd
import numpy as np

time_list = pd.date_range(start="2020/1/1", end="2021/12/12").to_list()
user = ["pony", "mark", "john", "sina", "mary"]
user_list = np.random.choice(user, size=len(time_list), replace=True)

df = pd.DataFrame(data={"user": user_list, "login_date": time_list})
print(df)

df_count = df.groupby('user', as_index=False).login_date.count()
df_count.rename(columns={"login_date": "login_count"}, inplace=True)
df_count.sort_values("login_count", inplace=True)
df_count = df_count.reset_index(drop=True)
print(df_count)
