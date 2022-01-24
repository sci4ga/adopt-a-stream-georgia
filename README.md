# Adopt-a-Stream Georgia data science projects

Local water quality impacts health, well-being, and the local economy in many ways. Data about water quality in Georgia has been collected for many years by [Adopt-a-Stream](https://adoptastream.georgia.gov/) (AaS), and is made publicly available through their [web portal](http://aas.gaepd.org). This is a great beginning to promoting public access and involvement in monitoring the impact of poor quality water on communities, and in finding causal connections between water quality outcomes and economic or political decisions about land use, industrial regulation, etc.

The water quality dataset hosted by AaS-GA was created through the volunteer efforts of many citizen scientists throughout the state over many years.

# Data sets

We currently have two datasets from AaS-GA. One is a direct database export sent by them in December, 2021 in XLS format. The other is scraped from their web portal in September, 2021, and contains significant differences from the direct export that are not yet well understood. The two raw datasets are recorded here.

# Project maturity

As of Jan 2022, we are in the earliest stages of gathering and preparing a dataset for further research.

The current project goals are the basic validation and preparation of the available data.

# Other resources used

[This API](https://geo.fcc.gov/api/census/block/find?latitude={}&longitude={}&format=json) provides an on-demand lookup for local information based on FIPS identifiers. `utils.py` provides code to use this, but this data is already pulled for all the recorded data points and cached in the repo.

Plotly's own record of [basic US demographics](https://raw.githubusercontent.com/plotly/datasets/master/minoritymajority.csv') that we use at the state level for GIS county information from `utils.get_state_map`, but it could be useful for scientific exploration at a later date.
