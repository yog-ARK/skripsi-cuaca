# 🌦️ Klasifikasi Cuaca Menggunakan Algoritma Random Forest

Aplikasi berbasis **Streamlit** yang dikembangkan sebagai implementasi penelitian skripsi untuk melakukan klasifikasi kondisi cuaca menggunakan algoritma **Random Forest**. Aplikasi ini menyediakan visualisasi data cuaca, evaluasi performa model menggunakan **K-Fold Cross Validation**, serta klasifikasi data cuaca baru melalui antarmuka web yang interaktif.

---

## 🌐 Demo Online

Aplikasi ini juga dapat diakses langsung melalui browser tanpa perlu instalasi, melalui tautan berikut:

🔗 https://skripsiyoga.streamlit.app

Aplikasi di-hosting menggunakan **Streamlit Community Cloud (tingkat gratis)**, sehingga aplikasi akan otomatis masuk ke mode **sleep (hibernasi)** apabila tidak ada pengunjung selama beberapa waktu. Hal ini bertujuan untuk menghemat resource server pada platform tersebut, bukan karena aplikasi mengalami error.

Apabila saat membuka tautan di atas muncul halaman bertuliskan **"Zzz... This app has gone to sleep"**, aplikasi dapat dibangunkan kembali dengan langkah berikut:

1. Klik tombol **"Yes, get this app back up!"** yang muncul pada halaman tersebut.
2. Tunggu beberapa saat (biasanya kurang dari satu menit) hingga aplikasi selesai dimuat ulang.
3. Aplikasi akan berjalan normal kembali setelah proses wake up selesai.

---

## ✨ Fitur

- 📊 Visualisasi data cuaca.
- 🌤️ Menampilkan informasi data cuaca.
- 🤖 Klasifikasi data cuaca baru menggunakan model Random Forest.
- 📈 Visualisasi hasil evaluasi model meliputi:
  - K-Fold Cross Validation
  - Confusion Matrix
  - Accuracy
  - Precision
  - Recall
  - F1-Score
- 📁 Import data cuaca dalam format Microsoft Excel.

---

## 🛠️ Teknologi

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib
- OpenPyXL
- Matplotlib
- Plotly

---

## 📂 Struktur Proyek

```text
skripsi-cuaca/
│
├── backup/                     # File cadangan (salinan dataset untuk keperluan re-train)
│   ├── data_preprocessed.xlsx
│   ├── fold_1.xlsx
│   ├── fold_2.xlsx
│   ├── fold_3.xlsx
│   ├── fold_4.xlsx
│   ├── fold_5.xlsx
│   ├── model_fold_1.pkl
│   ├── model_fold_2.pkl
│   ├── model_fold_3.pkl
│   ├── model_fold_4.pkl
│   ├── model_fold_5.pkl
│   └── model_full.pkl
│
├── pages/                      # Halaman aplikasi Streamlit
│   ├── 01_About.py
│   └── 02_Kelola_Data.py
│
├── 535220247_Program.py        # Program utama
├── training.py                 # Pelatihan model
├── Olah_Data.ipynb             # Notebook preprocessing dan eksperimen
│
├── model_full.pkl              # Model akhir
├── model_fold_1.pkl
├── model_fold_2.pkl
├── model_fold_3.pkl
├── model_fold_4.pkl
├── model_fold_5.pkl
│
├── fold_1.xlsx
├── fold_2.xlsx
├── fold_3.xlsx
├── fold_4.xlsx
├── fold_5.xlsx
│
├── Logbook Cuaca.xlsx          # Dataset utama
├── data_preprocessed.xlsx      # Dataset hasil preprocessing
├── data_baru.xlsx              # Dataset untuk pengujian
│
├── requirements.txt
└── README.md
```

---

## 📥 Instalasi

### 1. Clone repository

```bash
git clone https://github.com/yog-ARK/skripsi-cuaca.git
```

Masuk ke folder proyek.

```bash
cd skripsi-cuaca
```

---

### 2. Install seluruh dependency

```bash
pip install -r requirements.txt
```

---

## ▶️ Menjalankan Aplikasi

Jalankan aplikasi menggunakan perintah berikut.

```bash
streamlit run 535220247_Program.py
```

Secara otomatis browser akan membuka aplikasi pada alamat:

```text
http://localhost:8501
```

---

## 📊 Dataset

Repository ini menyertakan dataset yang digunakan selama penelitian, meliputi:

- Dataset utama (`Logbook Cuaca.xlsx`)
- Dataset hasil preprocessing (`data_preprocessed.xlsx`)
- Dataset untuk pengujian (`data_baru.xlsx`)
- Dataset pembagian K-Fold Cross Validation (`fold_1.xlsx` sampai `fold_5.xlsx`)

Seluruh dataset digunakan hanya untuk keperluan penelitian akademik dalam penyusunan skripsi.

---

## ⚖️ Sumber Data dan Kepatuhan terhadap *Terms of Use*

Data cuaca pada penelitian ini **dikumpulkan secara manual** setiap hari dengan mencatat informasi cuaca yang ditampilkan pada aplikasi **The Weather Channel**. Seluruh proses pengumpulan data dilakukan oleh penulis tanpa menggunakan perangkat lunak maupun metode otomatis.

Repository ini **tidak menggunakan** teknik:

- Web Crawling
- Web Scraping
- Automated Data Extraction
- Bot
- Spider
- Crawler
- Metode otomatis lainnya untuk memperoleh data dari layanan The Weather Channel.

Hal tersebut dilakukan sebagai bentuk kepatuhan terhadap **Terms of Use** milik The Weather Channel. Berdasarkan ketentuan penggunaan layanan, pengguna tidak diperbolehkan mengakses, memantau, menyalin, ataupun mengambil data dari layanan menggunakan **robot, spider, scraper, crawler, maupun perangkat otomatis lainnya tanpa izin tertulis** dari penyedia layanan.

Informasi lengkap dapat dilihat pada:

https://weather.com/privacy/terms-of-use

Dengan demikian, seluruh dataset pada repository ini merupakan hasil pencatatan manual oleh penulis dan digunakan semata-mata untuk kepentingan penelitian akademik.

---

## 📖 Manual Penggunaan

Panduan penggunaan aplikasi tersedia pada dokumen **Manual Penggunaan** yang disertakan bersama proyek.

---

## 👨‍🎓 Penulis

**Yoga Ramadhani Kabakora**

Program Studi Teknik Informatika  
Fakultas Teknologi Informasi  
Universitas Tarumanagara

---

## 📜 Lisensi

Repository ini dibuat sebagai bagian dari penelitian skripsi dan dipublikasikan untuk keperluan akademik serta pembelajaran.

Apabila menggunakan sebagian kode atau materi dari repository ini, harap mencantumkan atribusi kepada penulis.
