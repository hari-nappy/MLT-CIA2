#%%
import pandas as  pd
df=pd.read_csv("D:\\iitm\\CIA2\\classification.csv")
x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values

from sklearn.linear_model import LogisticRegression
log=LogisticRegression()
log.fit(x,y)
#%%
import pickle
pickle.dump(log,open('cmodel.pkl','wb'))