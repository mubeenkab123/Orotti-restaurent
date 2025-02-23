import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# --- Google Sheets Setup ---
def connect_to_gsheet():
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]
    
    # Debug: Print secrets
    st.write("Secrets:", st.secrets["gsheet"])
    
    # Use Streamlit secrets for credentials
    creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gsheet"], scope)
    return gspread.authorize(creds)
# Your specific Google Sheet ID from the URL
SPREADSHEET_ID = "1a_zt-I3cyjeQ5VlPRLifXyWVDHmg4cAx4jEXsclm7qw"

def save_customer_info(name, email):
    """Save customer info to Google Sheet"""
    try:
        client = connect_to_gsheet()
        sheet = client.open_by_key(SPREADSHEET_ID).worksheet("Customers")
        sheet.append_row([name, email])
    except Exception as e:
        st.error(f"Error saving data: {str(e)}")

def update_rating_counts(rating):
    """Update rating counts in Google Sheet"""
    try:
        client = connect_to_gsheet()
        sheet = client.open_by_key(SPREADSHEET_ID).worksheet("Ratings")
        
        # Find and update the rating count
        cell = sheet.find(rating)
        current_count = int(sheet.cell(cell.row, 2).value)
        sheet.update_cell(cell.row, 2, current_count + 1)
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
    
    # Create rating buttons with proper parameter tracking
    for label, color, rating, link in rating_buttons:
        st.markdown(f"""
        <a href='{link}' target='_blank' onclick='trackRating("{rating}")'
           style='display: block; text-align: center; background-color: {color}; 
           padding: 14px; border-radius: 5px; color: black; 
           text-decoration: none; font-weight: bold; margin: 10px 0;'
           onmouseover="this.style.opacity=0.8" onmouseout="this.style.opacity=1">
           {label}
        </a>
        """, unsafe_allow_html=True)

    # JavaScript to track rating clicks
    st.markdown("""
    <script>
    function trackRating(rating) {
        // Add temporary query parameter
        const url = new URL(window.location);
        url.searchParams.set('track_rating', rating);
        window.history.replaceState({}, '', url);
        
        // Send beacon to ensure tracking
        navigator.sendBeacon(window.location.href);
    }
    </script>
    """, unsafe_allow_html=True)

    # Handle rating tracking
    if "track_rating" in st.query_params:
        rating = st.query_params["track_rating"]
        update_rating_counts(rating)
        st.query_params.update(track_rating=None)

    st.markdown("---")
    st.write("We hope you had a great experience with us! To show our appreciation, we’d like to offer you a FREE travel guide PDF for Thrissur, which includes:")
    
    st.markdown("""
    - **Commuting Tips**  
    - **Suggested Itinerary**  
    - **Top Places to Visit**  
    - **Best Restaurants**  
    - **And much more!**  
    """)
    
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
