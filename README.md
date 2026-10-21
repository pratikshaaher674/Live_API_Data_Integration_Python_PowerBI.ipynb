# World Indicators Analysis | Python API Integration & Power BI Dashboard

**Python | REST API | Pandas | NumPy | Power BI | World Bank Open Data**

## Project Overview

The **World Indicators Analysis** project integrates development indicators from the World Bank API using Python and presents the processed data through an interactive Power BI dashboard.

The project explores economic performance, international trade, labour markets, poverty, environmental sustainability, healthcare, and technology adoption across countries and regions.

Python is used to retrieve paginated API responses, transform nested JSON data into structured tables, filter observations by year, and combine indicator records with country metadata. The resulting datasets are prepared as CSV files for analysis and visualization in Power BI.

The dashboard brings multiple development indicators together in a single view, helping users explore trends, compare countries and regions, and investigate relationships between selected indicators.

## Project Objectives

- Integrate World Bank development data through REST API requests.
- Automate data extraction across multiple indicators and API pages.
- Clean, transform, and organize JSON responses using Pandas.
- Combine indicator observations with country-level metadata.
- Prepare separate datasets for seven analytical categories.
- Develop an interactive Power BI dashboard for exploring global development indicators.
- Examine relationships between healthcare expenditure, life expectancy, internet penetration, immunization, and unemployment.

## Technology Stack

| Technology | Application |
|---|---|
| Python | API integration and data processing |
| Requests | HTTP requests to the World Bank API |
| Pandas | JSON normalization, filtering, merging, and transformation |
| NumPy | Numerical computing |
| World Bank API | Source of country and development indicator data |
| Jupyter Notebook | Code development and analysis |
| Power BI | Dashboard creation and interactive visualization |
| CSV | Storage and transfer of processed datasets |

## Data Source

**World Bank Open Data API**

The project uses the World Bank API to retrieve country metadata and development indicator observations.

Country endpoint:

`https://api.worldbank.org/v2/country?format=json&per_page=300`

Indicator endpoint pattern:

`https://api.worldbank.org/v2/country/all/indicator/{indicator_code}?format=json&per_page=1000&page={page}`

The API provides country information and indicator observations for different years. The project filters observations to retain years **after 2015**, meaning 2016 onward, subject to data availability for each indicator.

