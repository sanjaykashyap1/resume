import streamlit as st
# import matplotlib.pyplot as plt
# import seaborn as sns

# Customize the look and feel of the application
st.set_page_config(page_title="Sanjay Bhaskar Kashyap's Portfolio", page_icon=":mortar_board:", layout="wide")

# Add a custom logo/header
st.write("""
# Sanjay Bhaskar Kashyap
Data Scientist | Business Analyst 
""", unsafe_allow_html=True)

# Profile Image
# profile_image = plt.imread("C:/Users/19452/Desktop/ass1/WhatsApp Image 2023-02-07 at 11.05.00.jpeg")
# st.image(profile_image, use_column_width=False, caption="Profile Image")

# Contact Information
st.write("""
**Contact Information**
- Location: Boston, MA
- Phone: 9452447079
- Email: kashyap.sanj@northeastern.edu
- LinkedIn: linkedin.com/in/skashyap11
""", unsafe_allow_html=True)

# Education
st.header("Education")
st.write("""
**Master of Science, Information Systems**
Northeastern University, Boston, MA
Expected May 2024

**Bachelor of Engineering, Electronics and Telecommunication**
Visvesvaraya Technological University, Bangalore, IN
June 2019
""")

# Skills
st.header("Skills")
st.write("""
**Programming Languages**: Python, R, Java, SQL, C, C++, HTML, MATLAB

**Database**: Azure SQL Server, MS SQL Server, PostgreSQL, MySQL, Cassandra, MongoDB

**Technology & Tools**: Tableau, Power BI, Git, R-studio, Anaconda, Advanced Microsoft Excel, Powerpoint, Arduino, LabVIEW, Photoshop, Illustrator, NetBeans, Miro, Scikit learn, TensorFlow, Streamlit, Pytorch, NLTK, spaCy, CoreNLP, Snowflake
""")

# Work Experience
st.header("Work Experience")
st.write("""
**Business Analyst, McKinsey & Company**
January 2020 - August 2022

- Designed dashboards to segment visual analysts into profiles, helping the global consultants to increase the engagements and collaborate with the analysts by 30%
- Performed data extraction and enhanced data quality using SQL to generate business KPI’s for the stakeholders, and visualized using tableau dashboard for various lines of business
- Performed a variety of activities as a design traffic planner, including revising design requests, rerouting, confirming, elaborating on requirements, and accurately assigning requests with 99% accuracy
- Piloted and worked with the automation team to automate the tools required to amalgamate large sets of data improving the time efficiency of designers by 50%
- Examined the root causes of overused resources, developed measures for effective resource planning and reduced overtime utilization of the analysts by 40%
- Awarded with best quality award in the year 2021 for the most effective and efficient deliverables
""")

st.write("""
**Business Development Associate, Byju’s the learning application**
June 2019 - December 2019

- Led marketing and sales in numerous designated zones and analyzed transactional customer data from salesforce
- Led marketing and sales in numerous designated zones and analyzed transactional customer data from salesforce
-  Managed and exponentially grew sales pipeline and presales customers whilst optimizing active user experience with an increase of sales by 35%
""")

# Projects
st.header("Projects")
st.write("""
**KEYS – Student accommodation solution, Northeastern University**

- Created a JAVA Application to build a Student Accommodation System deploying the Java Swing Application and maintain backend database using SQL
""")

st.write("""
**Movie genre and dialogue prediction, Northeastern University**

- Demonstrated web scraping of the IMSDB website to scrape movie scripts of all genres, creating scenes into data frames and implementing random forest classifier, support vector machine (SVM), Linear discriminant analysis (LDA), PageRank machine learning algorithms and leveraged the Bayesian modelling to deliver insights
""")

st.write("""
**Programmable Transmitters and Data logging for Satellites, U R Rao Satellite Centre (ISRO), India**

-  Designed a command generator & data logger for test & evaluation of frequency programmable transmitters using LabVIEW in order to control frequency of satellites from ground station.

""")

st.write("""
**Damage detection and monitoring of flyovers/bridges, CMRIT, India**

-  Developed an IoT system to monitor the performance, control and store the data of the health of structures and provided accurate predictions regarding the structure's health by running predictive machine learning models
""")

st.write("""
**Crowd funding for farmers, CMRIT Collaborative Research lab**

- Project envisages machine learning algorithms to optimize crowd funding and loan disbursement for farmers by predicting loan-worthy candidates and provided advanced analytics on crop and weather data
""")


# Add a custom footer
st.write("""
## Thank you for visiting my portfolio!
""", unsafe_allow_html=True)
