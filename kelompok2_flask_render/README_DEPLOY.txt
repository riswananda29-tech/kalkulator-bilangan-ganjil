PAKET DEPLOY RENDER - KELOMPOK 2

Isi repository:
- app.py
- requirements.txt (Flask + Gunicorn)
- .python-version (Python 3.14.10)
- templates/index.html
- static/style.css

PENTING:
Jangan upload folder .venv ke GitHub.

Render:
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app

Setelah deploy berhasil, Render memberi URL publik onrender.com.
Free web service dapat tidur setelah 15 menit tanpa trafik; kunjungan pertama
setelah tidur bisa memerlukan sekitar satu menit untuk aktif kembali.
