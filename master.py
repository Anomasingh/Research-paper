import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
import matplotlib.ticker as mtick
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

prison = pd.read_csv(r'/workspaces/Research-paper/PRISON.csv', encoding='iso-8859-1')
st.title('Women Centric Data Analysis')
st.write('Head of the Dataset:')
st.dataframe(prison.head(), height=200 , width=900)
#st.table(prison.iloc[0:10])
#st.json({'foo':'bar','fu':'ba'})
#st.metric('My metric',42,2)
##Converting non-numeric columns to numeric
def convert_to_numeric(column_name):
    prison[column_name] = pd.to_numeric(prison[column_name], errors='coerce')

# Columns to convert
columns_to_convert = ['Cheating\n (Sec. 419,\n 420 IPC)',
                      'Criminal Breach of Trust (Sec. 406 -409 IPC)',
                      'Theft (Sec. 379 -382 IPC)']

# Convert the specified columns
for column in columns_to_convert:
    convert_to_numeric(column)

# Display the updated dataset
#st.write(prison)
st.write("Shape of the DataFrame:", prison.shape)
#st.write("Head of the DataFrame:", prison.head())
st.write("Columns of the DataFrame:", prison.columns)
# Display the data types of the columns
def main():
        st.write("Data Types:")
        st.write(prison.dtypes)

if __name__ == "__main__":
    main()
st.write("NULL Values count:", prison.isna().sum())
# Add a button to fill missing values with 0
st.write('Do not Forget to click this button')
if st.button("Fill Missing Values with 0"):
    prison = prison.fillna(0)
    st.write("Missing values filled with 0.")
# Display the total count of missing values in the entire DataFrame
st.write("NULL Values count:", prison.isnull().sum().sum())
st.write("Checking the Description of each column (like count,mean, minimum, maximum):", prison.describe())
columns_to_drop = ['State', 'District', 'Year']
dropping_state_district_year = prison.drop(columns_to_drop, axis=1)

# Display the head of the modified DataFrame
st.subheader('Modified DataFrame (after dropping state,district,year columns as they are not used in finding min, max,etc.):')
st.write(dropping_state_district_year.head())
st.write("Dropping Duplicates:", prison.drop_duplicates())
st.write("Finding the Sum of all the crimes:", dropping_state_district_year.sum(axis=0))
st.write("Finding the Maximum of all the crimes:", dropping_state_district_year.max(axis=0))

main_crimes = dropping_state_district_year.drop(['Other IPC Crime','Total Cog. Crime Under IPC'],axis=1)
st.write("Dropping Other IPC Crime and Total Cog. Crime Under IPC to find the maximum among all the crimes:",main_crimes.head())
Maximum = main_crimes.sum().sort_values(ascending = False)
# st.write("Finding the sum of the main crimes:",Maximum)
st.write("Finding the maximum among all the main crimes:",Maximum[Maximum == Maximum.max()])
st.write("States:",prison['State'].unique())
# Group by State and Year and sum the crime columns
state_crime_counts = prison.groupby(["State", "Year"])[[
    "Murder (Sec.302 & 303 IPC)",
       "Attempt To Commit Murder (Sec.307 IPC)",
       "C.H. Not Amoun- ting To Murder (Sec.304 &308 IPC)",
       "Rape (Sec.376 IPC)",
       "Kidnapping & Abduction (Sec.363-369,371-373 IPC)",
       "Dacoity (Sec.395\n to 398 IPC)",
       "Prepara- tion & Assembly for Dacoity (Sec. 399 \n 402 IPC)",
       "Robbery\n (Sec. 392 \n 394, 397 &\n 398 IPC)",
       "Burglary\n (Sec. 449 \n 452, 454,\n 455, 457 \n 460 IPC)",
       "Theft (Sec. 379 -382 IPC)",
       "Riots\n (Sec. 143-\n 145, 147-\n 151, 153,\n 153A,\n 153B, 157,\n 158, 160\n IPC)",
       "Criminal Breach of Trust (Sec. 406 -409 IPC)",
       "Cheating\n (Sec. 419,\n 420 IPC)",
       "Counter- Feiting (Sec. 231-254, 489A-\n 489D IPC)",
       "Arson (Sec. 435,436,\n 438 IPC)",
       "Hurt\n (Sec. 323-\n 333, 335-338\n IPC)",
       "Dowry Death (Sec. 304B IPC)", "Molestation\n (Sec. 354 IPC)",
       "Cruelty by Husband & Relatives (Sec. 498A IPC)",
       "Importa\n -tion of Girls (Sec.\n 366B IPC)",
       "Causing Death By Negligence (Sec. 304A IPC)", "Other IPC Crime",
       "Total Cog. Crime Under IPC"
]].sum()

