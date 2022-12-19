# Retrive Data

-retrieve intercept
intercept = model.named_steps["ridge"].intercept_

-retrieve coefficients
coefficients = model.named_steps["ridge"].coef_

-retrieve names
features = model.named_steps["onehotencoder"].get_feature_names()

-create a series of names and values
feat_imp = pd.Series(coefficients, index=features)
feat_imp

-sample output
surface_covered_in_m2               291.654156
lat                                 478.901375
lon                               -2492.221814
borough_Benito Juárez             13778.188880
borough_Iztacalco                   405.403127
borough_Azcapotzalco               2459.288646
borough_Coyoacán                   3737.561001
borough_Álvaro Obregón             3275.121061
borough_Iztapalapa               -13349.017448
borough_Cuauhtémoc                 -350.531990
borough_Tláhuac                  -14166.869486
borough_Miguel Hidalgo             1977.314718


# splitting data into feature matrix and target vector

target = "price_aprox_usd"  # <--- vector
features = ["surface_covered_in_m2", "lat", "lon", "borough"]   # <--- matrix
X_train = df[features]  # training data
y_train = df[target]    # " " " "

-The vector is what we are trying to predict using the matrix
-In this case we are trying to predict the price of a property
-using the features in the matrix

# Baseline
-Done after splitting data
-into features and vector

from sklearn.metrics import mean_absolute_error

y_mean = y_train.mean()
y_pred_baseline = [y_mean] * len(y_train)
baseline_mae = mean_absolute_error(y_train, y_pred_baseline)    # what our model needs to beat

#Predict
y_test_pred = pd.Series(model.predict(X_test))
y_test_pred.head()

# sample output
0    53538.366480
1    53171.988369
2    34263.884179
3    53488.425607
4    68738.924884
dtype: float64

#Build and Fit
from category_encoders import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.pipeline import make_pipeline

-build
model = make_pipeline(
    OneHotEncoder(use_cat_names=True),
    SimpleImputer(),
    Ridge()
)

-fit...
model.fit(X_train, y_train)
