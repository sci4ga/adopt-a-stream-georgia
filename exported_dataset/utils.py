"""Common utils library
"""

import pandas as pd
import numpy as np
import json
import time
import geopandas as gpd


def load_csv_export_dataset(filepath: str) -> pd.DataFrame:
    """Load AaS exported dataset
    Expect dtype warnings.
    """
    df = pd.read_csv(filepath, parse_dates=True, infer_datetime_format=True)
    # correct type on date field that doesn't parse properly from read_csv
    return df.assign(event_date=pd.to_datetime(df["event_date"]))

def get_loc_objects_from_series(loc_series: pd.Series) -> tuple:
    """The series should be SiteLocation.
    """
    loc_pairs = np.array(loc_series.apply(lambda s: [float(x) for x in s.split()]).values.tolist())
    # many pairs are repeated, which is redundant
    loc_pairs = np.unique(loc_pairs, axis=0)
    geo_locs = gpd.points_from_xy(loc_pairs.T[0], loc_pairs.T[1])
    # geo dataframe of geometries associated with no actual data (hence [])
    gdf = gpd.GeoDataFrame([], geometry=geo_locs)
    return loc_pairs, geo_locs, gdf

def fetch_geo_locs(geo_locs=None) -> list:
    """This is a very time-consuming scrape if you delete the file already provided.
    To recompute, you must pass the geo_locs parameter.
    """
    try:
        with open("geodata/GIS_loc.json", "r") as f:
            return json.load(f)
    except:
        results = []
        # grace period to avoid rate limiting
        wait = 0.5 # s
        for i in tqdm(range(len(geo_locs))):
            url = "https://geo.fcc.gov/api/census/block/find?latitude={}&longitude={}&format=json".format(gdf.geometry.x[i], gdf.geometry.y[i])
            # have to fake the user agent to allow lookup from within jupyter.
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            results.append(json.loads(urlopen(req).read().decode('utf-8')))
            time.sleep(wait)
        # store the results for reuse
        with open("geodata/GIS_loc.json", "w") as f:
            json.dump(results, f)
        return results
    
def get_state_map(state_name: str = 'Georgia') -> pd.DataFrame:
    """Fetch state map geometry from plotly's free online resources, except with the county name field
    altered from the default 'CTYNAME' to 'County' and the content simplified to remove the trailing word 'County'.
    
    State name must be capitalized, e.g. 'Georgia'
    """
    df_map = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/minoritymajority.csv')
    df_map = df_map[df_map['STNAME']==state_name]
    county_order = df_map['CTYNAME'].to_list()
    # remove trailing word ' County'
    counties_norm = [" ".join(c.split()[:-1]) for c in county_order]
    df_map.insert(2, 'County', counties_norm)
    return df_map.drop('CTYNAME', axis=1)


field_groups = {"core": """event_date
volunteer_time
createdby
createddate
data_entry
participants""".split('\n'),
                "basic": """rain_24_hours
weather
rain_hours
rain_inches
distance
air_temperature
stream
method
wqi
habitat
chem_detail_rid
air_temp
water_temp
min_temp
max_temp
calibrate
calibrate_comment
chemical_comment
ChemWarnings""".split('\n'),
                "chem": """do_saturation
reagent
reagent_other
ph1
ph2
DissolvedOxygen1
DissolvedOxygen2
Conductivity
Salinity1
Salinity2
SecchiDisk1
SecchiDisk2
ChlorophyllA
Alkalinity
AmmoniaN
NitrateN
Orthophosphate
SamplingDepth
SettleableSolids
Turbidity
Chloride
Hardness""".split('\n'),
                "bact": """bact_detail_rid
plate_blank
plate_one
plate_two
plate_three
plate_four
plate_five
colony_avg
hold_start_datetime
hold_end_datetime
three_M_plate
ecoli_idexx
fecal_coliform
ecoli_other
ecoli_other_unit""".split('\n'),
                "other": """Other1
Other2
Other3
Other4
Other5
Other6
Other7
Other1_Comm
Other2_Comm
Other3_Comm
Other4_Comm
Other5_Comm
Other6_Comm
Other7_Comm""".split('\n')
               }