def main():
    st.title("Total Number of Crimes in Different States Each Year")
    
    # Create a multiselect widget to choose states
    selected_states = st.multiselect("Select States", state_crime_counts.index.get_level_values("State").unique())

    if selected_states:
        # Filter the data based on selected states
        filtered_data = state_crime_counts.loc[selected_states]

        # Display the filtered data
        st.write("Total Crime Counts:")
        st.write(filtered_data)

if __name__ == "__main__":
    main()

def main():
    st.title("Maximum Crimes in Different States Each Year")
    
    # Create a multiselect widget to choose states
    selected_states = st.multiselect("Select States", prison['State'].unique())

    if selected_states:
        # Filter the data based on selected states
        filtered_data = prison[prison['State'].isin(selected_states)]
        
        # Group by State and Year and find the maximum of all crime columns
        max_crimes = filtered_data.groupby(["State", "Year"])[[
          "Murder (Sec.302 & 303 IPC)",
            "Attempt To Commit Murder (Sec.307 IPC)",
            "C.H. Not Amoun- ting To Murder (Sec.304 &308 IPC)",
            "Rape (Sec.376 IPC)",
            "Kidnapping & Abduction (Sec.363-369,371-373 IPC)",
            "Dacoity (Sec.395\n to 398 IPC)",
            "Prepara- tion & Assembly for Dacoity (Sec. 399 ‚\n 402 IPC)",
            "Robbery\n (Sec. 392 ‚\n 394, 397 &\n 398 IPC)",
            "Burglary\n (Sec. 449 ‚\n 452, 454,\n 455, 457 ‚\n 460 IPC)",
            "Theft (Sec. 379 -382 IPC)",
            "Riots\n (Sec. 143-\n 145, 147-\n 151, 153,\n 153A,\n 153B, 157,\n 158, 160\n IPC)",
            "Criminal Breach of Trust (Sec. 406 -409 IPC)",
            "Cheating\n (Sec. 419,\n 420 IPC)",
            "Counter- Feiting (Sec. 231-254, 489A-\n 489D IPC)",
            "Arson (Sec. 435,436,\n 438 IPC)",
            "Hurt\n (Sec. 323-\n 333, 335-338\n IPC)",
            "Dowry Death (Sec. 304B IPC)",
            "Molestation\n (Sec. 354 IPC)",
            "Cruelty by Husband & Relatives (Sec. 498A IPC)",
            "Importa\n -tion of Girls (Sec.\n 366B IPC)",
            "Causing Death By Negligence (Sec. 304A IPC)",
            "Other IPC Crime",
            "Total Cog. Crime Under IPC"
        ]].max()

        # Display the maximum crimes data
        st.write("Maximum Crimes:")
        st.write(max_crimes)

if __name__ == "__main__":
    main()
    
def main():
    st.title("Rows with Peak Crimes in Each Crime Category")

    for column in prison.columns:
        if column not in ["State", "Year", "District","Attempt To Commit Murder (Sec.307 IPC)",
            "C.H. Not Amoun- ting To Murder (Sec.304 &308 IPC)",
            "Dacoity (Sec.395\n to 398 IPC)",
            "Prepara- tion & Assembly for Dacoity (Sec. 399  402 IPC)",
            "Robbery (Sec. 392  394, 397 & 398 IPC)",
            "Burglary (Sec. 449  452, 454, 455, 457  460 IPC)",
            "Theft (Sec. 379 -382 IPC)",
            "Riots\n (Sec. 143-\n 145, 147-\n 151, 153,\n 153A,\n 153B, 157,\n 158, 160\n IPC)",
            "Criminal Breach of Trust (Sec. 406 -409 IPC)",
            "Cheating\n (Sec. 419,\n 420 IPC)",
            "Counter- Feiting (Sec. 231-254, 489A-\n 489D IPC)",
            "Arson (Sec. 435,436,\n 438 IPC)",
            "Hurt\n (Sec. 323-\n 333, 335-338\n IPC)",
            "Causing Death By Negligence (Sec. 304A IPC)"]:
            max_row = prison[prison[column] == prison[column].max()]

            if not max_row.empty:
                st.write(f"Crime Category: {column}")
                st.write("Row(s) with Maximum Value:")
                st.write(max_row)
                st.write("----------------------------")

if __name__ == "__main__":
    main()
    
    

