
    
init python:
    import random
    import os
    import time
    
    if not persistent.high_score:
        persistent.high_score = 0

    score = 0
    score_kg = 0.0
    sampah_list = [] 
    max_sampah = 3  
    sampah_speed = 4  
    ikan_list = []
    max_ikan = 1

    buff_active = False  
    buff_duration = 15.0  
    buff_timer = 0.0  
    buff_spawn_timer = 0.0 
    buff_spawn_interval = 30.0

    buff_item = None  
    buff_speed = 3
    
    paus_list = []  
    paus_spawn_timer = 0.0  
    paus_spawn_interval = 25.0  
    paus_width = 1080

    sampah_images = []  
    ikan_images = []
    
    for i in range(1, 4):  
        sampah_images.append(f"images/botol/sampah_{i}.png")   
        sampah_images.append(f"images/kresek/kresek_{i}.png")  #
        sampah_images.append(f"images/kaleng/kaleng_{i}.png")
        sampah_images.append(f"images/kardus/kardus_{i}.png")
        sampah_images.append(f"images/indomi/indomi_{i}.png")

    for i in range(1, 1): 
        ikan_images.append(f"images/ikan/ikankiri_{i}.png")
        ikan_images.append(f"images/ikan/ikankanan_{i}.png")

    

    def spawn_buff():
        global buff_item
        if not buff_item: 
            buff_x = random.choice([-100, config.screen_width + 100])  
            buff_y = random.randint(400, 800)  
            buff_speed_x = buff_speed if buff_x < 0 else -buff_speed  
            buff_item = {'x': buff_x, 'y': buff_y, 'speed_x': buff_speed_x, 'image': "images/buff/buff.png"}


    def catch_buff(x, y):
        global buff_active, buff_timer, max_sampah, sampah_speed, buff_item
        if buff_item and abs(buff_item['x'] - x) < 50 and abs(buff_item['y'] - y) < 50:
            buff_item = None 
            buff_active = True 
            buff_timer = buff_duration  
            max_sampah += 1  
            sampah_speed += 1  
    
    def reset_buff():
        global buff_active, max_sampah, sampah_speed
        buff_active = False
        max_sampah -= 1  
        sampah_speed -= 1


    def spawn_paus():
        if len(paus_list) < 1:  
            if random.choice([True, False]):  
                paus_image = "images/ikan/paustad_1.png"  
                paus_x = config.screen_width + paus_width  
                paus_speed_x = -2 
            else:
                paus_image = "images/ikan/paustad_2.png" 
                paus_x = -paus_width  
                paus_speed_x = 2  

            paus_y = random.randint(450, 600)  
            paus_list.append({'x': paus_x, 'y': paus_y, 'image': paus_image, 'speed_x': paus_speed_x})
    

    def spawn_sampah():
        if len(sampah_list) < max_sampah:  
            arah = random.choice(["kanan", "kiri"])  
            
            
            sampah_x = config.screen_width + 100 if arah == "kanan" else -100
            sampah_speed_x = -sampah_speed if arah == "kanan" else sampah_speed
            
            
            sampah_y = random.randint(400, 800)
            sampah_image = random.choice(sampah_images) 
            

            sampah_list.append({'x': sampah_x, 'y': sampah_y, 'image': sampah_image, 'speed_x': sampah_speed_x, 'popup_score': None, 'caught': False, 'opacity': 1.0, 'rise_speed': 2})




    def spawn_ikan():
        if len(ikan_list) < max_ikan:  
            if random.choice([True, False]):  
                ikan_image = "images/ikan/ikankiri_1.png"  
                ikan_x = config.screen_width + 100  
                ikan_speed_x = -3  
            else:
                ikan_image = "images/ikan/ikankanan_1.png"  
                ikan_x = -100  
                ikan_speed_x = 3  

            ikan_y = random.randint(400, 800)  
            ikan_list.append({'x': ikan_x, 'y': ikan_y, 'image': ikan_image, 'speed_x': ikan_speed_x, 'caught': False})

    
    def catch_sampah(x, y):
        global score_kg, score, sampah_terkumpul, score_1
        for sampah in sampah_list:
            
            if not sampah['caught'] and abs(sampah['x'] - x) < 50 and abs(sampah['y'] - y) < 50:
                sampah['caught'] = True  
                sampah['speed_x'] = 0  
                multiplier = 2 if buff_active else 1  
                if "kresek" in sampah['image']:
                    popup_score = f"+{20 * multiplier}"
                    score += 20 * multiplier
                    score_kg += 0.2
                    sampah_terkumpul += 1
                    score_1 += 20 * multiplier
                    #persistent.high_score += 20 * multiplier
                elif "kaleng" in sampah['image']:
                    popup_score = f"+{45 * multiplier}"
                    score += 45 * multiplier
                    score_kg += 0.4
                    sampah_terkumpul += 1
                    score_1 += 45 * multiplier
                    #persistent.high_score += 45 * multiplier
                elif "kardus" in sampah['image']:
                    popup_score = f"+{35 * multiplier}"
                    score += 35 * multiplier
                    score_kg += 0.3
                    sampah_terkumpul += 1
                    score_1 += 35 * multiplier
                    #persistent.high_score += 35 * multiplier
                elif "indomi" in sampah['image']:
                    popup_score = f"+{50 * multiplier}"
                    score += 50 * multiplier
                    score_kg += 0.5
                    sampah_terkumpul += 1
                    score_1 += 50 * multiplier
                    #persistent.high_score += 50 * multiplier
                else:
                    popup_score = f"+{10 * multiplier}"
                    score += 10 * multiplier
                    score_kg += 0.1
                    sampah_terkumpul += 1
                    score_1 += 10 * multiplier
                    #persistent.high_score += 10 * multiplier
                sampah['popup_score'] = {'text': popup_score, 'timer': 0.5}  
                break

    def catch_ikan(x, y):
        global score, score_1
        for ikan in ikan_list:
            if not ikan['caught'] and abs(ikan['x'] - x) < 50 and abs(ikan['y'] - y) < 50:
                ikan['caught'] = True
                ikan['speed_x'] = 0
                score_1 -= 12  
                #score -= 12  
                break

    
    def update_items():
        global sampah_list, ikan_list, paus_list, score, buff_timer, buff_spawn_timer, buff_item, paus_spawn_timer,score_1
        buff_spawn_timer += 1 / 60.0
        paus_spawn_timer += 1 / 120.0

        if buff_spawn_timer >= buff_spawn_interval:
            spawn_buff()
            buff_spawn_timer = 0.0

        if buff_item:
            buff_item['x'] += buff_item['speed_x']
            if buff_item['x'] < -100 or buff_item['x'] > config.screen_width + 100:
                buff_item = None

        if buff_active:
            buff_timer -= 1 / 60.0
            if buff_timer <= 0:
                reset_buff()
        
        if paus_spawn_timer >= paus_spawn_interval and len(paus_list) == 0:
            spawn_paus()
            paus_spawn_timer = 0.0
        
        for paus in paus_list[:]:
            paus['x'] += paus['speed_x']  
            if paus['x'] < -paus_width or paus['x'] > config.screen_width + paus_width:
                paus_list.remove(paus)

        for sampah in sampah_list[:]:  
            if sampah['caught']:
                if sampah['popup_score']:  
                    sampah['popup_score']['timer'] -= 1 / 60.0  
                    if sampah['popup_score']['timer'] <= 0:
                        sampah['popup_score'] = None  
                sampah['y'] -= sampah['rise_speed'] 
                sampah['opacity'] -= 0.2 
                if sampah['opacity'] <= 0:  
                    sampah_list.remove(sampah)
            else:
                sampah['x'] += sampah['speed_x']  
                if sampah['x'] < -100 or sampah['x'] > config.screen_width + 100:  
                    sampah_list.remove(sampah)
                    score_1 -= 6 if "kresek" in sampah['image'] else 3  
                    score_1 -= 10 if "kardus" in sampah['image'] else 3
                    score_1 -= 15 if "indomi" in sampah['image'] else 3
                    score_1 -= 13 if "kaleng" in sampah['image'] else 3
                    score_1 = max(score, 0)  

        for ikan in ikan_list[:]:
            if ikan['caught']:
                ikan['y'] -= 1.5
                if ikan['y'] < -100:  
                    ikan_list.remove(ikan)
            else:
                ikan['x'] += ikan['speed_x']
                if ikan['x'] < -100 or ikan['x'] > config.screen_width + 100:
                    ikan_list.remove(ikan)

    def update_high_score(score):
        if score > persistent.high_score:
            persistent.high_score = score

