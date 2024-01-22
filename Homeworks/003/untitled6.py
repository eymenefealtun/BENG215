#Importing libraries
#I used Pandas for data analysis, NumPy for mathematical calculations, and Matplotlib for plotting graphs.
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#Reading data
#The data is read from the file using the pd.read_csv function. The sep='\t' indicates that the data is in tabular (TSV) format, and index_col=0 uses the first column as the index.
file_path = "TFbinding-HW3-F23.txt"
data = pd.read_csv(file_path, sep='\t', index_col=0)
#Exploring data
TF_names = data.columns[:-1]
expression_levels = data['Expression Level']
#Statistical Analysis
#The mean and standard deviation of the 'Expression Level' column are calculated.
expression_mean = expression_levels.mean()
expression_std = expression_levels.std()

#Calculatin Total Binding Scores
data['Total Binding Score'] = data[TF_names].sum(axis=1)
total_binding_mean = data['Total Binding Score'].mean()
total_binding_std = data['Total Binding Score'].std()
#Two subplots are created for drawing histograms.
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12,6))


#Drawing histograms
#Expression Levels (First subplot)
axes[0].set_ylabel('Frequency')
axes[0].set_xlabel('Expression Level')
axes[0].set_title('Histogram of Expression Levels' )
axes[0].hist(expression_levels,color='lightcoral', edgecolor='black', bins=12)  #This line plots a histogram of the 'Expression Level' column on the first subplot.

axes[0].axvline(expression_mean, color='green', linestyle='dashed', linewidth=3, label=f'Mean: {expression_mean:.2f}')
axes[0].axvline(expression_mean + expression_std, color='red', linestyle='dashed', linewidth=3, label=f'Std: {expression_std:.2f}')
axes[0].legend()
#These lines add vertical lines representing the mean and mean + std to the first subplot.

#Total Binding Scores (second subplot)
axes[1].set_ylabel('Frequency')
axes[1].set_xlabel('Total Binding Score')
axes[1].set_title('Histogram of Total Binding Scores')
axes[1].hist(data['Total Binding Score'], color='skyblue', edgecolor="black",bins=12)  ##This line plots a histogram of the 'Total Binding Score' column on the second subplot.

#Lines representing the mean and standard deviation are added to the histogram.
axes[1].axvline(total_binding_mean, color='green', linestyle='dashed', linewidth=3, label=f'Mean: {total_binding_mean:.2f}')
axes[1].axvline(total_binding_mean + total_binding_std, color='red', linestyle='dashed', linewidth=3, label=f'Std: {total_binding_std:.2f}')
axes[1].legend()

#Linear regression model
X = data['Total Binding Score'].values.reshape(-1, 1)
y = expression_levels.values
#Calculating the coefficients of the linear regression model.
beta_1 = np.cov(X.flatten(), y)[0, 1] / np.var(X.flatten())
beta_0 = np.mean(y) - beta_1 * np.mean(X.flatten())
#Making predictions and calculating errors
predictions = beta_0 + beta_1 * X.flatten()
residuals = y - predictions

#Creating new chart
fig, ax = plt.subplots(figsize=(10, 6))
#Plotting a graph containing actual expression values, regression line, and errors.
ax.scatter(X, y, label='True Expression Values', color='green', marker='.')
ax.plot(X, predictions, label='Linear Regression Line', color='blue', linewidth=2)
ax.scatter(X, residuals, label='Residuals', color='red', marker='*', alpha=1)
ax.axhline(0, color='black', linestyle='--', linewidth=0.8, alpha=1)
ax.legend()
ax.set_xlabel('Total Binding Scores')
ax.set_ylabel('Expression Levels')
ax.set_title('Linear Regression Results')
ax.legend()
ax.set_xlabel('Total Binding Scores')
ax.set_ylabel('Expression Levels')
ax.set_title('Linear Regression Results')
ax.legend()
ax.set_xlabel('Total Binding Scores')
ax.set_ylabel('Expression Levels')
ax.set_title('Linear Regression Results')

plt.show()