def main():
    st.title("Crime Statistics by Year and Top 10 States")

    # Total number of Murder Cases Registered by Year
    st.header("Total Number of Murder (Sec.302 & 303 IPC) Cases Registered by Year")
    murder_cases_by_year = prison.groupby("Year")["Murder (Sec.302 & 303 IPC)"].sum()
    st.write(murder_cases_by_year)
    
    # Total number of Kidnapping and Abduction Cases Registered by Year
    st.header("Total Number of Kidnapping & Abduction (Sec.363-369,371-373 IPC) Cases Registered by Year")
    kidnapping_and_abduction_cases_by_year = prison.groupby("Year")["Kidnapping & Abduction (Sec.363-369,371-373 IPC)"].sum()
    st.write(kidnapping_and_abduction_cases_by_year)

    # Total number of Girl Importation Cases Registered by Year
    st.header("Total Number of Girl Importation Cases Registered by Year")
    girl_importation_cases_by_year = prison.groupby("Year")["Importa\n -tion of Girls (Sec.\n 366B IPC)"].sum()
    st.write(girl_importation_cases_by_year)

    # Total number of Dowry Death (Sec. 304B IPC) Cases Registered by Year
    st.header("Total Number of Dowry Death (Sec. 304B IPC) Cases Registered by Year")
    dowry_death_cases_by_year = prison.groupby("Year")["Dowry Death (Sec. 304B IPC)"].sum()
    st.write(dowry_death_cases_by_year)
    
    # Total number of Dowry Death (Sec. 304B IPC) Cases Registered by Year
    st.header("Total Number of Rape (Sec.376 IPC) Cases Registered by Year")
    rape_cases_by_year = prison.groupby("Year")["Rape (Sec.376 IPC)"].sum()
    st.write(rape_cases_by_year)
    
    # Total number of Molestation (Sec. 354 IPC) Cases Registered by Year
    st.header("Total Number of Molestation (Sec. 354 IPC) Cases Registered by Year")
    molestation_cases_by_year = prison.groupby("Year")["Molestation\n (Sec. 354 IPC)"].sum()
    st.write(molestation_cases_by_year)

    # Total number of Cruelty by Husband & Relatives (Sec. 498A IPC) Cases Registered by Year
    st.header("Total Number of Cruelty by Husband & Relatives (Sec. 498A IPC) Cases Registered by Year")
    cruelty_cases_by_year = prison.groupby("Year")["Cruelty by Husband & Relatives (Sec. 498A IPC)"].sum()
    st.write(cruelty_cases_by_year)
    
    # Top 10 States with the Most Murder (Sec.302 & 303 IPC) Cases
    st.header("Top 10 States with the Most Murder (Sec.302 & 303 IPC) Cases")
    top_states_by_rape_cases = prison.groupby("State")["Murder (Sec.302 & 303 IPC)"].sum().nlargest(10)
    st.write(top_states_by_rape_cases)
    
    # Top 10 States with the Most Kidnapping & Abduction (Sec.363-369,371-373 IPC) Cases
    st.header("Top 10 States with the Most Kidnapping & Abduction (Sec.363-369,371-373 IPC)")
    top_states_by_kidnapping_and_abduction_cases = prison.groupby("State")["Kidnapping & Abduction (Sec.363-369,371-373 IPC)"].sum().nlargest(10)
    st.write(top_states_by_kidnapping_and_abduction_cases)

    # Top 10 States with the Most Importation of Girls (Sec.\n 366B IPC) Cases
    st.header("Top 10 States with the Most Importation of Girls (Sec.\n 366B IPC) Cases")
    top_states_by_importation_of_girls_cases = prison.groupby("State")["Importa\n -tion of Girls (Sec.\n 366B IPC)"].sum().nlargest(10)
    st.write(top_states_by_importation_of_girls_cases)
    
    # Top 10 States with the Most Dowry Death (Sec. 304B IPC) Cases
    st.header("Top 10 States with the Most Dowry Death (Sec. 304B IPC)")
    top_states_by_dowry_death_cases = prison.groupby("State")["Dowry Death (Sec. 304B IPC)"].sum().nlargest(10)
    st.write(top_states_by_dowry_death_cases)
    
    # Top 10 States with the Most Rape (Sec.376 IPC) Cases
    st.header("Top 10 States with the Most Rape (Sec.376 IPC) Cases")
    top_states_by_rape_cases = prison.groupby("State")["Rape (Sec.376 IPC)"].sum().nlargest(10)
    st.write(top_states_by_rape_cases)
    
    # Top 10 States with the Most Molestation (Sec. 354 IPC) Cases
    st.header("Top 10 States with the Most Molestation (Sec. 354 IPC) Cases")
    top_states_by_molestation_cases = prison.groupby("State")["Molestation\n (Sec. 354 IPC)"].sum().nlargest(10)
    st.write(top_states_by_molestation_cases)
    
    # Top 10 States with the Most Rape (Sec.376 IPC) Cases
    st.header("Top 10 States with the Most Cruelty by Husband & Relatives (Sec. 498A IPC)")
    top_states_by_cruelty_by_husband_cases = prison.groupby("State")["Cruelty by Husband & Relatives (Sec. 498A IPC)"].sum().nlargest(10)
    st.write(top_states_by_cruelty_by_husband_cases)


if __name__ == "__main__":
    main()



