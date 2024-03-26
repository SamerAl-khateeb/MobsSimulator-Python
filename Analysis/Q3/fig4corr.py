# fig4corr.py         By: Samer Al-khateeb

# This code is a modified version of this code 
# https://www.statology.org/correlation-in-python/
# To run this code you need to install the following dependencies:
# For Mac users type:
#    pip install numpy
#    pip install scipy
#    pip install pandas
#    pip install matplotlib
#    pip install seaborn

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
csvFileName = 'fig4.csv'
csvFileContentAsDataFrame = (pd.read_csv(csvFileName))

array1 = csvFileContentAsDataFrame['MobParticipationRate']
array2 = csvFileContentAsDataFrame['AvgMobbersTimeToSayYes']
array3 = csvFileContentAsDataFrame['AvgMobbersTimeToSayNo']
array4 = csvFileContentAsDataFrame['AvgMobbersTimeToRespond']

# Spearman's rho
spearManCorrelationValue, spearManPValue = spearmanr(array1, array2)   
print("The SpearMan correlation coefficient is:", spearManCorrelationValue)
print("The p-value is:", spearManPValue)
print()
spearManCorrelationValue, spearManPValue = spearmanr(array1, array3)   
print("The SpearMan correlation coefficient is:", spearManCorrelationValue)
print("The p-value is:", spearManPValue)

print()
spearManCorrelationValue, spearManPValue = spearmanr(array1, array4)   
print("The SpearMan correlation coefficient is:", spearManCorrelationValue)
print("The p-value is:", spearManPValue)


#determininig pairwise correlation
#pearsonCorrelationMatrix = csvFileContentAsDataFrame.corr(method='pearson')
spearmanCorrelationMatrix = csvFileContentAsDataFrame.corr(method='spearman')

#print(pearsonCorrelationMatrix)
print(spearmanCorrelationMatrix)

fig = plt.figure()
fig.set_figwidth(20)
plt.subplots_adjust(bottom=0.25)

matrix2 = np.triu(spearmanCorrelationMatrix)
matrix2[np.diag_indices_from(matrix2)] = False
heatmap2 = sns.heatmap(spearmanCorrelationMatrix, vmin=-1, vmax=1, annot=True, cmap='Blues', mask=matrix2, annot_kws={"size": 18})
# Increase the label size
heatmap2.tick_params(axis='both', which='major', labelsize=12)
heatmap2.tick_params(axis='x', rotation=90)
heatmap2.tick_params(axis='y', rotation=0)  # No rotation for y-axis labels

# Give a title to the heatmap. Pad defines the distance of the title from the top of the heatmap.
#heatmap2.set_title('The Spearman Correlation Between Mobs Participation Rate and Average Mobbers Response Time (in Minutes) ', fontdict={'fontsize':12}, pad=12)
plt.show()
#to save the correlaiton matrix as a csv file
pd.DataFrame(spearmanCorrelationMatrix).to_csv("SpearmanCorrelationOutput.csv")


