# COVID-19
> ETL from JHU CSSE GitHub Repo to Create Tableau Visualization.

### Link to Medium Blog: [Automated ETL for LIVE Tableau Public Visualizations](https://towardsdatascience.com/automated-etl-for-live-tableau-public-visualizations-54f2b8652224)    

### Link to Visualization: [Coronavirus COVID-19 Cases Worldwide](https://public.tableau.com/profile/eklavya.saxena#!/vizhome/CoronavirusCOVID-19CasesWorldwide/COVID-19_Country)    


#### Steps performed in ETL:
1. Extract data from raw .csv files of GitHub User Content using 'pandas'
2. Melt and join created dataframes on column - 'Province_State','Country_Region','Lat','Long','Date'
3. Create a batch file and automate Python scripts with Task Scheduler on Windows
4. Connect Python to Google Sheets and export the cleaned dataframe using 'pygsheets'
