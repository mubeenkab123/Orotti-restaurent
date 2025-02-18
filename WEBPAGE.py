import streamlit as st


import streamlit as st

def main():
    st.set_page_config(page_title="We Value Your Feedback - Green Medicals", layout="centered")
    
    st.title("Thank You for Choosing Green Medicals!")
    
    st.markdown("---")
    
    st.subheader("Rate Your Experience")
    
    st.markdown("<a href='https://g.page/r/CYs8l7uEbQo4EBM/review?utm_source=email&utm_medium=review_request&utm_campaign=excellent' target='_blank' style='display: block; text-align: center; background-color: #00ff00; padding: 14px; border-radius: 5px; color: black; text-decoration: none; font-weight: bold;'>🌟 Excellent</a>", unsafe_allow_html=True)
    
    st.markdown("<a href='https://g.page/r/CYs8l7uEbQo4EBM/review?utm_source=email&utm_medium=review_request&utm_campaign=good' target='_blank' style='display: block; text-align: center; background-color: #00aaff; padding: 14px; border-radius: 5px; color: black; text-decoration: none; font-weight: bold;'>👍 Good</a>", unsafe_allow_html=True)
    
    st.markdown("<a href='https://forms.gle/9tSBdH7emrGxJ2Z39?utm_source=email&utm_medium=review_request&utm_campaign=average' target='_blank' style='display: block; text-align: center; background-color: #cccc00; padding: 14px; border-radius: 5px; color: black; text-decoration: none; font-weight: bold;'>😐 Average</a>", unsafe_allow_html=True)
    
    st.markdown("<a href='https://forms.gle/BXnXipFeZ29vStuQA?utm_source=email&utm_medium=review_request&utm_campaign=bad' target='_blank' style='display: block; text-align: center; background-color: #cc6600; padding: 14px; border-radius: 5px; color: black; text-decoration: none; font-weight: bold;'>👎 Bad</a>", unsafe_allow_html=True)
    
    st.markdown("<a href='https://forms.gle/BXnXipFeZ29vStuQA?utm_source=email&utm_medium=review_request&utm_campaign=poor' target='_blank' style='display: block; text-align: center; background-color: #cc0000; padding: 14px; border-radius: 5px; color: black; text-decoration: none; font-weight: bold;'>❌ Poor</a>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.write("We hope you had a great experience with us! To show our appreciation, we’d like to offer you a FREE travel guide PDF for Thrissur, which includes:")

    st.markdown("""
    - **Commuting Tips**  
    - **Suggested Itinerary**  
    - **Top Places to Visit**  
    - **Best Restaurants**  
    - **And much more!**  
    """)
    st.write("Once you submit your rating, we'll send you the travel guide PDF with all the helpful tips and insights for your next visit to Thrissur!")
    st.write("We greatly appreciate your time and feedback, and we look forward to serving you again!")
    
if __name__ == "__main__":
    main()
