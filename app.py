from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "asset" / "SAMUEL_RESUME.pdf"
profile_pic = current_dir / "asset" / "profile pic.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | SAMUEL BATAO"
PAGE_ICON = ":wave:"
CELLPHONE = "09664772804"

NAME = "ENGR.SAMUEL BATAO"
DESCRIPTION = """
ELECTRONIC ENGINEER AND TEAM LEADER TECHNICAL ENGINEER AND GOAL ORIENTED SEEKING LEARNING AND PROGRESS.
"""
EMAIL = "bataosamuel15@gmail.com"

PROJECTS = {

    "🏆 INFINERA DWDM PROJECT",

    "🏆 INFINERA CPE PROJECT",

    "🏆 CIENA CPE PROJECT",

}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<styles>{}</styles>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(CELLPHONE)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 3 Years expereince in Telecommunication industry
- ✔️ Good understanding in Networks designs
- ✔️ Good understanding in Customer Premises Equipment(CPE)
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader(" Skills")
st.write(
    """
- 👩‍💻 Programming: Python (pycharm)
- 📊 CPE Configuration: Gpon, AR617, AR614o, Ciena 3916
- 📚 Hybrid Technical: Site Survey, Installation, Provissioning, Migration
- 🗄️ Chatbot: ChatGPT
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Team Leader Technical Engineer | Digital Network Access**")
st.write("07/2023 - Present")
st.write("CPE CIENA Project")
st.write(
    """
- ► Train new Technical Engineer for deployment to site and client
- ► Configure Huawei and Ciena modem and Cisco Router
- ► Customer Premises Equipment Migration
"""
)


st.write("Technical Engineer / Digital Network Access ")
st.write("01/2022 - 06/2023")
st.write("CPE INFINERA Project")


st.write("Technical Engineer / Digital Network Access ")
st.write("03/2021 - 12/2022")
st.write("DWDM INFINERA Project")


# --- JOB 2


# --- JOB 3


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("PROJECT")
st.write("---")
st.write(PROJECTS)