style timer_text:
    size 30
    color "#000000"
    xalign 0.5
    yalign 0.5


screen game_screen:
    timer 1.0 repeat True action If(
    durasi > 0,
    [
        SetVariable('durasi', durasi - 1),
        
        # Menambah durasi setiap kelipatan 25 skor
        If(score % 25 == 0 and score > 0, SetVariable('durasi', durasi + 1)),
        
        # Menambah sampah_speed berdasarkan skor
        If(score > 4000, SetVariable('sampah_speed', 5)),
        If(score > 9000, SetVariable('sampah_speed', 6)),
        If(score > 13000, SetVariable('sampah_speed', 7)),
        If(score > 15000, SetVariable('sampah_speed', 8))
    ],
    [If(durasi == 0, [Hide('game_screen'), Jump('timeout')])])
    add "bgkanan.png"
    frame:
        style "frame_3"             
        xsize 620 ysize 620
        ypos -200 xalign 0.99
        #xalign 0.5  
        vbox:
            xalign 0.4 yalign 0.55
            text "{b}[durasi]{/b}" size 120 xalign 0.4
            #text "Score: [score_1:.0f] / 6000" style "timer_text"
            
    #add "gui/questnotif.png" zoom 0.15 ypos 0 xpos 0
    frame:
        style "frame_2"
        xsize 600 ysize 150
        vbox:
            spacing 10
            text "{b}Score            : [score]{/b}"  xpos 10
            text "{b}High Score : [persistent.high_score]{/b}" xpos 10

    if buff_active:
        frame:
            style "frame_2"
            xsize 300 ysize 150 ypos 160
            vbox:
                xalign 0.1 yalign 0.5
                text "Power Up!" color "#ff0000"
                text "[buff_timer:.1f]s" xpos 0 ypos 10
    

    for sampah in sampah_list:
        imagebutton:
            xpos sampah['x']
            ypos sampah['y']
            idle sampah['image']  
            activate_sound "audio/sfx/clicksampah.mp3"
            action Function(catch_sampah, sampah['x'], sampah['y'])  
        
        if sampah['popup_score']:  
            text sampah['popup_score']['text']:
                xpos sampah['x']
                ypos sampah['y'] - 30 
                size 30
                color "#ffffff" 

        add sampah['image'] xpos sampah['x'] ypos sampah['y'] alpha sampah['opacity']  
    
    for ikan in ikan_list:
        imagebutton:
            xpos ikan['x']
            ypos ikan['y']
            idle ikan['image']  
            activate_sound "audio/sfx/clickikan.mp3"
            action Function(catch_ikan, ikan['x'], ikan['y'])  
    if buff_item:
        imagebutton:
            xpos buff_item['x']
            ypos buff_item['y']
            idle buff_item['image']
            activate_sound "audio/sfx/clickbuff.mp3" 
            action Function(catch_buff, buff_item['x'], buff_item['y']) 
    
    for paus in paus_list:
        imagebutton:
            idle paus['image']
            xpos paus['x']
            ypos paus['y']
            focus_mask True
    $ update_high_score(score)
    $ spawn_sampah()  
    $ spawn_ikan()  
    $ update_items()  

    timer 0.001 repeat True action [Function(update_items)]
