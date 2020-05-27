# covid19-intervention-data
This repository contains Non-Pharmaceutical Interventions (NPIs) at the county level for a selection of counties within the United States. These NPIs are targeted at the novel coronavirus. This data is collected by hand with reference to government health websites and local news media reports. NPIs of different types are listed as columns and the rows indicate when that NPI went into effect for that particular locality. We provide this data free of restrictions, but ask that you attribute the data to Keystone Strategy. We have also produced the underlying data, uncleaned and with citation.

You can read more about this dataset, provided by Keystone Strategy, here: https://www.keystonestrategy.com/coronavirus-covid19-intervention-dataset-model/

# 4-16-2020 Update
On 4-16-2020, we pushed a complete update, including reformatting of the data. The data now includes all US states and territories and all counties with at least 100 confirmed cases as of 4/06/2020, according to JHU, for a total of over 380 localities. 

The data has been reformatted to have each locality's policy on a single row, including a start and end date. Since policies are still in place, no end dates have been recorded yet. This includes places where end dates have been announced, as we anticipate that there is a strong likelihood of those dates being extended.

We have also changed the defined categories to focus more on explicit government orders and less on recommendations. This helps us collect more uniform data across the 300+ localities. We have removed social distancing of a portion of the population, added shelter in place, re-defined social distancing as physical distance(6ft) between people, and added a religious gathering cancellation indicator.

There are two available sheets: a raw sheet of policies and an inherited sheet of policies. The raw sheet includes only policies ordered by that level of government; it would not capture a state policy applying to a county that has not issued its own order, even though the state policy is in effect in the county. The inherited level does capture this, having county policy start_dates tied to the state policy start date if either a) the county did not issue a policy of that type and the state did that applied to that county. or b) the county issued a policy after the state issued a policy applying to that county.

# NPIs Included
The NPIs defined are:

* social_distancing - Social Distancing mandate of at least 6 feet between people
* shelter_in_place - An order indicating that people should shelter in their homes except for essential reasons
* gathering_size_XX_to_YY - Gathering size limitation, with the digits indicating the ceiling of acceptable gatherings. A government order indicating that gatherings above that size are prohibited
* closing_of_public_venues - Closure of Public Venues. A government order closing gathering venues for in-person service, such as restaurants, bars, and theaters
* school_closure - Closure of schools and universities
* non_essential_services_closure - Non-Essential Services Closure, i.e. a government order closing non-essential services and shops
* lockdown – Lock Down (pending)
* religious_gathering_cancellation – Cancelling of religious gatherings, either explicitly or implicitly by applying gathering size / shelter-in-place limitations to religious gatherings as well.




# Covered Counties
We are working on expanding and updating the dataset in the changing circumstances. As of 4-16-2020, the dataset includes over 300 counties, including all counties with at least 100 confirmed cases as of April 6th, and all 50 states. The dataset covers the following FIP codes: 1, 2, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54, 55, 56, 66, 72, 1017, 1073, 1081, 1089, 1097, 1117, 2020, 4005, 4013, 4017, 4019, 4021, 5119, 6001, 6013, 6019, 6029, 6037, 6041, 6059, 6061, 6065, 6067, 6071, 6073, 6075, 6077, 6079, 6081, 6083, 6085, 6097, 6107, 6111, 8001, 8005, 8013, 8031, 8035, 8037, 8041, 8051, 8059, 8069, 8123, 9001, 9003, 9005, 9007, 9009, 9013, 10001, 10003, 10005, 11001, 12001, 12011, 12021, 12031, 12033, 12057, 12069, 12071, 12081, 12086, 12095, 12097, 12099, 12101, 12103, 12105, 12109, 12115, 12117, 12127, 13015, 13045, 13057, 13063, 13067, 13089, 13095, 13097, 13121, 13135, 13139, 13151, 13177, 15003, 16001, 16013, 16027, 17031, 17043, 17089, 17097, 17111, 17163, 17197, 18057, 18063, 18081, 18089, 18095, 18097, 18141, 19103, 19113, 19153, 20091, 20173, 20209, 21067, 21111, 22005, 22015, 22017, 22019, 22033, 22047, 22051, 22055, 22057, 22071, 22073, 22075, 22079, 22087, 22089, 22093, 22095, 22103, 22105, 22109, 23005, 23031, 24003, 24005, 24013, 24017, 24021, 24027, 24031, 24033, 24510, 25001, 25003, 25005, 25009, 25011, 25013, 25015, 25017, 25021, 25023, 25025, 25027, 26049, 26065, 26075, 26081, 26093, 26099, 26115, 26125, 26145, 26147, 26161, 26163, 27053, 27109, 27123, 28033, 28049, 28059, 29095, 29183, 29189, 29510, 30031, 31055, 32003, 32031, 33011, 33015, 34001, 34003, 34005, 34007, 34013, 34015, 34017, 34019, 34021, 34023, 34025, 34027, 34029, 34031, 34035, 34037, 34039, 34041, 35001, 35043, 35045, 36001, 36027, 36029, 36053, 36055, 36059, 36061, 36063, 36065, 36067, 36071, 36079, 36087, 36091, 36093, 36103, 36105, 36109, 36111, 36119, 37063, 37067, 37081, 37119, 37183, 39035, 39049, 39061, 39093, 39095, 39099, 39113, 39133, 39151, 39153, 39155, 40027, 40109, 40143, 41005, 41047, 41051, 41067, 42003, 42007, 42011, 42017, 42019, 42029, 42043, 42045, 42069, 42071, 42075, 42077, 42079, 42089, 42091, 42095, 42101, 42103, 42107, 42129, 42133, 44007, 45013, 45019, 45045, 45055, 45063, 45079, 45091, 46099, 47037, 47093, 47149, 47157, 47165, 47187, 47189, 48029, 48039, 48041, 48085, 48113, 48121, 48141, 48157, 48167, 48201, 48215, 48303, 48339, 48439, 48453, 48479, 49011, 49035, 49043, 49049, 50007, 51013, 51041, 51059, 51087, 51095, 51107, 51153, 51760, 51810, 53005, 53011, 53029, 53033, 53035, 53053, 53057, 53061, 53063, 53073, 53077, 55025, 55059, 55079, 55133.
