import streamlit as st
from PIL import Image

def app():
	image = Image.open('about1.jpg')
	st.image(image)

	st.markdown("""
# About

Welcome to our data analysis and visualization platform!

## Page Developer

This platform was developed by Julián Gaona, a data ethusiastic passion for turning data into valuable insights.Julián created this platform to help you explore and analyze breast cancer data with ease.

Connect with Julián on [LinkedIn](https://www.linkedin.com/in/juliangaona/) to learn more about his work and stay updated on the latest data analysis projects.

## Contact Information

If you have any questions, feedback, or inquiries, please feel free to reach out to us at [julian.gaona.gonzalez@gmail.com]. We value your input and look forward to helping you with your data analysis needs.""")

