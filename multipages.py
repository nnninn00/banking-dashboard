# # app.py (Home page)
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# st.set_page_config(page_title="Grey Dashboard", layout="wide")

# st.title("Grey Banking")

# # Load your CSV
# @st.cache
# def load_data():
#     return pd.read_csv("C:/Users/nazif/SHRDC/Jupyter Notebook/Day 4/banking/banking.csv")  # Update with your path

# data = load_data()

# st.write("This is the main page of the banking dashboard.")
# st.write(data.head())  # Display the first few rows of the data to understand its structure
# st.write("Column names:", data.columns)  # Show column names to ensure you're using the correct ones



# # pages/page1.py
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# st.title("Interactive Charts")

# # Load data
# @st.cache
# def load_data():
#     return pd.read_csv("C:/Users/nazif/SHRDC/Jupyter Notebook/Day 4/banking/banking.csv")  # Update with your path

# data = load_data()

# # Display column names for reference
# st.write("Column names:", data.columns)

# # Split page into two columns
# col1, col2 = st.columns(2)

# column1 = 'age'
# column2 = 'euribor3m'

# # Chart in first column
# with col1:
#     st.subheader("Chart 1")
#     fig, ax = plt.subplots()
#     ax.plot(data[column1])  
#     st.pyplot(fig)

# # Chart in second column
# with col2:
#     st.subheader("Chart 2")
#     fig, ax = plt.subplots()
#     ax.plot(data[column2])  # Replace 'column2' with actual column name
#     st.pyplot(fig)

# # Add interactivity
# col1_chart_type = st.sidebar.selectbox("Choose chart type for Column 1:", ["Line", "Bar"])
# col2_chart_type = st.sidebar.selectbox("Choose chart type for Column 2:", ["Line", "Bar"])

# # Update charts based on user selection
# if col1_chart_type == "Line":
#     col1.line_chart(data[column1])
# else:
#     col1.bar_chart(data[column1])

# if col2_chart_type == "Line":
#     col2.line_chart(data[column2])
# else:
#     col2.bar_chart(data[column2])


# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Load the dataset
# df = pd.read_csv('banking.csv')

# # Create a multipage structure
# st.set_page_config(page_title="Banking App", page_icon=":bank:", layout="wide")

# # Sidebar for navigation
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ["Home", "Charts"])

# if page == "Home":
#     st.title("Welcome to the Banking Data App")
#     st.write("This app helps you explore banking data interactively.")

# elif page == "Charts":
#     st.title("Interactive Charts")

#     # Create two columns
#     col1, col2 = st.columns(2)

#     # First chart in the first column
#     with col1:
#         st.subheader("Chart 1: Distribution of Age")
#         fig1 = px.histogram(df, x='age')
#         st.plotly_chart(fig1)

#     # Second chart in the second column
#     with col2:
#         st.subheader("Chart 2: Balance by Job")
#         fig2 = px.bar(df, x='job', y='balance')
#         st.plotly_chart(fig2)
        
#     # Add interactive control
#     st.subheader("Filter by Marital Status")
#     marital_status = st.selectbox("Choose marital status", df['marital'].unique())
#     filtered_df = df[df['marital'] == marital_status]
    
#     # Show filtered data in chart
#     st.write(f"Filtered Data by {marital_status} status:")
#     st.write(filtered_df)


##third
# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Load the dataset
# df = pd.read_csv('banking.csv')

# # Create a multipage structure
# st.set_page_config(page_title="Banking App", page_icon=":bank:", layout="wide")

# # Sidebar for navigation
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ["Home", "Charts"])

# if page == "Home":
#     st.title("Welcome to the Banking Data App")
#     st.write("This app helps you explore banking data interactively.")

# elif page == "Charts":
#     st.title("Interactive Charts")

#     # Create two columns
#     col1, col2 = st.columns(2)

#     # First chart in the first column
#     with col1:
#         st.subheader("Chart 1: Distribution of Age")
#         fig1 = px.histogram(df, x='age')
#         st.plotly_chart(fig1)

#     # Second chart in the second column (using 'duration' instead of 'balance')
#     with col2:
#         st.subheader("Chart 2: Stacked Bar Chart of Job by Duration (Stacked by Marital Status)")
#         fig2 = px.bar(df, x='job', y='duration', color='marital', title='Stacked Bar Chart of Job by Duration')
#         st.plotly_chart(fig2)
#     # with col2:
#     #     st.subheader("Chart 2: Funnel Chart of Customer Journey")
        
#     #     # Define stages of the funnel and counts (modify these as per your data)
#     #     funnel_data = {
#     #         'Stage': ['Inquiries', 'Applications', 'Approvals', 'Account Activations'],
#     #         'Count': [2000, 1500, 1000, 800]  # Replace with actual data
#     #     }
#     #     funnel_df = pd.DataFrame(funnel_data)

#     #     # Create funnel chart
#     #     fig_funnel = px.funnel(funnel_df, x='Count', y='Stage', title='Funnel Chart of Customer Journey',
#     #                             labels={"Count": "Number of Customers", "Stage": "Stage"})
        
