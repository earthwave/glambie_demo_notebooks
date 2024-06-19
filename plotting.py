import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from helpers import transform_string, create_change_dataframe_for_single_year

def single_region_derivative_plot(region_dataframe, region_name, unit):
    
    plt.subplots(1, 1, figsize=(12,8)) # change to end dates - 0.5 years

    plt.plot(region_dataframe.end_dates, region_dataframe.combined_mwe, linewidth=3, zorder=2, label='Combined change')
    plt.fill_between(region_dataframe.end_dates, region_dataframe.combined_mwe - region_dataframe.combined_mwe_errors,
                     region_dataframe.combined_mwe + region_dataframe.combined_mwe_errors, alpha=0.2)
    plt.hlines(0, region_dataframe.end_dates.values[0], region_dataframe.end_dates.values[-1], linestyle='dashed', color='purple')
    plt.xlabel('Year')
    plt.ylabel('Elevation Change [{}]'.format(unit))
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

    axs[0].plot(cumulative_data_all_gt.dates, cumulative_data_all_gt.changes, linewidth=3, zorder=2, label='Combined change - ' + transform_string(region_name))
    axs[0].fill_between(cumulative_data_all_gt.dates, cumulative_data_all_gt.changes - cumulative_errors_all_gt.errors,
                        cumulative_data_all_gt.changes + cumulative_errors_all_gt.errors, alpha=0.2)

    axs[0].plot(cumulative_data_all_gt_comparison.dates, cumulative_data_all_gt_comparison.changes, linewidth=3, zorder=2, label='Combined change - ' + transform_string(comparison_region_name))
    axs[0].fill_between(cumulative_data_all_gt_comparison.dates, cumulative_data_all_gt_comparison.changes - cumulative_errors_all_gt_comparison.errors,
                        cumulative_data_all_gt_comparison.changes + cumulative_errors_all_gt_comparison.errors, alpha=0.2)

    axs[0].set_xlabel('Year')
    axs[0].set_ylabel('Cumulative Change [Gt]')

    axs[1].plot(cumulative_data_all_mwe.dates, cumulative_data_all_mwe.changes, linewidth=3, zorder=2, label='Combined change - ' + transform_string(region_name))
    axs[1].fill_between(cumulative_data_all_mwe.dates, cumulative_data_all_mwe.changes - cumulative_errors_all_mwe.errors,
                        cumulative_data_all_mwe.changes + cumulative_errors_all_mwe.errors, alpha=0.2)

    axs[1].plot(cumulative_data_all_mwe_comparison.dates, cumulative_data_all_mwe_comparison.changes, linewidth=3, zorder=2, label='Combined change - ' + transform_string(comparison_region_name))
    axs[1].fill_between(cumulative_data_all_mwe_comparison.dates, cumulative_data_all_mwe_comparison.changes - cumulative_errors_all_mwe_comparison.errors,
                        cumulative_data_all_mwe_comparison.changes + cumulative_errors_all_mwe_comparison.errors, alpha=0.2)

    axs[1].set_xlabel('Year')
    axs[1].set_ylabel('Cumulative Change [meters water equivalent]')

    axs[0].legend(loc = 'lower left', fontsize=16)
    plt.suptitle('Regional comparison - ice loss between 2000 and 2024')

    return


def global_cumulative_plot(cumulative_data, cumulative_errors, global_dataframe, unit, colors_list):
    
    _, axs = plt.subplots(1, 1, figsize=(12,8))
    axs_2 = axs.twinx()  
    
    axs.bar(global_dataframe.start_dates, global_dataframe.combined_mwe, yerr=global_dataframe.combined_mwe_errors, capsize=3, color=colors_list[1], ecolor=colors_list[1], alpha=0.3, zorder=1) 
    axs.hlines(0, min(global_dataframe.start_dates), min(global_dataframe.start_dates), linestyle='dashed', color='k')
    axs.set_ylabel('Annual Change [m w.e. yr^-1]')
    axs.set_ylim(-1.0, 0.05)

    axs_2.plot(cumulative_data.dates, cumulative_data.changes, linewidth=3, zorder=2)
    axs_2.fill_between(cumulative_data.dates, cumulative_data.changes - cumulative_errors.errors, cumulative_data.changes + cumulative_errors.errors, alpha=0.2, zorder=2)

    axs_2.set_xlabel('Year')
    axs_2.set_ylabel('Cumulative Change [{}]'.format(unit))
    axs_2.set_title('Giga tonnes of global ice loss between 2000 and 2024')
    axs_2.set_ylim(-7000, 0.05)
    
    axs.grid(False)

    return


def global_comparison_stacked_region_plot(cumulative_data_all_gt, cumulative_errors_all_gt, cumulative_data_first_region_gt, first_region,
                                          cumulative_data_second_region_gt: pd.DataFrame = None, second_region: str = None,
                                          cumulative_data_third_region_gt: pd.DataFrame = None, third_region: str = None):
    
    plt.subplots(1, 1, figsize=(12,8))

    plt.plot(cumulative_data_all_gt.dates, cumulative_data_all_gt.changes, linewidth=3, zorder=2, label='Global change')
    plt.fill_between(cumulative_data_all_gt.dates, cumulative_data_all_gt.changes - cumulative_errors_all_gt.errors, cumulative_data_all_gt.changes + cumulative_errors_all_gt.errors, alpha=0.2)
    
    y = [cumulative_data_first_region_gt.changes,cumulative_data_second_region_gt.changes, cumulative_data_third_region_gt.changes]
    
    plt.stackplot(cumulative_data_all_gt.dates, y, labels=[transform_string(first_region), transform_string(second_region), transform_string(third_region)], alpha=0.4)

    plt.xlabel('Year')
    plt.ylabel('Cumulative Change [Gt]')
    
    plt.legend(loc = 'lower left', fontsize=16)

    plt.title('Global ice loss between 2000 and 2024 - contributions from {}, {} and {}'.format(transform_string(first_region), transform_string(second_region), transform_string(third_region)))


