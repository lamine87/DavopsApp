import pandas as pd
import pickle
from sklearn.metrics import accuracy_score

# Charger le modèle
with open('cancer_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Charger ou préparer les données de test
url = "https://raw.githubusercontent.com/AbdallahTayeb/DevOps-Course/main/sample.csv"
test_data = pd.read_csv(url)

# Assumer que les colonnes sont les mêmes que dans les données d'entraînement
X_test = test_data[model]

# Faire des prédictions
y_pred = model.predict(X_test)

# Calculer la précision
accuracy = accuracy_score(test_data['target'], y_pred)
print(f"Accuracy on test data: {accuracy}")

# Définir un seuil de classification (vous pouvez le personnaliser selon vos besoins)
threshold = 0.5

# Vérifier si le seuil est atteint
predictions_above_threshold = (model.predict_proba(X_test)[:, 1] > threshold).astype(int)
print(f"Predictions above threshold: {predictions_above_threshold}")
