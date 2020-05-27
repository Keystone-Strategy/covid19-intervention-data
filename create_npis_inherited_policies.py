"""
Create complete_npis_inherited_policies.csv from the raw file.

If county start_date is null or later than its state's start_date,
all relevant fields (start_date, end_date, citation, and note)
are inherited from the state; i.e., the county is assigned the state's
value for those fields, regardless of whether it has values already.

The script also makes all dates the ISO 8601 standard of YYYY-MM-DD.

It reads complete_npis_raw_policies.csv from and writes 
complete_npis_inherited_policies.csv to the current directory.
"""

import pandas as pd
import numpy as np

### Load data

raw = pd.read_csv('complete_npis_raw_policies.csv')

### Preprocess

# Set blanks to NaN for consistency.
raw.start_date = pd.to_datetime(raw.start_date, errors='coerce')
raw.end_date = pd.to_datetime(raw.end_date, errors='coerce')

# Define columns to merge on and for counties to inherit from states.
MERGE_COLS = ['state', 'npi']
INHERIT_COLS = ['start_date', 'end_date', 'citation', 'note']

# Separate state and county data frames.
state = raw[raw.county.isna()]
county = raw[~raw.county.isna()]

# Create state and county files with renamed inheritance columns
# to identify source of features.
state2 = state[MERGE_COLS + INHERIT_COLS].rename(
    columns=lambda x: x +'_state' if x in INHERIT_COLS else x)

county2 = county.rename(
    columns=lambda x: x +'_county' if x in INHERIT_COLS else x)

# Merge county and state files.
# Use a left join as some counties have state-NPI combinations that
# don't exist in the state data. Currently only New Jersey - Other.
county_merged = county2.merge(state2, on=MERGE_COLS, how='left')

# Identify rows where state data should be used.
# (Counties with a null county start_date or later than state's.
county_merged['use_state'] = (
    pd.isna(county_merged.start_date_county) |
    (county_merged.start_date_county > county_merged.start_date_state))

# Assign values for each inherited column.
for col in INHERIT_COLS:
    county_merged[col] = np.where(county_merged.use_state, 
                                  county_merged[col + '_state'], 
                                  county_merged[col + '_county'])

# Stack back with state file and export.
res = state.append(county_merged)[raw.columns]

# Ensure no rows got dropped.
assert res.shape[0] == raw.shape[0]

# Export.
res.to_csv('complete_npis_inherited_policies.csv', index=False)
