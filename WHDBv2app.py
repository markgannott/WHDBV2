import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset (Replace with actual file if needed)
data = {
    "Category": ["Total Cost (Low)", "Total Cost (Medium)", "Total Cost (High)"],
    "UK": [37561920194, 56342880291, 75123840388],
    "US": [224490439085, 336735658627, 448980878170],
    "Both": [262052359279, 393078538918, 524104718558]
}
df_cost = pd.DataFrame(data)

data_prevalence = {
    "Prevalence": ["Low", "Medium", "High"],
    "UK": [1620000, 2430000, 3240000],
    "US": [9682000, 14523000, 19364000],
    "Total Pop": [11302000, 16953000, 22604000]
}
df_prevalence = pd.DataFrame(data_prevalence)

data_per_capita = {
    "Type": ["Absenteeism Base", "Absenteeism Mult", "Absenteeism Total",
              "Presenteeism Base", "Presenteeism Mult", "Presenteeism Total",
              "WEP Base", "WEP Mult", "Stromberg Total WEP"],
    "UK": [4012, 3891, 7903, 3622, 1956, 5577, 13480, 9706, 23186],
    "US": [5038, 4887, 9925, 4548, 2456, 7004, 16928, 12188, 29117],
    "WA": [4891, 4744, 9635, 4415, 2384, 6799, 16434, 11833, 28267]
}
df_per_capita = pd.DataFrame(data_per_capita)

# Streamlit App
st.set_page_config(page_title="PCOS Economic Impact Dashboard", layout="wide")
st.title("PCOS Economic Burden Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")
cost_level = st.sidebar.radio("Select Cost Level", ["Low", "Medium", "High"], index=1)

# Cost Visualization
st.subheader("Total Economic Burden by Country")
df_filtered = df_cost[df_cost["Category"].str.contains(cost_level)]
fig_cost = px.bar(df_filtered, x="Category", y=["UK", "US", "Both"],
                  title="Economic Burden Breakdown", barmode="group")
st.plotly_chart(fig_cost)

# Prevalence Visualization
st.subheader("Prevalence of PCOS by Country")
fig_prevalence = px.bar(df_prevalence, x="Prevalence", y=["UK", "US", "Total Pop"],
                        title="Affected Population by Region", barmode="group")
st.plotly_chart(fig_prevalence)

# Workforce Economic Productivity Visualization
st.subheader("Per Capita Costs")
fig_per_capita = px.bar(df_per_capita, x="Type", y=["UK", "US", "WA"],
                        title="Workforce Economic Productivity Impact", barmode="group")
st.plotly_chart(fig_per_capita)

# Display DataTables
st.subheader("Data Overview")
st.write("Economic Burden Data")
st.dataframe(df_cost)
st.write("Prevalence Data")
st.dataframe(df_prevalence)
st.write("Workforce Economic Productivity Data")
st.dataframe(df_per_capita)

# Download Button
csv = df_cost.to_csv(index=False)
st.download_button("Download Cost Data", csv, "pcos_cost_data.csv", "text/csv")
