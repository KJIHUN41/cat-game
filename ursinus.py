#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from ursina import *
from random import uniform
import math

app = Ursina()
phase2_unlocked = False
orthographic=True
bosstophız=25
bossaci=0
bossaci2=120
bossaci3=240
ailcabocan=3
ailcabo_hit_cd = 0
ailcabo_hit_delay = 1 
shieldb=False
shieldb_time = 6.5        # kalkan kaç sn kapalı
shieldb_timer = 0       # geri sayım
shieldb_cd_timer = 0 
cooldown_box = False        # Turuncu box (Boss Larry) için
cooldown_shield = False
phase2_finished = False
phase3_started = False

aci = 0         
yaricap = 1.75
hiz = 70
level=1
levelrun=True
game_started = False
impact_font = "oyuny.ttf"
music =  Audio('bgms.ogg', loop=True, autoplay=True)
music.volume=0.3
larrymus = Audio('bossf1.ogg', loop=True, autoplay=False)
phase1m =  Audio('newphase1.ogg', loop=True, autoplay=False)
phase2m =  Audio('phase2m.ogg', loop=True, autoplay=False)
oyun_bitti_yazi = Text(text='OYUN BİTTİ', origin=(0,0), position=(0,0), scale=3, color=color.red,enabled=False)
bolumgecildi = Audio('bolumgecildiyeni.mp3', loop=False, autoplay=False)
phase2_music_started = False
phase2_started = False     
phase2_setup_done = False    
phase2_timer = -1.0          
phase2_label = Text(text='', scale=2, color=color.white, origin=(0,0), position=(0,0.12), enabled=False)
ailca = Entity(
    model='cube',
    texture=r'C:\Users\LENOVO\Ursinaproj\ailenbob.jpg',
    position=(2,8,0),
    scale=(0.5,0.5,0.5),enabled=False
    )
ailenspeed=12
direction5=1

boss2_labels_shown = False  # YENİ
bossal = Text(text='BOSS AİLENCAT!', scale=2, color=color.white, origin=(0,0), position=(0,0.15), font=impact_font, enabled=False)  # YENİ
bossah = Text(text='(bosa hasar vermek için önce butona basın ve sonra bossa dokunun)', scale=2, color=color.white, origin=(0,0), position=(0,0.10), font=impact_font, enabled=False)  # YENİ

ailca1 = Entity(
    model='cube',
    texture=r'C:\Users\LENOVO\Ursinaproj\ailenbob.jpg',
    position=(2,8,0),
    scale=(0.5,0.5,0.5),enabled=False
    )
ailca2 = Entity(
    model='cube',
    texture=r'C:\Users\LENOVO\Ursinaproj\ailenbob.jpg',
    position=(2,8,0),
    scale=(0.5,0.5,0.5),enabled=False)
ailcabo= Entity(model="cube",
                  texture=r'C:\Users\LENOVO\Ursinaproj\ailenbob.jpg',
                  position=(2,8,0),
                  scale=(0.7,0.7,0.7),
                  enabled=False)
lazer = Entity(
    model='sphere',
    color=color.red,
    position=(2,0,0),
    scale=(0.40,0.40,0.40),enabled=False,collider="sphere"
    )
lazer2 = Entity(
    model='sphere',
    color=color.red,
    position=(2,8,0),
    scale=(0.40,0.40,0.40),enabled=False,
    )
lazer3 = Entity(
    model='sphere',
    color=color.red,
    position=(2,8,0),
    scale=(0.40,0.40,0.40),enabled=False,collider="sphere"
    )
lazerbo = Entity(
    model='sphere',
    color=color.red,
    position=(2,8,0),
    scale=(0.55,0.55,0.55),enabled=False,collider="sphere"
    )
lazerbo2 = Entity(
    model='sphere',
    color=color.red,
    position=(4,8,0),
    scale=(0.55,0.55,0.55),enabled=False,collider="sphere"
    )
lazerbo3 = Entity(
    model='sphere',
    color=color.red,
    position=(6,8,0),
    scale=(0.55,0.55,0.55),enabled=False,collider="sphere"
    )
ailbodirection=1
ailenbossspeed=17.08

bosslarrycan=5
start_screen = Text(
    text="KEDİ OYUNU BETA \n\nBaşlamak için SPACE'e basın",
    scale=2,
    color=color.gold,
    origin=(0,0),
    position=(0,0.1),
    font=impact_font
)

