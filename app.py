import streamlit as st

# ==============================
# FUNGSI DASAR
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

def gronsfeld_decrypt(ciphertext, key):
    key_nums = [char_to_num(k) for k in key]
    result = ""

    for i, char in enumerate(ciphertext):
        c = char_to_num(char)
        k = key_nums[i % len(key_nums)]
        result += num_to_char(c - k)

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

def rail_fence_decrypt(cipher):
    half = (len(cipher) + 1) // 2
    rail1 = cipher[:half]
    rail2 = cipher[half:]

    result = ""
    i = j = 0

    for k in range(len(cipher)):
        if k % 2 == 0:
            result += rail1[i]
            i += 1
        else:
            result += rail2[j]
            j += 1

    return result

# ==============================
# REVERSE CIPHER
# ==============================
def reverse_cipher(text):
    return text[::-1]

# ==============================
# CIPHER BENUA
# ==============================
def benua_cipher_encrypt(text, benua):
    shift_map = {
        "Asia": 5,
        "Eropa": 7,
        "Afrika": 3,
        "Amerika": 4,
        "Australia": 6
    }

    shift = shift_map.get(benua, 0)
    return "".join(num_to_char(char_to_num(c) + shift) for c in text)

def benua_cipher_decrypt(text, benua):
    shift_map = {
        "Asia": 5,
        "Eropa": 7,
        "Afrika": 3,
        "Amerika": 4,
        "Australia": 6
    }

    shift = shift_map.get(benua, 0)
    return "".join(num_to_char(char_to_num(c) - shift) for c in text)

# ==============================
# STREAMLIT UI
# ==============================
st.set_page_config(page_title="Enkripsi & Dekripsi Gabungan", page_icon="🔐")

st.title("🔐 Aplikasi Enkripsi & Dekripsi Gabungan")
st.write("""
**Metode:**  
Gronsfeld → Rail Fence → Reverse → Cipher Benua
""")

mode = st.radio("Pilih Mode", ["Enkripsi", "Dekripsi"])

benua = st.selectbox(
    "Pilih Benua",
    ["Asia", "Eropa", "Afrika", "Amerika", "Australia"]
)

key = st.text_input("Masukkan Nama Negara (Key)", "Indonesia").upper()

if mode == "Enkripsi":
    plaintext = st.text_input("Masukkan Plainteks", "Kriptografi")

    if st.button("🔒 Enkripsi"):
        ptext = plaintext.upper().replace(" ", "")

        t1 = gronsfeld_encrypt(ptext, key)
        t2 = rail_fence_encrypt(t1)
        t3 = reverse_cipher(t2)
        t4 = benua_cipher_encrypt(t3, benua)

        st.success("Enkripsi Berhasil")
        st.write("**Gronsfeld Cipher:**", t1)
        st.write("**Rail Fence Cipher:**", t2)
        st.write("**Reverse Cipher:**", t3)
        st.write("**Cipher Benua:**", t4)

        st.subheader("🔑 Ciphertext Akhir")
        st.code(t4)

else:
    ciphertext = st.text_input("Masukkan Ciphertext", "FEWHIAEDKPX")

    if st.button("🔓 Dekripsi"):
        t1 = benua_cipher_decrypt(ciphertext, benua)
        t2 = reverse_cipher(t1)
        t3 = rail_fence_decrypt(t2)
        t4 = gronsfeld_decrypt(t3, key)

        st.success("Dekripsi Berhasil")
        st.write("**Hapus Cipher Benua:**", t1)
        st.write("**Reverse Cipher:**", t2)
        st.write("**Rail Fence Decrypt:**", t3)
        st.write("**Gronsfeld Decrypt:**", t4)

        st.subheader("📜 Plainteks")
        st.code(t4)

st.divider()
st.caption("© Widad Maspeke – Kriptografi Klasik")
