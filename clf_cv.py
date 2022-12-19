import libraries

# # classifier
clf = make_pipeline(SimpleImputer(), RandomForestClassifier(random_state=42))

# cross validation
cv_scores = cross_val_score(clf, X_train_over, y_train_over, cv=5, n_jobs=-1)
print(cv_scores)

class_report = classification_report(y_test, model.predict(X_test))
print(class_report)
