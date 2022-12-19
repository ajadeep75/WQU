""" Connecting to the Database """

import imports


# Connect to database
# Access a certain collection

# Create a Mongo-`client`
client = MongoClient(host="localhost", port=<portNumber>)

# Create a database: `db`
db = client["wqu-abtest"]

# Find your collection: `"<collectionName>"`
mscfe_app = db["<collectionName>"]


#Build Contingency

import imports
import crosstab


# `build_contingency_bar` function
def build_contingency_bar():
    # side-by-side bar chart
    fig = px.bar(
        data_frame=data,
        barmode="group",
        title="TITLE"
    )
    # Set axis labels
    fig.update_layout(xaxis_title="XTITLE", yaxis_title="YTITLE")
    return fig

# Display
cb_fig = build_contingency_bar()
cb_fig.write_image("images/7-5-16.png", scale=1, height=500, width=700)

cb_fig.show()

# Contingency Table

import imports


# contingency table
contingency_table = Table2x2(data.values)

# chi-square test
chi_square_test = contingency_table.test_nominal_association()

# odds ratio
odds_ratio = contingency_table.oddsratio.round(1)

# summary...
summary = contingency_table.summary()


# Mongo Instance
import imports
from our_mongo_class import MongoRepository


# An instance of class MongoRepository
repo = MongoRepository()
