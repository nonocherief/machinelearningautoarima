import process_data as futuredata
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from pmdarima import auto_arima
from sklearn.preprocessing import MinMaxScaler

# print(futuredata.status4)

itemc = futuredata.status4["cameras"]
itemc=itemc.dropna()
print(itemc)

train = itemc[0:len(itemc)-30]
test = itemc[len(itemc)-30:]
print(train)

# scaler=MinMaxScaler(feature_range=(0,1))
# print(itemc.to_numpy().reshape(-1, 1))
# scaled_data=scaler.fit_transform(itemc.to_numpy().reshape(-1, 1))
# scaled_data_new=scaled_data.reshape(-1)
# X_train, X_test = train_test_split(scaled_data_new, test_size=.20, random_state=0)
# print(X_train)
# print(X_test)

model = auto_arima(
	train.to_numpy(),
	start_p=1, 
	start_q=1,
    test='adf',       
    max_p=3, 
	max_q=3,
	m=12,
	start_P=0, 
    D=1, 
    trace=True,
	d=None,
	error_action="ignore",
	seasonal=True,
	suppress_warnings=True,
	stepwise=True)

print(model.summary())

forecast = model.predict(n_periods=30)
print(forecast)

print(test)
plt.plot(forecast)
plt.plot(test)
plt.show()


