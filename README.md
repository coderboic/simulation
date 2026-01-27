# Data Generation Using Modeling and Simulation for Machine Learning (GEKKO)

## Overview
This project demonstrates **simulation-based data generation** for machine learning using the **GEKKO** Python library. A nonlinear system is modeled and simulated to generate a synthetic dataset, which is then used to train and evaluate machine learning models.

## Methodology
- Define a nonlinear mathematical model  
- Specify parameter bounds  
- Run 1000 simulation experiments  
- Generate a dataset from simulation outputs  
- Train and compare ML regression models  

## Mathematical Model
y = a * x^2 + b * sin(x)


**Target Variable:** `y`

## Parameter Bounds

| Parameter | Range     |
|----------|-----------|
| a        | 0.1 – 2.0 |
| b        | 0.1 – 3.0 |
| x        | 0 – 10    |

## Tools Used
- Python  
- GEKKO  
- NumPy  
- Pandas  
- Scikit-learn  
- Matplotlib  

## Results

| Model          | MSE | R²  |
|---------------|-----|-----|
| Random Forest | 0.22| 0.98|

**Random Forest Regressor** achieved the best performance.

## Installation
```bash
pip install -r requirements.txt
