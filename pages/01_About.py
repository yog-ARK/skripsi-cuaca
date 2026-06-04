import streamlit as st

st.set_page_config(
    page_title="Tentang Aplikasi — Klasifikasi Cuaca DKI Jakarta",
    page_icon="🌤️",
    layout="wide",
)

# ─── JUDUL ─────────────────────────────────────────────────────────────────────
st.title("🌤️ Tentang Aplikasi")
st.markdown("---")

# ─── IDENTITAS ─────────────────────────────────────────────────────────────────
st.markdown("""
<div style="background: linear-gradient(135deg, #0369a1 0%, #0ea5e9 100%);
            border-radius: 16px; padding: 32px 36px; color: white; margin-bottom: 8px;">
    <div style="font-size: 13px; letter-spacing: 2px; text-transform: uppercase;
                opacity: 0.8; margin-bottom: 6px;">Skripsi · 2026</div>
    <div style="font-size: 20px; font-weight: 700; line-height: 1.4; margin-bottom: 20px;">
        Sistem Klasifikasi Cuaca DKI Jakarta Menggunakan Algoritma Random Forest
        dengan Evaluasi K-Fold Cross Validation
    </div>
    <div style="display: flex; gap: 40px; flex-wrap: wrap;">
        <div>
            <div style="font-size: 11px; opacity: 0.7; margin-bottom: 2px;">NAMA</div>
            <div style="font-size: 16px; font-weight: 600;">Yoga Ramadhani Kabakora</div>
        </div>
        <div>
            <div style="font-size: 11px; opacity: 0.7; margin-bottom: 2px;">NIM</div>
            <div style="font-size: 16px; font-weight: 600;">535220247</div>
        </div>
        <div>
            <div style="font-size: 11px; opacity: 0.7; margin-bottom: 2px;">PROGRAM STUDI</div>
            <div style="font-size: 16px; font-weight: 600;">Teknik Informatika</div>
        </div>
        <div>
            <div style="font-size: 11px; opacity: 0.7; margin-bottom: 2px;">UNIVERSITAS</div>
            <div style="font-size: 16px; font-weight: 600;">Universitas Tarumanagara</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── DOSEN PEMBIMBING ──────────────────────────────────────────────────────────
col_dsn1, col_dsn2 = st.columns(2)
with col_dsn1:
    st.markdown("""
<div style="border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px 24px;
            background: linear-gradient(135deg, #0369a1 0%, #0ea5e9 100%);">
    <div style="font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase;
                color: rgba(255,255,255,0.7); margin-bottom: 8px;">Dosen Pembimbing I</div>
    <div style="font-size: 17px; font-weight: 700; color: white; line-height: 1.3;">
        Prof. Dr. Ir. Dyah Erny Herwindiati, M.Si.
    </div>
</div>
""", unsafe_allow_html=True)

with col_dsn2:
    st.markdown("""
<div style="border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px 24px;
            background: linear-gradient(135deg, #0369a1 0%, #0ea5e9 100%);">
    <div style="font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase;
                color: rgba(255,255,255,0.7); margin-bottom: 8px;">Dosen Pembimbing II</div>
    <div style="font-size: 17px; font-weight: 700; color: white; line-height: 1.3;">
        Novario Jaya Perdana, S.Kom., M.T.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ─── TENTANG APLIKASI ──────────────────────────────────────────────────────────
st.header("💡 Tentang Aplikasi")
st.write(
    "Aplikasi ini dibuat sebagai bagian dari penelitian skripsi untuk mengklasifikasikan "
    "kondisi cuaca di lima wilayah administratif DKI Jakarta — yaitu Jakarta Barat, Pusat, "
    "Selatan, Timur, dan Utara — menggunakan teknologi *machine learning*."
)
st.write(
    "Cuaca di DKI Jakarta tidak selalu seragam antar wilayah. Jakarta Utara yang dekat laut "
    "bisa berbeda kondisinya dengan Jakarta Selatan yang lebih tinggi dan hijau. "
    "Aplikasi ini membantu memvisualisasikan perbedaan tersebut, mengevaluasi seberapa akurat "
    "model dalam mengenali pola cuaca, serta memprediksi kondisi cuaca dari data observasi baru."
)

st.subheader("Siapa yang bisa menggunakan aplikasi ini?")
st.write(
    "Aplikasi ini ditujukan untuk siapa saja yang ingin memahami pola cuaca DKI Jakarta "
    "secara visual dan interaktif — baik mahasiswa, peneliti, maupun masyarakat umum "
    "yang penasaran dengan kondisi cuaca antar wilayah di Jakarta."
)

st.markdown("---")

# ─── PANDUAN PENGGUNAAN ────────────────────────────────────────────────────────
st.header("🗺️ Panduan Penggunaan")
st.write("Aplikasi ini terdiri dari beberapa bagian yang bisa diakses dari halaman utama.")

panduan = {
    "📊 Data Cuaca": (
        "Menampilkan seluruh data observasi cuaca yang telah dikumpulkan. "
        "Bisa difilter berdasarkan lokasi, tanggal, waktu, dan jenis cuaca. "
        "Tersedia juga fitur untuk melihat kapan cuaca berbeda antar wilayah Jakarta pada waktu yang sama."
    ),
    "📈 Analisis Distribusi": (
        "Membandingkan jumlah data cuaca yang benar-benar terjadi dengan jumlah yang diprediksi "
        "oleh model untuk setiap kategori cuaca, ditampilkan dalam bentuk diagram batang."
    ),
    "🔍 Evaluasi Model": (
        "Menampilkan detail hasil pengujian model per fold, termasuk tabel prediksi benar/salah, "
        "nilai akurasi, dan confusion matrix yang menggambarkan pola kesalahan model."
    ),
    "📋 Ringkasan Evaluasi": (
        "Merangkum nilai rata-rata akurasi, presisi, recall, dan F1-Score dari seluruh pengujian "
        "dalam satu tampilan yang ringkas."
    ),
    "🔎 Perbandingan Hasil Klasifikasi": (
        "Menggabungkan seluruh hasil prediksi dan memudahkan analisis prediksi yang tepat "
        "maupun yang meleset, dengan filter yang bisa dikombinasikan secara bebas."
    ),
    "🔮 Klasifikasi Data Baru": (
        "Fitur utama aplikasi: masukkan data observasi cuaca baru, dan model akan memprediksi "
        "kondisi cuacanya beserta tingkat keyakinan untuk setiap kategori."
    ),
}

for judul, deskripsi in panduan.items():
    with st.expander(judul):
        st.write(deskripsi)

st.markdown("---")

# ─── TENTANG DATA ──────────────────────────────────────────────────────────────
st.header("🗂️ Tentang Data")

col_d1, col_d2, col_d3 = st.columns(3)
col_d1.metric("Total Observasi", "960 baris")
col_d2.metric("Periode Pengumpulan", "4 Feb – 10 Mei 2026")
col_d3.metric("Frekuensi Pencatatan", "2× sehari")

st.write(
    "Data dikumpulkan secara manual dari aplikasi cuaca pada pukul **09.00 WIB** dan **15.00 WIB** "
    "setiap harinya, mencakup lima wilayah administratif DKI Jakarta. "
    "Setiap pengamatan mencatat suhu, kelembapan, kecepatan angin, intensitas UV, "
    "dan kondisi cuaca saat itu."
)
st.write(
    "Ada enam kategori cuaca yang dikenali: "
    "**Badai Petir**, **Berawan**, **Cerah**, **Embun**, **Hujan**, dan **Kabut Asap**."
)

st.subheader("🌐 Sumber Data Meteorologi")
st.write(
    "Data meteorologi pada aplikasi ini bersumber dari layanan **The Weather Channel / weather.com**. "
    "Seluruh data diperoleh melalui **observasi dan pencatatan manual** — bukan melalui metode otomatis "
    "atau pengambilan data secara programatik."
)
st.markdown(
    "🔗 [The Weather Channel — weather.com](https://weather.com)",
    unsafe_allow_html=False,
)

st.markdown("---")

# ─── PERATURAN PENGGUNAAN DATA ─────────────────────────────────────────────────
st.header("⚖️ Peraturan Penggunaan Data")

st.markdown("""
<div style="background: linear-gradient(135deg, #1e3a5f 0%, #1e4976 100%);
            border-left: 5px solid #0ea5e9;
            border-radius: 12px; padding: 24px 28px; color: white; margin-bottom: 16px;">
    <div style="font-size: 15px; font-weight: 700; margin-bottom: 10px;">
        📌 Tujuan Penggunaan Data
    </div>
    <div style="font-size: 14px; line-height: 1.7; opacity: 0.92;">
        Data yang digunakan dalam aplikasi ini <strong>hanya diperuntukkan untuk kepentingan
        penelitian dan visualisasi akademik</strong> dalam rangka penyusunan skripsi di
        Universitas Tarumanagara. Data tidak digunakan untuk tujuan komersial, distribusi
        publik, atau kepentingan di luar lingkup akademik yang telah ditetapkan.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background: linear-gradient(135deg, #7f1d1d 0%, #991b1b 100%);
            border-left: 5px solid #ef4444;
            border-radius: 12px; padding: 24px 28px; color: white; margin-bottom: 16px;">
    <div style="font-size: 15px; font-weight: 700; margin-bottom: 10px;">
        🚫 Larangan Pengambilan Data Otomatis
    </div>
    <div style="font-size: 14px; line-height: 1.7; opacity: 0.92;">
        Pengguna aplikasi ini <strong>dilarang keras</strong> melakukan <em>crawling</em>,
        <em>scraping</em>, <em>automated extraction</em>, atau metode pengambilan data secara
        otomatis dalam bentuk apapun dari layanan <strong>The Weather Channel / weather.com</strong>.
        Tindakan tersebut merupakan pelanggaran terhadap <em>Terms of Use</em> resmi The Weather
        Channel dan dapat berakibat pada konsekuensi hukum.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background: linear-gradient(135deg, #14532d 0%, #166534 100%);
            border-left: 5px solid #22c55e;
            border-radius: 12px; padding: 24px 28px; color: white; margin-bottom: 8px;">
    <div style="font-size: 15px; font-weight: 700; margin-bottom: 10px;">
        ✅ Metode Pengumpulan yang Digunakan
    </div>
    <div style="font-size: 14px; line-height: 1.7; opacity: 0.92;">
        Seluruh data dalam penelitian ini dikumpulkan secara <strong>manual</strong> melalui
        pencatatan langsung dari aplikasi cuaca pada waktu-waktu yang telah ditentukan
        (pukul 09.00 WIB dan 15.00 WIB), sesuai dengan ketentuan yang diperbolehkan oleh
        penyedia layanan.
    </div>
</div>
""", unsafe_allow_html=True)

st.caption(
    "📄 Referensi: [The Weather Channel — Terms of Use](https://weather.com/privacy/terms-of-use)"
)

st.markdown("---")

# ─── TENTANG METODE ────────────────────────────────────────────────────────────
st.header("⚙️ Tentang Metode")

col_m1, col_m2 = st.columns(2)

with col_m1:
    st.subheader("🌳 Random Forest")
    st.write(
        "Random Forest adalah metode *machine learning* yang bekerja dengan membangun "
        "banyak 'pohon keputusan' secara bersamaan. Setiap pohon belajar dari bagian data "
        "yang berbeda-beda secara acak, lalu semua pohon memberikan suara untuk menentukan "
        "hasil akhir — seperti sistem voting. "
        "Hasilnya lebih akurat dan stabil dibandingkan hanya mengandalkan satu pohon keputusan saja."
    )

with col_m2:
    st.subheader("🔁 K-Fold Cross Validation")
    st.write(
        "K-Fold Cross Validation adalah cara menguji model secara adil. "
        "Data dibagi menjadi 5 bagian (fold) yang sama besar. "
        "Di setiap putaran, satu bagian dipakai untuk menguji model, "
        "dan empat bagian sisanya dipakai untuk melatihnya — "
        "seperti sistem ujian di mana setiap orang mendapat giliran menjadi penguji. "
        "Proses ini diulang 5 kali hingga semua bagian pernah diuji, "
        "lalu hasilnya dirata-rata untuk mendapatkan ukuran performa yang jujur."
    )