Source: [World Bank Open Data](https://data.worldbank.org/)

## Data Categories and Indicators

The project organizes the selected indicators into seven categories.

### 1. Economic Activity and Growth

- GDP growth (annual %)
- GDP per capita (current US$)

### 2. Labour Market

- Total unemployment rate
- Youth unemployment rate (ages 15–24)
- Total labour force

### 3. Trade and Globalization

- Exports of goods and services
- Imports of goods and services

### 4. Poverty and Inequality

- Poverty headcount ratio at national poverty lines
- Gini index

### 5. Environmental Indicators

- Renewable energy consumption (% of total final energy consumption)
- Forest area (% of land area)

### 6. Health Indicators

- Life expectancy at birth
- Infant mortality rate
- Access to at least basic drinking water services
- Current health expenditure (% of GDP)
- DPT immunization coverage
- Measles immunization coverage
- Risk of maternal death
- Deaths from communicable diseases
- Tuberculosis incidence
- Births attended by skilled health staff
- Maternal mortality ratio
- Population aged 65 and above
- HIV incidence rate

### 7. Technology Indicators

- Individuals using the internet (% of population)
- Mobile cellular subscriptions per 100 people

## Python Data Processing Workflow

1. **Country data extraction:** Retrieve country metadata, including region, income level, lending type, and country identifiers.
2. **API integration:** Request indicator data using World Bank indicator codes.
3. **Pagination:** Iterate through available API pages to retrieve records for each indicator.
4. **JSON normalization:** Convert nested API responses into tabular DataFrames.
5. **Data filtering:** Retain observations where the year is greater than 2015.
6. **Data transformation:** Rename fields and select relevant columns such as country, indicator, year, and value.
7. **Data integration:** Merge indicator datasets with country metadata using the country identifier.
8. **Column selection:** Remove unnecessary metadata columns from the analytical datasets.
9. **Dataset preparation:** Organize the processed data into seven category-specific DataFrames and corresponding CSV outputs.
10. **Power BI visualization:** Use the prepared datasets to create interactive visualizations and compare development indicators.

## Power BI Dashboard

The **World Indicators Analysis** dashboard uses a dark green theme with contrasting text, KPI cards, charts, tables, a heatmap, and year-based controls.
<img width="1113" height="742" alt="Screenshot 2026-10-21 163210" src="https://github.com/user-attachments/assets/7f0eab5d-1c23-4016-a7b7-5b893d8ee799" />

### Dashboard Components

**KPI Cards**

The dashboard displays summary metrics including:

- Average GDP per Capita
- Average Trade Value
- Average Spending on Health (% of GDP)
- Average GDP Growth (%)
- Forest Area (% of Land Area)

The displayed values depend on the underlying data, aggregation settings, and applied filters.

**Regional Analysis**

A bar chart compares average health spending as a percentage of GDP across World Bank regions.

**Indicator Trends Over Time**

A multi-series line chart explores changes in selected indicators, including forest area, GDP growth, internet usage, mobile subscriptions, renewable energy consumption, and unemployment.

**Internet Penetration and Immunization**

A scatter chart is designed to explore the relationship between internet penetration and child immunization indicators.

**Internet Penetration and Unemployment**

A scatter chart explores the relationship between internet usage and youth unemployment.

**Poverty Comparison Tables**

Two tables highlight countries ranked among the highest and lowest values for the displayed poverty-related measure.

**Indicator Heatmap**

A heatmap provides a visual comparison of relationships or patterns across selected indicator values. Interpretation depends on the specific measures and calculations used to generate the heatmap.

**Health Expenditure and Life Expectancy**

A scatter plot with a fitted trend line explores the relationship between health expenditure and life expectancy. The chart can help identify patterns and outliers across observations.

**Interactive Controls**

A region slicer and year-based controls help users filter and explore the available data.

## Key Analytical Questions

The dashboard is designed to investigate questions such as:

- How does average health expenditure vary across regions?
- How have selected development indicators changed over time?
- Is internet penetration associated with child immunization coverage?
- What relationship can be observed between internet penetration and youth unemployment?
- How does health expenditure relate to life expectancy?
- Which countries have the highest and lowest values for the selected poverty-related measure?
- How do economic, environmental, technological, and health indicators vary across countries?

These are exploratory questions. Observed relationships do not, by themselves, establish causation.

## Repository Structure

```text
Live_API_PowerBI_Project/
│
├── World_Bank_API_Data_Analysis.ipynb
├── Python_Script.Py
├── economic.csv
├── environment.csv
├── health.csv
├── labour_market.csv
├── poverty.csv
├── technology.csv
├── trade.csv
├── .gitignore
└── README.md
```

The notebook and Python script contain the data retrieval and processing workflow. The CSV files contain the prepared datasets used for analysis and Power BI visualization.

## How to Run the Project

### Prerequisites

- Python 3.x
- Jupyter Notebook
- Internet access
- Power BI Desktop

### 1. Clone the repository

```bash
git clone https://github.com/pratikshaaher674/Live_API_Data_Integration_Python_PowerBI.ipynb.git
```

### 2. Navigate to the project folder

```bash
cd Live_API_Data_Integration_Python_PowerBI.ipynb
```

### 3. Install the Python libraries

```bash
pip install pandas numpy requests jupyter
```

### 4. Run the data integration workflow

Open `World_Bank_API_Data_Analysis.ipynb` in Jupyter Notebook and execute its cells in sequence.

Alternatively, run the Python script:

```bash
python Python_Script.Py
```

The script requests data from the World Bank API, processes the responses, and prepares category-specific datasets. An internet connection is required to retrieve fresh API data.

### 5. Explore the Power BI dashboard
Open Power BI Desktop and connect to the prepared CSV datasets. Recreate or refresh the report using the appropriate dataset relationships, measures, and visualizations.

The published repository currently contains the Python files and CSV datasets. The Power BI report file can be added separately if you choose to share it.


## Key Learnings

- Working with REST APIs and paginated responses.
- Extracting and normalizing nested JSON data.
- Using Pandas for data cleaning and transformation.
- Combining country metadata with development indicators.
- Structuring data for multiple analytical use cases.
- Preparing CSV datasets for Power BI.
- Designing KPI cards, trend charts, scatter plots, tables, heatmaps, and interactive filters.
- Exploring relationships between global development indicators.

## Future Improvements

- Add API request timeouts, retry logic, and more robust error handling.
- Improve validation for missing or unexpected API values.
- Automate dataset refresh and dashboard updates.
- Document the calculations used in KPI cards and poverty rankings.
- Improve chart labels, tooltips, and indicator selection.
- Add verified analytical findings and further country-level comparisons.

## Acknowledgements

- **World Bank Open Data** for providing publicly available development indicators.
- This project was developed as a practical learning project focused on Python-based API integration, data preparation, and Power BI visualization.

## Author

**Pratiksha Aher**
 Data Analyst

Skills: Python | SQL | Excel | Power BI | Pandas | NumPy

GitHub: [pratikshaaher674](https://github.com/pratikshaaher674)
