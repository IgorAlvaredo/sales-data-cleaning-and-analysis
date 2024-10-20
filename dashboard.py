import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("./data/sales_data_sample.csv", sep=",")
df['ORDERDATE'] = pd.to_datetime(df["ORDERDATE"])
df = df.sort_values("ORDERDATE")

df["Month"] = df["ORDERDATE"].apply(lambda x: str(x.year) + "-" + str(x.month))

month = st.sidebar.selectbox("Mês", df["Month"].unique())
df_filtered = df[df["Month"] == month]
# df_filtered

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered,x="ORDERDATE", y="SALES", title="Faturamento por dia", color="CITY")
col1.plotly_chart(fig_date)

fig_prod = px.bar(df_filtered,x="ORDERDATE", y="PRODUCTLINE", title="Faturamento por tipo de produto", color="CITY", orientation="h")
col2.plotly_chart(fig_prod)

city_total = df_filtered.groupby("CITY")[["SALES"]].sum().reset_index()
fig_city = px.bar(city_total,x="CITY", y="SALES", title="Faturamento por cidade")
col3.plotly_chart(fig_city)

fig_kind = px.pie(df_filtered, values="SALES", names="DEALSIZE", title="Faturamento por cidade")
col4.plotly_chart(fig_kind)

city_status = df_filtered.groupby("CITY")[["QUANTITYORDERED"]].sum().reset_index()
fig_status = px.bar(df_filtered,x="CITY", y="QUANTITYORDERED",color="DEALSIZE", title="Quantidade de pedidos por cidade")
col5.plotly_chart(fig_status, use_container_width=True)