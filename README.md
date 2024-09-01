[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Yi0Zbe2y)
# MAST30034 Project 1 README.md
- Name: Jeremy Lau
- Student ID: 1356056

# Predicting Taxi Fare Prices in NYC: An Analysis of Temporal and Spatial Influences

## Model Pipeline
1. Run the `download.py` script: This retieves the relevant data through api
2. Run `taxi_violations_join.ipynb`: This creates the mapping key from taxi zones to police precincts
3. Run `yellow_taxi.py` and `violations_cleaning.py`: This preprocesses each of the datasets and makes plots for basic analysis
4. Run `modelling.ipynb`: This combines the datasets and produces a machine learning model
