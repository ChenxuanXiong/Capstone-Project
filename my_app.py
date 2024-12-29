import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#/usr/local/bin/python3 -m pip install matplotlib.pyplot    
#streamlit run "/Users/chenxuanxiong/Desktop/Capstone Project/my_app.py"

## https://www.bls.gov/ooh/most-new-jobs.htm
st.title('Job Market Trends Analysis')

st.write('## Visualization')
st.write('###  Most in-demand job positions in main industries')
industry_data = {
    "Technology": [("Software developer","$132,270")], 
    #https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm#:~:text=$101%2C800-,The%20median%20annual%20wage%20for%20software%20developers%20was%20$132%2C270%20in,percent%20earned%20more%20than%20$164%2C520.&text=99%2C840-,Most%20software%20developers%2C%20quality%20assurance%20analysts,and%20testers%20work%20full%20time.
    "Healthcare": [("Home health and personal care aides","$33,530")],
    #https://www.bls.gov/ooh/healthcare/home-health-aides-and-personal-care-aides.htm#:~:text=a%20standardized%20test.-,Pay,was%20$33%2C530%20in%20May%202023.
    "Finance": [("Financial managers","$156,100")],
    #https://www.bls.gov/ooh/management/financial-managers.htm#:~:text=$136%2C170-,The%20median%20annual%20wage%20for%20financial%20managers%20was%20$156%2C100%20in,percent%20earned%20more%20than%20$239%2C200.
    "Hospitality": [("Cooks, restaurant","$34,320")],
    #https://www.bls.gov/ooh/food-preparation-and-serving/cooks.htm
    "Retail": [("Stockers and order fillers","$36,390")],
    #https://www.bls.gov/oes/2023/may/oes537065.htm
}

industries = list(industry_data.keys())
selected_industry = st.selectbox("Select an industry", industries)

if selected_industry:
    st.write(f"Most demanded position in {selected_industry}:")
    for position, payment in industry_data[selected_industry]:
        st.write(f"- {position}")
        st.write(f"  Median Annual Payment: {payment}")  # Display payment on a new line

st.write("")

st.write('###  Job Demand in Different States')
st.image('/Users/chenxuanxiong/Desktop/Capstone Project/employment-by-state-nove.png')

st.write("")

st.write('### Top-paying roles in Technology vs. Healthcare')
role_data = {
    "Technology": [("Software Engineering Manager","$161,477"),("Back-End Developer","$158,984"),("Site Reliability Engineer","$155,517")], 
    #https://www.forbes.com/sites/insights-american-express/2024/11/26/5-findings-that-could-reveal-your-companys-path-to-payment-innovation/?
    "Healthcare": [("Physician or surgeon","$229,300"),("Dentist","$159,530"),("Podiatrist","$148,720")],
    #https://www.coursera.org/articles/best-paying-jobs-in-healthcare
}

industries = list(role_data.keys())
selected_industry = st.selectbox("Select an industry", industries)

# Display the most demanded positions and average payments for the selected industry
if selected_industry:
    st.write(f"Most demanded positions and average payments in {selected_industry}:")
    for position, payment in role_data[selected_industry]:
        st.write(f"- {position}: {payment}")

st.write("")

st.write("### The demand for software engineers over years")
st.image('https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fac29c573-0093-4f27-8b7c-14b96a849e7e_1920x1920.gif')
st.write("After a high growth from 2011-2022, the demand for software engineers grows slow since 2022.")

st.write("")

st.write("### Cities with the highest average salaries for data scientists")
#https://money.usnews.com/careers/best-jobs/data-scientist/salary

df = pd.read_csv("/Users/chenxuanxiong/Desktop/Capstone Project/Data Science Salary in Cities.csv")
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce').fillna(0).astype(int)
if 'City' in df.columns and 'Salary' in df.columns:
    fig, ax = plt.subplots()
    bars = ax.bar(df['City'], df['Salary'])

    ax.set_xticklabels(df['City'], rotation=45, ha='right')  # Rotate by 45 degrees

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 2, 
                int(yval), ha='center', va='bottom', fontsize=10) 

    ax.set_xlabel('City')
    ax.set_ylabel('Salary')
    ax.set_title('Salary Distribution by City')
    st.pyplot(fig)
else:
    st.write("The CSV must have 'Category' and 'Salary' columns.")


st.write("")
st.write("### The average salary for marketing roles change across different industries")
industry_data = {
    #https://thecmo.com/career-development/marketing-manager-salary/
    "Consumer Tech Industry": [("Average: $132,270")], 
    "Tech Infrastructure Industry": [("$90,000 to $130,000")],
    "Tech Services Industry": [("$80,000 to $120,000")],
    "E-commerce Industry": [("$100,518 to $134,670")],
}

