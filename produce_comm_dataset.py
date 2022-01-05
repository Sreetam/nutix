# -*- coding: utf-8 -*-
import pandas as pd
from datetime import date, timedelta
import matplotlib.pyplot as plt

raw = pd.read_csv("peanuts.csv")
pn = pd.DataFrame(columns=["price"], index=pd.to_datetime(raw.date), data=raw.price.values)
raw = pd.read_csv("BrentOil.csv")
bc = pd.DataFrame(columns=["price"], index=pd.to_datetime(raw.date), data=raw.price.values)
bc = bc[pn.index[0]-timedelta(days=1):pn.index[-1]]
bc.reset_index(inplace=True)
pn.reset_index(inplace=True)

oil = []
peanut = []
date = pd.date_range(bc.date[0],pn.date[359],freq='d')
for i in date:
  if i in list(pn.date):
    peanut.append(pn.loc[pn["date"]==i].price.values[0])
  else:
    peanut.append(peanut[-1])
  if i in list(bc.date):
    oil.append(bc.loc[bc["date"]==i].price.values[0])
  else:
    oil.append(oil[-1])
df = pd.DataFrame()
df['peanut'] = peanut
df['oil'] = oil
df.index = date
df.to_csv("commodities.csv")
ndf = (df-df.mean())/df.std()

plt.plot(ndf.peanut)
plt.plot(ndf.oil)
plt.savefig("pricefig.png")