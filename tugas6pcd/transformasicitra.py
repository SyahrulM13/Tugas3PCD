
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

# Membaca gambar
img = Image.open("WakilPresidenPenggantiGibranjpeg.jpeg").convert("RGB")

w, h = img.size

# 1. Translation
translation = Image.new("RGB", (w, h), (230, 230, 230))
translation.paste(img, (100, 50))

# 2. Scaling
scaling_05 = img.resize((int(w * 0.5), int(h * 0.5)))
scaling_2 = img.resize((w * 2, h * 2))

# 3. Rotation
rotasi_45 = img.rotate(45, expand=True)
rotasi_90 = img.rotate(90, expand=True)
rotasi_180 = img.rotate(180, expand=True)

# 4. Horizontal dan Vertical Flip
horizontal_flip = ImageOps.mirror(img)
vertical_flip = ImageOps.flip(img)

# 5. Menampilkan semua hasil transformasi
hasil = [
    ("Citra Asli", img),
    ("Translation", translation),
    ("Scaling 0.5", scaling_05),
    ("Scaling 2", scaling_2),
    ("Rotation 45 Derajat", rotasi_45),
    ("Rotation 90 Derajat", rotasi_90),
    ("Rotation 180 Derajat", rotasi_180),
    ("Horizontal Flip", horizontal_flip),
    ("Vertical Flip", vertical_flip)
]

plt.figure(figsize=(15, 18))

for i, (judul, gambar) in enumerate(hasil):
    plt.subplot(3, 3, i + 1)
    plt.imshow(gambar)
    plt.title(judul)
    plt.axis("off")

plt.tight_layout()
plt.show()

# 6. Menyimpan hasil transformasi
translation.save("translation.png")
scaling_05.save("scaling_05.png")
scaling_2.save("scaling_2.png")
rotasi_45.save("rotasi_45.png")
rotasi_90.save("rotasi_90.png")
rotasi_180.save("rotasi_180.png")
horizontal_flip.save("horizontal_flip.png")
vertical_flip.save("vertical_flip.png")

print("Semua transformasi berhasil dilakukan!")
