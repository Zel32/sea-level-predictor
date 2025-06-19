import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    df.plot.scatter(x='Year',y='CSIRO Adjusted Sea Level')
    

    # Create first line of best fit
    x1 = df['Year']
    y1 = df['CSIRO Adjusted Sea Level']    
    slope, intercept, r_value, p_value, std_err = linregress(x1, y1)
    
    additional_year = pd.Series(list(range(2014, 2051)))
    x1_for_pred = pd.concat([x1,additional_year], ignore_index=True)
    y_pred = [slope * xi + intercept for xi in x1_for_pred]
    
    plt.plot(x1_for_pred, y_pred, color='green', label='predicted sea level rise')
    
    # Create second line of best fit
    df_2 = df[(df['Year']>=2000)]
    x2 = df_2['Year']
    y2 = df_2['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(x2, y2)
    
    x2_for_pred = pd.concat([x2,additional_year], ignore_index=True)
    x2_for_pred
    y_pred2 = [slope * xi + intercept for xi in x2_for_pred]
    
    plt.plot(x2_for_pred, y_pred2, color='red', label='predicted sea level rise (using data from year >= 2000)')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title("Rise in Sea Level")

    # Add labels and title
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()