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
    
    return
    

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

    return

def region_comparison_plot(region_name, comparison_region_name, cumulative_data_all_gt, cumulative_errors_all_gt, cumulative_data_all_gt_comparison,
                           cumulative_errors_all_gt_comparison, cumulative_data_all_mwe, cumulative_errors_all_mwe,
                           cumulative_data_all_mwe_comparison, cumulative_errors_all_mwe_comparison):
    
    fig, axs = plt.subplots(1, 2, figsize=(20,8))

    axs[0].plot(cumulative_data_all_gt.dates, cumulative_data_all_gt.changes, linewidth=3, zorder=2, label='Consensus change - ' + transform_string(region_name))
    axs[0].fill_between(cumulative_data_all_gt.dates, cumulative_data_all_gt.changes - cumulative_errors_all_gt.errors,
                        cumulative_data_all_gt.changes + cumulative_errors_all_gt.errors, alpha=0.2)

    axs[0].plot(cumulative_data_all_gt_comparison.dates, cumulative_data_all_gt_comparison.changes, linewidth=3, zorder=2, label='Consensus change - ' + transform_string(comparison_region_name))
    axs[0].fill_between(cumulative_data_all_gt_comparison.dates, cumulative_data_all_gt_comparison.changes - cumulative_errors_all_gt_comparison.errors,
                        cumulative_data_all_gt_comparison.changes + cumulative_errors_all_gt_comparison.errors, alpha=0.2)

    axs[0].set_xlabel('Year')
    axs[0].set_ylabel('Cumulative Change [Gt]')

    axs[1].plot(cumulative_data_all_mwe.dates, cumulative_data_all_mwe.changes, linewidth=3, zorder=2, label='Consensus change - ' + transform_string(region_name))
    axs[1].fill_between(cumulative_data_all_mwe.dates, cumulative_data_all_mwe.changes - cumulative_errors_all_mwe.errors,
                        cumulative_data_all_mwe.changes + cumulative_errors_all_mwe.errors, alpha=0.2)

    axs[1].plot(cumulative_data_all_mwe_comparison.dates, cumulative_data_all_mwe_comparison.changes, linewidth=3, zorder=2, label='Consensus change - ' + transform_string(comparison_region_name))
    axs[1].fill_between(cumulative_data_all_mwe_comparison.dates, cumulative_data_all_mwe_comparison.changes - cumulative_errors_all_mwe_comparison.errors,
                        cumulative_data_all_mwe_comparison.changes + cumulative_errors_all_mwe_comparison.errors, alpha=0.2)

    axs[1].set_xlabel('Year')
    axs[1].set_ylabel('Cumulative Change [meters water equivalent]')

    axs[0].legend(loc = 'lower left', fontsize=16)
    plt.suptitle('Regional comparison - ice loss between 2000 and 2024')

    return