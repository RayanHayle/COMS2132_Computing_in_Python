# Personal Project

Step 1: Gather Data:
---------------------
- Collect historical economic data such as unemployment rates, GDP, or any economic indicators that can represent growth and recession.
- You could use public datasets like unemployment rates, GDP, or inflation.
- Use Pandas to load the CSV or Excel file.


Step 2: Analyze Data:
---------------------

- Find the overall average of the data to determine what qualifies as "growth" or "recession."
- Mark years as either “Recession” or “Growth” based on this comparison.

Step 3: Visualizations
---------------------
- Use Matplotlib or Plotly to generate graphs based on the data.
- Visualize the unemployment rates or GDP, marking years of recession and growth.

Step 4: Train a Machine Learning Model
---------------------

- Step 1: Train a Decision Tree Classifier:

- Use Scikit-learn to train a decision tree model using the economic data to predict whether future years will be in growth or recession.

Step 5: User input
---------------------

- Allow the user to input a starting year and predict the economic status for the next 5 years based on the trained model.

Example
--------
In file main.py: 
Train module called decision tree  on the data
Allow user to input year:
Input Year: 2003
Prediction for 2004-2008: 
2004: Growth
2005: Growth
2006: Recession
2007: Recession
2008: Growth
