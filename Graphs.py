# Histogram

import matplotlib.pyplot as plt

plt.hist(df["price_usd"])
plt.xlabel("Price [USD]")
plt.ylabel("Frequency")
plt.title("Distribution of Home Prices")

# Bar Chart

import pandas as pd

mean_price_by_region.plot(
    kind="bar",
    xlabel="Region",
    ylabel="Mean Price [USD]",
    title="Mean Home Price by Region"
);

# Scatter Plot

import matplotlib.pyplot as plt

plt.scatter(x=homes_by_state["area_m2"], y=homes_by_state["price_usd"])
plt.xlabel("Area [sq meters]")
plt.ylabel("Price [USD]")
plt.title("Rio Grande do Sul: Price vs. Area");

#Scatter Mapbox

import plotly.express as px

fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    center={"lat": -14.2, "lon": -51.9},  # Map will be centered on Brazil
    width=600,
    height=600,
    hover_data=["price_usd"],  # Display price when hovering mouse over house
)

fig.update_layout(mapbox_style="open-street-map")

fig.show()

# Time Series Plot
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(15, 6))
y.plot(xlabel="Date", ylabel="PM2.5 Level", title="Dar es Salaam PM2.5 Levels", ax=ax);

# Box Plot

sns.boxplot(x="severe_damage", y="plinth_area_sq_ft", data=df)
plt.xlabel("Severe Damage")
plt.ylabel("Plinth Area [sq. ft.]")
plt.title("Kavrepalanchok, Plinth Area vs Building Damage");

# PACF Plot

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(15, 6))
plot_pacf(y, ax=ax) 
plt.xlabel(<"xLabelvalue">)
plt.ylabel(<"yLabelvalue">)
plt.title(<"yourTitle">);

# ACF Plot

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(15, 6))
plot_acf(y, ax=ax)
plt.xlabel(<"xLabelvalue">)
plt.ylabel(<"yLabelvalue">)
plt.title(<"yourTitle">);

#Choropleth Map

import imports
import load


# `build_nat_choropleth` function
<df_Name>["count_pct"] = (<df_Name>["count"] / <df_Name>["count"].sum()) * 100


def build_nat_choropleth():
    fig = px.choropleth(
        data_frame= <df_Name>,
        locations="country_iso3",
        color="count_pct",
        projection="natural earth",
        color_continuous_scale=px.colors.sequential.Oranges,
        title="Title"
    )
    return fig

# Display image
nat_fig = build_nat_choropleth()
nat_fig.write_image("images/7-5-4.png", scale=1, height=500, width=700)

nat_fig.show()
