import streamlit as st
from PIL import Image
from didin import didin
from adina import adina


def main():
    st.title("Update Rekayasa Perangkat Lunak")
    menu = ["HOME", "DATA", "MEDIA", "ABOUT"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "HOME":
        st.text("""Saya adalah seorang programer yang saat ini sedang fokus dalam satu bahasa yaitu bahasa pemrograman Python.
                Menurut saya, bahasa pemrograman Python mudah untuk dipelajari.
        """)
        st.header("Rekayasa Perangkat Lunak")
        st.write("### PROFILE")
        st.image("2.png", caption="Photo Hanya Pemanis", use_column_width=True)

        st.write("Semua orang berpikir untuk mengubah dunia, tetapi tidak ada yang berpikir untuk mengubah dirinya sendiri")
        st.write("Jika hidup dapat diprediksi, itu akan berhenti menjadi hidup, dan menjadi tanpa rasa")
        st.write("jangan menghakimi diri sendiri sebagai sosok yang gagal kau sedang belajar dan dalam proses belajar kesalahan adalah mutlak")
        st.write("Keputusanmu, dan bukan kondisimu, yang menentukan takdirmu")

        social = ["Website", "Youtube", "Github", "Gmail"]
        Website = "https://mechanic-91.com/index.html"
        Youtube = "https://youtube.com/@softwaremechanical?si=cOO-lYPYuhHZf-ag"
        Github = "https://h7zgopizvkfg7otwzcfofq.streamlit.app/"
        Gmail = "adinaajha335@gmail.com"

        with st.expander("Links Metode Pembelajaran"):
            a = st.selectbox("Sosial", social)
            if a == "Website":
                st.write(Website)
            elif a == "Youtube":
                st.write(Youtube)
            elif a == "Github":
                st.write(Github)
            elif a == "Gmail":
                st.write(Gmail)
        st.image("dd.jpg", caption="Photo Hanya Pemanis", use_column_width=True)
        st.write("##")
        st.write("Silahkan Kunjungi link dibawah ini https://adinaajha.github.io/memory/")
        st.write("Silahkan Kunjungi link dibawah ini https://mechanic-91.com/index.html")
        st.write("Silahkan Kunjungi link dibawah ini https://youtube.com/@softwaremechanical?si=cOO-lYPYuhHZf-ag")
        st.write("Silahkan Kunjungi link dibawah ini adinaajha335@gmail.com")
        st.write("Silahkan Kunjungi link dibawah ini https://h7zgopizvkfg7otwzcfofq.streamlit.app/")
    elif choice == "DATA":
        didin()
    elif choice == "MEDIA":
        adina()
    else:
        st.header("Rekayasa Perangkat Lunak")
        st.write("### Adina - Manipulasi modul")
        st.image("dd.jpg", caption="Photo Hanya Pemanis", use_column_width=True)

        st.write("""Saya adalah seorang programer yang saat ini sedang fokus dalam satu bahasa yaitu bahasa pemrograman Python.

        """)

        social = ["Website", "Youtube", "Github", "Gmail"]
        Website = "https://mechanic-91.com/index.html"
        Youtube = "https://youtube.com/@softwaremechanical?si=cOO-lYPYuhHZf-ag"
        Github = "https://h7zgopizvkfg7otwzcfofq.streamlit.app/"
        Gmail = "adinaajha335@gmail.com"

        with st.expander("Links Metode Pembelajaran"):
            a = st.selectbox("Sosial", social)
            if a == "Website":
                st.write(Website)
            elif a == "Youtube":
                st.write(Youtube)
            elif a == "Github":
                st.write(Github)
            elif a == "Gmail":
                st.write(Gmail)

if __name__ == "__main__":
    main()
