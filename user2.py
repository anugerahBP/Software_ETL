import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Fungsi untuk membaca file dan mengembalikan dataframe
def load_data(file):
    if file.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.endswith('.xlsx'):
        df = pd.read_excel(file, engine='openpyxl')
    else:
        st.write("File tidak valid!")
        return None
    return df

# Fungsi untuk melakukan ETL
def process_data(df, selected_cols):
    # Memilih kolom yang dipilih oleh pengguna
    df_selected = df[selected_cols]
    
    # Transformasi data di sini (jika diperlukan)
    
    # Melakukan load data ke file CSV
    df_selected.to_csv('processed_data.csv', index=False)
    
    return df_selected

# Fungsi untuk menampilkan tabel
def show_table(df):
    st.write(df)

# Fungsi untuk menampilkan diagram batang
def show_bar_chart(df, x_col, y_col):
    fig, ax = plt.subplots()
    ax.bar(df[x_col], df[y_col])
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    st.pyplot(fig)

# Fungsi untuk menampilkan diagram garis
def show_line_chart(df, x_col, y_col):
    fig, ax = plt.subplots()
    ax.plot(df[x_col], df[y_col])
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    st.pyplot(fig)

# Main program
def main():
    st.title("Sistem Informasi Dashboard")
    
    # Mengambil file dari pengguna
    uploaded_file = st.file_uploader("Pilih file", type=['csv', 'xlsx'])
    if uploaded_file is not None:
        df = load_data(uploaded_file.name)
        
        # Mengambil kolom yang dipilih oleh pengguna
        selected_cols = st.multiselect("Pilih kolom", df.columns)
        if len(selected_cols) > 0:
            df_selected = process_data(df, selected_cols)
            show_table(df_selected)
            
            # Mengambil kolom yang dipilih untuk diagram batang
            x_col = st.selectbox("Pilih kolom untuk sumbu X pada diagram batang", df_selected.columns)
            y_col = st.selectbox("Pilih kolom untuk sumbu Y pada diagram batang", df_selected.columns)
            df[x_col] = df[x_col].astype(str)
            show_bar_chart(df_selected, x_col, y_col)
            
            # Mengambil kolom yang dipilih untuk diagram garis
            x_col = st.selectbox("Pilih kolom untuk sumbu X pada diagram garis", df_selected.columns)
            y_col = st.selectbox("Pilih kolom untuk sumbu Y pada diagram garis", df_selected.columns)
            show_line_chart(df_selected, x_col, y_col)

if __name__ == '__main__':
    main()
