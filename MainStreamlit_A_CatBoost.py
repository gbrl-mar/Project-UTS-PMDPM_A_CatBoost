import streamlit as st
import pickle
import os

def load_model(model_file):
    model_directory = r'D:\Kuliah UAJY\Semester 5\Pembelajaran Mesin\Project UTS PMDPM_A_CatBoost'
    model_path = os.path.join(model_directory, model_file)
    with open(model_path, 'rb') as f:
        return pickle.load(f)

def kelas_app():
    rf_model = load_model('BestModel_CLF_GBT_CatBoost.pkl')
    
    st.title("Prediksi Jenis Rumah")
    st.write("Aplikasi ini membantu user untuk mengecek jenis rumah yang ingin dibeli")

    squaremeters = st.number_input("Luas (m2)", min_value=0)
    numberofrooms = st.number_input("Jumlah Kamar", min_value=0)
    hasyard = st.selectbox("Apakah Ada Halaman?", ["yes", "no"])
    haspool = st.selectbox("Apakah Ada Kolam Renang?", ["yes", "no"])
    floors = st.number_input("Jumlah Lantai", min_value=0)
    citycode = st.number_input("Kode Kota", min_value=0)
    citypartrange = st.number_input("Rentang Partisi Kota", min_value=0)
    numprevowners = st.number_input("Jumlah Pemilik Sebelumnya", min_value=0)
    made = st.number_input("Tahun Dibuat", min_value=1900, max_value=2024)
    isnewbuilt = st.selectbox("Apakah Baru Dibangun?", ["yes", "no"])
    hasstormprotector = st.selectbox("Apakah Ada Pelindung Badai?", ["yes", "no"])
    basement = st.number_input("luas Basement?")
    attic = st.number_input("attic? M2")
    garage = st.number_input("Luas Garasi?")
    hasstorageroom = st.selectbox("Apakah Ada Ruang Penyimpanan?", ["yes", "no"])
    hasguestroom = st.number_input("Berapa Kamar Tamu?")

    input_hasyard = 1 if hasyard == "yes" else 0
    input_haspool = 1 if haspool == "yes" else 0
    input_isnewbuilt = 1 if isnewbuilt == "yes" else 0
    input_hasstormprotector = 1 if hasstormprotector == "yes" else 0
    input_hasstorageroom = 1 if hasstorageroom == "yes" else 0

    input_data = [[squaremeters, numberofrooms, input_hasyard, input_haspool, floors, citycode, citypartrange,
                   numprevowners, made, input_isnewbuilt, input_hasstormprotector, basement, attic, garage,
                   input_hasstorageroom, hasguestroom]]

    st.write("Data yang akan diinput ke model")
    st.write(input_data)

    if st.button("Prediksi"):
        rf_model_prediction = rf_model.predict(input_data)
        outcome = {'Basic':'Basic', 'Luxury':'Luxury', 'Middle':'Middle'}
        st.write(f"Property tersebut merupakan kelas :  **{outcome[rf_model_prediction[0]]}**")

def kelas2_app():
    rf_model = load_model('BestModel_REG_RR_CatBoost.pkl')

    st.title("Prediksi Harga Rumah")
    st.write("Aplikasi ini membantu user untuk mengecek estimasi harga rumah")

    squaremeters = st.number_input("Luas (m2)", min_value=0)
    numberofrooms = st.number_input("Jumlah Kamar", min_value=0)
    hasyard = st.selectbox("Apakah Ada Halaman?", ["yes", "no"])
    haspool = st.selectbox("Apakah Ada Kolam Renang?", ["yes", "no"])
    floors = st.number_input("Jumlah Lantai", min_value=0)
    citycode = st.number_input("Kode Kota", min_value=0)
    citypartrange = st.number_input("Rentang Partisi Kota", min_value=0)
    numprevowners = st.number_input("Jumlah Pemilik Sebelumnya", min_value=0)
    made = st.number_input("Tahun Dibuat", min_value=1900, max_value=2024)
    isnewbuilt = st.selectbox("Apakah Baru Dibangun?", ["yes", "no"])
    hasstormprotector = st.selectbox("Apakah Ada Pelindung Badai?", ["yes", "no"])
    basement = st.number_input("Luas Basement (m2)", min_value=0)
    attic = st.number_input("Luas Attic (m2)", min_value=0)
    garage = st.number_input("Luas Garasi (m2)", min_value=0)
    hasstorageroom = st.selectbox("Apakah Ada Ruang Penyimpanan?", ["yes", "no"])
    hasguestroom = st.number_input("Berapa Kamar Tamu?", min_value=0)

    input_hasyard = 1 if hasyard == "yes" else 0
    input_haspool = 1 if haspool == "yes" else 0
    input_isnewbuilt = 1 if isnewbuilt == "yes" else 0
    input_hasstormprotector = 1 if hasstormprotector == "yes" else 0
    input_hasstorageroom = 1 if hasstorageroom == "yes" else 0

    input_data = [[squaremeters, numberofrooms, input_hasyard, input_haspool, floors, citycode, citypartrange,
                   numprevowners, made, input_isnewbuilt, input_hasstormprotector, basement, attic, garage,
                   input_hasstorageroom, hasguestroom]]

    st.write("Data yang akan diinput ke model:")
    st.write(input_data)

    if st.button("Prediksi"):
        rf_model_prediction = rf_model.predict(input_data)
        formatted_price = "${:,.2f}".format(rf_model_prediction[0])
        st.write(f"Hasil prediksi model: {formatted_price}")

st.sidebar.title("Menu")
app_selection = st.sidebar.radio("Pilih Aplikasi", ("Prediksi Jenis Rumah", "Prediksi Harga Rumah"))

if app_selection == "Prediksi Jenis Rumah":
    kelas_app()
else:
    kelas2_app()
