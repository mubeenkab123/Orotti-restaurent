import streamlit as st
import pandas as pd
import os

# File paths - modify these if needed
CUSTOMER_FILE = r"C:\Users\USER\Desktop\cust name and email.xlsx"
RATING_FILE = r"C:\Users\USER\Desktop\rating.xlsx"

def save_customer_info(name, email):
    """Save customer name and email to Excel file"""
    data = {"Customer Name": [name], "Email": [email]}
    new_df = pd.DataFrame(data)
    
    if os.path.exists(CUSTOMER_FILE):
        existing_df = pd.read_excel(CUSTOMER_FILE)
        updated_df = pd.concat([existing_df, new_df], ignore_index=True)
    else:
        updated_df = new_df
    
    updated_df.to_excel(CUSTOMER_FILE, index=False)

def update_rating_counts(rating):
    """Update rating counts in Excel file"""
    try:
        if os.path.exists(RATING_FILE):
            df = pd.read_excel(RATING_FILE)
        else:
            df = pd.DataFrame({
                "Rating": ["Excellent", "Good", "Average", "Bad", "Poor"],
                "Count": [0, 0, 0, 0, 0]
            })
        
        df.loc[df["Rating"] == rating, "Count"] += 1
        df.to_excel(RATING_FILE, index=False)
    except Exception as e:
        st.error(f"Error updating ratings: {str(e)}")

def main():
    st.set_page_config(page_title="We Value Your Feedback - Green Medicals", layout="centered")
    
    st.title("Thank You for Choosing Green Medicals!")
    st.markdown("---")
    
    st.subheader("Rate Your Experience")
    
    rating_buttons = [
        ("🌟 Excellent", "#00ff00", "Excellent", 
         "https://g.page/r/CYs8l7uEbQo4EBM/review?utm_source=email&utm_medium=review_request&utm_campaign=excellent"),
        ("👍 Good", "#00aaff", "Good",
         "https://g.page/r/CYs8l7uEbQo4EBM/review?utm_source=email&utm_medium=review_request&utm_campaign=good"),
        ("😐 Average", "#cccc00", "Average",
         "https://forms.gle/9tSBdH7emrGxJ2Z39?utm_source=email&utm_medium=review_request&utm_campaign=average"),
        ("👎 Bad", "#cc6600", "Bad",
         "https://forms.gle/BXnXipFeZ29vStuQA?utm_source=email&utm_medium=review_request&utm_campaign=bad"),
        ("❌ Poor", "#cc0000", "Poor",
         "https://forms.gle/BXnXipFeZ29vStuQA?utm_source=email&utm_medium=review_request&utm_campaign=poor")
    ]
    
    # Create rating buttons and track clicks
    for label, color, rating, link in rating_buttons:
        btn = st.markdown(f"""
        <a href='{link}' target='_blank' onclick='trackRating("{rating}")'
           style='display: block; text-align: center; background-color: {color}; 
           padding: 14px; border-radius: 5px; color: black; 
           text-decoration: none; font-weight: bold; margin: 10px 0;'>
           {label}
        </a>
        """, unsafe_allow_html=True)
        
        # Track button press in session state
        if rating not in st.session_state:
            st.session_state[rating] = False

    # JavaScript to handle rating tracking
    st.markdown("""
    <script>
    function trackRating(rating) {
        fetch(`/proxy/track_rating?rating=${rating}`, {method: 'GET'});
    }
    </script>
    """, unsafe_allow_html=True)

    # Handle rating tracking endpoint
    query_params = st.experimental_get_query_params()
    if 'track_rating' in query_params:
        rating = query_params['track_rating'][0]
        update_rating_counts(rating)
        st.experimental_set_query_params()
    
    st.markdown("---")
    st.write("We hope you had a great experience with us! To show our appreciation, we’d like to offer you a FREE travel guide PDF for Thrissur, which includes:")
    
    st.markdown("""
    - **Commuting Tips**  
    - **Suggested Itinerary**  
    - **Top Places to Visit**  
    - **Best Restaurants**  
    - **And much more!**  
    """)
    
    st.write("We greatly appreciate your time and feedback, and we look forward to serving you again!")
    
    with st.form("customer_info"):
        name = st.text_input("Enter your name")
        email = st.text_input("Enter your email (optional) to receive the PDF")
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            if name:
                save_customer_info(name, email)
                st.success("Thank you! We will send you the travel guide PDF shortly.")
            else:
                st.error("Please enter your name to submit.")

if __name__ == "__main__":
    main()