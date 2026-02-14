init python:
    import os
    # On récupère le nom de la session via les variables d'environnement
    # 'USER' sur Mac/Linux, 'USERNAME' sur Windows
    nom_ordinateur = os.environ.get('USERNAME', os.environ.get('USER', 'Humain'))

image black = Solid("#000000")

image ctc_triangle:
    "ctc_84e2015"
    # Point de départ : invisible et légèrement plus bas
    alpha 0.0
    yoffset 5
    
    # Apparition fluide (0.6 seconde)
    parallel:
        linear 0.6 alpha 1.0
    parallel:
        linear 0.6 yoffset 0
        
    pause 0.2 # Temps de pause au sommet de l'éclat
    
    # Disparition fluide (0.6 seconde)
    parallel:
        linear 0.6 alpha 0.0
    parallel:
        linear 0.6 yoffset -5
        
    pause 0.1
    repeat
# === INITIALISATION ===
init -1 python:
    import random

    # On déclare les variables à None (vide) pour forcer leur définition plus tard
    store.audimat_min = None
    store.audimat_max = None
    store.audimat_courant = None

    def set_audimat_range(min_val, max_val):
        """Initialise ou change la plage de l'audimat"""
        store.audimat_min = min_val
        store.audimat_max = max_val
        # Si c'est le premier lancement, on initialise la valeur courante
        if store.audimat_courant is None:
            store.audimat_courant = (min_val + max_val) // 2
        else:
            # Sinon, on s'assure que la valeur actuelle ne sort pas des nouvelles bornes
            store.audimat_courant = max(min_val, min(max_val, store.audimat_courant))

    def get_audimat_text(st, at):
        """Calcule la variation et génère l'affichage"""
        
        # Sécurité : Si les variables ne sont pas encore définies, on n'affiche rien ou 0
        if store.audimat_courant is None:
            return Text("Initialisation...", size=35, color="#00e5ff"), 0.5

        # 1. Calcul de la fluctuation (ajuste 3000/8000 selon la nervosité voulue)
        variation = random.randint(-50000, 50000)
        
        # 2. Mise à jour de la valeur
        store.audimat_courant += variation
        
        # 3. Verrouillage entre min et max
        if store.audimat_courant < store.audimat_min:
            store.audimat_courant = store.audimat_min
        elif store.audimat_courant > store.audimat_max:
            store.audimat_courant = store.audimat_max
            
        # 4. Formatage visuel
        formated = "{:,}".format(store.audimat_courant).replace(",", " ")
        
        return Text(formated + " spectateurs", size=35, color="#00e5ff", bold=True), 0.5

# --- TRANSFORMATIONS SÉCURISÉES ---
transform tv_shrink:
    ease 0.8 zoom 0.7 xpos 400 ypos 150 matrixcolor BrightnessMatrix(-0.1)

# Transformation pour remettre l'écran à la normale 
transform tv_reset:
    ease 0.8 zoom 1.0 xpos 0 ypos 0 matrixcolor BrightnessMatrix(0.0)

# --- DÉFINITION DES PERSONNAGES ---
# On utilise les couleurs de ton interface (Rouge et Blanc/Gris)
# Définitions des personnages avec le petit logo de suite (CTC)
define m = Character("Mitsuko", color="#ffffff", image="mitsuko", ctc="ctc_triangle", ctc_position="nestled")
define mi = Character("Miki", color="#8B0000", image="Miki", ctc="ctc_triangle", ctc_position="nestled")
define d = Character("Daiki", color="#7f8c8d", ctc="ctc_triangle", ctc_position="nestled")
define chauffeur = Character("Chauffeur", color="#95a5a6", ctc="ctc_triangle", ctc_position="nestled")
define h = Character("Himari", color="#ff85a2", ctc="ctc_triangle", ctc_position="nestled")
define fan = Character("Lycéenne", color="#ff69b4", ctc="ctc_triangle", ctc_position="nestled")
define n = Character("Nobuyuki", color="#a29bfe", ctc="ctc_triangle", ctc_position="nestled")
define sato = Character("Inspecteur Sato", color="#607d8b", ctc="ctc_triangle", ctc_position="nestled")
define lyceenne1 = Character("Lycéenne 1", color="#ff69b4", ctc="ctc_triangle", ctc_position="nestled")
define lyceenne2 = Character("Lycéenne 2", color="#ff69b4", ctc="ctc_triangle", ctc_position="nestled")
define senpai = Character("Senpai", color="#ff6f61", ctc="ctc_triangle", ctc_position="nestled")
define penseedemitsuko = Character(None, what_italic=True, ctc="ctc_triangle", ctc_position="nestled")
define pr = Character("Prêtre", color="#bdc3c7", ctc="ctc_triangle", ctc_position="nestled")
define narration = Character(None, what_italic=True, ctc="ctc_triangle", ctc_position="nestled")

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

