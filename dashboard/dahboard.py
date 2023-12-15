import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Menyiapkan data
df_day = pd.read_csv("C:\\Users\\Sayur Untuk Santri.SUS\\STREAMLIT\\day.csv")
df_hour = pd.read_csv("C:\\Users\\Sayur Untuk Santri.SUS\\STREAMLIT\\hour.csv")
bike_sharing = df_day.merge(df_hour, on='dteday', how='inner', suffixes=('_daily', '_hourly'))

# Mengatur judul dan deskripsi aplikasi
st.title("Bike Sharing Data Analysis Dashboard")
st.write("by Ali Imron Nasrulloh")

# Menampilkan pertanyaan bisnis
st.header("Pertanyaan Bisnis:")
st.subheader("1. Bagaimana Hubungan Antara Season & Jumlah yang menyewa Sepeda dalam setiap harinya?")
st.write("Visualisasi 1: Jumlah Sewa Sepeda Harian Berdasarkan Musim")

# Visualisasi pertanyaan 1
seasonal_data = bike_sharing.groupby('season_daily')['cnt_daily'].mean().reset_index()
seasonal_data['season_name'] = ['Spring', 'Summer', 'Fall', 'Winter']
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='season_name', y='cnt_daily', data=seasonal_data, palette="viridis", ax=ax)
ax.set_title('Pengaruh Musim Terhadap Jumlah Sewa Sepeda Harian')
ax.set_xlabel('Musim')
ax.set_ylabel('Rata-rata Jumlah Sewa Harian')
st.pyplot(fig)

# Menampilkan pertanyaan bisnis lainnya
st.text("""
        Dari visualisasi di atas dapat kita lihat bahwa, jumlah yang sewa sepeda lebih banyak
        di musim gugur atau (fall) Kemudian Musim Panas (Summer)
        Poisis ketiga (Winter) Musim Dingin
        """)

# Menampilkan visualisasi Pertanyaan 2: Pola berdasarkan bulan dan jam
st.subheader("Pertanyaan 2: Pola Berdasarkan Bulan dan Jam")
# Mengatur warna palet
color_palette = sns.color_palette("husl", 12)  # Menggunakan palet warna "husl" dengan 12 warna

sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x="mnth_daily", y="cnt_daily", data=bike_sharing, ci=None, hue="yr_daily", palette=color_palette, linewidth=2, ax=ax)

# legend
ax.legend(title="Tahun", loc="upper left", bbox_to_anchor=(1, 1))

ax.set_title("Jumlah Sewa Sepeda Harian Berdasarkan Bulan")
ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Sewa Sepeda Harian")

ax.grid(axis="y", linestyle="--", alpha=0.7)

# Menyertakan plot ke dalam dashboard Streamlit
st.pyplot(fig)

# Menampilkan visualisasi Pertanyaan 2: Pola berdasarkan jam
st.subheader("Pertanyaan 2: Pola Berdasarkan Jam")
# Mengatur warna palet
sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x="hr", y="cnt_hourly", data=bike_sharing, ci=None, ax=ax)
ax.set_title("Jumlah Sewa Sepeda Harian berdasarkan Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Sewa Sepeda Harian")

# Menyertakan plot ke dalam dashboard Streamlit
st.pyplot(fig)
st.text('''
        Dari grafik di atas kita dapat menyimpulkan bahwa sewa sepeda lebih banyak
        pada bulan 6 dan bulan 9 Berdasarkan Jam jumlah sewa sepeda banyak terjadi
        antara jam 8 pagi dan jam 17 hingga jam 18
        ''')

# Menampilkan visualisasi Pertanyaan 3: Trend Penggunaan Sepeda di Hari Kerja dan Hari Libur
st.subheader("Pertanyaan 3: Trend Penggunaan Sepeda di Hari Kerja dan Hari Libur")
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="workingday_daily", y="cnt_daily", data=bike_sharing, ci=None, palette="muted", ax=ax)

ax.set_xlabel("Hari Libur (0)          Hari Kerja (1)")
ax.set_ylabel("Jumlah Sewa Sepeda Harian")
ax.set_title("Perbandingan Jumlah Peminjaman Sepeda antara Hari Kerja dan Hari Libur")

# Menyertakan plot ke dalam dashboard Streamlit
st.pyplot(fig)
st.text('''
        Berdasarkan hasil analisis, dapat disimpulkan bahwa bisnis sewa sepeda
        cenderung mengalami permintaan yang lebih tinggi pada hari kerja dibandingkan
        dengan hari libur.
        ''')

# Menampilkan kesimpulan dari analisis
st.header("Kesimpulan:")
st.write("Berikut adalah kesimpulan dari hasil analisis data.")
st.text('''
        1. Musim Gugur (Fall) Menjadi Pilihan Favorit:
        Jumlah sewa sepeda tertinggi terjadi pada musim gugur (Fall), diikuti oleh musim panas (Summer).
        Keputusan bisnis dapat mencakup peningkatan persediaan sepeda dan pelayanan terkait
        selama musim gugur, karena permintaan konsumen cenderung tinggi pada periode ini.''')

st.text('''
        2. Musim Semi (Spring) Memiliki Permintaan yang Lebih Rendah:
        Musim Semi (Spring) menunjukkan jumlah sewa yang lebih rendah dibandingkan musim lainnya.
        Bisnis dapat mempertimbangkan strategi khusus, seperti promosi musiman atau diskon, untuk
        meningkatkan minat sewa sepeda selama musim dingin.''')

st.text('''
        3. Strategi Pemasaran Terfokus pada Musim Gugur dan Musim Panas:
        Mengingat tingginya permintaan selama musim gugur dan musim panas, bisnis dapat mengalokasikan
        sumber daya pemasaran dan promosi lebih intensif pada periode ini.
        Penawaran spesial, paket bundel, atau acara-acara khusus dapat menarik lebih
        banyak pelanggan selama musim puncak.''')

# Menampilkan informasi kontak
st.header("Informasi Kontak:")
st.write("Nama: Ali Imron Nasrulloh")
st.write("Email: imronnasrulloh009@gmail.com")
st.write("Id Dicoding: imron_nasrulloh009")
