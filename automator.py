import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Data
df = pd.read_csv('raw_business_data.csv')

# 2. Cleaning Data (Hanya ambil yang sudah PAID)
paid_data = df[df['Status'] == 'Paid']

# 3. Analisis: Revenue per Produk
revenue_per_product = paid_data.groupby('Product')['Revenue'].sum()

# 4. Analisis: Status Penjualan (Berapa banyak yang Pending/Cancelled)
status_counts = df['Status'].value_counts()

print("--- LAPORAN OTOMATIS ---")
print(f"Total Revenue Bersih: ${revenue_per_product.sum()}")
print("\nDetail per Produk:")
print(revenue_per_product)

# 5. Visualisasi: Bikin Grafik Batang
# plt.figure(figsize=(10, 6))
# revenue_per_product.plot(kind='bar', color=['#4285f4', '#34a853', '#fbbc05'])
# plt.title('Revenue by Product (Automated Report)')
# plt.ylabel('Revenue ($)')
# plt.xlabel('Product Name')
# plt.grid(axis='y', linestyle='--', alpha=0.7)

import pandas as pd
import matplotlib.pyplot as plt

# --- DATA PROCESSING (Sama seperti sebelumnya) ---
df = pd.read_csv('raw_business_data.csv')
paid_data = df[df['Status'] == 'Paid']
revenue_per_product = paid_data.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

# --- VISUALISASI ESTETIK ---
# Set ukuran dan resolusi tinggi (DPI)
plt.figure(figsize=(10, 6), dpi=100)

# Pilih warna modern (Vibrant Blue, Soft Green, Warm Orange)
colors = ['#007bff', '#28a745', '#fd7e14']

# Bikin Bar Chart dengan sudut yang tegas dan warna solid
bars = plt.bar(revenue_per_product.index, revenue_per_product.values, 
               color=colors, width=0.6, edgecolor='white', linewidth=1)

# Tambahin Label Angka di atas Bar (Biar gak usah nebak-nebak angkanya)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, f'${yval}', 
             ha='center', va='bottom', fontsize=11, fontweight='bold', color='#333')

# Poles Axis & Title
plt.title('Business Revenue Analytics', fontsize=18, fontweight='bold', pad=20, color='#222')
plt.ylabel('Total Revenue ($)', fontsize=12, labelpad=10)
plt.xticks(fontsize=11)

# Hapus garis border atas dan kanan biar "Clean"
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#ddd')
ax.spines['bottom'].set_color('#ddd')

# Grid horizontal tipis saja
plt.grid(axis='y', linestyle='--', alpha=0.3)

# Kasih padding biar gak kepotong
plt.tight_layout()

# Simpan ulang!
plt.savefig('revenue_report.png', bbox_inches='tight')
print("\n✨ Grafik estetik 'revenue_report.png' berhasil di-update!")

# Simpan Grafik sebagai Gambar (buat dipajang di Portfolio!)
plt.savefig('revenue_report.png')
print("\n✅ Grafik 'revenue_report.png' berhasil dibuat!")