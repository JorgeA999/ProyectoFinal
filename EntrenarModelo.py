import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle


DF = 'DatasetML/dataset_entrenamiento.csv'
MOUT = 'Modelo/modelo_iri.pkl'


df = pd.read_csv(DF)
df = df.dropna()
X = df[['pend_prom', 'rug_mean', 'var_cota']]
y = df['IRI_oficial']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)


print('R2 en test:', model.score(X_test, y_test))


with open(MOUT, 'wb') as f:
pickle.dump(model, f)


print('Modelo guardado en', MOUT)