def global_comparison_region_plot(cumulative_data_all_gt, cumulative_errors_all_gt, cumulative_data_first_region_gt, cumulative_errors_first_region_gt, first_region,
                                  cumulative_data_second_region_gt: pd.DataFrame = None, cumulative_errors_second_region_gt: pd.DataFrame = None, second_region: str = None,
                                  cumulative_data_third_region_gt: pd.DataFrame = None, cumulative_errors_third_region_gt: pd.DataFrame = None, third_region: str = None, shaded: bool = False):
    
    plt.subplots(1, 1, figsize=(12,8))

    plt.plot(cumulative_data_all_gt.dates, cumulative_data_all_gt.changes, linewidth=3, zorder=2, label='Global change')
    plt.fill_between(cumulative_data_all_gt.dates, cumulative_data_all_gt.changes - cumulative_errors_all_gt.errors, cumulative_data_all_gt.changes + cumulative_errors_all_gt.errors, alpha=0.2)
    
    plt.plot(cumulative_data_first_region_gt.dates, cumulative_data_first_region_gt.changes, linestyle='dotted', linewidth=3, zorder=2, alpha=0.7, label='{}'.format(transform_string(first_region)))
    if shaded:
        plt.fill_between(cumulative_data_first_region_gt.dates, cumulative_data_first_region_gt.changes, alpha=0.2)
    else:
        plt.fill_between(cumulative_data_first_region_gt.dates, cumulative_data_first_region_gt.changes - cumulative_errors_first_region_gt.errors, cumulative_data_first_region_gt.changes + cumulative_errors_first_region_gt.errors, alpha=0.2)
    
    if cumulative_data_second_region_gt is not None:
        plt.plot(cumulative_data_second_region_gt.dates, cumulative_data_second_region_gt.changes, linestyle='dotted', linewidth=3, zorder=2, alpha=0.7, label='{}'.format(transform_string(second_region)))
        plt.fill_between(cumulative_data_second_region_gt.dates, cumulative_data_second_region_gt.changes - cumulative_errors_second_region_gt.errors, cumulative_data_second_region_gt.changes + cumulative_errors_second_region_gt.errors, alpha=0.2)
    
    if cumulative_data_third_region_gt is not None:
        plt.plot(cumulative_data_third_region_gt.dates, cumulative_data_third_region_gt.changes, linestyle='dotted', linewidth=3, zorder=2, alpha=0.7, label='{}'.format(transform_string(third_region)))
        plt.fill_between(cumulative_data_third_region_gt.dates, cumulative_data_third_region_gt.changes - cumulative_errors_third_region_gt.errors, cumulative_data_third_region_gt.changes + cumulative_errors_third_region_gt.errors, alpha=0.2)

    plt.xlabel('Year')
    plt.ylabel('Cumulative Change [Gt]')
    
    plt.legend(loc = 'lower left', fontsize=16)
    if second_region is not None:
        plt.title('Global ice loss between 2000 and 2024 - contributions from {}, {} and {}'.format(transform_string(first_region), transform_string(second_region), transform_string(third_region)))
    else:
        plt.title('Global ice loss between 2000 and 2024 - contribution from {}'.format(transform_string(first_region)))
    plt.legend(loc='lower left')
    
    return


def histogram_of_region_contributions_to_global_loss(glambie_dataframe_dict, global_dict, chosen_year, colors_list):

    chosen_year_all_regions_df, total_change = create_change_dataframe_for_single_year(glambie_dataframe_dict, global_dict, chosen_year)
    
    index = np.arange(19)
    # Show proportion of total change that comes from each region
    fig, axs = plt.subplots(1, 1, figsize=(10, 10))
    axs.barh(index, (chosen_year_all_regions_df.change / total_change)*100, tick_label=chosen_year_all_regions_df.region, color=colors_list)

    axs.set_xlabel('Percentage of Global Cumulative Change 2000 - {} [%]'.format(chosen_year))
    plt.suptitle('Global Cumulative Change 2000 - {} = {} Gt'.format(chosen_year, round(total_change, 2)))
    plt.tight_layout()


def histogram_of_region_contributions_to_global_loss_two_years(glambie_dataframe_dict, global_dict, chosen_year, comparison_year):
    
    chosen_year_all_regions_df, total_change = create_change_dataframe_for_single_year(glambie_dataframe_dict, global_dict, chosen_year)
    comparison_year_all_regions_df, total_change_comparison = create_change_dataframe_for_single_year(glambie_dataframe_dict, global_dict, comparison_year)
    bar_width = 0.35
    
    index = np.arange(19)
    fig, axs = plt.subplots(1, 1, figsize=(10, 10))
    axs.barh(index, (chosen_year_all_regions_df.change / total_change)*100, bar_width, tick_label=chosen_year_all_regions_df.region, label='Change from 2000 - {}'.format(str(chosen_year)))
    axs.barh(index+bar_width, (comparison_year_all_regions_df.change / total_change_comparison)*100, bar_width, label='Change from 2000 - {}'.format(str(comparison_year)))

    axs.set_xlabel('Percentage of Global Cumulative Change [%]')
    
    plt.legend(loc='upper right', fontsize=16)