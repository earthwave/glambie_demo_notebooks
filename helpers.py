import numpy as np
import pandas as pd
import ipywidgets as widgets


def glambie_regions_dropdown(first_region_choice: str = None):
  regions = {'Alaska': '1_alaska', 'Western Canada & US': '2_western_canada_us', 'Arctic Canada North': '3_arctic_canada_north', 'Arctic Canada South': '4_arctic_canada_south',
             'Greenland Periphery': '5_greenland_periphery', 'Iceland': '6_iceland', 'Svalbard': '7_svalbard', 'Scandinavia': '8_scandinavia', 'Russian Arctic': '9_russian_arctic',
             'North Asia': '10_north_asia', 'Central Europe': '11_central_europe', 'Caucasus & Middle East': '12_caucasus_middle_east', 'Central Asia': '13_central_asia',
             'South Asia West': '14_south_asia_west', 'South Asia East': '15_south_asia_east', 'Low Latitudes': '16_low_latitudes', 'Southern Andes': '17_southern_andes',
             'New Zealand': '18_new_zealand', 'Antarctic and Subantarctic Islands': '19_antarctic_and_subantarctic'}
  if first_region_choice is not None:
    regions = {key:val for key, val in regions.items() if val != first_region_choice}
  a = widgets.Dropdown(
    options=regions,
    description='Region:'
)
  return a


def derivative_to_cumulative(start_dates, end_dates, changes, calculate_as_errors: bool = False):

    contains_no_gaps = [start_date == end_date for start_date, end_date in zip(start_dates[1:], end_dates[:-1])]
    # add an extra row to dataset for each gap, so that it's represented in the cumulative timeseries as no data
    if calculate_as_errors:
        changes = [0, *np.array(pd.Series(np.square(changes)).cumsum())**0.5]
    else:
        changes = [0, *np.array(pd.Series(changes).cumsum())]

    if not all(contains_no_gaps):
        indices_of_gaps = [i for i, x in enumerate(contains_no_gaps) if not (x)]
        start_dates = list(start_dates.copy())
        end_dates = list(end_dates.copy())
        for idx in indices_of_gaps:
            start_date_to_insert = end_dates[idx]
            end_date_to_insert = start_dates[idx + 1]
            # add no data row
            start_dates.insert(idx + 1, start_date_to_insert)
            end_dates.insert(idx + 1, end_date_to_insert)
            changes.insert(idx + 2, None)  # already in cumulative, hence +2
            # add last row before gap again after gap
            start_dates.insert(idx + 2, start_dates[idx + 1])
            end_dates.insert(idx + 2, end_dates[idx + 1])
            changes.insert(idx + 3, changes[idx + 1])  # already in cumulative, hence +3
    dates = [start_dates[0], *end_dates]

    if calculate_as_errors:
        return pd.DataFrame({'dates': dates, 'errors': changes})
    else:
        return pd.DataFrame({'dates': dates, 'changes': changes})
    

def transform_string(input_string):
    transformed_string = input_string.replace('_', ' ')
    capitalized_string = transformed_string.title()
    region_list = capitalized_string.split(' ')[1:]
    combined_string = " ".join(region_list)
    return combined_string