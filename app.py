import streamlit as st
import datetime
import socket


st.title("DEMO SITE")
st.write("The Site is Loaded from contanier havaing ID: ")
st.subheader(socket.gethostname())


col1, col2 = st.beta_columns(2)
with col1:
    st.image("https://www.biography.com/.image/c_fit%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_620/MTQ4MDU5NDU0MzgwNzEzNDk0/lionel_messi_photo_josep_lago_afp_getty_images_664928892_resizedjpg.jpg", width=300)
    if st.button("Like Messi"):
      st.image("https://i2.wp.com/www.9sportpro.com/wp-content/uploads/2018/06/31E51647-9F5B-4580-901F-02049B0F155E.jpeg?fit=634%2C761&ssl=1", width=355)

with col2:
    st.image("https://images-na.ssl-images-amazon.com/images/I/81KjxAq%2BcoL._SL1500_.jpg", width=355)
    if st.button("Like Ronaldo"):
        st.image("https://thumbs.dreamstime.com/z/no-goat-sign-vector-illustratioon-white-background-warning-112398430.jpg", width=355)
 