# --- IMAGES ET PLACEHOLDERS ---
image bg jet_prive = Solid("#1a1a1a") # Placeholder pour la cabine First Class
image bg ciel_nuit = Solid("#000010") # Placeholder pour le ciel au-dessus du Pacifique

# --- TRANSITION CALENDRIER ---
label calendrier_transition:
    scene black with fade
    pause 1.0
    
    show text "{size=80}FÉVRIER 2015{/size}" at truecenter with dissolve
    pause 1.5
    hide text with dissolve

    show text "{size=50}3 février 21h{/size}" at truecenter with dissolve
    pause 1.0
    hide text with dissolve

    show text "{size=120}{b}3 FÉVRIER - 23h{/b}{/size}" at truecenter with easeinbottom
    pause 2.0
    hide text with fade
    return

    # --- TRANSITION CALENDRIER ---
label calendrier_chapitre_3:
    scene black with fade
    pause 1.0
    show text "{size=80}FÉVRIER 2015{/size}" at truecenter with dissolve
    pause 1.0
    hide text with dissolve
    show text "{size=120}{b}4 FÉVRIER - 08h00{/b}{/size}" at truecenter with easeinbottom
    pause 2.0
    hide text with fade
    return

label calendrier_chapitre_4:
    scene black with fade
    pause 1.0
    
    # Affichage du mois
    show text "{size=80}FÉVRIER 2015{/size}" at truecenter with dissolve
    pause 1.0
    hide text with dissolve

    # Animation du jour 5 (couleur bleue électrique pour l'aspect TV)
    show text "{size=150}{color=#00e5ff}{b}5{/b}{/color}{/size}" at truecenter with easeinbottom
    play sound "camera_click.ogg" # Bruit de déclencheur photo
    pause 1.0
    
    # Heure précise
    show text "{size=60}07:30{/size}" at truecenter with dissolve
    pause 1.5
    hide text with fade
    return


label cal(mois="FÉVRIER 2015", jour_heure="", rappel_heure=None, son=None):
    scene black with fade
    pause 1.0
    
    # 1. Affichage du mois/année
    show text "{size=80}[mois]{/size}" at truecenter with dissolve
    pause 1.0
    hide text with dissolve

    # 2. Optionnel : Affichage d'une heure intermédiaire (comme dans ton premier exemple)
    if rappel_heure:
        show text "{size=50}[rappel_heure]{/size}" at truecenter with dissolve
        pause 1.0
        hide text with dissolve

    # 3. Affichage de la date/heure principale
    # On vérifie si un son doit être joué (ex: le clic caméra)
 
    show text "{size=120}{b}[jour_heure]{/b}{/size}" at truecenter with easeinbottom
    pause 2.0
    hide text with fade


# --- VARIABLES ET ÉTATS ---
default tv_mode = False
default tension_score = 0
default tv_camera_name = ""
default chat_messages = []

# --- ANIMATION SCINTILLANTE ---
transform heart_beat:
    pause 0.5
    ease 0.6 alpha 0.3
    ease 0.6 alpha 1.0
    repeat

