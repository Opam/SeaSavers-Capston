default durasi = 120
default sampah_terkumpul = 0
default score_1 = 0
define config.rollback_enabled = False
# Variabel karakter
define sagara = Character("Sagara", color = "#9afa5a", who_bold=True, who_outlines = [(1, "#000")])
define ibu = Character("Ibu", color = "#c9770a", who_bold=True, who_outlines = [(1,"#000")])
define pembawa_berita = Character("Pembawa Berita", color = "#0048ff", who_bold=True, who_outlines = [(1, "#000")])

# animasi masuk
transform fade_in:
    alpha 0.0
    linear 1.0 alpha 1.0
transform fide_out:
    alpha 1.0
    linear 1.0 alpha 0.0
transform slide_in_right:
    xalign 2.0
    easein 1.0 xalign 1.0
transform slide_in_left:
    xalign 0.0
    easein 1.0 xalign 0.1

style text_center:
    xalign 0.5
    size 40
    color "#fff"

label start:
    play music dialogscene
    scene scene 1 with dissolve
    pause 1.0
    "Di suatu pagi yang indah di kota kecil di pinggiran pantai yang bernama kota Pantara Indah"
    "Kota ini terkenal dengan pasar ikan yang sangat fresh karena para nelayan di pasar mengambil ikan langsung dari lautan sana "
    "tapi akhir akhir ini banyak ikan yang kurang fresh di karenakan banyak limbah sampah yang tersebar di lautan bahkan terdapat ikan yang cacat dikarenakan limbah sampah plastik yang di buang ke lautan."
    stop music

    play music banguntidur
    ibu "SAGARAAA!!!! BANGUNNN!!! SUDAH JAM 8 KATANYA KAMU PAGI INI MAU KE LAUT"
    scene scene 1 1
    show menguap at right, fade_in:
        zoom 0.7
        ypos 1.4
    sagara "Iya sebentar..."
    ibu "Ayo cepat bangun, nanti siang kita masih ada acara di kota sebelah ayo bangun"
    sagara "Iya ibu, aku mau sarapan sebentar sebelum pergi ke laut"
    scene black with fade
    stop music

    # scene lihat berita di televisi
    play music breakingnews
    scene dapur with dissolve
    show bangun tidur at right, fade_in:
        zoom 0.7
        ypos 1.4
    sagara "Ada berita apa pagi ini"
    scene scene 2 with dissolve
    pembawa_berita "Selamat pagi,pemirsa. pagi ini Kami membawa kabar yang sangat memprihatinkan tentang kondisi lautan kita."

    scene scene 2 2
    show bangun tidur at right:
        zoom 0.7
        ypos 1.4
    sagara "Hadehh, lagi-lagi berita tentang orang buang sampah ke laut, stress."

    scene scene 2
    pembawa_berita "Limbah plastik terus meningkat dan kini telah memenuhi perairan kita, mencemari ekosistem laut yang menjadi sumber kehidupan."
    pembawa_berita "Data terbaru menunjukan bahwa hampir puluhan ton sampah dibuang ke lautan tahunnya."
    pembawa_berita "Limbah ini tidak hanya merusak lingkungan, tetapi juga membawa dampak buruk bagi makhluk hidup di laut."
    pembawa_berita "Banyak ikan kini mengalami cacat fisik karena mengonsumsi partikel plastik atau terjebak dalam tumpukan sampah."
    pembawa_berita "Akibatnya ikan-ikan ini tidak lagi dapat dijual dalam kondisi segar di pasar, dan ini juga mengancam mata pencaharian nelayan serta kesehatan konsumen."
    pembawa_berita "Selain itu, sampah yang mengapung di permukaan laut juga merusak keindahan alam yang seharusnya menjadi kebanggan kita."
    pembawa_berita "Terumbu karang yang dulu indah kini tertutup oleh limbah, mengganggu pemanngan bawah laut yang memikat hati."
    pembawa_berita "Situasi ini tidak bisa dibiarkan, kita semua harus bertindak! Kurangi penggunaan plastik dan pastikan sampah dibuang ke tempat yang semestinya."
    pembawa_berita "Setiap langkah kecil dari kita semua bisa membawa perubahan besar."
    pembawa_berita "Mari kita bersama-sama menjaga lautan kita agar tetap indah,sehat dan menj-"

    scene dapur 
    show kesel at right:
        zoom 0.7
        ypos 1.4
    sagara "Huft, masih ada orang yang buang sampah ke laut semoga cepat tersadar."
    stop music
    jump pergikelaut
    
