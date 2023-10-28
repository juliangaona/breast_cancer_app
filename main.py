import streamlit as st
from streamlit_option_menu import option_menu
import about,home,graph,data_sample



st.set_page_config(
	page_title="Breast Cancer Site",
	page_icon='	:crab:',
	layout='wide',

	)

class Multiapp:
	def _ini_(self):
		self.apps=[]

	def add_app(self,title,function):
		self.apps.append({
			"title":title,
			"function": function
			})

	def run():
		with st.sidebar:
			app = option_menu(
				menu_title="Breast Cancer Site",
				options=["Home","Data Structure","Exploratory Data Analysis","About"],
				icons=["house-heart-fill","clipboard-data-fill","file-bar-graph-fill","chat-left-dots-fill"],
				menu_icon="window-sidebar", 
				default_index=1,
				styles={
				"container":{"padding":"5!important","background-color":'black'},
				"icon": {"color": "white", "font-size": "23px"},
				"nav-link": {"color":"white","font-size": "15px",
				"text-align": "left","margin":"0px","--hover-color": "#adadad"},
				"nav-link-selected": {"background-color": "#FFC0CB","font-size": "14px"},}
				)

		if app == "Home":
			home.app()	
		if app == "Data Structure":
			data_sample.app()  
		if app == "Exploratory Data Analysis":
			graph.app()
		if app == "About":
			about.app()        
	   

	run()