screen monde_de_la_television():
    zorder 100
    add Solid("#050505")
    
    # Bandeau supérieur
    frame:
        background Solid("#CC0000")
        xfill True ysize 100
        padding (20, 20)
        hbox:
            spacing 40
            text "MONDE DE LA TÉLÉVISION" size 45 bold True color "#fff" outlines [(2, "#000", 0, 0)]
            text "DIRECT : [tv_camera_name]" size 18 color "#ffcccc" yalign 0.5

    vbox:
        xpos 20 ypos 120 spacing 30 xsize 350
        vbox:
            text "AUDIENCE GLOBALE" size 16 color "#aaa"
            add DynamicDisplayable(get_audimat_text)
            text "FLUX : CONTENU EXCLUSIF" size 12 color "#00ff00"
        
        vbox:
            text "TENSION PSYCHOLOGIQUE" size 16 color "#aaa"
            bar value StaticValue(tension_score, 100) xsize 300 ysize 15
        
        null height 30
        
        # --- ZONE DE CHAT AVEC VIEWPORT (DÉFILEMENT) ---
        vbox:
            spacing 8
            text "CHAT EN DIRECT" size 14 bold True color "#00e5ff"
            null height 5
            
            viewport:
                xsize 350
                ysize 450      # Hauteur de la zone visible du chat
                mousewheel True # Active la molette
                draggable True  # Permet de faire glisser le chat
                scrollbars "vertical" # Affiche une barre de défilement à droite
                
                vbox:
                    spacing 10
                    for msg in chat_messages:
                        text msg size 14 color "#fff" line_spacing 2

    key "t" action [Hide("monde_de_la_television"), Function(renpy.show_layer_at, tv_reset, layer='master'), SetVariable("tv_mode", False)]
    key "T" action [Hide("monde_de_la_television"), Function(renpy.show_layer_at, tv_reset, layer='master'), SetVariable("tv_mode", False)]

# --- INDICATEUR SCINTILLANT ---
screen indicateur_tv_discret():
    zorder 50
    if not tv_mode:
        frame:
            background Solid("#1a1a1a") align (0.98, 0.02) padding (10, 5)
            hbox:
                spacing 10
                frame:
                    background Solid("#00e5ff") padding (5, 2) at heart_beat
                    text "T" color "#000" size 18 bold True
                text "ACCÈS TV" color "#fff" size 14 yalign 0.5
        key "t" action [Show("monde_de_la_television"), Function(renpy.show_layer_at, tv_shrink, layer='master'), SetVariable("tv_mode", True), Return()]

# --- NOTIFICATION ---
screen system_notification(message):
    modal True
    zorder 200
    add Solid("#000000f2")
    key "t" action [Show("monde_de_la_television"), Function(renpy.show_layer_at, tv_shrink, layer='master'), SetVariable("tv_mode", True), Return()]
    key "T" action [Show("monde_de_la_television"), Function(renpy.show_layer_at, tv_shrink, layer='master'), SetVariable("tv_mode", True), Return()]

    frame:
        align (0.5, 0.5) background Solid("#1a1a1a") padding (40, 40) xsize 850
        frame:
            background Solid("#ff0000") xsize 852 ysize 402 align (0.5, 0.5) 
            frame:
                background Solid("#1a1a1a") xsize 850 ysize 400 align (0.5, 0.5) padding (40, 40)
                vbox:
                    spacing 25
                    text "ALERTE : ÉVÉNEMENT MÉDIATIQUE" color "#ff0000" size 30 bold True xalign 0.5
                    text message color "#fff" size 24 text_align 0.5 xalign 0.5
                    null height 20
                    text "APPUYEZ SUR [[T]] POUR ACCÉDER AU MONDE DE LA TÉLÉVISION" color "#00e5ff" size 18 italic True xalign 0.5

        
label call_meta_mode(min_aud, max_aud, cam, tension, chat, notif):
    $ set_audimat_range(min_aud, max_aud)
    $ tv_camera_name = cam
    $ tension_score = tension
    $ chat_messages = chat
    call screen system_notification(notif)
    return

label call_meta_mode2(min_aud, max_aud, cam, tension, chat, notif):
    $ set_audimat_range(min_aud, max_aud)
    $ tv_camera_name = cam
    $ tension_score = tension
    $ chat_messages = chat
    call screen indicateur_tv_discret
    return
