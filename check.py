import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('PV - 1CP - S1.csv', skip_blank_lines=True)
df = df.apply(pd.to_numeric, errors='coerce')
df = df.drop(columns=["Nom","Prénom" , "Doublant","Matricule","Unnamed: 3", "Unnamed: 5", "Unnamed: 19"])
df = df.dropna(axis=0, how='all')
df = df / 100
#print(df.dtypes)
print("Current row count:", df.shape[0])  # After cleaning
# Get descriptive stats
summary = df.describe()
print(df.columns)
# Print for specific subjects
print(summary.loc[['mean', '50%', 'std', 'min', 'max']])

cols_to_convert = ['Analyse 1', 'Algèbre 1', 'Proba 1', 'Physique 1', 'Chimie 1', 'Informatique 1', 'Dessin technique', 'Ingénierie humaine 1', 'Economie générale', 'Anglais 1', 'Français 1', 'M.G. S1']
low_performance_subjects = summary.loc['mean', :][summary.loc['mean', :] < 10]
print(low_performance_subjects)
top_performers = df[df[cols_to_convert].max(axis=1) > 18]
print(top_performers)
correlation_matrix = df[cols_to_convert].corr()
print(correlation_matrix)
 # Dictionary mapping old column names to new column names
column_name_mapping = {
    'Analyse 1': 'Analysis 1',
    'Algèbre 1': 'Algebra 1',
    'Proba 1': 'Probability 1',
    'Physique 1': 'Physics 1',
    'Chimie 1': 'Chemistry 1',
    'Informatique 1': 'Computer Science 1',
    'Dessin technique': 'Technical Drawing',
    'Ingénierie humaine 1': 'Human Engineering 1',
    'Economie générale': 'General Economics',
    'Anglais 1': 'English 1',
    'Français 1': 'French 1',
    'TOTAL S1': 'S1 Total',
    'M.G. S1': 'S1 General Average'
}

df.rename(columns=column_name_mapping, inplace=True)



sns.set_theme(style="whitegrid", palette="muted")

subjects = ['Analysis 1', 'Algebra 1', 'Probability 1', 'Physics 1', 'Chemistry 1', 
            'Computer Science 1', 'Technical Drawing', 'Human Engineering 1', 
            'General Economics', 'English 1', 'French 1', 'S1 Total', 'S1 General Average']

for subject in subjects:
    if subject in df.columns:  # Check if subject exists in the columns
        plt.figure(figsize=(10, 6))  # Adjust the size of the plot for better clarity
        sns.histplot(df[subject], kde=True, color="royalblue", bins=15, stat="density", linewidth=1.5)
        
        # Adding titles and labels with larger font sizes
        plt.title(f'Distribution of {subject} Grades', fontsize=16, fontweight='bold')
        plt.xlabel('Grade', fontsize=14)
        plt.ylabel('Density', fontsize=14)
        
        plt.grid(True, linestyle='--', alpha=0.7)
        
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        
        plt.tight_layout()  # Adjust layout for better fit
        plt.savefig(f"{subject.replace(' ', '_')}_distribution.png")
    else:
        print(f"Warning: '{subject}' is not a valid column in the DataFrame.")

correlation_matrix = df.corr()

plt.figure(figsize=(12, 8))

sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", center=0, linewidths=0.5, vmin=-1, vmax=1)

plt.title('Correlation Matrix of Subject Grades', fontsize=16, fontweight='bold')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)


plt.tight_layout()
plt.savefig("correlation_matrix.png")


correlation_matrix = df.corr()

plt.figure(figsize=(14, 10))

sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="RdYlBu_r", center=0, 
            linewidths=0.8, linecolor='white', vmin=-1, vmax=1, 
            annot_kws={"size": 12, "weight": 'bold', "color": 'black'}, 
            cbar_kws={'shrink': 0.8, 'aspect': 10, 'label': 'Correlation Coefficient'})
plt.title('Correlation Matrix of Subject Grades', fontsize=18, fontweight='bold')
plt.xticks(fontsize=14, rotation=45, ha='right')
plt.yticks(fontsize=14, rotation=0)

plt.tight_layout()

plt.show()

