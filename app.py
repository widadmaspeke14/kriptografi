import streamlit as st

# ==============================
# FUNGSI BANTUAN
# ==============================
def char_to_num(c):
    return ord(c) - 65

def num_to_char(n):
    return chr((n % 26) + 65)

# ==============================
# GRONSFELD CIPHER
# ==============================
def gronsfeld_encrypt(plaintext, key):
    key_nums = [char_to_num(k) for k in key]
    result = ""

    for i, char in enumerate(plaintext):
        p = char_to_num(char)
        k = key_nums[i % len(key_nums)]
        result += num_to_char(p + k)

    return result

# ==============================
# RAIL FENCE (2 REL)
# ==============================
def rail_fence_encrypt(text):
    rail1, rail2 = "", ""

    for i, c in enumerate(text):
        if i % 2 == 0:
            rail1 += c
        else:
            rail2 += c

    return rail1 + rail2

# ==============================
# REVERSE CIPHER
# ==============================
def reverse_cipher(text):
    return text[::-1]

# ==============================
# CIPHER BENUA
# ==============================
def benua_cipher(text, benua):
    shift_map = {
        "Asia": 5,
        "Eropa": 7,
        "Afrika": 3,
        "Amerika": 4,
        "Australia": 6
    }

    shift = shift_map.get(benua, 0)
    result = ""

    for c in text:
        result += num_to_char(char_to_num(c) + shift)

    return result

# ==============================
# STREAMLIT UI
# ==============================
st.set_page_config(page_title="Enkripsi Gabungan", page_icon="🔐", layout="centered")

st.title("🔐 Aplikasi Enkripsi Gabungan")
st.write("""
**Metode:**  
Gronsfeld Cipher → Rail Fence (2 rel) → Reverse Cipher → Cipher Benua  
""")

st.divider()

# INPUT USER
plaintext = st.text_input("Masukkan Plainteks", "Kriptografi")
key = st.text_input("Masukkan Nama Negara (Key)", "Indonesia")

benua = st.selectbox(
    "Pilih Benua",
    ["Asia", "Eropa", "Afrika", "Amerika", "Australia"]
)

# PROSES ENKRIPSI
if st.button("🔒 Enkripsi"):
    ptext = plaintext.upper().replace(" ", "")
    key = key.upper()

    tahap1 = gronsfeld_encrypt(ptext, key)
    tahap2 = rail_fence_encrypt(tahap1)
    tahap3 = reverse_cipher(tahap2)
    tahap4 = benua_cipher(tahap3, benua)

    st.success("Proses Enkripsi Berhasil")

    st.subheader("📌 Hasil Tiap Tahap")
    st.write("**1. Gronsfeld Cipher** :", tahap1)
    st.write("**2. Rail Fence Cipher** :", tahap2)
    st.write("**3. Reverse Cipher** :", tahap3)
    st.write("**4. Cipher Benua** :", tahap4)

    st.subheader("🔑 Ciphertext Akhir")
    st.code(tahap4, language="text")

st.divider()
st.caption("© Widad Maspeke – Kriptografi Klasik")
