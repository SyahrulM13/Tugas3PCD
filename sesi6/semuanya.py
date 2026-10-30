import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca citra
img = cv2.imread("balap.webp")

if img is None:
    raise FileNotFoundError("File balap.webp tidak ditemukan!")

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

tinggi, lebar = img.shape[:2]

# 1. TRANSLATION
# Menggeser gambar 150 piksel ke kanan dan 75 piksel ke bawah
M_trans = np.float32([
    [1, 0, 150],
    [0, 1, 75]
])

translation = cv2.warpAffine(
    img, M_trans, (lebar, tinggi)
)

# 2. SCALING
# Memperkecil gambar dengan faktor 0.5
scaling_05 = cv2.resize(
    img,
    None,
    fx=0.5,
    fy=0.5,
    interpolation=cv2.INTER_LINEAR
)

# Memperbesar gambar dengan faktor 2
scaling_2 = cv2.resize(
    img,
    None,
    fx=2,
    fy=2,
    interpolation=cv2.INTER_LINEAR
)

# Fungsi rotasi agar seluruh gambar tetap terlihat
def rotate_bound(image, sudut):
    h, w = image.shape[:2]

    pusat = (w / 2, h / 2)

    M = cv2.getRotationMatrix2D(
        pusat, sudut, 1.0
    )

    cos = abs(M[0, 0])
    sin = abs(M[0, 1])

    lebar_baru = int((h * sin) + (w * cos))
    tinggi_baru = int((h * cos) + (w * sin))

    M[0, 2] += (lebar_baru / 2) - pusat[0]
    M[1, 2] += (tinggi_baru / 2) - pusat[1]

    return cv2.warpAffine(
        image, M, (lebar_baru, tinggi_baru)
    )

# 3. ROTATION
# Rotasi 45 derajat
rotasi_45 = rotate_bound(img, 45)

# Rotasi 90 derajat
rotasi_90 = rotate_bound(img, 90)

# Rotasi 180 derajat
rotasi_180 = rotate_bound(img, 180)

# 4. FLIP
# Membalik gambar secara horizontal
horizontal_flip = cv2.flip(img, 1)

# Membalik gambar secara vertikal
vertical_flip = cv2.flip(img, 0)

# Menampilkan citra asli dan seluruh hasil transformasi
hasil = [
    ("Citra Asli", img),
    ("Translation", translation),
    ("Scaling 0.5x", scaling_05),
    ("Scaling 2x", scaling_2),
    ("Rotation 45 Derajat", rotasi_45),
    ("Rotation 90 Derajat", rotasi_90),
    ("Rotation 180 Derajat", rotasi_180),
    ("Horizontal Flip", horizontal_flip),
    ("Vertical Flip", vertical_flip)
]

# Membuat tampilan 3 baris dan 3 kolom
fig, axes = plt.subplots(3, 3, figsize=(15, 10))

for ax, (judul, citra) in zip(axes.flat, hasil):
    ax.imshow(citra)
    ax.set_title(judul)
    ax.axis("off")

plt.tight_layout()

# Menyimpan hasil transformasi
plt.savefig(
    "hasil_transformasi_citra.png",
    dpi=160,
    bbox_inches="tight"
)

# Menampilkan gambar
plt.show()

# Menampilkan ukuran citra
print("Ukuran citra asli:",
      lebar, "x", tinggi)

print("Ukuran scaling 0.5x:",
      scaling_05.shape[1], "x",
      scaling_05.shape[0])

print("Ukuran scaling 2x:",
      scaling_2.shape[1], "x",
      scaling_2.shape[0])