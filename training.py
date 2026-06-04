"""
training.py
Modul training model Random Forest dengan K-Fold Cross Validation.
Dipanggil dari 02_Kelola_Data.py setelah data baru ditambahkan.
"""

import pandas as pd
import numpy as np
import joblib
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

BASE_DIR = Path(__file__).parent
FEATURE_COLS = ['Suhu (celcius)', 'Kelembapan (%)', 'Angin (km/h)', 'Intensitas UV', 'Lokasi', 'Waktu']
K = 5

RF_PARAMS = dict(
    n_estimators=1000,
    criterion='gini',
    max_features='sqrt',
    bootstrap=True,
    max_depth=None,
    max_leaf_nodes=None,
    ccp_alpha=0.0,
    min_samples_split=2,
    min_samples_leaf=1,
)



# ── PEMBAGIAN FOLD ──────────────────────────────────────────────────────────────

def bagi_fold(data, k=K):
    """Bagi data menjadi k fold secara berurutan tanpa shuffle.
    Data diurutkan dulu berdasarkan Lokasi, Waktu, No — konsisten dengan Olah_Data.ipynb.
    """
    data = data.sort_values(by=['Lokasi', 'Waktu', 'No']).reset_index(drop=True)
    n = len(data)
    fold_sizes = [n // k] * k
    for i in range(n % k):
        fold_sizes[i] += 1

    folds = []
    current = 0
    for size in fold_sizes:
        folds.append(data.iloc[current:current + size])
        current += size

    return folds


# ── TRAINING ────────────────────────────────────────────────────────────────────

def train(data, log_callback=None):
    """
    Latih model_full dan 5 model per fold.
    Kembalikan dict berisi akurasi per fold dan rata-rata.
    """
    data = data.reset_index(drop=True)

    # Encoding
    le_lokasi = LabelEncoder()
    le_target = LabelEncoder()

    data_enc = data.copy()
    data_enc['Lokasi'] = le_lokasi.fit_transform(data_enc['Lokasi'])
    data_enc['Waktu']  = pd.to_numeric(data_enc['Waktu'], errors='coerce')

    X_full = data_enc[FEATURE_COLS]
    y_full = le_target.fit_transform(data_enc['Cuaca'])

    # Train model full
    if log_callback:
        log_callback("Melatih model_full dengan seluruh data...")
    model_full = RandomForestClassifier(**RF_PARAMS)
    model_full.fit(X_full, y_full)
    joblib.dump(model_full, BASE_DIR / "model_full.pkl")
    if log_callback:
        log_callback("✅ model_full tersimpan")

    # Bagi fold
    folds = bagi_fold(data)
    fold_accuracies = []

    for i in range(K):
        if log_callback:
            log_callback(f"Melatih model fold {i+1}/{K}...")

        # Simpan fold ke Excel
        folds[i].to_excel(BASE_DIR / f"fold_{i+1}.xlsx", index=False)

        # Siapkan data latih
        train_folds = [folds[j] for j in range(K) if j != i]
        train_data  = pd.concat(train_folds).reset_index(drop=True)
        test_data   = folds[i].reset_index(drop=True)

        train_enc = train_data.copy()
        train_enc['Lokasi'] = le_lokasi.transform(train_enc['Lokasi'])
        train_enc['Waktu']  = pd.to_numeric(train_enc['Waktu'], errors='coerce')

        test_enc = test_data.copy()
        test_enc['Lokasi'] = le_lokasi.transform(test_enc['Lokasi'])
        test_enc['Waktu']  = pd.to_numeric(test_enc['Waktu'], errors='coerce')

        X_train = train_enc[FEATURE_COLS]
        y_train = le_target.transform(train_enc['Cuaca'])
        X_test  = test_enc[FEATURE_COLS]
        y_test  = le_target.transform(test_enc['Cuaca'])

        model = RandomForestClassifier(**RF_PARAMS)
        model.fit(X_train, y_train)
        joblib.dump(model, BASE_DIR / f"model_fold_{i+1}.pkl")

        acc = (model.predict(X_test) == y_test).mean()
        fold_accuracies.append(round(acc * 100, 2))

        if log_callback:
            log_callback(f"✅ Fold {i+1} selesai — Akurasi: {acc*100:.2f}%")

    avg_acc = round(np.mean(fold_accuracies), 2)

    if log_callback:
        log_callback(f"\n🎯 Rata-rata Akurasi: {avg_acc}%")

    return {
        "fold_accuracies": fold_accuracies,
        "avg_accuracy": avg_acc,
    }


# ── FUNGSI UTAMA ────────────────────────────────────────────────────────────────

def jalankan_training(df_preprocessed, log_callback=None):
    """
    Entry point yang dipanggil dari 02_Kelola_Data.py.
    Menerima DataFrame yang sudah bersih, langsung training.
    """
    # Simpan data_preprocessed
    df_preprocessed.to_excel(BASE_DIR / "data_preprocessed.xlsx", index=False)
    if log_callback:
        log_callback(f"💾 data_preprocessed.xlsx disimpan ({len(df_preprocessed)} baris)")

    # Training
    hasil = train(df_preprocessed, log_callback=log_callback)
    return hasil