phase2_setup_done = False

bossspeed=14.81
oyun_bitti = False
boss_aktif_mi = False
box = Entity(model='cube',
             color=color.orange, 
             collider='box',
             enabled=False
            )
cooldown= False
coolsüre = 3
box.collider=None
oyun = Entity(
    model='quad',
    scale=(20, 10),
    texture=r'C:\Users\LENOVO\Ursinaproj\kedi.jpg',z=1,enabled=False)
bsekranı = Entity(
    model='quad',
    scale=(20, 10),
    texture=r'C:\Users\LENOVO\Ursinaproj\download.jpg',z=1,enabled=True)
speed = 14.81
direction = 1 
trok2 = Entity(
    model='cube',
    texture=r'C:\Users\LENOVO\Ursinaproj\larry.jpg',
    position=(-12,0,0),
    scale=(1,1,1)
    )
skor=15
phase2_unlocked = False
phase2_invoked = False
yazi = Text(
    text=f'{skor}',          # Yazının içeriği
    scale=2,              # Yazı boyutu
    color=color.yellow,   # Yazı rengi (isteğe bağlı)
    origin=(0, 0),        # Ortalamayı merkezden hesaplar
    position=(0, .45)     # Ekranın üst kısmına taşır (y=0.45 yaklaşık üst orta)
)
giristxt = Text(
    text=""" OYUN BİLGİLENDİRMESİ
    Kedi oyunu,refleks ve tahmine bağlı bir dodging oyunudur.
    Oyunda 10 bölüm bulunmakta olup her bbölümün atak mekaniği farklıdır
    amacınız her 10 bölümü ölmeden atlatıp bossu yenmektir.İyi eğlenceler
    UYARI:SADECE BİR CANIN VAR. 
    (Oyunu başlatmak için Z ye basın)""",scale=2,
    color=color.gold,
    origin=(0,0),
    position=(0,0.1),
    font=impact_font,enabled=False)
trok4 = Entity(
    model='cube',
    texture=r'C:\Users\LENOVO\Ursinaproj\larry.jpg',
    position=(-12,0,0),
    scale=(1,1,1)
    )
bosslarry = Entity(
    model='cube',
    texture=r'C:\Users\LENOVO\Ursinaproj\larry.jpg',
    position=(-12,0,0),
    scale=(2.3,2.3,2.3),
    enabled=False
    )
toxt=Text(text=0,position=(0.40,-0.45))
toxt.enabled=False
toxt2=Text(text=0,position=(0.40,-0.45))
toxt2.enabled=False
trok3 = Entity(
    model='cube',
    texture=r'C:\Users\LENOVO\Ursinaproj\larry.jpg',
    position=(-12,0,0),
    scale=(1,1,1),enabled=True
    )
trok5 = Entity(
    model='cube',
    texture=r'C:\Users\LENOVO\Ursinaproj\larry.jpg',
    position=(-12,0,0),
    scale=(1,1,1),enabled=True
    )
trok1 = Entity(
    model='cube',
    texture=r'C:\Users\LENOVO\Ursinaproj\you.jpg',enabled=False,
    position=(2,0,0),
    scale=(0.5,0.5,0.5)
    )
shieldbreaker= Entity(
    model="cube",
    color=color.blue,
    collider="box",enabled=False)

trok1.collider = 'box'
trok2.collider = 'box'
trok3.collider = 'box'
trok4.collider = 'box'
trok5.collider = 'box'
bosslarry.collider = "box"
master_volume = 0.5
def move_enemy(e):
    global direction,speed,skor,dokunma

    e.x += time.dt * direction * speed

    if e.x > 12:
        direction = -1
        e.y = uniform(-4, 4)
        skor=skor-1
        yazi.text = str(skor)
        
        
        
    if e.x < -12:
        direction = 1
        e.y = uniform(-4, 4)
        skor=skor-1
        yazi.text = str(skor)
leader_enemy = trok2      
last_dir = direction      
enemies = [trok2, trok3, trok4, trok5]
skor2=15
bossdirection=1
kazandın=Text(text='TEBRİKLER BÖLÜMÜ GEÇTİN', color=color.green, scale=2, origin=(0,0))
kazandın.enabled=False
def circle_hit(a, b, r=0.6):
    
    dx = a.x - b.x
    dy = a.y - b.y
    return (dx*dx + dy*dy) <= (r*r)
