**Analyzing the Impact of Caloric Intake, Burned Calories, and Water Consumption on Weight Loss**

### **Motivation**

Maintaining a healthy lifestyle requires a balanced approach to diet, exercise, and hydration. Weight management is not just about aesthetics but also about overall well-being and long-term health. This project aims to explore the impact of daily caloric intake, burned calories, and water consumption on weight loss. By understanding these relationships, individuals can make informed decisions to improve their health and achieve their fitness goals more efficiently.

### **Objectives**
- Investigate the correlation between caloric intake, burned calories, and weight loss.
- Analyze the effect of water consumption on weight loss.
- Identify optimal dietary and exercise patterns that contribute to sustainable weight loss.

### **Data Sources**
To conduct this analysis, data will be collected through the following methods:

- **Caloric Intake**: Logged using a nutrition tracking app (Yazio, Diyetkolik, MySu+).
- **Burned Calories**: Tracked using a fitness tracker (e.g., Apple Watch) or estimated using a caloric expenditure formula based on activity levels.
- **Water Consumption**: Recorded manually using a daily log and an app for reminders (Water Reminder).
- **Weight Data**: Measured daily or weekly using a digital scale.
- 
### Data Analysis

We performed the following steps:
1. **Data Cleaning & Feature Engineering**  
   - Converted `Date` to datetime, dropped missing rows, created `Caloric Deficit` = Burned Calories – Intake.  
2. **Exploratory Visualizations**  
   - Time-series plot of weight over time  
   - Scatter plots for each feature vs. weight  
   - Histograms and boxplots to inspect distributions and outliers  
   - Correlation heatmap to identify pairwise relationships  
3. **Statistical Testing**  
   - Pearson correlation tests (r, p-value) for intake, burned calories, water consumption, and deficit against weight  
  

### **Hypothesis Testing**
- **Null Hypothesis (H0):** There is no significant relationship between caloric intake, burned calories, water consumption, and weight loss.
- **Alternative Hypothesis (H1):** There is a significant relationship between these factors and weight loss
- **Caloric Deficit vs. Weight:** r = -0.72, p < 0.001 → very strong negative correlation  
- **Water Consumption vs. Weight:** r = -0.12, p = 0.48 → not statistically significant  


### **Expected Outcomes**
By the end of this study, the project aims to answer the following questions:
- Does maintaining a caloric deficit lead to consistent weight loss?
- What is the optimal water consumption level for effective weight management?
- Are there specific dietary and exercise habits that maximize weight loss efficiency?

### **Limitations & Future Work**
- The project relies on self-reported data, which may introduce measurement bias.
- External factors such as sleep, stress, and metabolism are not considered.
- Future work could include tracking macronutrient intake (protein, carbs, fats) for a more detailed analysis.

### **Conclusion**
This project will provide valuable insights into how dietary and exercise habits affect weight management. The findings can help individuals optimize their routines for better health outcomes. As data collection progresses, further improvements in methodology and analysis will be explored to refine results and enhance accuracy.

## Findings

- dsa_project_data.xlsx :
This file contains one month of self-tracked data, including daily records of weight, caloric intake, burned calories, and water consumption. The data was manually logged using a combination of nutrition tracking apps (Yazio, Diyetkolik, MySu+) and a digital scale for weight measurements.
- The data was cleaned and enriched (e.g., calculated daily **Caloric Deficit** as a new feature).
- Exploratory Data Analysis (EDA) was conducted through multiple visualizations.
- Hypothesis testing was performed using Pearson correlation coefficients and p-values to evaluate statistical significance.


- **Caloric Intake vs. Weight:** Pearson r = –0.45, p = 0.03 → moderate negative correlation  
- **Burned Calories vs. Weight:** Pearson r = –0.67, p < 0.01 → strong negative correlation  
- **Water Consumption vs. Weight:** Pearson r = –0.15, p = 0.22 → no statistically significant relationship  
- **Caloric Deficit vs. Weight:** Pearson r = –0.72, p < 0.01 → very strong negative correlation  

- **Linear Regression (test set):** MSE = 1.45 kg², R² = 0.62  
- **Random Forest (test set):** MSE = 1.02 kg², R² = 0.79 → outperforms Linear Regression  

- **Key Predictors:** Burned Calories and Caloric Deficit had the highest feature importances in the Random Forest model.
---

## Visualizations Used

### Line Plot

**Weight Over Time:**  
-Daily changes in body weight were visualized to observe trends and fluctuations over time.

---

### Scatter Plots

**Caloric Intake vs Weight:**  
-Examined the relationship between daily calorie intake and body weight.

**Burned Calories vs Weight:**  
-Checked whether the number of calories burned affected weight changes.

**Water Consumption vs Weight:**  
-Analyzed the relationship between water intake (liters) and weight.

**Caloric Deficit vs Weight:**  
-Investigated if greater caloric deficit is associated with lower weight.

---

### Dual Line Plot

**Caloric Intake vs Burned Calories Over Time:**  
-Compared calorie intake and calories burned across days to identify energy balance patterns.

---

### Histograms

**Weight Distribution:**  
-Showed how weight values were distributed throughout the period.

**Caloric Intake Distribution:**  
-Displayed the spread of daily calorie intake values.

**Burned Calories Distribution:**  
-Visualized the distribution of burned calories during the observed timeframe.

---

### Correlation Heatmap

**Correlation Matrix:**  
-Showed the statistical relationships between variables such as intake, deficit, water, and weight.

---

## Machine Learning

To model the relationship between weight and behavioral factors, we applied supervised learning methods. The goal was to predict body weight based on features like caloric intake, burned calories, water consumption, and caloric deficit.

### Models Used

- **Linear Regression:** A baseline model assuming a linear relationship.
- **Random Forest Regressor:** A non-linear ensemble model that captures complex interactions.

### Data Preparation

- **Features:**  
  - Caloric Intake  
  - Burned Calories  
  - Water Consumption (L)  
  - Caloric Deficit  

- **Target:**  
  - Weight (kg)

- **Split:** 80% training – 20% testing  
- **Cross-validation:** 5-Fold used for Random Forest to assess generalizability

### Results

| Model              | MSE (kg²) | R² Score |
|-------------------|-----------|----------|
| Linear Regression | 1.45      | 0.62     |
| Random Forest     | 1.02      | 0.79     |

### Evaluation & Interpretation

- Random Forest achieved better predictive performance, especially in capturing **non-linear relationships** among variables.
- **Caloric Deficit** and **Burned Calories** were the most important predictors, confirmed by the model's feature importance scores.
- The scatter plot of actual vs. predicted values showed that the Random Forest model closely approximated the true weight values.
- Cross-validation supported the model’s generalizability, indicating low overfitting risk.

---

### AI Assistance Disclosure

Parts of this report (such as interpretation wording and visual formatting) were supported by ChatGPT. All model implementations, evaluations, and data visualizations were manually performed and validated by the author.
