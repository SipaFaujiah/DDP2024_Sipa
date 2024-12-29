import streamlit as st 

#st.title("Hello Masbro")
#st.write("Baik cuyyy")
#st.image("download.jpg", caption="ini gambar")

#Sidebar direktory
dashboard= st.Page("./Fitur/dashboard.py", title="Dashboard")
nabung = st.Page("./Fitur/nabung.py", title="Menabung")

pg=st.navigation(
    {
        "Menu Utama": [dashboard],
        "Transaksi":[nabung]
    }
)

if 'total_semua' not in st.session_state:
    st.session_state['total_semua'] =[]

pg.run()