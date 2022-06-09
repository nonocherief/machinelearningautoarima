from re import T
import pandas as pd
import matplotlib.pyplot as plt
status = pd.read_csv("data.csv", parse_dates=True)
# status.head()
# print(status)
status2=status.groupby(["date","item"],as_index=False).agg({"price":["count"]})
print(status2)
status3=status2.pivot(index="date",columns="item")
status4=status3.droplevel(axis=1, level=[0,1])
print(status4)

status4.plot()
plt.show()