screen game_screen_misi_1:

    add "bgkanan.png"
    frame:
        style "frame_3"             
        xsize 620 ysize 620
        ypos -200 xalign 0.99
        #xalign 0.5  
        vbox:
            xalign 0.4 yalign 0.55
            text "{b}[durasi]{/b}" size 120 xalign 0.4
            #text "Score: [score_1:.0f] / 6000" style "timer_text"
            
        add "gui/questnotif.png" zoom 0.15 ypos 340 xpos 20
        text "{b}Sampah: [sampah_terkumpul]/50{/b}" ypos 380 xpos 100
        timer 1.0 repeat True action If(
            durasi > 0,
            [SetVariable('durasi', durasi - 1), If(sampah_terkumpul >= 50, [Hide('game_screen_misi_1'), Jump('misi_1_berhasil')])],
            [If(sampah_terkumpul < 50, [Hide('game_screen_misi_1'), Jump('misi_1_gagal')])]
        )


    for sampah in sampah_list:
        imagebutton:
            xpos sampah['x']
            ypos sampah['y']
            idle sampah['image'] 
            activate_sound "audio/sfx/clicksampah.mp3"
            action Function(catch_sampah, sampah['x'], sampah['y'])
        
        if sampah['popup_score']:
            text sampah['popup_score']['text']:
                xpos sampah['x']
                ypos sampah['y'] - 30  
                size 30
                color "#ffffff" 


        add sampah['image'] xpos sampah['x'] ypos sampah['y'] alpha sampah['opacity']  
    
    

    for ikan in ikan_list:
        imagebutton:
            xpos ikan['x']
            ypos ikan['y']
            idle ikan['image']  
            activate_sound "audio/sfx/clickikan.mp3"
            action Function(catch_ikan, ikan['x'], ikan['y'])  


    $ spawn_sampah() 
    #$ spawn_ikan()  
    $ update_items() 

    timer 0.001 repeat True action [Function(update_items)]