# Sagara keluar rumah untuk pergi ke laut
label pergikelaut:
    play music pergikelaut
    scene scene 3 with dissolve:
        zoom 0.7
    pause 3.0
    # scene scene 3:
    #     zoom 0.7
    sagara "LET'S GOOOOOOO!!!!!!!!! AKAN KU BASMI SEMUA SAMPAH DILAUTAN!!!"

# Sagara tiba di laut
label lautan:
    # Scene Sampai di laut
    scene scene 4 with dissolve:
        zoom 0.7
    pause 1.0
    "Sesampainya di lautan sagara melihat banyak sekali sampah yang mengapung di lautan yang mengganggu pemandangannya, sagara yang berada di atas kapal mulai bergegas untuk mengambil sampah-sampah"
    sagara "Hadeehh, kenapa banyak bgt sih sampah yang ngapung bikin repot orang lain saja"
    stop music
    jump misi_1

label misi_1:
    # Menampilkan screen game
    scene black
    play music gameplay

    $ durasi = 120
    $ sampah_terkumpul = 0
    $ renpy.pause(1.0, hard=True)
    
    "Misi 1: Kumpulkan 50 sampah dalam waktu 120 detik!"
    call screen game_screen_misi_1
   

    # Tunggu sampai durasi habis
    return
        
label misi_1_berhasil:
    stop music
    play sound win
    hide screen game_screen_misi_1
    hide screen lose_condition
    show screen win_condition
    $ renpy.pause(3.0, hard=True)

    "Selamat! Anda berhasil menyelesaikan Misi 1."
    hide screen win_condition
    jump misi_2

label misi_1_gagal:
    stop music
    play sound wrong
    hide screen game_screen_misi_1
    show screen lose_condition
    hide screen win_condition
    
    $ renpy.pause(3.0, hard=True)
    "Anda gagal menyelesaikan Misi 1. Coba lagi!"
    jump misi_1

label misi_2:
    play music gameplay
    hide screen win_condition
    scene bgkanan
    $ durasi = 90
    $ score_1 = 0.0

    
    
    "Misi 2: Kumpulkan skor sebanyak 6000 dalam waktu 60 detik!"
    "akan ada item buff dan ikan"
    "buff akan menambah jumlah spawn sampah dan melipat gandakan score"
    "menangkap ikan akan mengurangi score"

    call screen game_screen_misi_2
 
    # Tunggu sampai durasi habis
    return

label misi_2_berhasil:
    stop music
    play sound win
    hide screen game_screen_misi_2
    hide screen lose_condition
    show screen win_condition
    $ renpy.pause(3.0, hard=True)
    "Selamat! Anda berhasil menyelesaikan Misi 2."
    

    jump misi_3

label misi_2_gagal:
    stop music
    play sound wrong
    hide screen game_screen_misi_2
    show screen lose_condition
    hide screen win_condition
    $ renpy.pause(3.0, hard=True)
    "Anda gagal menyelesaikan Misi 2. Coba lagi!"
    

    jump misi_2

label misi_3:
    play music gameplay
    hide screen win_condition
    scene bgkanan

    $ sampah_speed = 5
    $ durasi = 90
    $ score_1 = 0

    "Misi terakhir"
    "kumpulkan score 6000 dalam waktu 90 detik"

    call screen game_screen_misi_3
    
    #tunggu sampai durasi habis
    return

label misi_3_berhasil:
    stop music
    play sound win
    hide screen game_screen_misi_2
    hide screen lose_condition
    show screen win_condition
    $ renpy.pause(3.0, hard=True)
    "Selamat! Anda berhasil menyelesaikan Misi 3."
    

    jump Selesai

label misi_3_gagal:
    stop music
    play sound wrong
    hide screen game_screen_misi_2
    show screen lose_condition
    hide screen win_condition
    $ renpy.pause(3.0, hard=True)
    "Anda gagal menyelesaikan Misi 3. Coba lagi!"

    jump misi_3

# Game selesai
label Selesai:
    play music ending
    hide screen win_condition
    hide screen game_screen
    scene scene 5:
        zoom 0.7

    "Sagara akhirnya selesai membersihkan sampah yang mengapung dilautan dan dia mulai mengemasi sampah ke dalam tas sampah"
    scene scene 6:
        zoom 0.7

    sagara "Hufff akhirnya selesai juga ternyata banyak juga, untung aku membawa banyak tas sampah hari ini semoga sesampainya di pantai orang tidak mengira aku habis mencuri uang di bank."
    stop music
    return