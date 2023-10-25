import streamlit as st
import pandas as pd

def app():
	st.header("Breast Cancer Data Structure")
	st.write("Here you can explore a sample of the breast cancer dataset. Feel free to play with this data and learn more about breast cancer.")
	

	df = pd.read_csv('breast_cancer.csv')
	columns_list = df.columns.to_list()
	num_row,num_col=df.shape
	data_types=df.dtypes
	cat_col=df.select_dtypes(exclude="number").columns.to_list()
	numerical_col=df.select_dtypes(include="number").columns.to_list()

	
	st.write("The breast cancer data set contains columns: ",num_col," and rows:",num_row)
	st.write("Target variable: ",cat_col[0])

	with st.container():
		with st.expander("Show all features"):
			st.json(data_types.to_dict())
		with st.expander("Show all numerical features"):
			st.write(numerical_col)
		with st.expander("Show all catergorical features"):
			st.write(cat_col[0])

	with st.container():
		st.subheader("Dataset Sample")
		
		df_columns=df.columns.to_list()
		selected_columns=st.multiselect("Select the columns to display: ", df_columns)
		rows=len(df.index)
		number_rows=st.slider('Select the number of rows',2,10,rows)
		if selected_columns:
			st.dataframe(df[selected_columns].head(number_rows))
		else:
			st.dataframe(df.head(number_rows))