screen game_screen_misi_2:

    add "bgkanan.png"
    frame:
        style "frame_3"             
        xsize 620 ysize 620
        ypos -200 xalign 0.99
        #xalign 0.5  
        vbox:
            xalign 0.4 yalign 0.55
            text "{b}[durasi]{/b}" size 120 xalign 0.4
            #text "Score: [score_1:.0f] / 6000" style "timer_text"

        timer 1.0 repeat True action If(
            durasi > 0,
            [SetVariable('durasi', durasi - 1), If(score_1 >= 5000, [Hide('game_screen_misi_2'), Jump('misi_2_berhasil')])],
            [If(score_1 < 5000, [Hide('game_screen_misi_2'), Jump('misi_2_gagal')])]
        )

    if buff_active:
        frame:
            style "frame_2"
            xsize 300 ysize 150 ypos 160
            vbox:
                xalign 0.1 yalign 0.5
                text "Power Up!" color "#ff0000"
                text "[buff_timer:.1f]s" xpos 0 ypos 10
    
    
    for sampah in sampah_list:
        imagebutton:
            xpos sampah['x']
            ypos sampah['y']
            idle sampah['image'] 
            activate_sound "audio/sfx/clicksampah.mp3"
            action Function(catch_sampah, sampah['x'], sampah['y'])
        
        if sampah['popup_score']:
            text sampah['popup_score']['text']:
                xpos sampah['x']
                ypos sampah['y'] - 30  
                size 30
                color "#ffffff"  


        add sampah['image'] xpos sampah['x'] ypos sampah['y'] alpha sampah['opacity']  
    
    for ikan in ikan_list:
        imagebutton:
            xpos ikan['x']
            ypos ikan['y']
            idle ikan['image']  
            activate_sound "audio/sfx/clickikan.mp3"
            action Function(catch_ikan, ikan['x'], ikan['y'])  
    if buff_item:
        imagebutton:
            xpos buff_item['x']
            ypos buff_item['y']
            idle buff_item['image']
            activate_sound "audio/sfx/clickbuff.mp3" 
            action Function(catch_buff, buff_item['x'], buff_item['y']) 
    
    for paus in paus_list:
        imagebutton:
            idle paus['image']
            xpos paus['x']
            ypos paus['y']
            focus_mask True

    $ spawn_sampah()  
    $ spawn_ikan()  
    $ update_items()  

    timer 0.001 repeat True action [Function(update_items)]


