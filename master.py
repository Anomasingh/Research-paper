import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

prison = pd.read_csv(r'E:/python internship/FINAL DATASET - Sheet2.csv')
st.title('Women Centric Data Analysis')
st.dataframe(prison, height=200 , width=900)
#st.table(prison.iloc[0:10])
#st.json({'foo':'bar','fu':'ba'})
#st.metric('My metric',42,2)
##Converting non-numeric columns to numeric
def convert_to_numeric(column_name):
    return pd.to_numeric(prison[column_name], errors='coerce')

# Columns to convert
columns_to_convert = ['Cheating\n (Sec. 419,\n 420 IPC)',
                      'Criminal Breach of Trust (Sec. 406 -409 IPC)',
                      'Theft (Sec. 379 -382 IPC)']

# Convert the specified columns
for column in columns_to_convert:
    prison[column] = convert_to_numeric(column)

# Display the updated dataset
#st.write(prison)
st.write("Shape of the DataFrame:", prison.shape)
st.write("Head of the DataFrame:", prison.head())
st.write("Columns of the DataFrame:", prison.columns)
st.write("NULL Values count:", prison.isna().sum())
# Add a button to fill missing values with 0
if st.button("Fill Missing Values with 0"):
    prison = prison.fillna(0)
    st.write("Missing values filled with 0.")
# Display the total count of missing values in the entire DataFrame
st.write("NULL Values count:", prison.isnull().sum().sum())
st.write("Checking the Description of each column (like count,mean, minimum, maximum):", prison.describe())
columns_to_drop = ['State', 'District', 'Year']
dropping_state_district_year = prison.drop(columns_to_drop, axis=1)

# Display the head of the modified DataFrame
st.subheader('Modified DataFrame (after dropping columns):')
st.write(dropping_state_district_year.head())
st.write("Dropping Duplicates:", prison.drop_duplicates())
st.write("Finding the Sum of all the crimes:", dropping_state_district_year.sum(axis=0))
st.write("Finding the Maximum of all the crimes:", dropping_state_district_year.max(axis=0))

main_crimes = dropping_state_district_year.drop(['Other IPC Crime','Total Cog. Crime Under IPC'],axis=1)
st.write("Dropping Other IPC Crime and Total Cog. Crime Under IPC to find the maximum among all the crimes:",main_crimes.head())
Maximum = main_crimes.sum().sort_values(ascending = False)
st.write("Finding the sum of the main crimes:",Maximum)
st.write("Finding the maximum among all the main crimes:",Maximum[Maximum == Maximum.max()])
st.write("States:",prison['State'].unique())


