# COVID-19
> ETL from JHU CSSE GitHub Repo to Create Tableau Visualization.
### Link to Viz. [Coronavirus COVID-19 Cases Worldwide](https://public.tableau.com/profile/eklavya.saxena#!/vizhome/CoronavirusCOVID-19CasesWorldwide/COVID-19_Country)    


#### Steps performed in ETL:
- Extract .csv files from 'GitHub repository raw' URLs using 'pandas' read_csv
- Merge created dataframes on column - 'Province_State','Country_Region','Lat','Long','Date'
- As required, replace NaNs from the data
- Export the cleaned pandas dataframe to google sheets using 'pygsheets'