screen game_screen_misi_3:

    add "bgkanan.png"
    frame:
        style "frame_3"             
        xsize 620 ysize 620
        ypos -200 xalign 0.99
        #xalign 0.5  
        vbox:
            xalign 0.4 yalign 0.55
            text "{b}[durasi]{/b}" size 120 xalign 0.4
            #text "Score: [score_1:.0f] / 6000" style "timer_text"

        timer 1.0 repeat True action If(
            durasi > 0,
            [SetVariable('durasi', durasi - 1), If(score_1 >= 8000, [Hide('game_screen_misi_3'), Jump('misi_3_berhasil')])],
            [If(score_1 < 8000, [Hide('game_screen_misi_3'), Jump('misi_3_gagal')])]
        )

    if buff_active:
        frame:
            style "frame_2"
            xsize 300 ysize 150 ypos 160
            vbox:
                xalign 0.1 yalign 0.5
                text "Power Up!" color "#ff0000"
                text "[buff_timer:.1f]s" xpos 0 ypos 10
    
    

    for sampah in sampah_list:
        imagebutton:
            xpos sampah['x']
            ypos sampah['y']
            idle sampah['image']  
            activate_sound "audio/sfx/clicksampah.mp3"
            action Function(catch_sampah, sampah['x'], sampah['y'])  
        
        if sampah['popup_score']:  
            text sampah['popup_score']['text']:
                xpos sampah['x']
                ypos sampah['y'] - 30 
                size 30
                color "#ffffff" 

        add sampah['image'] xpos sampah['x'] ypos sampah['y'] alpha sampah['opacity']  
    
    for ikan in ikan_list:
        imagebutton:
            xpos ikan['x']
            ypos ikan['y']
            idle ikan['image']  
            activate_sound "audio/sfx/clickikan.mp3"
            action Function(catch_ikan, ikan['x'], ikan['y'])  
    if buff_item:
        imagebutton:
            xpos buff_item['x']
            ypos buff_item['y']
            idle buff_item['image']
            activate_sound "audio/sfx/clickbuff.mp3" 
            action Function(catch_buff, buff_item['x'], buff_item['y']) 
    
    for paus in paus_list:
        imagebutton:
            idle paus['image']
            xpos paus['x']
            ypos paus['y']
            focus_mask True

    $ spawn_sampah()  
    $ spawn_ikan()  
    $ update_items()  

    timer 0.001 repeat True action [Function(update_items)]

screen win_condition_1:
    
    frame:
        background "images/win.png"
        #text "{b}MISI BERHASIL{/b}" color "#FFFFFF" xalign 0.5 yalign 0.1 size 70
        button:
            ypos 681 xpos 1006
            xsize 100 ysize 100
            background "gui/button/lanjutkan.png"
            hover_background "gui/button/lanjutkanhover.png"
            action Jump("misi_2")
            activate_sound "audio/sfx/click.mp3"

        button:
            ypos 681 xpos 804
            xsize 100 ysize 100
            background "gui/button/cobalagi.png"
            hover_background "gui/button/cobalagihover.png"
            action Jump("misi_1")
            activate_sound "audio/sfx/click.mp3"
screen win_condition_2:
    
    frame:
        background "images/win.png"
        #text "{b}MISI BERHASIL{/b}" color "#FFFFFF" xalign 0.5 yalign 0.1 size 70
        button:
            ypos 681 xpos 1006
            xsize 100 ysize 100
            background "gui/button/lanjutkan.png"
            hover_background "gui/button/lanjutkanhover.png"
            action Jump("misi_3")
            activate_sound "audio/sfx/click.mp3"

        button:
            ypos 681 xpos 804
            xsize 100 ysize 100
            background "gui/button/cobalagi.png"
            hover_background "gui/button/cobalagihover.png"
            action Jump("misi_2")
            activate_sound "audio/sfx/click.mp3"
