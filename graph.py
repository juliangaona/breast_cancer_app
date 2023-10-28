import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import scipy.stats as stats
from sklearn.preprocessing import StandardScaler
import numpy as np
from scipy.stats import f_oneway


df = pd.read_csv('breast_cancer.csv')
df= df.drop("id", axis='columns')

def app():
	st.markdown("# Breast Cancer Data: Exploratory Data Analysis")
	st.write("Here you can explore in detail all features and gather key insights to fight back the breast cáncer.")

	with st.container():
		st.markdown("## Univariate Analysis: Target Variable 'diagnosis' ")
		st.write("Complete Later")
		diagnosis_count = df['diagnosis'].value_counts()
		c1,c2 = st.columns(2)
		with c1:
			
			fig = px.bar(diagnosis_count, x=diagnosis_count.index,y=diagnosis_count,title='Number of Diagnosis Results',color=diagnosis_count.index, color_continuous_scale='reds')
			fig.update_xaxes(title_text="Diagnosis")
			fig.update_yaxes(title_text="Patient Count")

			st.plotly_chart(fig)

		with c2:
			fig = px.pie(diagnosis_count, names=diagnosis_count.index,values=diagnosis_count,title='Number of Diagnosis Results', hole=.3)
			st.plotly_chart(fig)
		
		st.write('There is a high number of patients diagnosed with benignant breast cancer. Only 37.3% of the patients are diagnosed with malignant breast cancer')

		st.markdown("## Data Distribution ")

		st.markdown("#### Let's explore the distribution of all variables. Select the variable that you would like to explore")
		selected_feature = st.selectbox("Choose a feature", df.columns)

		fig = px.histogram(df[selected_feature],color=df['diagnosis'], title="Histogram Plot")
		st.plotly_chart(fig)



		
		try:
			statistic, p_value = stats.shapiro(df[selected_feature])

			alpha = 0.05

			st.markdown("#### Shapiro-Wilk Test Results: Testing Data Normal Distribution")

			# Print the results
			st.write("Shapiro-Wilk Test Statistic:", statistic)
			st.write("p-value:", p_value)


			# Interpret the results
			if p_value > alpha:
			    st.info("Sample looks normally distributed (fail to reject H0)")
			else:
			    st.info("Sample does not look normally distributed (reject H0)")
		except ValueError:
			st.warning('The shapiro test is not appropiated for categorical variables. Try another feature')

		st.markdown("---")
		st.markdown("## Multivariate Analysis: 'All Features ")
		st.markdown("#### Let's	explore	the data distribution of all variables in the same scale")
		st.write("""The graph below has scaled the data for all variables to make a valid comparison of the distributions.

- The violin plot displays the distribution of numerical data and provides insights into its summary statistics, including the median, quartiles, and the shape of the data's probability density.

- Select the variables you would like to compare from the list displayed in the select option.""")




		df_columns=df.loc[:, df.columns != 'diagnosis'].columns.to_list()
		selected_columns=st.multiselect("Select the columns to display: ", df_columns)
		scaler = StandardScaler()
		df_scale=pd.DataFrame(scaler.fit_transform(df.loc[:, df.columns != 'diagnosis']))
		df_scale. columns = df.loc[:, df.columns != 'diagnosis'].columns.tolist()
		df_scale =df_scale.join(df['diagnosis'])
		
		
		if selected_columns:
			fig = px.violin(df_scale[selected_columns],box=True,color=df_scale['diagnosis'], title="Violin Plot")
			fig.update_layout(width=1500, height=700)
			st.plotly_chart(fig)
		else:
			df_num=df_scale

			fig = px.violin(df_scale.loc[:, df_scale.columns != 'diagnosis'],color=df_scale['diagnosis'], title="Violin Plot")
			fig.update_layout(width=1500, height=700)
			st.plotly_chart(fig)

		st.markdown("""Let's interpret the plot above together. In this chart, the dark blue represents benignant cases, and the light blue represents malignant cases.

For instance, when we examine features like `radius_mean`, `texture_mean`, `perimeter_mean`, `area_mean`,`smoothness_mean`, `compactness_mean`, `concavity_mean`, `concave_points_mean`, `symetry_mean`,`radious_se`,`perimeter_se`,`area_se`,`compactness_se`,`concativity_se`, `concave point_se`,`radious_worst`,`texture_worst`,`perimter_worst`,`area_worst`,`smoothness_worst`,`compactness_worst`,`concativity`,`concave points_worst`,`symetry_worst`,`fractal_dimensionm_worst`,we observe that the medians of malignant and benign cases are different. This separation suggests that these features could be valuable for classification tasks.

However, when we shift our attention to features such as `fractal_dimension_mean`, `texture_se`, and `smoothness_se`, and `symmetry_se` the medians of malignant and benign cases do not exhibit clear separation. Consequently, these particular features may not provide substantial information for classification purposes.
""")
		st.markdown("---")
		st.markdown("## Correlation Analysis: 'All Features' ")
		st.markdown("#### Let's	explore	the data correlation of all variables")
		st.write("""CHANGE THE TEXT""")
		df_columns=df.loc[:, df.columns != 'diagnosis'].columns.to_list()
		selected_columns=st.multiselect("Select the columns to display: ", df_columns,key='pairplot')
		selected_columns.append('diagnosis')

		

		if selected_columns:
			try:


				st.markdown("### Pairplot")
				pairplot = sns.pairplot(df[selected_columns],palette = "RdPu", diag_kind="kde", hue='diagnosis')  # Use 'diag_kind' to display density plots on the diagonal
				st.pyplot(pairplot)

				st.markdown("### HeatMap")
				tresh_hold=st.slider('Select the absolute correlation treshold',0.0,1.0,0.1)

				st.markdown("""In this chart, the darker the color the higher the absolute linear correlation between the variables. In this example, I have used a treshold of 0.7 to filter only those high correlation between the features. However, you can play with the slider to find different insights. The lower the treshold the more relations can be found but with less colinearity. 

For instance, most of the `_mean` features are highly correwith features `_worst`. And when you see the scatter plot of this featurs in the pairplot above you can see a linear upward trend for the data. But in the other hand for example we, dont see a strong linear relashionship for thops features `_se` and thos features `_mean`, this can be seen clearly in how the scatter plot doesnt show a linear trean rather the dots seams to be in the same place. 

This could help to decide which features to use in a classification model and which one discard. Remeber that for a classification model we want more variance therefore, we tend to discard on of the highly correlated variables. 

Another interesting insight is that malignat class is positive correlated while benignant class is negatiely correlated with the same features: `radius_mean`,`perimeter_mean`, `area_mean`, `concave_points_mean`, `radius_worst`,`perimeter_worst`,`area_worst`,`concave_points_worts`. And as mention before the mean and wors features are the same as those are highly correlated with each other.
		""")
				df_dummies = pd.get_dummies(df['diagnosis'])
				
				#del df_dummies[df_dummies.columns[-1]]
				df_new = pd.concat([df, df_dummies], axis=1)
				del df_new['diagnosis']
				corr_matrix = df_new.corr()
				corr_matrix[np.abs(corr_matrix)<tresh_hold] = np.nan
				mask = np.zeros_like(corr_matrix, dtype=np.bool)
				mask[np.triu_indices_from(mask)] = True
				#matrix = np.triu(corr_matrix)

				# Create a correlation heatmap using Seaborn and Matplotlib

				fig, ax = plt.subplots(figsize=(12,12))
				sns.heatmap(corr_matrix,cmap="RdPu", vmin=-1,vmax=1,fmt=".2f",ax=ax,mask=mask)
				
				st.write(fig)
			except ValueError:
				st.warning('Select at least TWO features')

			try:
				
				st.markdown("### Statistical Test Correlation w/ Target Variable")
				selected_feature = st.selectbox("Choose a feature", df.columns,key='anova')
				CategoryGroupLists=df.groupby('diagnosis')[selected_feature].apply(list)
				 
				# Performing the ANOVA test
				# We accept the Assumption(H0) only when P-Value &gt; 0.05
				AnovaResults = f_oneway(*CategoryGroupLists)
				st.write('Assumption(H0) is that the selected feature is NOT correlated with `diagnosis`')
				st.write('P-Value for Anova is: ', AnovaResults[1])

				alpha_anova = 0.05

					# Interpret the results
				if AnovaResults[1] > alpha_anova:
				    st.info("The feature selected is NOT correlated with the target variable `diagnosis` (fail to reject H0)")
				else:
				    st.info("The feature selected IS correlated with the target variable `diagnosis` (reject H0)")
			except	ValueError:
				st.warning('Select a non cathegorical feature')


			try:
				st.subheader('Scatter Plot with Color-Coded Dots')
				x_column = st.selectbox("Select X-axis column", df.columns)
				y_column = st.selectbox("Select Y-axis column", df.columns)
				target_column = 'diagnosis'

				# Get unique target categories for coloring
				categories = df[target_column].unique()
				pink_palette = ['deeppink','pink']

				fig, ax = plt.subplots(figsize=(10, 6))
				for i,category in enumerate(categories):
					subset = df[df[target_column] == category]
					ax.scatter(subset[x_column], subset[y_column], label=category, alpha=0.7,c=pink_palette[i])

				ax.set_xlabel(x_column)
				ax.set_ylabel(y_column)
				ax.set_title(f'{x_column} vs. {y_column}')
				plt.legend()
				st.pyplot(fig)
			except	ValueError:
				st.warning('Select a non cathegorical feature')





			





		