def ailenmove(e):
    global direction5, ailenspeed,skor2

    
    e.y += time.dt * ailenspeed * direction5

    if e.y > 9:
        e.x = uniform(-7, 7)
        direction5 = -1
        skor2=skor2-1
        yazi.text = str(skor2)
    if e.y < -9:
        e.x = uniform(-7, 7)
        direction5 = 1
        skor2=skor2-1
        yazi.text = str(skor2)
def ailenboss(e):
    global ailenbossspeed,ailbodirection

    
    e.y += time.dt * ailenbossspeed * ailbodirection

    if e.y > 8:
        e.x = uniform(-7, 7)
        ailbodirection = -1
    if e.y < -8:
        e.x = uniform(-7, 4)
        ailbodirection = 1
        
    
def boss(e):
    global bossdirection,bossspeed

    e.x += time.dt * bossspeed * bossdirection

    if e.x > 12:
        bossdirection =- 1
        e.y = uniform(-4, 4)
        bossspeed = bossspeed
        
        
    if e.x < -12:
        bossdirection = 1
        e.y = uniform(-4, 4)
phase2_started = False
ses_yazi = Text(text=f"Ses: {int(master_volume*100)}%", position=(-.85, .45), scale=1, color=color.white)        
def update():
    global   speed,oyun_bitti,skor,boss_aktif_mi,enabled,cooldown,coolsüre,bosslarrycan,aci,bossaci,bossaci2,bossaci3,bosstophız,shieldb,reset_shieldb,shieldb_time,shieldb_timer,shieldb_cd_timer,ailcabodef,ailcabocan,vur_ailcabo,ailcabo_hit_cd,ailcabo_hit_delay,ailenbossspeed,master_volume,ses_yazi,phase2_unlocked,phase2_invoked,boss2_labels_shown,phase2_unlocked,play_only,startp2,phase2_started,phase2_setup_done,phase2_music_started,phase2_timer,phase2_started,phase3_finished

       # Bu frame'i bitir ama oyun_bitti = False, oyun devam edecek
    global aci
    global game_started
    global last_dir, direction
    if not game_started:
        if held_keys["space"]:
            giristxt.enabled=True
            start_screen.enabled=False
        if held_keys["z"]:
            bsekranı.enabled=False
            oyun.enabled=True
            trok1.enabled=True
            giristxt.enabled=False
            game_started=True
            music.pause()
            phase1m.play()   
              
    
        return
    
    if game_started:
        
        ailcalar = [ailca, ailca1, ailca2]
        lazerler = [lazer, lazer2, lazer3]
        boss_lazerler = [lazerbo, lazerbo2, lazerbo3]
        boss_aci = [bossaci, bossaci2, bossaci3]
    for lazer_obj, ailca_obj in zip(lazerler, ailcalar):
        
           
        aci -= hiz * time.dt
        r = math.radians(aci)
        lazer_obj.x = ailca_obj.x + math.cos(r) * yaricap
        lazer_obj.y = ailca_obj.y + math.sin(r) * yaricap


    for i, lazer_obj in enumerate(boss_lazerler):
        boss_aci[i] -= bosstophız * time.dt
        r = math.radians(boss_aci[i])
        lazer_obj.x = ailcabo.x + math.cos(r) * yaricap
        lazer_obj.y = ailcabo.y + math.sin(r) * yaricap
    if oyun_bitti:
        
        return
   
    if phase2_started:
        if ailcabocan <= 0:
            
            
            
            ailca.enabled = False
            ailca1.enabled = False
            ailca2.enabled = False
            lazer.enabled = False
            lazer2.enabled = False
            lazer3.enabled = False
            ailcabo.enabled = False
            lazerbo.enabled = False
            lazerbo2.enabled = False
            lazerbo3.enabled = False
            ailca.collider = None
            ailca1.collider = None
            ailca2.collider = None
            lazer.collider = None
            lazer2.collider = None
            lazer3.collider = None
            ailcabo.collider = None
            lazerbo.collider = None
            
            lazerbo2.collider = None
            lazerbo3.collider = None
            phase2_started=False
            phase2_finished=True
            return   
        
        box.enabled = False
        box.collider=None      
                
        if ailcabocan >= 0:
            ailca.enabled = True
            ailca1.enabled = True
            ailca2.enabled = True
            ailca.collider = "box"
            ailca1.collider = "box"
            ailca2.collider = "box"
            ailca1.y = ailca.y
            ailca2.y = ailca.y
            ailenmove(ailca)
            ailenmove(ailca1)
            ailenmove(ailca2)
            lazer.enabled = True
            lazer2.enabled = True
            lazer3.enabled = True
            lazer.collider = "sphere"
            lazer2.collider = "sphere"
            lazer3.collider = "sphere"
        ailcabo.enabled = False   
        ailcabo.collider = None
        shieldbreaker.enabled = False
        shieldbreaker.collider = None
        _update_shieldbreaker_appearance()
        tehlikeler = [lazer, lazer2, lazer3, ailca, ailca1, ailca2]
        if not shieldb:
            tehlikeler += [lazerbo, lazerbo2, lazerbo3]

        for obj in tehlikeler:
            if circle_hit(trok1, obj, r=0.6):
                oyun_bitti = True
                oyun_bitti_yazi.enabled = True
                return
        if skor2 <= 0:
            ailcabo.enabled = True
            ailenboss(ailcabo)
            toxt2.enabled = True
            toxt2.text = "uzaylı kedi can: {}".format(ailcabocan)
            shieldbreaker.enabled = True
            if not boss2_labels_shown:
                boss2_labels_shown = True       # YENİ
                bossal.enabled = True
                bossah.enabled = True
                invoke(setattr, bossal, 'enabled', False, delay=4)
                invoke(setattr, bossah, 'enabled', False, delay=4)
                
      
        if shieldb_timer > 0:
               
    
                
            shieldb_timer -= time.dt
        if shieldb_timer <= 0:
               
                
                # süresi bitti, tekrar aç
            shieldb = False
        if shieldb_cd_timer > 0:
               
               
    
            shieldb_cd_timer -= time.dt

    # --- kalkan butonuna dokundu mu? ---
        if (shieldbreaker.enabled and not shieldb and shieldb_cd_timer <= 0
        and circle_hit(trok1, shieldbreaker, r=0.8)):
                
            shieldb_timer = shieldb_time
            shieldb_cd_timer = 0.3
            shieldb = True
            dugmeye_basildi2()
            invoke(reset_shieldb, delay=5) # 5 sn sonra tekrar açılsın
               
               
        if shieldb:
                
            lazerbo.enabled = False
            lazerbo2.enabled = False
            lazerbo3.enabled = False
            lazerbo.collider = None
            lazerbo2.collider = None
            lazerbo3.collider = None
            ailenbossspeed=7.5
            ailcabo.collider = "box"
        if not shieldb:
            lazerbo.enabled = True
            lazerbo2.enabled = True
            lazerbo3.enabled = True
            ailenbossspeed=7.5
            ailcabo.collider = None
            
                    
                    
            
        if ailcabo_hit_cd > 0:
                
            ailcabo_hit_cd -= time.dt
        if ailcabo.enabled and ailcabo_hit_cd <= 0 and circle_hit(trok1, ailcabo, r=0.7):
            ailcabocan -= 1
            ailcabo_hit_cd = ailcabo_hit_delay
    if held_keys["w"]:
        trok1.y = trok1.y+16*time.dt
    if held_keys["s"]:
        trok1.y = trok1.y-16*time.dt
    if held_keys["d"]:
         trok1.x = trok1.x+16*time.dt
    if held_keys["a"]:
        trok1.x = trok1.x-16*time.dt  
    if held_keys['o']:
        master_volume -= 0.01
        
    if held_keys['p']:
        master_volume += 0.01
        
    master_volume = max(0.0, min(1.0, master_volume))
    ses_yazi.text = "Ses: " + str(int(master_volume*100)) + "%"
    
    for snd in (music, larrymus, phase1m, phase2m, bolumgecildi):
        snd.volume = master_volume
    if bosslarrycan > 0:
        for enemy1 in [trok2,trok3,trok4,trok5]:
            move_enemy(enemy1)
            
        for enemy4 in [trok2,trok3,trok4,trok5,bosslarry]:
        
            
            
                
            if trok1.intersects(enemy4).hit:
                
                oyun_bitti = True
                oyun_bitti_yazi.enabled=True   
        if trok1.intersects(enemy1).hit:
            
        
            oyun_bitti = True
            oyun_bitti_yazi.enabled=True
        
    if skor == 0 and not boss_aktif_mi:
        for enemy3 in [trok2,trok3,trok4,trok5,bosslarry]:
            
            move_enemy(enemy3)    
            if rect_hit(trok1, enemy3, 0.5, 0.5):
                oyun_bitti = True
                oyun_bitti_yazi.enabled = True
        box.collider = "box"
        box.enabled=True
        boss_aktif_mi = True
        bosslarry.enabled = True   
        bosslarry.position = (-12, 0, 0)  
        bossl =Text(
            text='BOSS LARRY',
            scale=2,
            color=color.white,
            origin=(0,0),
            position=(0,0.15),font=impact_font)
        bossh = Text(
            text='bosa hasar vermek için butona bas',
            scale=2,
            color=color.white,
            origin=(0,0),
            position=(0,0.10),font=impact_font)
        
        
        invoke(setattr, bossl, 'enabled', False, delay=4)
        invoke(setattr, bossh, 'enabled', False, delay=4)
    if boss_aktif_mi and bosslarrycan > 0:
        boss(bosslarry)
        toxt.enabled = True
        toxt.text = "boss larry can: {}".format(bosslarrycan)
    if not boss_aktif_mi and bosslarrycan > 0:
        toxt.enabled=False
    if held_keys["r"]:
        update()
        application.quit()
    trok1.x = clamp(trok1.x, -6.75, 5.75)
    trok1.y = clamp(trok1.y, -3.75, 3.75)
    if boss_aktif_mi and box.enabled and rect_hit(trok1, box, 0.6, 0.6):
        dugmeye_basildi()
     
    if bosslarrycan <= 0 and phase2_started == False:
        
        win1 = Text(
            text="""TEBRİKLER BÖLÜMÜ GEÇTİN
bölüm 2""",
            scale=2,
            position=(0,0.15),
            font=impact_font
        )
        invoke(setattr, win1, 'enabled', False, delay=4)

        
        
        bosslarrycan = -1
        
        
        
        bosslarry.enabled = False
        trok2.enabled = False
        trok3.enabled = False
        trok4.enabled = False
        trok5.enabled = False
        bosslarry.collider = None
        trok5.collider = None
        trok4.collider = None
        trok3.collider = None
        trok2.collider = None
        toxt.enabled = False
        boss_aktif_mi = False 
        phase1m.stop(),
        phase2m.play()
        phase2_started = True

        
        
        

        
        
        
        
        
        
