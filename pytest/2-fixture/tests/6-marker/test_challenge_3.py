# Pertanyaan :
# 1. Apa fungsi utama marker?
# 2. Apa perbedaan marker buatan sendiri dan marker bawaan pytest?
# 3. Kenapa satu test boleh memiliki lebih dari satu marker?
# 4. Kenapa `@pytest.mark.smoke.ui` tidak bisa digunakan?
# 5. Apa fungsi operator `and`, `or`, dan `not` pada `-m`?

# Jawaban :
# 1. Marker berfungsi untuk memberi label atau mengelompokkan test agar mudah dipilih saat dijalankan.
# 2. Marker buatan sendiri hanya sebagai label, sedangkan marker bawaan pytest memiliki perilaku khusus, seperti skip dan xfail.
# 3. Karena satu test bisa termasuk ke lebih dari satu kategori, misalnya smoke dan ui.
# 4. Karena setiap marker adalah decorator yang berdiri sendiri, sehingga harus ditulis terpisah.
# 5. Operator and, or, dan not digunakan untuk memilih test berdasarkan kombinasi marker.