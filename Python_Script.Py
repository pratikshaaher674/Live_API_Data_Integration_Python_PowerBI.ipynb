
import numpy as np
import pandas as pd
import requests
import time


# ------------------------------ World Bank countries endpoint------------------------------

url = "https://api.worldbank.org/v2/country?format=json&per_page=300"
response = requests.get(url)
data=response.json()
countries = data[1]
countries = pd.DataFrame(countries)
countries['region'] = countries['region'].apply(lambda x: x['value'])
countries['incomeLevel'] = countries['incomeLevel'].apply(lambda x: x['value'])
countries['lendingType'] = countries['lendingType'].apply(lambda x: x['value'])

countries.drop(columns=['adminregion'], inplace=True)
countries.rename(columns={'iso2Code':'country_id'}, inplace=True)

#------------------------------Getting List of API------------------------------ # not mentioning over here as we have to already decide the API before writing python code in Power BI.

#------------------------------ Getting data for the indicators------------------------------
indicator_groups = {
    "economic_activity_growth": [
        "NY.GDP.MKTP.KD.ZG",    # GDP growth (annual %)
        "NY.GDP.PCAP.CD"        # GDP per capita (current US$)
    ],
    "labour_market_indicators": [
        "SL.UEM.TOTL.ZS",       # Unemployment total
        "SL.UEM.1524.ZS",       # Unemployment youth total (ages 15-24)
        "SL.TLF.TOTL.IN"        # Labour force, total
    ],
    "trade_globalization": [
        "NE.EXP.GNFS.CD",       # Exports of goods and services (current US$)
        "NE.IMP.GNFS.CD"        # Imports of goods and services (current US$)
    ],
    "poverty_inequality": [
        "SI.POV.NAHC",          # Poverty headcount ratio at national poverty lines (% of population)
        "SI.POV.GINI"           # Gini index (measure of income inequality)
    ],
    "environmental_indicators": [
        "EG.FEC.RNEW.ZS",       # Renewable energy consumption (% of total final energy consumption)
        "AG.LND.FRST.ZS"        # Forest area (% of land area)
    ],
    "health_indicators": [
        "SP.DYN.LE00.IN",       # Life expectancy at birth
        "SP.DYN.IMRT.IN",       # Infant mortality rate
        "SH.H2O.BASW.ZS",       # Access to at least basic water services (% of population)
        "SH.XPD.CHEX.GD.ZS",    # Current health expenditure (% of GDP)
        "SH.IMM.IDPT",          # Immunization, DPT (% of children ages 12-23 months)
        "SH.IMM.MEAS",          # Immunization, measles (% of children ages 12-23 months)
        "SH.MMR.RISK.ZS",       # Risk of maternal death
        "SH.DTH.COMM.ZS",       # Deaths from communicable diseases (% of total)
        "SH.TBS.INCD",          # Tuberculosis incidence (per 100,000 people)
        "SH.STA.BRTC.ZS",       # Births attended by skilled health staff (%)
        "SH.STA.MMRT",          # Maternal mortality ratio (modeled estimate, per 100,000 live births)
        "SP.POP.65UP.TO.ZS",    # Population ages 65 and above (% of total population)
        "SH.HIV.INCD.ZS"        # HIV incidence rate (per 1,000 uninfected population ages 15-49)
    ],
    "technology_indicators": [
        "IT.NET.USER.ZS",       # Individuals using the Internet (% of population)
        "IT.CEL.SETS.P2"        # Mobile cellular subscriptions (per 100 people)
    ]
}


base_url = "https://api.worldbank.org/v2/country/all/indicator/{}?format=json&per_page=1000&page={}"

category_dataframes = {}

for category, indicators in indicator_groups.items():
    print(f"\nFetching data for category: {category}")

    all_dfs_for_category = []  # to hold DataFrames of all indicators in this category

    for indicator_code in indicators:
        print(f"  Fetching indicator: {indicator_code}")
        page = 1

        while True:
            # Prepare URL with indicator and page number
            url = base_url.format(indicator_code, page)  # modifying the above url with the page number and code

            # Request data
            response = requests.get(url)
            if response.status_code != 200:
                print(f"   Failed at page {page} with status code {response.status_code}")
                break

            data = response.json()
            if len(data) < 2:
                print(f"   No data for indicator {indicator_code} on page {page}")
                break

            total_pages = data[0]['pages']  # extracting total pages
            records = data[1]

            # Normalize JSON to flat table
            df = pd.json_normalize(records)

            # Select and rename useful columns
            df = df[
                [
                    'country.id',
                    'country.value',
                    'indicator.id',
                    'indicator.value',
                    'date',
                    'value'
                ]
            ].rename(columns={
                'country.id': 'country_id',
                'country.value': 'country_name',
                'indicator.id': 'indicator_id',
                'indicator.value': 'indicator_name',
                'date': 'year'
            })

            # Filter for years > 2015
            df = df[df['year'].astype(int) > 2015]

            # Append current page data
            all_dfs_for_category.append(df)

            # Check if last page
            if page >= total_pages:  #running loop till the last page.
                break
            else:
                page += 1
                time.sleep(0.2)  # polite pause

    # Concatenate all dataframes for this category if any data fetched
    if all_dfs_for_category:
        combined_df = pd.concat(all_dfs_for_category, ignore_index=True)
        category_dataframes[category] = combined_df
        print(f"   Total rows collected for {category}: {len(combined_df)}")
    else:
        print(f"   No data collected for {category}")

print("\n Data fetching complete for all categories.")


#------------------------------ Getting different dataframe from each set of indicators ------------------------------

economic_activity = category_dataframes.get("economic_activity_growth", pd.DataFrame())
labor_market_jobs = category_dataframes.get("labour_market_indicators", pd.DataFrame())
trade_globalization = category_dataframes.get("trade_globalization", pd.DataFrame())
poverty_inequality = category_dataframes.get("poverty_inequality", pd.DataFrame())
environmental_indicators = category_dataframes.get("environmental_indicators", pd.DataFrame())
health_indicators = category_dataframes.get("health_indicators", pd.DataFrame())
technology_indicators = category_dataframes.get("technology_indicators", pd.DataFrame())


#------------------------------ Merge example for each category - adjust 'countries' DataFrame accordingly ------------------------------

economic = pd.merge(economic_activity, countries, on='country_id', how='inner')
labour_market = pd.merge(labor_market_jobs, countries, on='country_id', how='inner')
trade = pd.merge(trade_globalization, countries, on='country_id', how='inner')
poverty = pd.merge(poverty_inequality, countries, on='country_id', how='inner')
environment = pd.merge(environmental_indicators, countries, on='country_id', how='inner')
health = pd.merge(health_indicators, countries, on='country_id', how='inner')
technology = pd.merge(technology_indicators, countries, on='country_id', how='inner')


#------------------------------ Dropping un-necessary columns ------------------------------

economic.drop(columns=["indicator_id","name","capitalCity","id"], inplace=True)
labour_market.drop(columns=["indicator_id","name","capitalCity","id"], inplace=True)
trade.drop(columns=["indicator_id","name","capitalCity","id"], inplace=True)
poverty.drop(columns=["indicator_id","name","capitalCity","id"], inplace=True)
environment.drop(columns=["indicator_id","name","capitalCity","id"], inplace=True)
health.drop(columns=["indicator_id","name","capitalCity","id"], inplace=True)
technology.drop(columns=["indicator_id","name","capitalCity","id"], inplace=True)