def startp2():
    global phase2_started
    phase2_started==True
def play_only(track):
    """Önce tüm sesleri durdur, sonra sadece belirtilen parçayı çal."""
    for snd in (music, larrymus, phase1m, phase2m, bolumgecildi):
        try:
            snd.stop()
        except:
            pass
    track.play()

    

def rect_hit(a, b, rx=0.5, ry=0.5):
    
    dx = abs(a.x - b.x)
    dy = abs(a.y - b.y)
    return (dx <= rx) and (dy <= ry)                
def unlock_phase2():
    global phase2_unlocked,phase2_music_started
    phase2_unlocked = True
    phase2_unlocked = True
    if not phase2_music_started:
        phase2m.play()
        
        phase2_music_started = True
def reset_shieldb():
    global shieldb
    shieldb = False            
def kutukaybol():
    box.collider=None
    box.enabled=False
def dugmeye_basildi2():
    global cooldown
    if cooldown:
     
        
        return
    cooldown = True
    _update_shieldbreaker_appearance()   # << renk hemen güncellensin
    invoke(cooldownuzay, delay=coolsüre)
    
def cooldownuzay():
    global cooldown
    cooldown = False
    shieldbreaker.color = color.blue
def gizle():
    
    kazandın.enabled = False


def cooldown_bitir():
    global cooldown
    cooldown = False
    box.color = color.azure
def _update_shieldbreaker_appearance():
    # cooldown True ise gri, değilse mavi
    shieldbreaker.color = color.gray if cooldown else color.blue    
    
def dugmeye_basildi():
    global cooldown,bosslarrycan
    if cooldown:
     
        
        return

    bosslarrycan -= 1
    cooldown = True
    box.color = color.gray
    invoke(cooldown_bitir, delay=coolsüre)
    
        
        
app.run()