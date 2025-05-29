# WeightAnalysis.py

if __name__ == "__main__":
    # 2. Import Libraries
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy.stats import pearsonr
    import statsmodels.api as sm
    
    
    # 3. Load the Dataset
    file_path = "dsa_project_data.xlsx"
    
    # Check if the file exists in the current directory
    import os
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found.")
        print("Please ensure the file is in the correct directory or provide the full path.")
        # List files in the current directory to help the user
        print("Files in current directory:", os.listdir())
    else:
        data = pd.read_excel(file_path)
        print("Dataset loaded successfully.")
    
    # 4. Data Cleaning
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    print("Missing values per column:\n", data.isnull().sum())
    data.dropna(inplace=True)
    data['Caloric Deficit'] = data['Burned Calories'] - data['Caloric Intake']
    
    
    # Weight Over Time
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Weight (kg)'], marker='o')
    plt.title('Weight Over Time')
    plt.xlabel('Date')
    plt.ylabel('Weight (kg)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    
    # Caloric Intake vs. Weight
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x='Caloric Intake', y='Weight (kg)', data=data)
    plt.title('Caloric Intake vs. Weight')
    plt.show()
    
    
    # Burned Calories vs. Weight
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x='Burned Calories', y='Weight (kg)', data=data)
    plt.title('Burned Calories vs. Weight')
    plt.show()
    
    
    # Water Consumption vs. Weight
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x='Water Consumption (L)', y='Weight (kg)', data=data)
    plt.title('Water Consumption vs. Weight')
    plt.show()
    
    
    # Caloric Deficit vs. Weight
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x='Caloric Deficit', y='Weight (kg)', data=data)
    plt.title('Caloric Deficit vs. Weight')
    plt.show()
    
    
    # Correlation Matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.show()
    
    
    # Boxplot: Water Consumption vs. Weight
    plt.figure(figsize=(6, 4))
    sns.boxplot(x='Water Consumption (L)', y='Weight (kg)', data=data)
    plt.title('Weight Distribution by Water Consumption Level')
    plt.show()
    
    
    # Caloric Intake vs. Burned Calories Over Time
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Caloric Intake'], marker='o', label='Caloric Intake')
    plt.plot(data['Date'], data['Burned Calories'], marker='s', label='Burned Calories')
    plt.title('Caloric Intake vs Burned Calories Over Time')
    plt.xlabel('Date')
    plt.ylabel('Calories')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    
    # Histograms
    plt.figure(figsize=(6, 4))
    sns.histplot(data['Weight (kg)'], bins=10, kde=True)
    plt.title('Histogram of Weight')
    plt.xlabel('Weight (kg)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
    
    plt.figure(figsize=(6, 4))
    sns.histplot(data['Caloric Intake'], bins=10, kde=True)
    plt.title('Histogram of Caloric Intake')
    plt.xlabel('Calories')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
    
    plt.figure(figsize=(6, 4))
    sns.histplot(data['Burned Calories'], bins=10, kde=True)
    plt.title('Histogram of Burned Calories')
    plt.xlabel('Calories Burned')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
    
    
    # 6. Hypothesis Testing: Caloric Intake vs. Weight
    corr_intake, pval_intake = pearsonr(data['Caloric Intake'], data['Weight (kg)'])
    print(f"Caloric Intake & Weight: r = {corr_intake:.3f}, p = {pval_intake:.4f}")
    if pval_intake < 0.05:
        print("--> Statistically significant.")
    else:
        print("--> Not statistically significant.")
    
    
    # Burned Calories vs. Weight
    corr_burned, pval_burned = pearsonr(data['Burned Calories'], data['Weight (kg)'])
    print(f"Burned Calories & Weight: r = {corr_burned:.3f}, p = {pval_burned:.4f}")
    if pval_burned < 0.05:
        print("--> Statistically significant.")
    else:
        print("--> Not statistically significant.")
    
    
    # Water Consumption vs. Weight
    corr_water, pval_water = pearsonr(data['Water Consumption (L)'], data['Weight (kg)'])
    print(f"Water Consumption & Weight: r = {corr_water:.3f}, p = {pval_water:.4f}")
    if pval_water < 0.05:
        print("--> Statistically significant.")
    else:
        print("--> Not statistically significant.")
    
    
    # Caloric Deficit vs. Weight
    corr_deficit, pval_deficit = pearsonr(data['Caloric Deficit'], data['Weight (kg)'])
    print(f"Caloric Deficit & Weight: r = {corr_deficit:.3f}, p = {pval_deficit:.4f}")
    if pval_deficit < 0.05:
        print("--> Statistically significant.")
    else:
        print("--> Not statistically significant.")
    
    
    # 5.1 Feature & Target
    # The dataset is stored in the variable 'data', not 'df'.
    X = data[["Caloric Intake", "Burned Calories", "Water Consumption (L)", "Caloric Deficit"]]
    y = data["Weight (kg)"]
    
    
    # 5.2 Train–Test Split
    from sklearn.model_selection import train_test_split
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    
    # 5.3 Train models
    from sklearn.linear_model import LinearRegression
    from sklearn.ensemble import RandomForestRegressor
    
    # Linear Regression
    lr = LinearRegression().fit(X_train, y_train)
    y_pred_lr = lr.predict(X_test)
    
    # Random Forest
    rf = RandomForestRegressor(n_estimators=100, random_state=42).fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)
    
    
    # 5.4 Evaluate
    from sklearn.metrics import mean_squared_error, r2_score
    
    def eval_model(name, y_true, y_pred):
        mse = mean_squared_error(y_true, y_pred)
        r2  = r2_score(y_true, y_pred)
        print(f"{name:17s} → MSE: {mse:.3f}, R²: {r2:.3f}")
    
    eval_model("Linear Regression", y_test, y_pred_lr)
    eval_model("Random Forest",    y_test, y_pred_rf)
    
    
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    # Actual vs Predicted for Linear Regression
    plt.figure(figsize=(6,6))
    plt.scatter(y_test, y_pred_lr, alpha=0.7)
    plt.plot([y.min(), y.max()], [y.min(), y.max()], "--", linewidth=2)
    plt.xlabel("Actual Weight (kg)")
    plt.ylabel("Predicted Weight (kg)")
    plt.title("Linear Regression: Actual vs. Predicted")
    plt.tight_layout()
    plt.show()
    
    # Feature importances for Random Forest
    feat_imp = rf.feature_importances_
    sns.barplot(x=feat_imp, y=X.columns)
    plt.title("Random Forest Feature Importances")
    plt.xlabel("Importance")
    plt.tight_layout()
    plt.show()
    
    
    import pandas as pd
    import matplotlib.pyplot as plt
    
    # Ensure 'rf' is defined by running the model training cell before this one.
    # Assuming the cell defining and training rf (step 5.3) has been run:
    feature_names = ["Caloric Intake", "Burned Calories", "Water Consumption (L)", "Caloric Deficit"]
    importances = rf.feature_importances_
    
    importance_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importances
    }).sort_values(by='Importance', ascending=True)
    
    plt.figure(figsize=(8, 5))
    plt.barh(importance_df['Feature'], importance_df['Importance'])
    plt.xlabel("Feature Importance")
    plt.title("Random Forest Feature Importances")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    # Predict on test set
    y_pred = rf.predict(X_test)
    
    # Actual vs Predicted Plot
    plt.figure(figsize=(6, 6))
    plt.scatter(y_test, y_pred, alpha=0.7)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # y=x line
    plt.xlabel("Actual Weight (kg)")
    plt.ylabel("Predicted Weight (kg)")
    plt.title("Actual vs Predicted Weight (Random Forest)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    
    from sklearn.model_selection import cross_val_score
    
    # Perform 5-Fold Cross Validation on Random Forest
    cv_scores = cross_val_score(rf, X, y, cv=5, scoring='r2')
    
    print("Cross-Validation R² Scores:", cv_scores)
    print("Average R² Score:", round(cv_scores.mean(), 3))
