from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, ConfigurationError

app = Flask(__name__)

# Riwayat input yang disimpan dalam list
history = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        connection_string = request.form['connection_string']
        try:
            # Coba koneksi ke MongoDB
            client = MongoClient(connection_string)
            client.admin.command('ping')  # Cek koneksi dengan command 'ping'
            result = "Koneksi berhasil!"
            error = None
            recommendation = None
        except ServerSelectionTimeoutError as e:
            result = None
            error = f"Error: Koneksi gagal. {str(e)}"
            recommendation = "Pastikan URL koneksi MongoDB Anda benar dan jaringan Anda tidak bermasalah."
        except ConfigurationError as e:
            result = None
            error = f"Error: Konfigurasi salah. {str(e)}"
            recommendation = "Periksa konfigurasi string koneksi dan pastikan parameter sudah benar."
        except Exception as e:
            result = None
            error = f"Error: Terjadi kesalahan. {str(e)}"
            recommendation = "Periksa koneksi string dan pastikan Anda memiliki izin yang benar."

        # Simpan riwayat input, string koneksi, dan pesan error
        history.append({
            'no': len(history) + 1,
            'connection_string': connection_string,
            'error': error or result
        })

        return render_template('index.html', result=result, error=error, recommendation=recommendation)

    return render_template('index.html', result=None, error=None, recommendation=None)

@app.route('/history')
def history_page():
    return render_template('history.html', history=history)

if __name__ == '__main__':
    app.run(debug=True)
