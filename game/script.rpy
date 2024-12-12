default durasi = 120
default sampah_terkumpul = 0
default score_1 = 0
define config.rollback_enabled = False
# Variabel karakter
define sagara = Character("Sagara", color = "#000000")
define ibu = Character("Ibu", color = "#000000")
define pembawa_berita = Character("Pembawa Berita", color = "#000000")
define narrator = Character(None, what_style="narrator_style")
define game = Character(None, what_style="game_style")



style narrator_style is default:
    font "gui/font/monotype-corsiva.ttf"
    size 45
    color "#000000"
    xpos 170
    ypos 70 
    text_align 0.5
    xmaximum 1600

style game_style is default:
    font "gui/font/SourceSerif4-VariableFont.ttf"
    size 45
    color "#000000"
    xpos 400
    ypos 70 
    text_align 0.5
    xmaximum 1300

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

label splashscreen:
    $ renpy.movie_cutscene("movies/splashscreen.mpg")

    return

label start:
    call screen menuminigame
    stop music
    scene black with fade
    pause 2.5
    play music dialogscene    
    scene scene 1 with fade
    pause 2.5
    "Di suatu pagi yang indah di kota kecil di pinggiran pantai yang bernama kota Pantara Indah"
    "Kota ini terkenal dengan pasar ikan yang sangat segar karena para nelayan di pasar mengambil ikan langsung dari lautan sana "
    "tapi akhir akhir ini banyak ikan yang kurang segar di karenakan banyak limbah sampah yang tersebar di lautan bahkan terdapat ikan yang cacat dikarenakan limbah sampah plastik yang di buang ke lautan."
    stop music

    play music banguntidur
    scene dapur with dissolve
    ibu "SAGARAAA!!!! BANGUNNN!!! SUDAH JAM 8 KATANYA KAMU PAGI INI MAU KE LAUT..."
    show menguap at right with easeinright:
        zoom 0.7
        ypos 1.4
    sagara "Iya sebentar..."
    ibu "Ayo cepat bangun, nanti siang kita masih ada acara di kota sebelah ayo bangun"
    sagara "Iya ibu, aku mau sarapan sebentar sebelum pergi ke laut"
    
    scene dapur with dissolve    
    show bangun tidur at center, fade_in:
        zoom 0.7
        ypos 1.4
    sagara "Aku masih ngantuk banget semalaman begadang, ada berita apa pagi ini?"    
    scene black with fade
    stop music

    # scene berita di televisi
    play music breakingnews
    scene scene 2 with dissolve
    pembawa_berita "Selamat pagi pemirsa, pagi ini Kami membawa kabar yang sangat memprihatinkan tentang kondisi lautan kita."

    scene scene 2 2
    show kesel at right with easeinright:
        zoom 0.7
        ypos 1.4
    sagara "Hadehh, lagi-lagi berita tentang banyak sampah ke lautan mau sampai kapan coba berita kaya gini, stress."

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
    pembawa_berita "Mari kita bersama-sama menjaga lautan kita agar tetap indah,sehat dan menjadi sumber kehidupan yang berkelanjutan."
    pembawa_berita "Itulah berita dari kami, semoga kita semua bisa bersama-sama menjaga kelestarian lautan kita. Terima kasih dan selamat pagi."

    scene scene 2 2
    show kesel at center:
        zoom 0.7
        ypos 1.4
    sagara "Huft, masih ada orang yang buang sampah ke laut semoga cepat tersadar."
    sagara "Oke! aku harus segera pergi ke laut untuk membersihkan sampah yang ada di laut, semoga aku bisa membersihkan sampah yang ada"
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
    sagara "Hadeehh, kenapa banyak banget sih sampah yang ngapung bikin repot orang lain saja"
    stop music
    jump misi_1

label misi_1:
    # Menampilkan screen game
    scene background
    show ngomong at right:
        zoom 0.7
        ypos 1.4
    play music gameplay

    $ durasi = 120
    $ sampah_terkumpul = 0
    $ renpy.pause(1.0, hard=True)
    
    sagara "Misi 1: Kumpulkan 50 sampah dalam waktu 120 detik!"
    call screen game_screen_misi_1

    # Tunggu sampai durasi habis
    return
        
