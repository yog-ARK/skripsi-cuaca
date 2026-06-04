import streamlit as st
import pandas as pd
from pathlib import Path
import sys
import shutil

BASE_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(BASE_DIR))
import training

st.set_page_config(
    page_title="Kelola Data — Klasifikasi Cuaca DKI Jakarta",
    page_icon="🗂️",
    layout="wide",
)

LOKASI_VALID = ["Jakarta Barat", "Jakarta Pusat", "Jakarta Selatan", "Jakarta Timur", "Jakarta Utara"]
CUACA_VALID  = ["Badai Petir", "Berawan", "Cerah", "Embun", "Hujan", "Kabut Asap"]

DATA_PATH    = BASE_DIR / "data_preprocessed.xlsx"
DATA_BARU_PATH = BASE_DIR / "data_baru.xlsx"
BACKUP_DIR   = BASE_DIR / "backup"
BACKUP_FILES = [
    "data_preprocessed.xlsx",
    "model_full.pkl",
    "model_fold_1.pkl", "model_fold_2.pkl", "model_fold_3.pkl",
    "model_fold_4.pkl", "model_fold_5.pkl",
    "fold_1.xlsx", "fold_2.xlsx", "fold_3.xlsx", "fold_4.xlsx", "fold_5.xlsx",
]


def load_existing():
    if DATA_PATH.exists():
        return pd.read_excel(DATA_PATH)
    return pd.DataFrame()


def load_data_baru():
    if DATA_BARU_PATH.exists():
        return pd.read_excel(DATA_BARU_PATH)
    return pd.DataFrame()


def simpan_data_baru(df_baru_tambahan):
    """Append baris baru ke data_baru.xlsx tanpa menyentuh data_preprocessed.xlsx."""
    df_existing_baru = load_data_baru()
    df_final = pd.concat([df_existing_baru, df_baru_tambahan], ignore_index=True)
    df_final.to_excel(DATA_BARU_PATH, index=False)
    return df_final


# ── HEADER ──────────────────────────────────────────────────────────────────────
st.title("🗂️ Kelola Data")
st.write(
    "Tambahkan data observasi cuaca baru, lalu latih ulang model "
    "agar hasil klasifikasi mencerminkan data terbaru."
)
st.markdown("---")

tab1, tab2, tab3 = st.tabs(["➕ Tambah Data", "🔁 Latih Ulang Model", "🔄 Reset ke Data Awal"])


