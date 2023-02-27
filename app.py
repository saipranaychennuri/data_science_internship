import streamlit as st
from PIL import Image
import os



st.title("SAI PRANAY CHENNURI PORTFOLIO")


image = Image.open('saipranay.jpg')

col1, col3 = st.columns(2)

with col1:
   
    
    st.caption("Name : SAI PRANAY CHENNURI")
    st.caption("Mobile : 8247850421")
    st.caption("Email : saipranaychennuri@gmail.com")
    st.caption("LinkedIn : http://www.linkedin.com/in/sai-pranay-chennuri-289799242/ ")


with col3:
   
   st.image(image, caption=None, width=160, use_column_width=int, clamp=False, channels="RGB", output_format="auto")

st.subheader("Career Objective :")
st.text(' To secure a challenging and growth-oriented entry-level position in a dynamic and \n forward-thinking organization where I can utilize myeducation, skills, and passion \n to contribute to the company\'s successand further my professional development.')

st.subheader("Education")
st.text('')
st.subheader('BACHELOR OF SCIENCE \n(DATA SCIENCE)')
st.subheader('NSV Degree College,Jagtial')
st.text('2020-2023')

st.text('INTERMEDIATE/+2 \n (Mathematics-Physics-Chemistry)')
st.subheader('Sri Chaitanya Junior College- Jagtial')
st.text('2018-2020')

st.text('SECONDARY SCHOOL')
st.subheader('Chandra Grammar High School')
st.text('2017-2018')

st.text('')
st.subheader('TECHNICAL SKILLS')
st.text('Python')
st.text('Data Engineering with Python')
st.text('Machine Learning')
st.text('Data Analytics')
st.text('Web Scraping')
st.text('SQL & No SQL')
st.text('Ms-Excel')
st.text('HTML & CSS')

st.subheader('CERTIFICATIONS')
st.text('Successfully completed MASTER CLASS ON MACHINE LEARNING at Pantech Prolabs India pvt Ltd (Certificate No:PS-2022-ML-0621)')
st.text('Successfully completed Clean Data in SQL using MySQL Workbench an online \n non - credit project authorized by Coursera Project Network and offered \n through Coursera.')
st.text('Successfully completed Business Analytics using Power BI andTableau at Excelr.\n Certificate Code : 11253E/EXCELR')
st.text('Successfully completed Business Analytics using Power BI andTableau at Excelr.\n Certificate Code : 11253E/EXCELR')

st.subheader('PROJECTS')
st.caption("STUDENT MARKS MANAGEMENT SYSTEM")
st.text("17th October 2022-16th November 2022")
st.text("In this project we managed the student data.\nWe created a web application Python/Django.\nIt consists of CRUD operation.")
st.text("STUDENT MARKS PREDICTION USIGN PYTHON")
st.text("Aug 2022 - Aug 2022")
st.text("I used SCI-KIT LEARN to predict the student's marks using Python")
st.text("FLIPKART WEB SCRAPING USING PYTHON")
st.text("Jun 2022 - Jun 2022")
st.text("I used BeautifulSoup and URL library in this project.")


data1=open("saipranayresume.pdf","rb").read()
st.download_button(label="Download",data=data1)