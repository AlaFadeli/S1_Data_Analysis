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




sns.set_theme(style="white", palette="muted")

subjects = ['Analysis 1', 'Algebra 1', 'Probability 1', 'Physics 1', 'Chemistry 1', 
            'Computer Science 1', 'Technical Drawing', 'Human Engineering 1', 
            'General Economics', 'English 1', 'French 1', 'S1 Total', 'S1 General Average']

for subject in subjects:
    if subject in df.columns:
        plt.figure(figsize=(12, 6))
        sns.histplot(df[subject], kde=True, color="dodgerblue", bins=20, stat="density", 
                     linewidth=1.7, edgecolor='black', alpha=0.8)
        
        mean_val = df[subject].mean()
        median_val = df[subject].median()
        
        plt.axvline(mean_val, color="orange", linestyle="--", label=f'Mean: {mean_val:.2f}')
        plt.axvline(median_val, color="green", linestyle="--", label=f'Median: {median_val:.2f}')
        
        plt.title(f'Distribution of {subject} Grades', fontsize=18, fontweight='bold', color="darkslategray")
        plt.xlabel('Grade', fontsize=14)
        plt.ylabel('Density', fontsize=14)
        
        plt.grid(True, linestyle='--', alpha=0.3)
        
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        
        plt.legend(title='Statistics', loc='upper right', fontsize=12, title_fontsize=14, frameon=False)
        
        plt.tight_layout()
        
        plt.savefig(f"{subject.replace(' ', '_').lower()}_distribution_modern.png")
#        plt.show()
    else:
        print(f"Warning: '{subject}' is not a valid column in the DataFrame.")

sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="RdYlBu_r", center=0, 
            linewidths=0.8, linecolor='white', vmin=-1, vmax=1, 
            annot_kws={"size": 12, "weight": 'bold', "color": 'black'}, 
            cbar_kws={'shrink': 0.8, 'aspect': 10, 'label': 'Correlation Coefficient'})
plt.title('Correlation Matrix of Subject Grades', fontsize=18, fontweight='bold')
plt.xticks(fontsize=14, rotation=45, ha='right')
plt.yticks(fontsize=14, rotation=0)

plt.tight_layout()

#plt.show()

plt.figure(figsize=(10, 6))

sns.regplot(
    x='Physics 1', y='S1 General Average', data=df,
    scatter_kws={'s': 100, 'color': '#4C72B0', 'edgecolor': 'black', 'alpha': 0.7}, 
    line_kws={'color': '#D65F5F', 'lw': 2, 'ls': '--', 'alpha': 0.8},
    ci=None, robust=True
)

plt.title('Physics 1 vs S1 General Average', fontsize=18, fontweight='bold', color='#333333')
plt.xlabel('Physics 1 Marks', fontsize=14, color='#555555')
plt.ylabel('S1 General Average', fontsize=14, color='#555555')

plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(fontsize=12, color='#555555')
plt.yticks(fontsize=12, color='#555555')

plt.tight_layout()
plt.savefig("Physics_Vs_Average.png")
plt.show()

