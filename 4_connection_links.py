import streamlit as st 
st.title("Connection Links") 
st.write(""" 
Feel free to connect with me, **Hamza Ansari** on the following 
platforms. Whether you have questions about the project, ideas for 
improvements, or just want to connect, these platforms are the 
best way to reach me! 
""") 
# Example dummy paths for logos 
linkedin_logo = "img/LinkedIn.png" 
github_logo = "img/Github.png" 
col1, col2 =  st.columns(2) 

# Display logos with links 
with col1: 
    st.image(linkedin_logo, width=50) 
    st.markdown("[LinkedIn]( https://www.linkedin.com/in/hamza-ansari11)") 
with col2: 
    st.image(github_logo, width=50) 
    st.markdown("[GitHub]( https://github.com/hamza-ansari11)") 

st.write(""" 
If you're interested in knowing more about the **AI-Powered Data 
Science Dashboard** or other projects, check out my GitHub 
profile. I'm always open to feedback and collaboration! 
""")