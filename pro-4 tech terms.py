#Log Reg

model_lr = make_pipeline(
    OneHotEncoder(use_cat_names=True),
    LogisticRegression(max_iter=<1000-3000>)   #max_iter: varies: suppresses the 'ConvergenceWarning'
)
# Fit model to training data
model_lr.fit(X_train, y_train)

#Accuracy
lr_train_acc = accuracy_score(y_train, model_lr.predict(X_train))
lr_val_acc = model_lr.score(X_val, y_val)

print("Logistic Regression, Training Accuracy Score:", lr_train_acc)
print("Logistic Regression, Validation Accuracy Score:", lr_val_acc)

# sample output
Logistic Regression, Training Accuracy Score: 0.6515042628948486
Logistic Regression, Validation Accuracy Score: 0.6536878552296335
    
    
    
# Decision Trees

depth_hyperparams = range(1, 16)    # for max_depth
training_acc = []
validation_acc = []
for d in depth_hyperparams:
    model_dt = make_pipeline(
        OrdinalEncoder(), 
        DecisionTreeClassifier(max_depth= d, random_state=42)
    )
    # Fit model to training data
    model_dt.fit(X_train, y_train)
    # Calculate training accuracy score and append to `training_acc`
    training_acc.append(model_dt.score(X_train, y_train))
    # Calculate validation accuracy score and append to `training_acc`
    validation_acc.append(model_dt.score(X_val, y_val))

print("Training Accuracy Scores:", training_acc[:6])
print("Validation Accuracy Scores:", validation_acc[:6])


# sample output
Training Accuracy Scores: [0.6303041191650606, 0.6303041191650606, 0.642292490118577, 0.653529546271192, 0.6543951915852743, 0.6576617776761506]
Validation Accuracy Scores: [0.6350035931273273, 0.6350035931273273, 0.6453909975828053, 0.6527732410008493, 0.6529039001763899, 0.6584569151368654]
  
  
  
# Validation curve
plt.plot(depth_hyperparams, training_acc, label="Training")
plt.plot(depth_hyperparams, validation_acc, label="validation")
plt.xlabel("Max Depth")
plt.ylabel("Accuracy Score")
plt.title("Validation Curve, Decision Tree Model")
plt.legend();


# build & fit again
final_model_dt = make_pipeline(
    OrdinalEncoder(), 
    DecisionTreeClassifier(max_depth=10, random_state=42)
)
# Fit model to training data
final_model_dt.fit(X, y)    #final_model_dt.fit(X_train, y_train)



#Project - 4 tests
# test type 1
X_test = pd.read_csv("filePath.csv", index_col="b_id")
y_test_pred = pd.Series(final_model_dt.predict(X_test))
y_test_pred[:5]

  # sample output
  0    1
  1    1
  2    1
  3    1
  4    0
  dtype: int64


# test type 2
test_acc = model.score(X_test, y_test)
print("Test Accuracy:", round(test_acc, 2))
  
  # sample output
  Test Accuracy: 0.72
    

# test type 3
acc_train = accuracy_score(y_train, model_lr.predict(X_train))
acc_test = model_lr.score(X_test, y_test)

print("LR Training Accuracy:", acc_train)
print("LR Validation Accuracy:", acc_test)

  # sample output
  LR Training Accuracy: 0.717985042664646
  LR Validation Accuracy: 0.7218817948211109

    
    
#Project - 4 Communicate
# DECISION TREE
features = X_train.columns
importances = <yourModel eg final_model_dt>.named_steps["decisiontreeclassifier"].feature_importances_
feat_imp = pd.Series(importances, index=features).sort_values()
feat_imp.head()

# sample output
plan_configuration        0.004189
land_surface_condition    0.008599
foundation_type           0.009967
position                  0.011795
ground_floor_type         0.013521
dtype: float64


# LOGISTIC REG
features = model_lr.named_steps["onehotencoder"].get_feature_names()
importances = model_lr.named_steps["logisticregression"].coef_[0]
feat_imp = pd.Series(np.exp(importances), index=features).sort_values()
feat_imp.head()

# sample output
superstructure_Brick, cement mortar    0.345719
foundation_type_RC                     0.364478
roof_type_RCC/RB/RBC                   0.415979
ground_floor_type_RC                   0.527756
caste_household_Kumal                  0.543642
dtype: float64



# horizontal bar chart
feat_imp.plot(kind="barh")
plt.xlabel("importance")
plt.ylabel("Label")
plt.title("Feature Importance");
