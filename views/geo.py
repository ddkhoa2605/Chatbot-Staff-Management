import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import plotly.express as px
import matplotlib.pyplot as plt

def app():
    # Load the data
    data_path = 'data\\world_population.csv'
    population_data = pd.read_csv(data_path)

    # Sidebar - Year and Prediction Selection
    st.sidebar.title("Population Visualization and Prediction")
    map_year = st.sidebar.selectbox("Select Year for Map", ['2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970'])
    prediction_year = st.sidebar.slider("Select Future Year for Prediction", 2025, 2050, step=5)

    # Filter data for map visualization and rename longitude column
    map_data = population_data[['Country/Territory', 'lat', 'long', map_year]].dropna()
    map_data = map_data.rename(columns={map_year: 'Population', 'long': 'lon'})

    # Display Map
    st.title(f"World Population in {map_year}")
    st.map(map_data[['lat', 'lon']], zoom=1, use_container_width=True)

    # Train Random Forest Model for Population Prediction
    years = ['1970', '1980', '1990', '2000', '2010', '2015', '2020', '2022']
    population_data = population_data.dropna(subset=years + ['Growth Rate'])

    # Prepare features and target
    X = population_data[years]
    y = population_data['2022'] * (1 + population_data['Growth Rate']) ** (prediction_year - 2022)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model training
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Prediction and evaluation
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    st.write(f"Mean Squared Error on Test Set: {mse:.2f}")

    # Predict future population
    future_population = model.predict(X)
    population_data[f"Predicted_{prediction_year}"] = future_population

    # Merge predictions with map data
    map_data_pred = map_data.merge(population_data[['Country/Territory', f'Predicted_{prediction_year}']],
                                   on='Country/Territory', how='left')

    # Map with predictions
    st.subheader(f"Predicted Population for {prediction_year}")
    st.map(map_data_pred[['lat', 'lon']], zoom=1, use_container_width=True)

    # Display prediction results
    st.write(f"Population Predictions for {prediction_year}")
    st.write(map_data_pred[['Country/Territory', 'Population', f'Predicted_{prediction_year}']])

    # Optional: Scatter plot for model performance
    plt.figure(figsize=(10, 5))
    plt.scatter(y_test, y_pred, alpha=0.7)
    plt.xlabel("Actual Population")
    plt.ylabel("Predicted Population")
    plt.title(f"Random Forest Model Predictions vs Actuals for {prediction_year}")
    st.pyplot(plt)

# Run the app function
if __name__ == "__main__":
    app()
