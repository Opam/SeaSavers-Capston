default quiz_questions = [
    {"question": "Apa dampak utama sampah plastik di laut?", "choices": ["Meningkatkan populasi ikan", "Mencemari ekosistem laut", "Membuat air lebih jernih", "Mengurangi jumlah plankton"], "answer": "Mencemari ekosistem laut"},
    {"question": "Jenis sampah apa yang paling sulit terurai di alam?", "choices": ["Plastik", "Kertas", "Sisa makanan", "Daun kering"], "answer": "Plastik"},
    {"question": "Apa yang dimaksud dengan 3R dalam pengelolaan sampah?", "choices": ["Reduce, Reuse, Recycle", "Recycle, Remove, Replace", "Reduce, Remove, Reuse", "Rebuild, Reuse, Recycle"], "answer": "Reduce, Reuse, Recycle"},
    {"question": "Berapa lama waktu yang dibutuhkan plastik untuk terurai di alam?", "choices": ["10 tahun", "50 tahun", "100 tahun", "500 tahun"], "answer": "500 tahun"},
    {"question": "Apa langkah pertama yang sebaiknya dilakukan untuk mengurangi sampah plastik?", "choices": ["Membuangnya ke laut", "Menggunakan tas belanja kain", "Membakar plastik", "Menguburnya di tanah"], "answer": "Menggunakan tas belanja kain"},
    {"question": "Apa nama zona laut yang dipenuhi sampah plastik di Samudra Pasifik?", "choices": ["Pulau Sampah", "Great Pacific Garbage Patch", "Zona Sampah Pasifik", "Samudra Plastik"], "answer": "Great Pacific Garbage Patch"},
    {"question": "Apa yang dapat dilakukan untuk mengurangi penggunaan botol plastik sekali pakai?", "choices": ["Menggunakan botol minum yang dapat diisi ulang", "Membuangnya ke sungai", "Mengganti dengan botol kaca sekali pakai", "Tidak minum air botolan"], "answer": "Menggunakan botol minum yang dapat diisi ulang"},
    {"question": "Apa dampak utama dari sampah organik yang dibuang sembarangan?", "choices": ["Mengurangi kesuburan tanah", "Mencemari udara dengan bau busuk", "Menghasilkan sampah plastik", "Membuat air lebih jernih"], "answer": "Mencemari udara dengan bau busuk"},
    {"question": "Bagaimana cara terbaik mengolah sampah organik?", "choices": ["Dibakar", "Didaur ulang menjadi kompos", "Dibuang ke laut", "Disimpan dalam plastik"], "answer": "Didaur ulang menjadi kompos"},
    {"question": "Apa yang sebaiknya dilakukan dengan sampah elektronik?", "choices": ["Dibuang ke tempat sampah biasa", "Didaur ulang di tempat khusus", "Dibakar untuk mengurangi limbah", "Dibuang ke sungai"], "answer": "Didaur ulang di tempat khusus"}
]


default current_question_index = 0
default score_kuis = 0

init python:
    def check_answer(selected, correct):
            if selected == correct:
                #renpy.notify("Benar!")
                renpy.store.score_kuis += 10
            else:
                #renpy.notify("Salah!")
                renpy.store.score_kuis += 0
        
    def next_question():
        renpy.store.current_question_index += 1
        if renpy.store.current_question_index >= len(renpy.store.quiz_questions):
            renpy.jump("kuis_end")

screen kuis:
    add "gui/menua.png"
    add "images/karakter/Senyum.png" xpos -90 xzoom -1 zoom 0.85
        # Dapatkan pertanyaan saat ini
    $ current_question = quiz_questions[current_question_index]
    $ question_text = current_question["question"]
    $ choices = current_question["choices"]
    $ correct_answer = current_question["answer"]

    # Tampilkan pertanyaan
    frame:
        style "frame_5"
        xsize 895 ysize 479
        xalign 0.9 yalign 0.1
        text "{b}[question_text]{/b}" size 30 xalign 0.5 yalign 0.5

        vbox:
            xalign 0.5 ypos 500
            spacing 20
            for choice in choices:
                    #xsize 895 ysize 110 xalign 0.5
                button:
                    xsize 895 ysize 110
                    background Frame("gui/frame4.png", 10, 10)
                    hover_background Frame("gui/button/kkhover.png", 10, 10)
                    #xalign 0.1 yalign 0.5
                    text choice size 29 xalign 0.1 yalign 0.5
                    action [
                        Function(check_answer, choice, correct_answer),
                        Function(next_question)
                    ]
                    activate_sound "audio/sfx/click.mp3"

screen nilai_kuis:
    frame:
        background "images/timeout.png"
        vbox:
            spacing 10
            yalign 0.45 xalign 0.5
            vbox:
                yalign 0.45 xalign 0.5
                spacing 2
                text "{b}Score:" xalign 0.5
                text "{b}[score_kuis]{/b}"  xalign 0.5

        button:
            ypos 650 xpos 1013
            xsize 100 ysize 100
            background "gui/button/lanjutkan.png"
            hover_background "gui/button/lanjutkanhover.png"
            action Return()
            activate_sound "audio/sfx/click.mp3"

        button:
            ypos 650 xpos 788
            xsize 100 ysize 100
            background "gui/button/cobalagi.png"
            hover_background "gui/button/cobalagihover.png"
            action Jump("kuis")
            activate_sound "audio/sfx/click.mp3"