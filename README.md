# S1_Data_Analysis
# Student Performance Data Analysis

## Project Overview

This project analyzes the academic performance of first-year engineering students. The dataset includes grades for several subjects and aims to identify trends, correlations, and provide valuable insights to improve the students' academic outcomes.

### Objective:
- Analyze student performance data.
- Identify correlations between different subjects and the overall performance.
- Visualize and interpret these relationships to improve educational strategies.

---

## Data Description

The dataset contains student marks for the following subjects:

1. **Analysis 1**  
2. **Algebra 1**  
3. **Probability 1**  
4. **Physics 1**  
5. **Chemistry 1**  
6. **Informatics 1**  
7. **Technical Drawing**  
8. **Human Engineering 1**  
9. **General Economics**  
10. **English 1**  
11. **French 1**  
12. **Total S1** (Total score for Semester 1)  
13. **M.G. S1** (Mastery Grade for Semester 1)

---

## Data Preprocessing

1. **Data Cleaning**:
   - Missing values were handled by filling them with the mean value of each respective subject.
   - Numerical columns were normalized by dividing values by 100.
   
2. **Column Renaming**: 
   - French subject names were translated into English for consistency.
   
3. **Outliers Removal**: 
   - Extreme outliers were removed based on certain predefined criteria.

---

## Analysis & Visualizations

### 1. Descriptive Statistics
Descriptive statistics were calculated for each subject, including:
- **Mean**: Average performance in each subject.
- **Standard Deviation**: Spread of the marks for each subject.
- **Min/Max**: Minimum and maximum scores for each subject.

### 2. Correlation Matrix
The correlation matrix was computed using the Pearson correlation coefficient to identify relationships between subjects. The correlation values range from -1 (perfect negative correlation) to +1 (perfect positive correlation), with values closer to 0 indicating weak or no correlation.

### 3. Correlation Heatmap
A heatmap was generated to visually represent the correlation matrix. Strong correlations are represented by darker colors, while weak correlations are lighter.

### 4. Distribution of Marks  
Histograms were plotted for each subject to show the distribution of student marks. These visualizations help us understand the frequency of certain ranges of grades and identify trends in student performance.

---

## Detailed Interpretation of Results

### Correlations with General Average (Total S1)
We analyze the correlation of each subject with the **Total S1** (overall performance) score to determine which subjects most influence a student's overall grade.

#### 1. **Analysis 1**
- **Correlation with Total S1**: **Strong Positive Correlation**
- **Interpretation**: "Analysis 1" has a very strong positive correlation with the general average. This suggests that students who perform well in "Analysis 1" tend to score well overall. This is likely due to the foundational role of analysis skills in many other subjects.

#### 2. **Algebra 1**
- **Correlation with Total S1**: **Strong Positive Correlation**
- **Interpretation**: Like "Analysis 1," "Algebra 1" shows a strong positive correlation with the total score. This suggests that algebra, which involves problem-solving and logical reasoning, is highly predictive of overall academic success.

#### 3. **Probability 1**
- **Correlation with Total S1**: **Moderate Positive Correlation**
- **Interpretation**: "Probability 1" has a moderate positive correlation with the general average. While it is important for understanding statistics and data analysis, students who excel in probability also tend to do well in other subjects, although not as strongly as in "Analysis 1" or "Algebra 1."

#### 4. **Physics 1**
- **Correlation with Total S1**: **Moderate Positive Correlation**
- **Interpretation**: "Physics 1" is moderately correlated with the overall grade. Students who do well in physics tend to have good academic performance, although the correlation is not as strong as that of "Analysis 1" and "Algebra 1." Physics requires a mix of conceptual understanding and applied problem-solving, which may explain its moderate effect on the general average.

#### 5. **Chemistry 1**
- **Correlation with Total S1**: **Weak Positive Correlation**
- **Interpretation**: Chemistry 1 shows a weak positive correlation with the general average. Students performing well in chemistry may not always perform similarly in other subjects, indicating that chemistry skills are not as interconnected with other subjects as "Analysis" or "Algebra."

