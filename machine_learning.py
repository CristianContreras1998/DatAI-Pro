import category_encoders as ce
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb
import lightgbm as lgb
from catboost import CatBoostRegressor


def preparar_datos_para_modelos(df):
    """
    Prepara los datos para los modelos de machine learning, aplicando encoding, normalización y división en entrenamiento y prueba.
    
    Parámetros:
    - df: DataFrame - Conjunto de datos que contiene todas las características y la variable objetivo 'Price'.
    
    Retorna:
    - X_train, X_test, y_train, y_test: Conjuntos de entrenamiento y prueba preparados.
    """
    X = df.drop(['Price', 'Postcode'], axis=1)
    y = df['Price']

    # Aplicar Target Encoding a la variable 'County'
    target_encoder = ce.TargetEncoder(cols=['County'])
    X['County'] = target_encoder.fit_transform(X['County'], y)

    # Normalizar las variables numéricas
    numerical_features = ['Month', 'Year', 'Property Age', 'County_Frequency', 'County']
    scaler = StandardScaler()
    X[numerical_features] = scaler.fit_transform(X[numerical_features])

    # Crear dummies para las variables categóricas
    categorical_features = ['Property Type', 'Old/New', 'Duration', 'PPD Category Type']
    X = pd.get_dummies(X, columns=categorical_features, drop_first=True)

    # Dividir los datos en conjuntos de entrenamiento y prueba (80% - 20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test


def entrenar_regresion_lineal(X_train, X_test, y_train, y_test):
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    y_pred = lr_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2


def entrenar_random_forest(X_train, X_test, y_train, y_test):
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    y_pred = rf_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2


def entrenar_xgboost(X_train, X_test, y_train, y_test):
    xgb_model = xgb.XGBRegressor(objective="reg:squarederror", random_state=42)
    xgb_model.fit(X_train, y_train)
    y_pred = xgb_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2


def entrenar_lightgbm(X_train, X_test, y_train, y_test):
    lgb_model = lgb.LGBMRegressor(random_state=42)
    lgb_model.fit(X_train, y_train)
    y_pred = lgb_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2


def entrenar_catboost(X_train, X_test, y_train, y_test):
    cat_model = CatBoostRegressor(silent=True, random_state=42)
    cat_model.fit(X_train, y_train)
    y_pred = cat_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2