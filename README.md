# Instruksi Untuk Menjalankan Script Test QA
##### Muhamad Fadli Anjasmoro
------------------------------------------------------------------------------------

## Langkah - Langkahnya :
### 1. Download
| Apk/lainnya | Link |
| ------ | ------ |
| Visual Studio Code | https://code.visualstudio.com/download |
| Python | https://www.python.org/downloads/ |
| Google Chrome | https://www.google.co.id/chrome/?brand=YTUH&gclid=CjwKCAiAvK2bBhB8EiwAZUbP1Iyr_-uygw_T26UokDENIpmnLW8PMvdG4tgJAhpPNqwwffh9FvnLfBoCXPkQAvD_BwE&gclsrc=aw.ds |
| ChromeDriver | https://chromedriver.chromium.org/ |
##### Note : 
Versi Google Chrome harus sama dengan versi Chromedrivernya. Jika Google Chrome menggunakan versi 107 maka chromedriver harus download versi 107
cek versi Google Chrome : Klik titik 3 pojok kanan atas halaman web google chrome -> klik Bantuan -> Pilih Tentang Google Chrome.

### 2. Install
- Install atau update GOOGLE CHROME yang sama versi dengan chromedriver
- Install (ekstrak) CHROME DRIVER yang telah di download, kemudian Salin/Copy "chromedriver.exe" Paste ke  C:\Program Files atau C:\Program Files (x86) sesuai folder "Google" anda kemudian MASUKAN JUGA ke PATH di ENVIRONMENT VARIABLES PC dengan caranya yaitu = ketik di search windows "environment"-> bila muncul "Edit the system environment variables" lalu pilih -> klik "Environment Variables" -> Klik "Path" pada bagian System Variables -> Lalu klik tombol Edit -> Klik Tombol New -> Tambahkan alamat chromedriver.exe yang tadi (C:\Program Files\chromedriver.exe) lalu klik OK -> OK -> OK
- Install PYTHON yang telah didownload jangan lupa untuk centang semua bagian kotak agar ditambahkan ke path environtment secara otomatis, jika tidak atau mengecek langkahnya sama seperti chromedriver yaitu masukan ke PATH di ENVIRONMENT VARIABLES PC seperti contoh saya masukan C:\Users\mufad\AppData\Local\Programs\Python\Python311\ dan C:\Users\mufad\AppData\Local\Programs\Python\Python311\Scripts\ ke dalam path.
- Instal VISUAL STUDIO CODE dan jangan lupa untuk instal extensions setelah aplikasi ini dibuka yaitu extensions (Python,Pylance, dan Python Indent)

### 3. Buka Command Prompt (CMD) Install Selenium dan Pyautogui
Ketik (lambang Windows+R)pada keyboard PC/Laptop atau "Klik Kanan pada Windows pilih Run" -> Ketik cmd -> OK(Enter).
- Cek Versi Python 
```sh
python --version
```
- Install Selenium
```sh
pip install selenium
```
- Install Pyautogui
```sh
pip install PyAutoGUI
```
- Jika sudah selesai, maka close CMD.

### 4. Buka Visual Studio Code, Open File Script yang telah saya buat, Klik Run untuk Testing.

### 5. Selesai

[![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://saythanks.io/to/kennethreitz)