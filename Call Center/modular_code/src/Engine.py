import  pandas as pd
import matplotlib.pyplot as plt
from ML_Pipeline.Stationarity import Stationarity
from ML_Pipeline.RandomWalk import RandomWalk
from ML_Pipeline.WhiteNoise import WhiteNoise
from ML_Pipeline.Seasonality import Seasonality
from ML_Pipeline.WinterHolt import Winterholt
from ML_Pipeline.ARIMA import ARIMA_Model

# importing the data
raw_csv_data = pd.read_excel("../input/CallCenterData.xlsx")

# check point of data
df_comp = raw_csv_data.copy()

df_comp.set_index("month", inplace=True)

# seeting the frequency as monthly
df_comp = df_comp.asfreq('M')


#df_comp.Healthcare.plot(figsize=(20,5), title="Healthcare")
#plt.savefig("../output/healthcare.png")

#WhiteNoise().white_noise(df_comp)

RandomWalk().random_walk()

#Stationarity().stationarity(df_comp)

#Seasonality().seasonality(df_comp)

#Winterholt().holt(df_comp)

#ARIMA_Model().compute(df_comp)