#     #     st.plotly_chart(fig_funnel)

        
#     # Add interactive control
#     st.subheader("Filter by Marital Status")
#     marital_status = st.selectbox("Choose marital status", df['marital'].unique())
#     filtered_df = df[df['marital'] == marital_status]
    
#     # Show filtered data in chart
#     st.write(f"Filtered Data by {marital_status} status:")
#     st.write(filtered_df)



# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Load the dataset
# df = pd.read_csv('banking.csv')

# # Create a multipage structure
# st.set_page_config(page_title="Banking App", page_icon=":bank:", layout="wide")

# # Sidebar for navigation
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ["Home", "Charts"])

# if page == "Home":
#     st.title("Welcome to the Banking Data App")
#     st.write("This app helps you explore banking data interactively.")

# elif page == "Charts":
#     st.title("Interactive Charts")



#    # Add a dropdown to filter by job type
#     job_filter = st.selectbox("Select Job", options=["All"] + list(df['job'].unique()), index=0)

#     # Filter the dataframe based on selected job type
#     if job_filter != "All":
#         filtered_df = df[df['job'] == job_filter]
#     else:
#         filtered_df = df

#     # Create two columns
#     col1, col2 = st.columns(2)

#     # First chart in the first column
#     with col1:
#         st.subheader("Chart 1: Distribution of Age")
#         fig1 = px.histogram(filtered_df, x='age', title=f"Age Distribution for {job_filter if job_filter != 'All' else 'All Jobs'}")
#         st.plotly_chart(fig1)

#     # Second chart in the second column (using 'duration' instead of 'balance')
#     with col2:
#         st.subheader("Chart 2: Duration by Job")
#         fig2 = px.bar(filtered_df, x='job', y='duration', color="marital", title=f"Duration by Job for {job_filter if job_filter != 'All' else 'All Jobs'}")
#         st.plotly_chart(fig2)

#     # Add interactive control for marital status
#     st.subheader("Filter by Marital Status")
#     marital_status = st.selectbox("Choose marital status", options=["All"] + list(df['marital'].unique()))

#     # Filter the dataframe based on selected marital status
#     if marital_status != "All":
#         filtered_df = filtered_df[filtered_df['marital'] == marital_status]

#     # Show filtered data in chart and table
#     st.write(f"Filtered Data by {marital_status} status:" if marital_status != "All" else "Complete Data:")
#     st.write(filtered_df)


import streamlit as st
import pandas as pd
import plotly.express as px
import base64

# Load the dataset
df = pd.read_csv('banking.csv')

# Create a multipage structure
st.set_page_config(page_title="Banking App", page_icon=":bank:", layout="wide")

# Function to load and encode an image file
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# # Specify the local image file path (ensure the path is correct)
# img_file_path = "C:\Users\nazif\SHRDC\Jupyter Notebook\Day 4\banking\background.png" 

# # Encode the image file to base64
# base64_img = get_base64_of_bin_file(img_file_path)

# # Background image or color styling
# page_bg_img = f'''
# <style>
# body {{
#     background-image: url("data:image/jpeg;base64,{base64_img}");
#     background-size: cover;
#     background-repeat: no-repeat;
#     background-attachment: fixed;
# }}
# </style>
# '''

# st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Charts"])

if page == "Home":
    st.title("Welcome to the Banking Data App")
    st.write("This app helps you explore banking data interactively.")
    from PIL import Image
    logo = Image.open('background.png')
    st.image(logo)

elif page == "Charts":
    st.title("Interactive Charts")

    # Add a dropdown to filter by job type
    job_filter = st.selectbox("Select Job", options=["All"] + list(df['job'].unique()), index=0)

    # Filter the dataframe based on selected job type
    if job_filter != "All":
        filtered_df = df[df['job'] == job_filter]
    else:
        filtered_df = df

    # Create two columns
    col1, col2 = st.columns(2)

    # First chart in the first column
    with col1:
        st.subheader("Chart 1: Distribution of Age")
        fig1 = px.histogram(filtered_df, x='age', title=f"Age Distribution for {job_filter if job_filter != 'All' else 'All Jobs'}")
        st.plotly_chart(fig1)

    # Second chart in the second column (using 'duration' instead of 'balance')
    with col2:
        st.subheader("Chart 2: Duration by Job")
        fig2 = px.bar(filtered_df, x='job', y='duration', color="marital", title=f"Duration by Job for {job_filter if job_filter != 'All' else 'All Jobs'}")
        st.plotly_chart(fig2)

    # Add interactive control for marital status
    st.subheader("Filter by Marital Status")
    marital_status = st.selectbox("Choose marital status", options=["All"] + list(df['marital'].unique()))

    # Filter the dataframe based on selected marital status
    if marital_status != "All":
        filtered_df = filtered_df[filtered_df['marital'] == marital_status]

    # Show filtered data in chart and table
    st.write(f"Filtered Data by {marital_status} status:" if marital_status != "All" else "Complete Data:")
    st.write(filtered_df)