label misi_1_berhasil:
    stop music
    play sound win
    scene background
    hide screen game_screen_misi_1
    hide screen lose_condition
    call screen win_condition_1
    $ renpy.pause(3.0, hard=True)

    #game "Selamat! Anda berhasil menyelesaikan Misi 1."
    hide screen win_condition
    #jump misi_2

label misi_1_gagal:
    stop music
    play sound wrong
    scene background
    hide screen game_screen_misi_1
    call screen lose_condition_1
    hide screen win_condition_1
    
    $ renpy.pause(3.0, hard=True)
    #game "Anda gagal menyelesaikan Misi 1. Coba lagi!"
    #jump misi_1

label misi_2:
    play music gameplay
    hide screen win_condition
    scene background
    show ngomong at right:
        zoom 0.7
        ypos 1.4
    $ durasi = 90
    $ score_1 = 0.0
    
    sagara "Misi 2: Kumpulkan skor sebanyak 5000 dalam waktu 60 detik!"
    sagara "Akan ada item buff dan ikan, buff akan menambah jumlah spawn sampah dan melipat gandakan score"
    sagara "Jika menangkap ikan akan mengurangi score"

    call screen game_screen_misi_2

    # Tunggu sampai durasi habis
    #return

label misi_2_berhasil:
    stop music
    play sound win
    scene background
    hide screen game_screen_misi_2
    hide screen lose_condition_2
    call screen win_condition_2
    $ renpy.pause(3.0, hard=True)
    #game "Selamat! Anda berhasil menyelesaikan Misi 2."
    

    #jump misi_3

label misi_2_gagal:
    stop music
    play sound wrong
    scene background
    hide screen game_screen_misi_2
    call screen lose_condition_2
    hide screen win_condition
    $ renpy.pause(3.0, hard=True)
    #game "Anda gagal menyelesaikan Misi 2. Coba lagi!"
    

    #jump misi_2

label misi_3:
    play music gameplay
    hide screen win_condition_2
    scene background
    show ngomong at right:
        zoom 0.7
        ypos 1.4

    $ sampah_speed = 5
    $ durasi = 90
    $ score_1 = 0

    sagara "Misi terakhir!, dimisi ini kumpulkan score 8000 dalam waktu 90 detik"

    call screen game_screen_misi_3
    
    #tunggu sampai durasi habis
    return

label misi_3_berhasil:
    stop music
    play sound win
    scene background
    hide screen game_screen_misi_2
    hide screen lose_condition_3
    call screen win_condition_3
    $ renpy.pause(3.0, hard=True)
    #game "Selamat! Anda berhasil menyelesaikan Misi 3."
    

    #jump Selesai

label misi_3_gagal:
    stop music
    play sound wrong
    scene background
    hide screen game_screen_misi_2
    call screen lose_condition_3
    hide screen win_condition_3
    $ renpy.pause(3.0, hard=True)
    game "Anda gagal menyelesaikan Misi 3. Coba lagi!"

    
    #jump misi_3

label modebebas:
    stop music
    scene black with fade
    pause 1.5
    play music gameplay
    $ score_1 = 0
    $ score = 0
    $ sampah_speed = 4
    $ durasi = 90

    call screen game_screen
    stop music

label kuis:
    stop music
    scene black with fade
    pause 1.5
    play music quiz
    $ current_question_index = 0
    $ score_kuis = 0
    
    call screen kuis
    stop music
    #return


# Game selesai
label Selesai:
    play music dialogscene
    hide screen win_condition
    hide screen game_screen      
    scene scene 5:
        zoom 0.7
    "Sagara akhirnya selesai membersihkan sampah yang mengapung dilautan dan dia mulai mengemasi sampah ke dalam tas sampah"
    sagara "Hufff akhirnya selesai juga ternyata banyak juga, untung aku membawa banyak tas sampah hari ini semoga sesampainya di pantai orang tidak mengira aku habis mencuri uang di bank."
    stop music

    play music ending   
    scene black with fade
    $ renpy.pause(2.0, hard=True)
    scene ending
    $ renpy.pause(4.0, hard=True)
    scene black with fade
    centered ""
    stop music

    return

label timeout:
    call screen timeout
    #return

label kuis_end:
    call screen nilai_kuis
    #return
