import streamlit as st
import time
from streamlit_extras.switch_page_button import switch_page

# Typing Animation Without Rerun Issue
def typing_animation(text, speed=0.05):
    placeholder = st.empty()  # Placeholder for updating text dynamically
    displayed_text = ""
    for char in text:
        displayed_text += char
        placeholder.markdown(f"## {displayed_text}")
        time.sleep(speed)

# Main Portfolio Function
def main():
    st.set_page_config(page_title="My Portfolio", page_icon="🎨", layout="wide")

    # CSS Styling for Animations & UI
    st.markdown("""
        <style>
            @keyframes fadeIn {
                from {opacity: 0;}
                to {opacity: 1;}
            }
            @keyframes bounce {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-10px); }
            }
            .fade-in { animation: fadeIn 2s; }
            .bounce { animation: bounce 1.5s infinite; }
            .header {
                font-size: 45px;
                font-weight: bold;
                color: #FF5733;
                text-align: center;
            }
            .sub-header {
                font-size: 30px;
                color: #3498DB;
                text-align: center;
                margin-top: -15px;
            }
            .profile-pic {
                display: flex;
                justify-content: center;
                margin-top: 20px;
            }
            .social-links {
                text-align: center;
                margin-top: 20px;
            }
            .social-links a {
                margin: 0 10px;
                text-decoration: none;
                font-size: 24px;
            }
            .university-section {
                text-align: center;
                margin-top: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Portfolio Header with Animation
    st.markdown("<div class='header fade-in'>👋 Welcome to My Portfolio</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header bounce'>Mobile App Developer | AI Enthusiast | Innovator</div>", unsafe_allow_html=True)

    # Adding a Profile Picture (Optional)
    st.markdown("<div class='profile-pic'><img src='https://avatars.githubusercontent.com/u/9919?v=4' width='150' style='border-radius:50%;'></div>", unsafe_allow_html=True)

    # Typing Effect for Introduction with University Logo
    if "intro_done" not in st.session_state:
        typing_animation("I am a passionate Developer 🚀")
        typing_animation("Graduated from Zamindar PG College, Gujrat 🎓 Affiliated with University of Sargodha (UOS)")

        # Display UOS Logo (Replace with actual image URL or upload locally)
        st.markdown("""
        <div class="university-section">
            <img src="st.image("C:/Users/Eden Computers/Desktop/streamliy/uos_logo.jpeg", width=200)
" width="150">
        </div>
        """, unsafe_allow_html=True)

        st.session_state["intro_done"] = True
    else:
        st.markdown("## I am a passionate Developer 🚀")
        st.markdown("### 🎓 Graduated BS (hons 4 year) Computer Science  from Zamindar PG College, Affiliated with University of Sargodha")

        # Display UOS Logo Again
        st.image("uoslogo.jpeg", width=150)


    # Sidebar Navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["🏠 Home", "📂 Projects", "📬 Contact"])

    # Home Page
    if page == "🏠 Home":
        st.markdown("### About Me")
        st.write("🚀 I am a **Mobile App Developer** specializing in **Python, Java, XML, and AI-driven applications**.")
        st.write("💡 Passionate about **building interactive applications**, AI models, and scalable cloud solutions.")
        st.write("🔥 Experienced in **Streamlit, React, Flask, Firebase, and Google Cloud, Web Development**.")

        # Social Links Section
        st.markdown("""
        <div class="social-links">
            <a href="mailto:youremail@example.com" target="_blank">📧 Email</a> |
            <a href="http://www.linkedin.com/in/hira-nawaz-544632348" target="_blank">🔗 LinkedIn</a> |
            <a href="https://github.com/HiraNawaz2415" target="_blank">🐙 GitHub</a>
        </div>
        """, unsafe_allow_html=True)

    # Projects Page
    elif page == "📂 Projects":
        st.markdown("### 🛠️ My Projects")
        st.markdown("""
        - 📱 **Fitness Tracking App** – Step counter, workout planner & nutrition tracker.  
        - 🤖 **AI Chatbot** – Smart assistant for answering health & fitness queries.  
        - 🍎 **Web-based Nutrition Tracker** – Meal logging & calorie tracking using AI.  
        """)

    # Contact Page
    elif page == "📬 Contact":
        st.markdown("### ✉️ Get in Touch")
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")
            submit = st.form_submit_button("Send")
            if submit:
                st.success("✅ Message Sent Successfully! I'll get back to you soon.")

# Run the App
if __name__ == "__main__":
    main()