screen win_condition_3:
    
    frame:
        background "images/win.png"
        #text "{b}MISI BERHASIL{/b}" color "#FFFFFF" xalign 0.5 yalign 0.1 size 70
        button:
            ypos 681 xpos 1006
            xsize 100 ysize 100
            background "gui/button/lanjutkan.png"
            hover_background "gui/button/lanjutkanhover.png"
            action Jump("Selesai")
            activate_sound "audio/sfx/click.mp3"

        button:
            ypos 681 xpos 804
            xsize 100 ysize 100
            background "gui/button/cobalagi.png"
            hover_background "gui/button/cobalagihover.png"
            action Jump("misi_3")
            activate_sound "audio/sfx/click.mp3"
screen lose_condition_1:
    frame:
        background "images/lose.png"
        button:
            ypos 671 xpos 906
            xsize 100 ysize 100
            background "gui/button/cobalagi.png"
            hover_background "gui/button/cobalagihover.png"
            action Jump("misi_1")
            activate_sound "audio/sfx/click.mp3"
screen lose_condition_2:
    frame:
        background "images/lose.png"
        button:
            ypos 671 xpos 906
            xsize 100 ysize 100
            background "gui/button/cobalagi.png"
            hover_background "gui/button/cobalagihover.png"
            action Jump("misi_2")
            activate_sound "audio/sfx/click.mp3"
screen lose_condition_3:
    frame:
        background "images/lose.png"
        button:
            ypos 671 xpos 906
            xsize 100 ysize 100
            background "gui/button/cobalagi.png"
            hover_background "gui/button/cobalagihover.png"
            action Jump("misi_3")
            activate_sound "audio/sfx/click.mp3"
screen test:
    frame :
    
        xsize 500 ysize 100
        yalign 0.1 xpos 0#1450

        text "{b}Quest:{/b}"
        vbox:
            text "Kumpulkan plastik: [plastik_count]/[plastik_target]" xpos 20 ypos 45
        #text "Plastik: [plastik_count]/[plastik_target]" xpos 10 ypos 50

    frame:

        xsize 500 ysize 100
        yalign 0.0 xpos 0
        vbox:
            text "{b}Score:{/b} [score:.1f]" #xpos 10 ypos 10
            text "{b}Sampah:{/b} [score_kg:.1f]kg" xpos 0 ypos 5
screen timeout:
    frame:
        background "images/timeout.png"
        vbox:
            spacing 10
            yalign 0.45 xalign 0.5
            vbox:
                yalign 0.45 xalign 0.5
                spacing 2
                text "{b}Score:" xalign 0.5
                text "{b}[score]{/b}"  xalign 0.5
            vbox:
                yalign 0.45 xalign 0.5
                spacing 2
                text "{b}High Score:" xalign 0.5
                text "{b}[persistent.high_score]{/b}" xalign 0.5 #xpos 10

        button:
            ypos 650 xpos 1013
            xsize 100 ysize 100
            background "gui/button/lanjutkan.png"
            hover_background "gui/button/lanjutkanhover.png"
            action MainMenu()
            activate_sound "audio/sfx/click.mp3"

        button:
            ypos 650 xpos 788
            xsize 100 ysize 100
            background "gui/button/cobalagi.png"
            hover_background "gui/button/cobalagihover.png"
            action Jump("modebebas")
            activate_sound "audio/sfx/click.mp3"
screen menuminigame:
    add "gui/overlay/game_menu.png"
    button:
        ypos 442
        xsize 603 ysize 135
        background "gui/button/modeceritaidle.png"
        hover_background "gui/button/ceritahover.png"
        action Return()
        activate_sound "audio/sfx/click.mp3"

    button:
        ypos 546
        xsize 603 ysize 135
        background "gui/button/bebasidle.png"
        hover_background "gui/button/bebashover.png"
        action Jump("modebebas")
        activate_sound "audio/sfx/click.mp3" 

    button:
        ypos 651
        xsize 603 ysize 135
        background "gui/button/kuisidle.png"
        hover_background "gui/button/kuishover.png"
        action Jump("kuis")
        activate_sound "audio/sfx/click.mp3"   

