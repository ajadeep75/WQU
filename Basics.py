# ADDING COLUMNS

df2.head()

	property_type	state	region	lat	lon	area_m2	price_brl
0	apartment	Pernambuco	Northeast	-8.134204	-34.906326	72.0	414222.98
1	apartment	Pernambuco	Northeast	-8.126664	-34.903924	136.0	848408.53
2	apartment	Pernambuco	Northeast	-8.125550	-34.907601	75.0	299438.28
3	apartment	Pernambuco	Northeast	-8.120249	-34.895920	187.0	848408.53
4	apartment	Pernambuco	Northeast	-8.142666	-34.906906	80.0	464129.36

# price_brl ---> price in Brazilian reals
# create new column price_usd
# use 1 USD = 3.19 Brazilian reals

df2["price_usd"] = df2["price_brl"] / 3.19
df2.head()

	property_type	state	region	lat	lon	area_m2	price_brl	price_usd
0	apartment	Pernambuco	Northeast	-8.134204	-34.906326	72.0	414222.98	129850.463950
1	apartment	Pernambuco	Northeast	-8.126664	-34.903924	136.0	848408.53	265958.786834
2	apartment	Pernambuco	Northeast	-8.125550	-34.907601	75.0	299438.28	93867.799373
3	apartment	Pernambuco	Northeast	-8.120249	-34.895920	187.0	848408.53	265958.786834
4	apartment	Pernambuco	Northeast	-8.142666	-34.906906	80.0	464129.36	145495.097179


# DROP COLUMNS
# drop price_brl

df2 = df2.drop("price_brl", axis="columns")
df2.head()

	property_type	state	region	lat	lon	area_m2	price_usd
0	apartment	Pernambuco	Northeast	-8.134204	-34.906326	72.0	129850.463950
1	apartment	Pernambuco	Northeast	-8.126664	-34.903924	136.0	265958.786834
2	apartment	Pernambuco	Northeast	-8.125550	-34.907601	75.0	93867.799373
3	apartment	Pernambuco	Northeast	-8.120249	-34.895920	187.0	265958.786834
4	apartment	Pernambuco	Northeast	-8.142666	-34.906906	80.0	145495.097179

# concatenate 2 data frames using concat

df = pd.concat([df1, df2])

# df1.shape before dropping NaNs ---> (12834, 6)

df1.dropna(inplace=True)  # drop rows with null values
df1.shape

# Output
(11551, 6)

#Import CSV
df1 = pd.read_csv("data/brasil-real-estate-1.csv")
df1.shape

# Inspect Data
df1.info()
df1.shape
df1.head()   # Displays the first 5 rows starting from 0

# Correlation Coefficient
corr1= homes_by_state["area_m2"].corr(homes_by_state["price_usd"])

# Describe Method
summary_stats = dfa.describe()

# Groupby Method
mean_price_by_region = df.groupby("region")["price_usd"].mean().sort_values(ascending=True)

# Value Counts Method
 - counts the number of items/ things

homes_by_state = df_south["state"].value_counts()
homes_by_state


Rio Grande do Sul    2643
Santa Catarina       2634
Paraná               2544
Name: state, dtype: int64
    
