# correlationAnalysis.py         By: Samer Al-khateeb

# code is a modified version of this code 
# https://www.statology.org/correlation-in-python/
# To run this code you need to install the following dependencies:
# For Mac users type:
#    pip install numpy
#    pip install scipy
#    pip install pandas
#    pip install matplotlib
#    pip install seaborn

# very important tutorial and explanation 
# https://realpython.com/numpy-scipy-pandas-correlation-python/

# for correlation analysis
import numpy as np

# for calculating the p-value
from scipy.stats.stats import pearsonr
from scipy.stats.stats import spearmanr
from scipy.stats.stats import kendalltau
from scipy.stats.stats import linregress

# to work with pandas data frame, i.e., when we have multiple columns
import pandas as pd

#to make graphs
import seaborn as sns
import matplotlib.pyplot as plt 

#converting the csv content into a dataframe
#csvFileName = 'fig2.csv'
# Specify the columns you want to read
#columns_to_keep = ['Threshold', 'Act', 'Withdraw', 'Power_Exchange', 'Act_Against', 'Participation_Rate']
#csvFileContentAsDataFrame = pd.read_csv(csvFileName, usecols=columns_to_keep)

csvFileName = 'fig3.csv'
csvFileContentAsDataFrame = pd.read_csv(csvFileName)


# The value of the Pearson correlation coefficient 
# ranges between -1 to +1. If it is near -1, there 
# is a strong negative linear relationship between 
# variables. If it is 0, there is no linear relation, 
# and at +1, there is a strong relationship between variables.

# p value: It is the probability significance value. It checks 
# whether to accept or reject the null hypothesis.
# The null hypothesis means that there is no relationship between 
# variables under consideration.

#determininig pairwise correlation
pearsonCorrelationMatrix = csvFileContentAsDataFrame.corr(method='pearson')
print(pearsonCorrelationMatrix)

# figure refrence https://medium.com/@szabo.bibor/how-to-create-a-seaborn-correlation-heatmap-in-python-834c0686b88e
fig = plt.figure()
fig.set_figwidth(20)
#plt.subplots_adjust(top=0.10)
plt.subplots_adjust(bottom=0.40)
plt.subplots_adjust(left=0.25)
#plt.subplots_adjust(right=0.10)

# Store heatmap object in a variable to easily access it when you want to include more features 
# (such as title). Set the range of values to be displayed on the colormap from -1 to 1, and set 
# the annotation to True to display the correlation values on the heatmap. for the heatmap 
# colors check this URL https://matplotlib.org/3.5.1/tutorials/colors/colormaps.html
matrix = np.triu(pearsonCorrelationMatrix)
matrix[np.diag_indices_from(matrix)] = False
heatmap = sns.heatmap(pearsonCorrelationMatrix, vmin=-1, vmax=1, annot=True, cmap='Blues', mask=matrix, annot_kws={"size": 18})

# Format the labels
#heatmap.tick_params(axis='both', which='major', labelsize=15)

heatmap.tick_params(axis='x', rotation=90)
#heatmap.tick_params(axis='y', rotation=90)
heatmap.tick_params(axis='both', which='major', labelsize=15)

# Give a title to the heatmap. Pad defines the distance of the title from the top of the heatmap.
#heatmap.set_title('Title goes here', fontdict={'fontsize':12}, pad=12)
plt.show()





#to save the correlaiton matrix as a csv file
pd.DataFrame(pearsonCorrelationMatrix).to_csv("PearsonCorrelationOutput.csv")

# Create an empty DataFrame to store p-values
p_values = pd.DataFrame(columns=pearsonCorrelationMatrix.columns, index=pearsonCorrelationMatrix.columns)

# Calculate p-values
for col1 in pearsonCorrelationMatrix.columns:
    for col2 in pearsonCorrelationMatrix.columns:
        pearson_corr, p_value = pearsonr(csvFileContentAsDataFrame[col1], csvFileContentAsDataFrame[col2])
        p_values.at[col1, col2] = p_value

#to save the p-values matrix as a csv file
pd.DataFrame(p_values).to_csv("PearsonCorrelation_p-values.csv")

# Display correlation matrix with p-values
print("Pearson correlation coefficients:")
print(pearsonCorrelationMatrix)
print("\nP-values:")
print(p_values)