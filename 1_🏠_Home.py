import streamlit as st
import streamlit_authenticator as stauth
import pickle
from pathlib import Path



names = ["Shahid", "Uzama", "Lafri", "Vinod"]
usernames = ["Shahid", "Uzama", "Lafri", "Vinod"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days=0)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:

    st.title('WELCOME TO DATA HABOUR 🚢')

    st.header('🌊Test the Waters')
    st.subheader('Understand your customers and competition before you make decisions')
    st.write("Research")
    st.write("Structured: Chat with tabular data store in a SQL database")
    st.write("            Data contains Customers and Watches    ")
    st.write("Unstructured: Chat with textual data stored in a Vector Database")
    st.write("              Contains textual data about some watches")

    st.header('🌊Take the plunge')
    st.subheader('Generate tailor made marketing decisions unique to each customer')
    st.write("Research analyzer: A Chat bot used to analyze customer sentiments on Watch types")
    st.write("Decisions: Analyse Customer plots . ")
    st.write("           Analyze Customer segments using kmeans and Vector database")
    authenticator.logout("Logout", "sidebar")