industries = list(industry_data.keys())
selected_industry = st.selectbox("Select an industry", industries)

if selected_industry:
    st.write(f"Most demanded position in {selected_industry}:")
    for salary in industry_data[selected_industry]:
        st.write(f" Payment range: {salary}")



st.write("")
st.write("### The job market for students between metropolitan and rural areas")
#https://www.ers.usda.gov/data-products/chart-gallery/gallery/chart-detail/?chartId=106147
st.image('https://www.ers.usda.gov/webdocs/charts/106148/educational-attainment_768px.png?v=8466.3')
st.write("")

st.write("### Industries are hiring the most in the post-COVID job market")
#https://cepr.net/job-growth-since-the-pandemic-which-sectors-are-leading-the-way/
st.image('/Users/chenxuanxiong/Desktop/Capstone Project/change in employment post pandemic.png')
st.write("Offices of mental health practitioners hired the most in the post-COVID job market")
st.write("")

st.write("### The demand for jobs requiring remote work vary by region")
#https://www.weforum.org/stories/2023/04/remote-jobs-growing-fastest-locations-sectors/
st.image('/Users/chenxuanxiong/Desktop/Capstone Project/remote work by region.png')
st.write("")

st.write("### Industries experiencing a decline in hiring")
#https://www.uschamber.com/workforce/understanding-americas-labor-shortage-the-most-impacted-industries
st.image('https://uschamber.imgix.net/https%3A%2F%2Fwww.uschamber.com%2Fassets%2Fimages%2FAmerica-Works-Charts-December2024_6_Web.png?auto=compress%2Cformat&fit=clip&fm=png&q=80&w=1200&s=0e401ed65ac599a5f640cbe93a370b18')
st.write("Most industries are rising in unemployment rate since 2022, it might because the economy is in a slump.")
st.write("")

st.write("### The hiring trend for AI-related jobs")
#https://www.linkedin.com/pulse/ai-hiring-trends-report-april-2024-auraintel-qhimf/
st.image('https://media.licdn.com/dms/image/v2/D4D12AQE4tmslF4hQOA/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1716384390016?e=1740614400&v=beta&t=YYcBpgqftFehVhYWjO-Uy6ftBU4K-5Zzgx20GqkU0co')
st.image('https://media.licdn.com/dms/image/v2/D4D12AQGHwBrooGmciw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1716384378211?e=1740614400&v=beta&t=pgkOIJqZ1yZYJ2xMA5o5_kJl4g3wZVENeu_VngEjK2o')
st.write("Unlike the overall hiring trend that we saw in LinkedIn's latest Industry Hiring Trends Report, total number of new AI job postings increased in April, with a 7% uptick compared to March 2024 and almost a 30% increase compared to beginning of the year. Share of AI jobs compared to overall software jobs also increased from ~5.3% to ~6.4% in April vs March 2024, continuing an overall increase trend started in 2023 — this indicates that AI hiring market is much more active than the overall IT hiring market.")
st.write("")

st.write("### Fastest growing occupation")
#https://www.bls.gov/emp/tables/fastest-growing-occupations.htm
st.image('/Users/chenxuanxiong/Desktop/Capstone Project/Grow fast roles.png')
st.write("")

st.write("### Top job roles that offer remote or hybrid work options")
#https://online.usc.edu/news/best-careers-hybrid-jobs-remote-work/
st.write('According to USC Online, the top job roles that offer remote or hybrid work options are:Human Resources Manager, Software Engineer, Accountant, Social Media Manager, Nurse Practitioner, Project Manager, Paralegal, and Graphic Designer.')
st.write("")

st.write("### The job demand for international students fluctuate throughout the year?")
#https://interstride.com/blog/peak-recruitment-seasons-by-industry-that-international-students-should-know/#:~:text=Peak%20recruitment%20seasons%20to%20know%20Overall%2C%20the,popular%20recruitment%20months%20are%20September%20and%20February.
st.write('The job demand for international students typically peaks around fall semester, particularly in September and October, as companies begin recruiting for summer internships and full-time positions starting the following year, with additional spikes in February and during the spring semester when companies are actively hiring for upcoming roles.')
st.image('https://interstride.com/wp-content/uploads/2024/05/image1-e1714536323911.jpg')
st.write("")