# ════════════════════════════════════════════════════════════════════════════════
# TAB 1 — TAMBAH DATA
# ════════════════════════════════════════════════════════════════════════════════
with tab1:

    st.header("Tambah Data Observasi Baru")
    st.write(
        "Data yang disimpan di sini akan ditampung sementara di **data_baru.xlsx** "
        "dan belum mengubah dataset utama. "
        "Pergi ke tab **Latih Ulang Model** untuk menggabungkan dan melatih model baru."
    )

    # Info data baru yang sudah ditampung
    df_baru_ada = load_data_baru()
    if not df_baru_ada.empty:
        st.info(f"📋 Data baru yang sudah ditampung: **{len(df_baru_ada)} baris** (belum digabung ke dataset utama)")
    else:
        st.info("📋 Belum ada data baru yang ditampung.")

    st.markdown("---")
    input_tab1, input_tab2 = st.tabs(["✏️ Input Per Baris", "📂 Upload File Excel"])

    # ── INPUT PER BARIS ──────────────────────────────────────────────────────────
    with input_tab1:
        st.subheader("Input Satu Baris Observasi")

        with st.form("form_tambah_baris"):
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                input_tanggal = st.date_input("Tanggal")
                input_waktu   = st.number_input("Waktu (jam)", min_value=0, max_value=23, value=9, step=1,
                                                help="Format 24 jam. Contoh: 9 untuk 09.00 WIB")
                input_lokasi  = st.selectbox("Lokasi", options=LOKASI_VALID)
            with col_b:
                input_suhu = st.number_input("Suhu (°C)", min_value=24.0, max_value=36.0,
                                             value=None, step=0.1, placeholder="24.0 – 36.0")
                input_kelembapan = st.number_input("Kelembapan (%)", min_value=38.0, max_value=100.0,
                                                   value=None, step=0.1, placeholder="38.0 – 100.0")
            with col_c:
                input_angin = st.number_input("Kecepatan Angin (km/h)", min_value=3.0, max_value=40.0,
                                              value=None, step=0.1, placeholder="3.0 – 40.0")
                input_uv    = st.number_input("Indeks UV", min_value=0.0, max_value=11.0,
                                              value=None, step=0.1, placeholder="0.0 – 11.0")
                input_cuaca = st.selectbox("Kondisi Cuaca", options=CUACA_VALID)

            simpan_baris = st.form_submit_button("💾 Simpan ke Data Baru", use_container_width=True, type="primary")

        if simpan_baris:
            kosong = []
            if input_suhu is None:        kosong.append("Suhu")
            if input_kelembapan is None:  kosong.append("Kelembapan")
            if input_angin is None:       kosong.append("Kecepatan Angin")
            if input_uv is None:          kosong.append("Indeks UV")
            if kosong:
                st.error(f"❌ Kolom berikut belum diisi: **{', '.join(kosong)}**")
                st.stop()

            # Tentukan nomor No — lanjutkan dari data awal + data baru yang ada
            df_awal = load_existing()
            df_baru = load_data_baru()
            no_max  = max(
                int(df_awal['No'].max()) if not df_awal.empty and 'No' in df_awal.columns else 0,
                int(df_baru['No'].max()) if not df_baru.empty and 'No' in df_baru.columns else 0,
            )

            baris_baru = pd.DataFrame([{
                'No':             no_max + 1,
                'Tanggal':        pd.to_datetime(input_tanggal),
                'Waktu':          float(input_waktu),
                'Lokasi':         input_lokasi,
                'Suhu (celcius)': input_suhu,
                'Kelembapan (%)': input_kelembapan,
                'Angin (km/h)':   input_angin,
                'Intensitas UV':  input_uv,
                'Cuaca':          input_cuaca,
            }])

            df_final = simpan_data_baru(baris_baru)
            st.success(f"✅ Baris berhasil ditambahkan. Data baru yang ditampung: **{len(df_final)} baris**.")

    # ── UPLOAD EXCEL ─────────────────────────────────────────────────────────────
    with input_tab2:
        st.subheader("Upload File Excel")
        st.warning(
            "⚠️ **Persyaratan data yang diupload:**\n\n"
            "- Data **harus sudah bersih** — tidak boleh ada nilai kosong\n"
            "- Kolom Lokasi harus berisi salah satu dari: **Jakarta Barat, Jakarta Pusat, Jakarta Selatan, Jakarta Timur, Jakarta Utara**\n"
            "- Kolom Cuaca harus berisi salah satu dari: **Badai Petir, Berawan, Cerah, Embun, Hujan, Kabut Asap**\n"
            "- Format Tanggal: **DD/MM/YYYY** atau **YYYY-MM-DD**\n"
            "- Kolom Waktu diisi angka jam (contoh: 9 untuk 09.00 WIB)"
        )

        uploaded_file = st.file_uploader("Pilih file Excel (.xlsx)", type=["xlsx"])

        if uploaded_file:
            try:
                df_upload = pd.read_excel(uploaded_file)
                st.success(f"✅ File berhasil dibaca — **{len(df_upload)} baris** terdeteksi")

                st.subheader("Petakan Kolom File Anda")
                kolom_file = list(df_upload.columns)

                def tebak_kolom(kata_kunci):
                    for k in kata_kunci:
                        for col in kolom_file:
                            if k.lower() in col.lower():
                                return col
                    return kolom_file[0]

                col_m1, col_m2 = st.columns(2)
                with col_m1:
                    map_no         = st.selectbox("No",              kolom_file, index=kolom_file.index(tebak_kolom(['no', 'nomor', 'id'])))
                    map_tanggal    = st.selectbox("Tanggal",          kolom_file, index=kolom_file.index(tebak_kolom(['tanggal', 'date', 'tgl'])))
                    map_waktu      = st.selectbox("Waktu",            kolom_file, index=kolom_file.index(tebak_kolom(['waktu', 'jam', 'time'])))
                    map_lokasi     = st.selectbox("Lokasi",           kolom_file, index=kolom_file.index(tebak_kolom(['lokasi', 'wilayah', 'location'])))
                with col_m2:
                    map_suhu       = st.selectbox("Suhu (°C)",        kolom_file, index=kolom_file.index(tebak_kolom(['suhu', 'temp', 'temperature'])))
                    map_kelembapan = st.selectbox("Kelembapan (%)",   kolom_file, index=kolom_file.index(tebak_kolom(['kelembapan', 'humid', 'rh'])))
                    map_angin      = st.selectbox("Kecepatan Angin",  kolom_file, index=kolom_file.index(tebak_kolom(['angin', 'wind'])))
                    map_uv         = st.selectbox("Indeks UV",        kolom_file, index=kolom_file.index(tebak_kolom(['uv', 'intensitas'])))
                    map_cuaca      = st.selectbox("Kondisi Cuaca",    kolom_file, index=kolom_file.index(tebak_kolom(['cuaca', 'kondisi', 'weather'])))

                df_mapped = df_upload.rename(columns={
                    map_no: 'No', map_tanggal: 'Tanggal', map_waktu: 'Waktu',
                    map_lokasi: 'Lokasi', map_suhu: 'Suhu (celcius)',
                    map_kelembapan: 'Kelembapan (%)', map_angin: 'Angin (km/h)',
                    map_uv: 'Intensitas UV', map_cuaca: 'Cuaca',
                })[['No', 'Tanggal', 'Waktu', 'Lokasi', 'Suhu (celcius)',
                     'Kelembapan (%)', 'Angin (km/h)', 'Intensitas UV', 'Cuaca']]

                # Normalisasi kapitalisasi Lokasi dan Cuaca
                df_mapped['Lokasi'] = df_mapped['Lokasi'].str.strip().str.title()
                df_mapped['Cuaca']  = df_mapped['Cuaca'].str.strip().str.title()

                st.subheader("Preview (5 Baris Pertama)")
                st.dataframe(df_mapped.head(), use_container_width=True)

                error_validasi = []
                if df_mapped.isnull().any().any():
                    kosong_cols = df_mapped.columns[df_mapped.isnull().any()].tolist()
                    error_validasi.append(f"Terdapat nilai kosong di kolom: **{', '.join(kosong_cols)}**")
                lokasi_invalid = df_mapped[~df_mapped['Lokasi'].isin(LOKASI_VALID)]['Lokasi'].unique()
                if len(lokasi_invalid) > 0:
                    error_validasi.append(f"Nilai Lokasi tidak dikenal: **{', '.join(str(x) for x in lokasi_invalid)}**")
                cuaca_invalid = df_mapped[~df_mapped['Cuaca'].isin(CUACA_VALID)]['Cuaca'].unique()
                if len(cuaca_invalid) > 0:
                    error_validasi.append(f"Nilai Cuaca tidak dikenal: **{', '.join(str(x) for x in cuaca_invalid)}**")

                if error_validasi:
                    st.error("❌ Data tidak dapat disimpan:\n\n" + "\n".join(f"- {e}" for e in error_validasi))
                else:
                    st.success(f"✅ Data valid — {len(df_mapped)} baris siap ditampung.")

                    if st.button("💾 Simpan ke Data Baru", type="primary", use_container_width=True):
                        # Sesuaikan No agar tidak bentrok
                        df_awal = load_existing()
                        df_baru = load_data_baru()
                        no_offset = max(
                            int(df_awal['No'].max()) if not df_awal.empty and 'No' in df_awal.columns else 0,
                            int(df_baru['No'].max()) if not df_baru.empty and 'No' in df_baru.columns else 0,
                        )
                        df_mapped['No'] = df_mapped['No'] + no_offset

                        df_final = simpan_data_baru(df_mapped)
                        st.success(f"✅ Data berhasil ditampung. Data baru yang tersimpan: **{len(df_final)} baris**.")

            except Exception as e:
                st.error(f"❌ Gagal membaca file: `{str(e)}`")


