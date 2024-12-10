import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Load the data
data_path = 'dashboard/day.csv'
df = pd.read_csv(data_path)

# Preprocess the data
df['season'] = df['season'].map({1: 'Springer', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
df['workingday'] = df['workingday'].map({0: 'Hari Libur', 1: 'Hari Kerja'})

# Analysis for the season with the highest rentals
season_rentals = df.groupby('season')['cnt'].sum().reset_index().sort_values(by='cnt', ascending=False)
top_season = season_rentals.iloc[0]['season']

# Analysis for rentals on working days vs non-working days
workingday_rentals = df.groupby('workingday')['cnt'].sum().reset_index().sort_values(by='cnt', ascending=False)
top_workingday = workingday_rentals.iloc[0]['workingday']

# Title of the dashboard
st.title("Bike Sharing Analysis Dashboard")

# Create tabs
tab1, tab2 = st.tabs(["Season Analysis", "Working Day Analysis"])

# Content for Season Analysis tab
with tab1:
    st.header("Season Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Total Penyewaan By Season")
        st.bar_chart(season_rentals.set_index('season')['cnt'])

        st.subheader("Season  Tertinggi")
        st.write(f"Musim tertinggi adalah **{top_season}**.")

    with col2:
        st.subheader("Season Data")
        st.write(season_rentals)

# Content for Working Day Analysis tab
with tab2:
    st.header("Working Day Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Total by Working Day")
        st.bar_chart(workingday_rentals.set_index('workingday')['cnt'])

        st.subheader("Penyewaan Tertinggi")
        st.write(f"Penyewaan tertinggi adalah hari**{top_workingday}**.")

    with col2:
        st.subheader("Detailed Workingday Data")
        st.write(workingday_rentals)

# tab1, tab2= st.tabs(["Read Data", "Grafik"])
# # col1, col2, col3, col4, col5 = st.columns(5)

# with tab1:
#     # Display the data table
#     st.header("Data Table")
#     st.write(df)

#     # Display summary statistics
#     st.header("Summary Statistics")
#     st.write(df.describe())

# with tab2:
#     # Plot a line chart of two columns
#     st.subheader("Line Chart")
#     column1 = st.selectbox("Select column for X-axis", df.columns)
#     column2 = st.selectbox("Select column for Y-axis", df.columns)
#     if st.button("Generate Line Chart"):
#         fig, ax = plt.subplots()
#         ax.plot(df[column1], df[column2], label=f'{column2} over {column1}')
#         ax.set_xlabel(column1)
#         ax.set_ylabel(column2)
#         ax.legend()
#         st.pyplot(fig)

#     # Plot a bar chart of one column
#     st.subheader("Bar Chart")
#     bar_column = st.selectbox("Select column for Bar Chart", df.columns)
#     if st.button("Generate Bar Chart"):
#         fig, ax = plt.subplots()
#         ax.bar(df.index, df[bar_column], label=bar_column)
#         ax.set_xlabel("Index")
#         ax.set_ylabel(bar_column)
#         ax.legend()
#         st.pyplot(fig)

#     # Plot a histogram of one column
#     st.subheader("Histogram")
#     hist_column = st.selectbox("Select column for Histogram", df.columns)
#     if st.button("Generate Histogram"):
#         fig, ax = plt.subplots()
#         ax.hist(df[hist_column], bins=20, label=hist_column)
#         ax.set_xlabel(hist_column)
#         ax.set_ylabel("Frequency")
#         ax.legend()
#         st.pyplot(fig)















