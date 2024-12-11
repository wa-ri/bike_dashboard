import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


sns.set(style='dark')

# Load the data
data_path = 'dashboard/day.csv'
bike_day = pd.read_csv(data_path)

# Convert the 'dteday' column to datetime
bike_day['dteday'] = pd.to_datetime(bike_day['dteday'])

# Preprocess the data
bike_day['season'] = bike_day['season'].map({1: 'Springer', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
bike_day['workingday'] = bike_day['workingday'].map({0: 'Hari Libur', 1: 'Hari Kerja'})

# Set up Streamlit interface
st.title('Bike Sharing Data Analysis')

# Create tabs
tab1, tab2 = st.tabs(["Season Analysis", "Working Day Analysis"])

# Date filter
st.sidebar.header('Filter by Date')
start_date = st.sidebar.date_input('Start Date', bike_day['dteday'].min())
end_date = st.sidebar.date_input('End Date', bike_day['dteday'].max())

# Filter data based on selected date range
filtered_data = bike_day[(bike_day['dteday'] >= pd.to_datetime(start_date)) & (bike_day['dteday'] <= pd.to_datetime(end_date))]

# Group by season and calculate the sum of 'cnt'
season_grouped = filtered_data.groupby('season')['cnt'].sum().reset_index()
workingday_grouped = filtered_data.groupby('workingday')['cnt'].sum().reset_index()


with tab1:
    # Display the filtered data and the results
    st.subheader('Filtered Data')
    st.write(filtered_data)

    st.subheader('Total Count by Season')
    st.write(season_grouped)

    # Optional: Plotting
    st.subheader('Total Count by Season (Bar Chart)')
    st.bar_chart(season_grouped.set_index('season'))
with tab2:
     # Display the filtered data and the results
    st.subheader('Filtered Data')
    st.write(filtered_data)

    st.subheader('Total Count by workingday')
    st.write(workingday_grouped)

    # Optional: Plotting
    st.subheader('Total Count by workingday (Bar Chart)')
    st.bar_chart(workingday_grouped.set_index('workingday'))