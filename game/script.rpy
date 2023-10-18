define a = Character('Anis', color="#c8ffc8")

label start:

    scene kelas pagi with dissolve
    
    show anis senang with moveinright:
        xalign 0.5
        yalign 1.0
    show anis bicara
    
    a "Selamat datang di Aplikasi Media Pembelajaran Interaktif."    
    a "Aplikasi ini dibuat sebagai alat bantu dalam belajar Mata Pelajaran Media Pembelajaran Interaktif."
    a "Apakah kamu sudah siap untuk belajar?"
    
    show anis senang
    
    menu:
        "Ya aku siap.":
            jump start_siap
            
        "Aku belum siap.":
            jump start_belum_siap
            
label start_siap:
    show anis bicara
    
    a "Baguslah kalau begitu. Ayo kita mulai."
    
    show anis senang
    
    jump menu_pembelajaran
    
label start_belum_siap:
    show anis bicara
    
    a "Siap tidak siap harus siap yaaa..."
    
    show anis senang
    
    jump menu_pembelajaran
        
label menu_pembelajaran:
    scene kelas siang with dissolve
    
    menu:
        "Konsep Media Interaktif":
            jump konsep_media_interaktif
            
        "Desain Perancangan Alur Multimedia Interaktif":
            jump desain_alur_multimedia
            
        "Desain User Interface Multimedia Interaktif":
            jump desain_interface_multimedia
            
        "Keluar":
            return

label konsep_media_interaktif:
    scene kelas pagi with dissolve
    
    show anis bicara:
        xalign 0.5
        yalign 1.0
    
    a "Apa itu media pembelajaran interaktif? Media pembelajaran interaktif adalah teknologi yang memanfaatkan komputer dan perangkat digital lainnya untuk menciptakan lingkungan pembelajaran yang mendukung, menarik, dan memotivasi peserta didik dalam belajar."
    a "Ada banyak jenis media pembelajaran interaktif, seperti video interaktif, game edukatif, aplikasi belajar, dan masih banyak lagi."
    a "Salah satu keuntungan media pembelajaran interaktif adalah kemampuannya untuk memberikan umpan balik langsung. Misalnya, jika kamu menjawab soal dan jawabanmu salah, aplikasi tersebut akan langsung memberi tahu bahwa jawabanmu salah dan memberikan penjelasan yang benar."
    a "Media pembelajaran interaktif juga memungkinkan kamu belajar sesuai dengan kecepatanmu sendiri. Kemudian, media ini juga bisa memudahkan guru untuk melacak kemajuan belajarmu."
    a "Tentu saja, media ini tidak bisa menggantikan peran guru sepenuhnya, tetapi bisa menjadi alat bantu yang sangat efektif dalam proses belajar mengajar." 
    
    a "Apakah perlu diulang lagi?"
    
    show anis senang
    
    menu:
        "Ya, ulangi lagi.":
            jump konsep_media_interaktif
            
        "Tidak perlu. Kembali ke menu utama saja.":
            jump menu_pembelajaran
            
label desain_alur_multimedia:
    scene kelas pagi with dissolve
    
    show anis bicara:
        xalign 0.5
        yalign 1.0
        
    a "Pemahaman akan tujuan ini akan membantu kita merancang desain yang efektif dan menarik. Desain alur multimedia harus mencakup semua konten yang relevan dan informasi yang diperlukan siswa."
    a "Konsep, prinsip dan data harus disajikan secara jelas dan efektif. Penggunaan grafis, foto, diagram, dan animasi dapat membantu dalam penyajian informasi ini."
    a "Selanjutnya, interaktivitas adalah hal penting dalam media pembelajaran interaktif. Siswa dapat berinteraksi dengan materi belajar melalui kuis, latihan, atau simulasi."
    a "Dalam mendesain interaktivitas, kita harus memastikan bahwa semua interaksi mendukung tujuan yang telah ditentukan sebelumnya dan memberikan umpan balik yang bermanfaat bagi siswa."
    a "Tidak kalah pentingnya adalah desain navigasi. Siswa harus dapat bergerak dengan mudah melalui media belajar. Navigasi juga harus intuitif dan konsisten sepanjang materi."
    a "Terakhir, penting untuk menguji desain kita sebelum diterapkan. Uji coba ini membantu kita untuk memperbaiki kesalahan dan memastikan bahwa media belajar berfungsi sebagaimana mestinya."
    
    a "Apakah perlu diulang lagi?"
    
    show anis senang
    
    menu:
        "Ya, ulangi lagi.":
            jump desain_alur_multimedia
            
        "Tidak perlu. Kembali ke menu utama saja.":
            jump menu_pembelajaran
            
label desain_interface_multimedia:
    scene kelas pagi with dissolve
    
    show anis bicara:
        xalign 0.5
        yalign 1.0
        
    a "Apakah kalian tahu apa itu user interface (UI)?"
    a "User Interface adalah elemen-elemen yang memungkinkan pengguna berinteraksi dengan suatu perangkat atau aplikasi."
    a "Selama pengguna berinteraksi dengan aplikasi atau sistem, interaksi tersebut harus sesederhana dan seintuitif mungkin."
    a "Itu sebabnya desain UI sangat penting dalam pengembangan aplikasi atau game."
    a "Faktor-faktor penting dalam deain user interface multimedia interaktif adalah konsistensi, responsif, fungsi intuitif, dan estetika."
    a "Desain UI harus konsisten, berarti warna, font, dan elemen lainnya harus sama atau serasi di semua halaman dan fiturnya."
    a "Selain itu, UI harus responsif, ini berarti harus merespons interaksi pengguna secepat mungkin dan beri mereka umpan balik yang jelas."
    a "Terlebih lagi, fungsi dari sebuah UI harus intuitif, yang berarti pengguna harus bisa menebak bagaimana cara menggunakan aplikasi atau game hanya dengan melihat antarmukanya."
    a "Dan tentu saja, UI harus tampak bagus secara visual, karena pengguna biasanya lebih suka antarmuka yang menarik dan menyenangkan untuk dilihat."
    a "Membuat UI yang baik itu rumit, tetapi Ren'py, mesin game visual novel yang kita gunakan sekarang, sangat membantu dalam proses ini."
    a "Dengan Ren'py, kita bisa membuat UI yang menarik dengan mudah dan cepat, dan juga memberi kita banyak kontrol atas tampilan dan perilakunya."
    a "Jadi, jika kalian ingin membuat game visual novel dengan UI yang bagus, Ren'py adalah pilihan yang sempurna."
    
    a "Apakah perlu diulang lagi?"
    
    show anis senang
    
    menu:
        "Ya, ulangi lagi.":
            jump desain_interface_multimedia
            
        "Tidak perlu. Kembali ke menu utama saja.":
            jump menu_pembelajaran
   