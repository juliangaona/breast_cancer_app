import streamlit as st
from PIL import Image

def app():
	
	st.markdown("""# Breast Cancer Data Explorer

Welcome to the Breast Cancer Data Explorer, a Streamlit application for analyzing breast cancer data. This application allows users to explore and gain insights from breast cancer datasets.

## Table of Contents

1. [About Breast Cancer](#about-breast-cancer)
2. [Home](#home)
3. [Data Structure](#data-structure)
4. [Exploratory Data Analysis](#exploratory-data-analysis)
5. [About](#about)

## About Breast Cancer""")

	image = Image.open('home1.jpg')
	st.image(image)
	st.markdown("""	
### What is Breast Cancer?

Breast cancer is a malignant tumor that originates in the cells of the breast. It can occur in both women and men, although it is far more common in women. Breast cancer can develop in various parts of the breast, including the milk ducts, lobules, or in the connective tissues.

### Risk Factors

Several risk factors can increase the likelihood of developing breast cancer, including:

- **Gender:** Women are at a significantly higher risk than men.
- **Age:** The risk of breast cancer increases with age.
- **Genetics:** A family history of breast cancer or specific genetic mutations (e.g., BRCA1 and BRCA2) can increase the risk.
- **Hormone Replacement Therapy (HRT):** Certain hormone therapies may increase the risk.
- **Personal History:** Individuals with a previous breast cancer diagnosis have an increased risk of recurrence.

### Early Diagnosis

Early detection is critical for successful breast cancer treatment. Methods for early diagnosis include:

- **Breast Self-Exams:** Regular self-exams help individuals become familiar with their breast tissue, making it easier to detect any changes.
- **Mammograms:** These X-ray images can reveal tumors before they become palpable.
- **Clinical Breast Exams:** Healthcare professionals can perform thorough breast exams during routine check-ups.

### Treatment

Breast cancer treatment options depend on the stage, type, and individual factors. Treatment methods may include:

- **Surgery:** Removing the tumor and, in some cases, the entire breast (mastectomy).
- **Radiation Therapy:** Using high-energy rays to kill cancer cells.
- **Chemotherapy:** Administering drugs to kill cancer cells.
- **Hormone Therapy:** Blocking hormones that fuel certain types of breast cancer.
- **Targeted Therapy:** Targeting specific molecules involved in cancer growth.
- **Immunotherapy:** Enhancing the body's immune response to fight cancer.



### Disease Awareness

Breast cancer awareness is crucial for education, early detection, and prevention. It involves campaigns, fundraising efforts, and events to promote knowledge about the disease. Early detection and timely treatment can significantly improve outcomes for those diagnosed with breast cancer.

---

## Home

This application provides an interactive platform for users to explore breast cancer data and gain insights into this critical area of healthcare.

## Data Structure

The breast cancer dataset is structured with various features and labels. It typically includes data points such as patient age, tumor size, tumor type, histological grade, and more. Understanding the structure of the data is essential for meaningful analysis.

## Exploratory Data Analysis

Exploratory Data Analysis (EDA) is a crucial step in understanding the breast cancer dataset. In this section of the application, you can:

- Visualize data distribution and summary statistics.
- Explore relationships between different features.
- Identify trends and potential correlations within the dataset.
- Gain insights that can aid in decision-making and research.""")
