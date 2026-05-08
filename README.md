# Iowa Cancer Crisis — County Incidence Analysis

An end-to-end data analysis project examining cancer incidence rates across 98 Iowa counties, with a focus on rural vs urban disparities and alignment with the 2026 Iowa Cancer Registry findings on agricultural pesticide exposure.

## Project Overview

After reading the 2026 Iowa Cancer Registry report highlighting elevated cancer rates in Iowa's farming population, I decided to build a full data pipeline to explore the county-level data myself. This project covers data extraction, cleaning, relational database design, SQL analysis, and Power BI visualization.

## Key Findings

- All 10 highest-incidence counties in Iowa are rural
- 95 of 98 Iowa counties have stable or rising cancer rates — only 3 are improving
- Cass County has the highest incidence rate in the state at 581.9 per 100,000 — 83 points above the state average — and is still rising
- Rural counties have a maximum incidence rate of 581.9 vs 540.6 for urban counties
- The data is consistent with the 2026 Iowa Cancer Registry report linking Iowa's farming population to elevated pesticide and nitrate exposure

## Tech Stack

- **Python** — data extraction, cleaning, and loading (pandas, mysql-connector-python)
- **MySQL** — relational database design and storage
- **SQL** — analytical queries for trend analysis and hotspot identification
- **Power BI** — interactive dashboard for visualization
- **GitHub** — version control and project documentation

## Data Sources

- [NCI State Cancer Profiles](https://statecancerprofiles.cancer.gov) — county-level age-adjusted incidence rates 2018-2022
- [CDC WONDER](https://wonder.cdc.gov/cancer.html) — statewide cancer incidence trends 1999-2022
- [Iowa Cancer Registry 2026 Report](https://shri.public-health.uiowa.edu/cancer-data/iowa-cancer-reports/) — farming population context and pesticide exposure research

## Project Structure
