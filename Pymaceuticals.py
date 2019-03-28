#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '../../Downloads'))
	print(os.getcwd())
except:
	pass

#%%
# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


#%%
# Read CSV
trial_csv = pd.read_csv("Resources/clinicaltrial_data.csv")
drug_csv = pd.read_csv("Resources/mouse_drug_data.csv")


#%%
combine_data = trial_csv.merge(drug_csv,on='Mouse ID',how='outer')
combine_data.head()


#%%
group_drug = combine_data.groupby(['Drug','Timepoint']).mean()['Tumor Volume (mm3)']
group_drug_df = pd.DataFrame(group_drug)
group_drug_df.head()


#%%
#why this one works and _df does not work?
#sem = standard error of mean. reliability of data. this case 89%
group_drug_df['Sem'] = group_drug.sem(axis=None,skipna=None,level=None, ddof=1, numeric_only=None)
group_drug_df.sort_values(['Tumor Volume (mm3)'],ascending=True).head()


#%%
group_drug_pivot = group_drug_df.pivot_table(values='Tumor Volume (mm3)',index='Timepoint', columns='Drug')
group_drug_pivot


#%%
group_drug_sem = group_drug_df.pivot_table(index='Timepoint',columns='Drug',values='Sem')  
group_drug_sem


#%%
plt.errorbar(group_drug_pivot.index, group_drug_pivot['Capomulin'], yerr=group_drug_sem['Capomulin'],
             color='r', marker='o', markersize=5, linestyle='--', linewidth=0.5)

plt.errorbar(group_drug_pivot.index, group_drug_pivot['Infubinol'], yerr=group_drug_sem['Infubinol'],
             color='b', marker='o', markersize=5, linestyle='--', linewidth=0.5)

plt.errorbar(group_drug_pivot.index, group_drug_pivot['Ketapril'], yerr=group_drug_sem['Ketapril'],
             color='g', marker='o', markersize=5, linestyle='--', linewidth=0.5)

plt.errorbar(group_drug_pivot.index, group_drug_pivot['Placebo'], yerr=group_drug_sem['Placebo'],
             color='black', marker='o', markersize=5, linestyle='--', linewidth=0.5)

x_lim = len(group_drug_sem.index)
# Chart title
plt.title("Tumor Response to Treatment")
# x label
plt.xlabel("Time (Days)")
# y label
plt.ylabel("Tumor Volume (mm3)")
# legend 
plt.legend(loc='upper left')
plt.show()


#%%
Met_data = combine_data.groupby(['Drug','Timepoint']).mean()['Metastatic Sites']
Met_data_df = pd.DataFrame(Met_data)
Met_data_df.head()


#%%
Met_data_df['Sem'] = Met_data.sem(axis=None,skipna=None,level=None, ddof=1, numeric_only=None)
Met_data_df.head()


#%%
Meta_data_pivot = Met_data_df.pivot_table(values='Metastatic Sites',index='Timepoint', columns='Drug')
Meta_data_pivot


#%%
Mouse_data = combine_data.groupby(['Drug','Timepoint']).count()['Mouse ID']
Mouse_data_df = pd.DataFrame(Mouse_data)
Mouse_data_df.head()


#%%
Mouse_data_pivot = Mouse_data_df.pivot_table(values='Mouse ID',index='Timepoint', columns='Drug')
Mouse_data_pivot


#%%
# Create scatter plot to show the survival rate of mice through the course of treatment
plt.errorbar(Mouse_data_pivot.index, Mouse_data_pivot['Capomulin'], 
             color='r', marker='o', markersize=5, linestyle='--', linewidth=0.5)

plt.errorbar(Mouse_data_pivot.index, Mouse_data_pivot['Infubinol'], 
             color='b', marker='o', markersize=5, linestyle='--', linewidth=0.5)

plt.errorbar(Mouse_data_pivot.index, Mouse_data_pivot['Ketapril'], 
             color='g', marker='o', markersize=5, linestyle='--', linewidth=0.5)

plt.errorbar(Mouse_data_pivot.index, Mouse_data_pivot['Placebo'], 
             color='black', marker='o', markersize=5, linestyle='--', linewidth=0.5)

# Chart title
plt.title("Survival During Treatment")
# x label
plt.xlabel("Treatment Duration (Days)")
# y label
plt.ylabel("Survival Rate (%)")
# legend 
plt.legend(loc='upper right')
plt.show()


#%%
drug_max = combine_data.groupby(['Drug']).max()['Tumor Volume (mm3)']
drug_min = combine_data.groupby(['Drug']).max()['Tumor Volume (mm3)']
drug_change = (drug_max - drug_min) / drug_min
drug_change


#%%
tumor_volume_change_percentage =  ((group_drug_pivot.iloc[-1]-group_drug_pivot.iloc[0])/group_drug_pivot.iloc[0]) * 100
tumor_volume_change_percentage


#%%
tumor_volume_change_percentage.index


#%%
tumor_volume_change_percentage.values


#%%
x_axis = np.arange(len(tumor_volume_change_percentage.values))
x_axis


#%%
# Create a bar chart based upon the above data
plt.bar(x_axis, tumor_volume_change_percentage.values, color="r", align="edge")
# Create the ticks for our bar chart's x axis
tick_locations = [value+0.4 for value in x_axis]
plt.xticks(tick_locations, tumor_volume_change_percentage.index)
# Set the limits of the x axis
plt.xlim(0, len(x_axis))
# make clean x labels
plt.tight_layout()
# Give the chart a title, x label, and y label
plt.title("Tumor Change Over 45 Day Treatment")
plt.xlabel("Drugs")
plt.ylabel("% Tumor Volume Change")
# Save an image of the chart and print it to the screen
plt.savefig("% Tumor Volume Change")
plt.show()


#%%
# Save an image of the chart and print it to the screen
plt.savefig("% Tumor Volume Change")
plt.show()