#### 6. **Informatics 1**
- **Correlation with Total S1**: **Moderate Positive Correlation**
- **Interpretation**: "Informatics 1" has a moderate positive correlation with the total score. It shows a link to other subjects, particularly those involving logical thinking, such as "Technical Drawing" and "Mathematics." Students who excel in informatics generally have a strong overall performance.

#### 7. **Technical Drawing**
- **Correlation with Total S1**: **Weak Positive Correlation**
- **Interpretation**: "Technical Drawing" shows a weak correlation with the general average. While it's important for students pursuing engineering, it does not strongly correlate with performance in other subjects.

#### 8. **Human Engineering 1**
- **Correlation with Total S1**: **Weak Positive Correlation**
- **Interpretation**: "Human Engineering 1" shows a weak correlation with the total grade, suggesting that students' performance in this subject does not significantly affect their overall academic success compared to other subjects.

#### 9. **General Economics**
- **Correlation with Total S1**: **Moderate Positive Correlation**
- **Interpretation**: "General Economics" shows a moderate correlation with overall performance. While it is not as strongly correlated as "Mathematics" or "Physics," students excelling in economics generally perform well in other subjects as well.

#### 10. **English 1**
- **Correlation with Total S1**: **Weak Positive Correlation**
- **Interpretation**: The correlation between "English 1" and the general average is weak, suggesting that students' performance in English is somewhat independent of their overall academic performance.

#### 11. **French 1**
- **Correlation with Total S1**: **Weak Positive Correlation**
- **Interpretation**: Similar to English, "French 1" shows a weak positive correlation with the total score. While language skills are valuable, they do not appear to have as strong an impact on the overall performance compared to subjects like mathematics and physics.

---

## Visual Insights

### 1. **Heatmap of Correlations**
The heatmap visualizes the correlation matrix and highlights the relationships between subjects. The color intensity helps to quickly identify which subjects are most related to each other and to the general average.

- **Strongest correlations**: "Analysis 1" and "Algebra 1" show the strongest positive correlations with "Total S1," indicating their importance in overall performance.
- **Weaker correlations**: Subjects like "Chemistry 1" and "English 1" show weaker correlations with the overall grade, which may suggest that these subjects are not as crucial for determining a student's success across the entire semester.

### 2. **Distribution of Marks**
Histograms for each subject were plotted to show the distribution of student marks. These visualizations reveal the spread of student performance across each subject. For example:
- Subjects like "Analysis 1" and "Algebra 1" show a wider spread of marks, indicating more variability in student performance.
- Subjects like "French 1" and "English 1" show a narrower distribution, indicating more uniformity in student grades.

---

## Conclusions & Recommendations

### Conclusions
- **Highly Correlated Subjects**: "Analysis 1" and "Algebra 1" are the most strongly correlated with the overall grade, suggesting that improvement in these subjects may have a significant positive impact on student performance.
- **Moderate Correlation**: Subjects like "Probability 1," "Physics 1," and "General Economics" show moderate positive correlations with the general average, indicating that strong performance in these areas also contributes to overall success, but not as strongly as in mathematics-related subjects.
- **Weak Correlation**: Subjects like "Chemistry 1," "English 1," and "French 1" have weak correlations with the general grade, meaning performance in these areas does not strongly influence the total score.

### Recommendations
- **Targeted Support for Mathematics**: Given the strong correlation between "Analysis 1" and "Algebra 1" with the overall grade, students struggling in these subjects should receive additional support to improve their academic performance.
- **Focus on Interdisciplinary Learning**: Encouraging interdisciplinary learning, particularly combining mathematics and physics with informatics, could help students excel across multiple subjects.
- **Curriculum Review**: For subjects like "Chemistry 1" and "French 1," which show weaker correlations with the general average, a review of teaching methods and curriculum could ensure that students see more relevance and interconnection with other subjects.

---

This README provides a clear, detailed interpretation of the data analysis, with an emphasis on the correlation between each subject and the general average. It also offers actionable insights and recommendations based on the data.