# ════════════════════════════════════════════════════════════════════════════════
# TAB 2 — LATIH ULANG MODEL
# ════════════════════════════════════════════════════════════════════════════════
with tab2:

    st.header("Latih Ulang Model")

    df_awal = load_existing()
    df_baru = load_data_baru()

    # Info ringkasan
    col_i1, col_i2, col_i3 = st.columns(3)
    col_i1.metric("Data Awal (dataset utama)", f"{len(df_awal):,} baris")
    col_i2.metric("Data Baru (belum digabung)", f"{len(df_baru):,} baris")
    col_i3.metric("Total jika digabung", f"{len(df_awal) + len(df_baru):,} baris")

    if df_baru.empty:
        st.warning("⚠️ Belum ada data baru yang ditampung. Tambahkan data di tab **Tambah Data** terlebih dahulu.")

    st.markdown("---")
    st.subheader("Pilih Data untuk Training")

    opsi_data = st.radio(
        "Data yang digunakan:",
        options=[
            "Gabungkan data awal + data baru  ✅ Direkomendasikan",
            "Data baru saja",
        ],
        disabled=df_baru.empty,
    )

    if "baru saja" in opsi_data:
        st.warning(
            f"⚠️ Model hanya dilatih dari **{len(df_baru)} baris** data baru. "
            "Akurasi bisa menurun drastis jika jumlah data sedikit."
        )

    st.markdown("---")
    st.subheader("Mulai Training")
    st.write(
        "Proses ini melatih 6 model secara berurutan "
        "(5 fold + 1 model full). Estimasi waktu: **3–8 menit**."
    )

    tombol_train = st.button(
        "🚀 Mulai Latih Ulang Model",
        type="primary",
        use_container_width=True,
        disabled=df_baru.empty,
    )

    if tombol_train:
        # Tentukan data yang dipakai
        if "Gabungkan" in opsi_data:
            df_train = pd.concat([df_awal, df_baru], ignore_index=True)
            label_data = f"data awal ({len(df_awal)}) + data baru ({len(df_baru)}) = {len(df_train)} baris"
        else:
            df_train = df_baru.copy()
            label_data = f"data baru saja ({len(df_baru)} baris)"

        log_area  = st.empty()
        progress  = st.progress(0, text="Mempersiapkan training...")
        log_lines = []
        total_steps = 7

        def update_log(msg):
            log_lines.append(msg)
            log_area.code("\n".join(log_lines), language=None)

        step = [0]

        def log_and_progress(msg):
            update_log(msg)
            step[0] += 1
            progress.progress(min(step[0] / total_steps, 1.0), text=msg)

        try:
            update_log(f"Menggunakan {label_data}")

            with st.spinner("Training sedang berjalan..."):
                hasil = training.jalankan_training(
                    df_preprocessed=df_train,
                    log_callback=log_and_progress,
                )

            progress.progress(1.0, text="✅ Training selesai!")
            st.success("### ✅ Model berhasil dilatih ulang!")

            # Hasil akurasi
            st.subheader("Hasil Evaluasi")
            col_r1, col_r2, col_r3, col_r4, col_r5, col_r6 = st.columns(6)
            for i, acc in enumerate([col_r1, col_r2, col_r3, col_r4, col_r5]):
                acc.metric(f"Fold {i+1}", f"{hasil['fold_accuracies'][i]}%")
            col_r6.metric("Rata-rata", f"{hasil['avg_accuracy']}%")

            # Kosongkan data_baru.xlsx setelah retrain berhasil
            pd.DataFrame().to_excel(DATA_BARU_PATH, index=False)

            st.cache_data.clear()
            st.cache_resource.clear()

            st.info("💡 Data baru telah digabung dan model sudah diperbarui. Buka halaman utama untuk melihat hasilnya.")

        except Exception as e:
            progress.empty()
            st.error(f"❌ Training gagal: `{str(e)}`")
            update_log(f"ERROR: {str(e)}")


