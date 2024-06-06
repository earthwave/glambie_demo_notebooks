import matplotlib.pyplot as plt
import pandas as pd

from helpers import transform_string

def single_region_derivative_plot(region_dataframe, region_name):
    
    plt.subplots(1, 1, figsize=(12,8)) # change to end dates - 0.5 years

    plt.plot(region_dataframe.end_dates, region_dataframe.consensus_mwe, linewidth=3, zorder=2, label='Combined change')
    plt.fill_between(region_dataframe.end_dates, region_dataframe.consensus_mwe - region_dataframe.consensus_mwe_errors,
                     region_dataframe.consensus_mwe + region_dataframe.consensus_mwe_errors, alpha=0.2)
    plt.hlines(0, region_dataframe.end_dates.values[0], region_dataframe.end_dates.values[-1], linestyle='dashed', color='purple')
    plt.xlabel('Year')
    plt.ylabel('Elevation Change (meters water equivalent)')
    plt.title(transform_string(region_name) + ' - change in elevation between 2000 and 2024')

    plt.legend(loc='lower left')
    

def single_region_cumulative_plot(cumulative_data, cumulative_errors, region_name, unit,
                                  alimetry_data: pd.DataFrame = None, gravimetry_data: pd.DataFrame = None,
                                  demdiff_and_glaciological_data: pd.DataFrame = None):
    
    plt.subplots(1, 1, figsize=(12,8))

    plt.plot(cumulative_data.dates, cumulative_data.changes, linewidth=3, zorder=2, label='Combined change')
    plt.fill_between(cumulative_data.dates, cumulative_data.changes - cumulative_errors.errors, cumulative_data.changes + cumulative_errors.errors, alpha=0.2)
    if alimetry_data is not None:
        plt.plot(alimetry_data.dates, alimetry_data.changes, linestyle='dashed', zorder=1, alpha=0.7, label='Altimetry')
    if gravimetry_data is not None:
        plt.plot(gravimetry_data.dates, gravimetry_data.changes, linestyle='dashed', zorder=1, alpha=0.7, label='Gravimetry')
    if demdiff_and_glaciological_data is not None:
        plt.plot(demdiff_and_glaciological_data.dates, demdiff_and_glaciological_data.changes, linestyle='dashed', zorder=1, alpha=0.7, label='DemDiff and Glaciological')
    plt.xlabel('Year')
    plt.ylabel('Cumulative Change [{}]'.format(unit))
    plt.title(transform_string(region_name) + ' - {} of ice loss between 2000 and 2024'.format(unit))

    plt.legend(loc='lower left')