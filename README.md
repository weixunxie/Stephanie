# Pets Data Management and Analysis

## Overview

This project is a Python program to manage and analyze pet data. It covers various topics including decision making, loops, functions, modules, and data visualization using libraries like Matplotlib, Seaborn, and Plotly.

## Files

- `main.py`: Main script to run the analysis and visualization.
- `pet_analysis.py`: Module containing functions for data loading, cleaning, and analysis.
- `README.md`: This file providing instructions and explanations.

## Instructions

### Setup

1. Make sure you have Python installed on your system.
2. Install the required libraries using pip:
    ```
    pip install pandas matplotlib seaborn plotly
    ```

### Running the Project

1. Place the `pets.csv` file in the same directory as the scripts.
2. Run the main script:
    ```
    python main.py
    ```

### Functions

- **load_data(file_path)**: Loads the CSV file into a pandas DataFrame.
- **clean_data(df)**: Cleans the DataFrame by handling missing values and ensuring appropriate data types.
- **calculate_average_price(df, species)**: Returns the average price of pets in a given species.
- **find_pets_with_feature(df, feature)**: Returns a list of names of pets with a specified special feature.
- **get_species_statistics(df)**: Returns a dictionary with species names as keys and their respective average prices and average ages as values.
- **plot_price_distribution(df)**: Plots the distribution of prices using a histogram and saves the plot as `price_distribution.png`.
- **plot_average_price_by_species(df)**: Plots the average price by species using a bar chart and saves the plot as `average_price_by_species.png`.
- **plot_price_vs_age(df)**: Plots a scatter plot of price vs. age using Seaborn and saves the plot as `price_vs_age.png`.
- **plot_age_distribution_by_species(df)**: Plots the distribution of ages for each species using a box plot with Plotly and saves the plot as `age_distribution_by_species.png`.