# ════════════════════════════════════════════════════════════════════════════════
# TAB 3 — RESET KE DATA AWAL
# ════════════════════════════════════════════════════════════════════════════════
with tab3:

    st.header("Reset ke Data dan Model Awal")
    st.write(
        "Mengembalikan seluruh data dan model ke kondisi awal — "
        "960 baris data hasil pengumpulan pertama dan model yang dilatih dari data tersebut. "
        "Semua data tambahan dan model hasil retrain akan hilang."
    )

    backup_ada    = BACKUP_DIR.exists()
    files_missing = [f for f in BACKUP_FILES if not (BACKUP_DIR / f).exists()] if backup_ada else BACKUP_FILES

    if not backup_ada or files_missing:
        st.error(
            "❌ Folder `backup/` tidak ditemukan atau tidak lengkap.\n\n" +
            (f"File yang tidak ada: **{', '.join(files_missing)}**" if files_missing else
             "Pastikan folder `backup/` sudah dibuat dan diisi dengan file awal.")
        )
        st.info(
            "💡 Cara menyiapkan backup:\n\n"
            "1. Jalankan `Olah_Data.ipynb` di Colab hingga selesai\n"
            "2. Download semua file output dari Colab\n"
            "3. Buat folder `backup/` di direktori yang sama dengan `Program.py`\n"
            "4. Salin semua file tersebut ke dalam folder `backup/`"
        )
    else:
        try:
            df_backup = pd.read_excel(BACKUP_DIR / "data_preprocessed.xlsx")
            st.info(f"📦 Backup tersedia — **{len(df_backup)} baris data** dan **{len(BACKUP_FILES)} file**")
        except Exception:
            st.info("📦 Backup tersedia.")

        df_now = load_existing()
        df_baru_now = load_data_baru()
        col_rs1, col_rs2 = st.columns(2)
        col_rs1.metric("Dataset utama saat ini", f"{len(df_now):,} baris")
        col_rs2.metric("Data baru yang belum dilatih", f"{len(df_baru_now):,} baris")

        st.warning("⚠️ Tindakan ini **tidak dapat dibatalkan**. Seluruh perubahan akan hilang.")

        konfirmasi = st.checkbox("Saya mengerti dan ingin mereset ke data awal")
        tombol_reset = st.button(
            "🔄 Reset Sekarang", type="primary",
            use_container_width=True, disabled=not konfirmasi,
        )

        if tombol_reset:
            try:
                for filename in BACKUP_FILES:
                    shutil.copy2(BACKUP_DIR / filename, BASE_DIR / filename)

                # Kosongkan data_baru.xlsx
                pd.DataFrame().to_excel(DATA_BARU_PATH, index=False)

                st.cache_data.clear()
                st.cache_resource.clear()

                st.success(f"✅ Reset berhasil! Dataset dikembalikan ke {len(df_backup)} baris data awal.")
                st.info("💡 Buka halaman utama untuk melihat hasilnya.")

            except Exception as e:
                st.error(f"❌ Reset gagal: `{str(e)}`")
