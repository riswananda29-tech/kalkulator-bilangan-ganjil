from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    error = None
    awal_value = ""
    akhir_value = ""

    if request.method == "POST":
        awal_value = request.form.get("awal", "").strip()
        akhir_value = request.form.get("akhir", "").strip()

        try:
            awal = int(awal_value)
            akhir = int(akhir_value)

            if awal > akhir:
                error = "Angka awal harus lebih kecil atau sama dengan angka akhir."
            else:
                bilangan = [angka for angka in range(awal, akhir + 1) if angka % 2 != 0]
                hasil = {
                    "bilangan": bilangan,
                    "jumlah": len(bilangan),
                    "total": sum(bilangan)
                }
        except ValueError:
            error = "Masukkan angka bulat yang valid pada kedua kolom."

    return render_template(
        "index.html",
        hasil=hasil,
        error=error,
        awal=awal_value,
        akhir=akhir_value
    )

if __name__ == "__main__":
    app.run(debug=True)