st.write("## Causal Inference")
st.write("### Does job location influence the salary of international students in tech roles?")
import statsmodels.api as sm
data = pd.read_csv("/Users/chenxuanxiong/Desktop/Capstone Project/9.17 LinkedIn.csv")
data['minPay'] = pd.to_numeric(data['minPay'], errors='coerce')
data['maxPay'] = pd.to_numeric(data['maxPay'], errors='coerce')
data['Average_Salary'] = (data['minPay'] + data['maxPay']) / 2
data['State'] = data['Job_location'].str.extract(r',\s*([A-Z]{2})$')
filtered_data = data[['State', 'Average_Salary']].dropna()
st.write("Null Hypothesis (H0): Job location (State) does not influence the salary of international students in tech roles.")
st.write("Alternative Hypothesis (H1): Job location (State) influences the salary of international students in tech roles.")
st.write("Data: 9.17 LinkedIn")
st.write("Regression Model: Salary ~ State")
filtered_data['State'] = filtered_data['State'].astype('category')
import statsmodels.formula.api as smf
model = smf.ols('Average_Salary ~ C(State)', data=filtered_data).fit()

model_summary = model.summary()
model_summary
st.write(model_summary)
st.write("Based on the p-value of all states, all p-value > 0.05, meaning no state shows a statistically significant effect on salary compared to the baseline (Intercept). Therefore, we fail to reject the null hypothesis that job location does not influence the salary of international students in tech roles.")
st.write("")

st.write("### How does obtaining a master's degree impact the likelihood of landing a higher-paying job?")
#https://www.bls.gov/careeroutlook/2022/data-on-display/education-pays.htm
st.image("/Users/chenxuanxiong/Desktop/Capstone Project/earnings-and-unemploymen.png")
st.write("According to the data from the Bureau of Labor Statistics, obtaining a master's degree tend to landing a higher-paying job. But we can not definitively state that obtaining a master's degree impacts the likelihood of landing a higher-paying job from this data. More detailed, individual-level data are needed to make such a conclusion.")
st.write("")

st.write("###  Due to my current limitations and the lack of available data, I believe the remaining causal inference questions require extensive research, investigation, and survey data for proper analysis. Therefore, I will not be providing answers to them in this project.")
st.write("")

st.write("## Prediction")
st.write("###  What are the top job sectors that will see the most growth in the next five years?")
st.image('/Users/chenxuanxiong/Desktop/Capstone Project/fast grow roles 2.png')
st.write("")

st.write("###  Can we predict the demand for software engineering roles based on industry trends?")
st.write("Yes we can. Based on previous research, the demand for software engineering roles is expected to grow in the next five years but grow slowly.")
st.write("")

st.write("###  How will automation impact job demand in the manufacturing sector?")
st.write("The empirical results show that the automated machines in manufacturing industry have a significant impact on labor force employment in enterprises, mainly in the form of the destruction effect on low-skilled labor force and the creation effect on high-skilled labor force. The substitution effect of automated machines in manufacturing firms is driven by two primary mechanisms: the expansion effect on output and the enhancement effect on productivity.")
st.write("------By PubMed Central: How automated machines influence employment in manufacturing enterprises?")
st.write("")

st.write("###  What job positions are most likely to be replaced by AI in the near future?")
st.write("Data entry clerks and processors are among the most vulnerable to AI automation. Machine learning algorithms can now handle vast amounts of data with speed and accuracy that far surpasses human capabilities.")
st.write("------By LinkedIn: Top Jobs Most at Risk of Being Replaced by AI")

st.write("###  Which industries will see the biggest increase in hiring for AI-related jobs?")
st.write("According to Indeed, job postings mentioning AI that saw the biggest growth in the first 11 months of 2024 were senior scientists, software engineering managers, research engineers, and researchers.")
st.write("")

st.write("### Can we predict job demand fluctuations based on seasonality and industry cycles?")
st.write("The job demand for international students typically peaks around fall semester, particularly in September and October, as companies begin recruiting for summer internships and full-time positions starting the following year, with additional spikes in February and during the spring semester when companies are actively hiring for upcoming roles.")
st.write("")



st.write("### What will be the impact of AI on job creation in the tech sector over the next decade?")
st.write("The World Economic Forum's Future of Jobs Report illuminates the dual nature of AI's impact: By 2025, while 85 million jobs may be displaced by automation, an impressive 97 million new roles are projected to emerge, reflecting a shift in the division of labor between humans, machines and algorithms.")
st.write("------By Forbes: The Future Of Work: Embracing AI's Job Creation Potential")

st.write("Rest of the questions are regarding to international students, which I do not have data to make predictions. Therefore, I will not be providing answers to them in this project.")







