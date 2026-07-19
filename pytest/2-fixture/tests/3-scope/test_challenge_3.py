# Pertanyaan :
# 1. Apa perbedaan `scope="function"` dan `scope="session"`?
# 2. Menurutmu kenapa browser pada Playwright sering menggunakan `scope="session"`?

# Jawaban :
# 1. scope funciton -> fixture dipanggil dan dijalankan tiap fungsi yang menggunakan fixture itu dijalankan
# scope session -> fixture dipanggil dan dijalankan tiap test berjalan, jadi sekali test cuman sekali aja fixture dipanggil dan dijalankan

# 2. karena membuka browser itu mahal di waktu, jadi pake scope session aja biar cuman satu test itu sekali buka browsernya
# scope="session"
# Fixture dijalankan sekali di awal sesi pytest,
# kemudian digunakan oleh semua test yang membutuhkan fixture tersebut.
# Setelah seluruh test selesai,
# fixture baru dibersihkan (cleanup).