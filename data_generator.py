import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Buat data transaksi 30 hari terakhir
dates = [datetime.now() - timedelta(days=i) for i in range(30)]
data = {
    'Date': np.random.choice(dates, 100),
    'Product': np.random.choice(['AI Consultant', 'Video Script', 'Prompt Pack'], 100),
    'Revenue': np.random.randint(50, 500, 100),
    'Status': np.random.choice(['Paid', 'Pending', 'Cancelled'], 100, p=[0.8, 0.1, 0.1])
}

df = pd.DataFrame(data)
df.to_csv('raw_business_data.csv', index=False)
print("✅ File 'raw_business_data.csv' berhasil dibuat!")