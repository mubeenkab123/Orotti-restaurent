import streamlit as st


import streamlit as st
import pandas as pd
import os

def save_feedback(name, rating, email):
    file_path = "customer_feedback.xlsx"
    data = {"Customer Name": [name], "Rating": [rating], "Email": [email]}
    df = pd.DataFrame(data)
    
    if os.path.exists(file_path):
        existing_df = pd.read_excel(file_path)
        df = pd.concat([existing_df, df], ignore_index=True)
    
    df.to_excel(file_path, index=False)

def main():
    st.set_page_config(page_title="We Value Your Feedback - Green Medicals", layout="centered")
    
    st.title("Thank You for Choosing Green Medicals!")
    
    
    st.markdown("---")
    
    st.subheader("Rate Your Experience")
    
    buttons = [
        ("🌟 Excellent", "#00ff00", "https://g.page/r/CYs8l7uEbQo4EBM/review?utm_source=email&utm_medium=review_request&utm_campaign=excellent"),
        ("👍 Good", "#00aaff", "https://g.page/r/CYs8l7uEbQo4EBM/review?utm_source=email&utm_medium=review_request&utm_campaign=good"),
        ("😐 Average", "#cccc00", "https://forms.gle/9tSBdH7emrGxJ2Z39?utm_source=email&utm_medium=review_request&utm_campaign=average"),
        ("👎 Bad", "#cc6600", "https://forms.gle/BXnXipFeZ29vStuQA?utm_source=email&utm_medium=review_request&utm_campaign=bad"),
        ("❌ Poor", "#cc0000", "https://forms.gle/BXnXipFeZ29vStuQA?utm_source=email&utm_medium=review_request&utm_campaign=poor")
    ]
    
    for label, color, link in buttons:
        st.markdown(
            f"""
            <a href='{link}' target='_blank' style='display: block; text-align: center; background-color: {color}; 
            padding: 14px; border-radius: 5px; color: black; text-decoration: none; font-weight: bold;'>{label}</a>
            """, 
            unsafe_allow_html=True
        )
    
    st.markdown("---")
    
    
    st.write("We greatly appreciate your time and feedback, and we look forward to serving you again!")
    st.write("We hope you had a great experience with us! To show our appreciation, we’d like to offer you a FREE travel guide PDF for Thrissur, which includes:")
    
    st.markdown("""
    - **Commuting Tips**  
    - **Suggested Itinerary**  
    - **Top Places to Visit**  
    - **Best Restaurants**  
    - **And much more!**  
    """)
    
   
    name = st.text_input("Enter your name", key="name_input")
    email = st.text_input("Enter your email (optional) to receive the PDF", key="email_pdf")
    
    if st.button("Submit", key="submit_info"):
        save_feedback(name, "Name Submission", email)
        st.success("Thank you! We will send you the travel guide PDF shortly.")
    
if __name__ == "__main__":
    main()
