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


label start:

    scene test1 with fade

    play music "Livingadream.wav"

    show mitsuko at center with dissolve

    # 3. La ligne de dialogue méta-fictionnelle
    m "Bonjour, je m'appelle Mitsuko Amano. Je suis une idole japonaise, et je vais vous raconter mon histoire. Je suis le premier personnage crée par Gildas."
    
    scene bg jet_prive with fade
    
    narration "Le terminal privé de l'aéroport de Los Angeles s'effaçait déjà derrière les vitres teintées de la passerelle."

    stop music fadeout 1.5
    
    narration "Après une semaine harassante sous les projecteurs californiens pour le concert de Himari, le calme de la cabine 'First Class' de la JAL semblait être un sanctuaire de soie et de cuir."
    
    narration "Miki entra la première, son tailleur sombre impeccable malgré la fatigue. Elle se tourna vers Mitsuko avec un sourire qui n'appartenait qu'à lui."

    mi "On y est, mon cœur. Dis-moi, tu préfères être près du hublot pour regarder les nuages, ou tu veux te mettre à l'aise côté couloir ?"

    m "Je vais prendre le hublot, maman. J'ai besoin de calme."

    mi "Très bien, mon grand garçon. Installe-toi."

    narration "Miki l'aida à ranger son sac avec une attention presque excessive. Elle s'approcha de lui, posant une main fraîche sur son front, puis sur sa joue."

    mi "Tu as l'air épuisé, mon bébé. Le trajet jusqu'à Tokyo va être si long... Je ne veux pas que tu manques de quoi que ce soit."
    
    mi "Regarde la carte, j'ai déjà demandé au chef de te préparer leur meilleur bœuf Wagyu et ce homard que tu aimes tant. Tu dois reprendre des forces."

    m "Maman, je n'ai pas si faim que ça..."

    # Changement de ton : Doux mais ferme
    mi "Ne sois pas capricieux, chéri. Tu travailles tellement dur. Si tu ne manges pas, c'est mon cœur à moi qui va se serrer. Fais-le pour ta maman, d'accord ?"

    narration "L'avion commença à vibrer, amorçant son recul sur le tarmac."

    mi "Dans quelques jours, Himari nous rejoindra et nous serons de nouveau au complet. Mais pour l'instant, c'est notre moment à nous deux. Profite de ce silence, mon trésor."
    
    mi "Daiki ne sera pas là pour nous déranger avant demain matin."

    narration "Elle marqua une pause, son regard se perdant un instant vers l'avant de l'appareil."

    mi "Est-ce que tu te rends compte de la chance qu'on a, Mitsuko ? Personne ne peut nous atteindre ici. On est au-dessus de tout le monde."

    scene bg ciel_nuit with dissolve
    narration "Le voyage ne faisait que commencer. Les heures s'étiraient dans un silence artificiel."
    narration "À l'extérieur, le ciel était devenu d'un noir d'encre. Miki ne dormait pas. Elle surveillait le sommeil léger de son fils, comme elle surveillait tout le reste."

    scene bg jet_prive with dissolve
    narration "Mitsuko finit par se redresser. Le silence de la cabine est seulement rompu par le ronronnement sourd des réacteurs."

    m "Maman... Tu penses que Papa nous attendra à la maison ? Ou il sera encore en rendez-vous pour l'agence ?"

    narration "Miki s'arrête net. Le cliquetis du cristal contre le bois résonne comme un coup de feu."

    # Passage au ton glacial
    mi "Comment l'as-tu appelé ?"

    m "... Papa. Enfin, Daiki. Je me disais juste que pour notre retour des USA, ça serait bien qu'on dîne tous les trois, ou..."

    mi "Mitsuko, regarde-moi. Bien en face."

    mi "Ce mot, 'Papa', tu le bannis de ton vocabulaire quand tu parles de cet homme. Est-ce que c'est clair ?"
    
    mi "Daiki Amano n'est rien d'autre qu'une erreur biologique que j'ai dû ramasser dans le caniveau pour vous donner un nom légal."

    m "Mais il reste le mari avec qui tu vis, et il dirige techniquement..."

    mi "Il ne dirige rien du tout ! C’est un sac à vin qui pisse son argent dans des bouteilles de saké de troisième zone."
    
    mi "Ce type est une loque. Un raté qui n'est même pas foutu de se souvenir de l'heure de ton concert parce qu'il est trop occupé à cuver dans son propre vomi."

    narration "Elle se rapproche, son visage à quelques centimètres de celui de Mitsuko."

    mi "Tu veux savoir la vérité ? Si je ne l'avais pas épousé, il vous aurait vendus ou abandonnés à l'assistance publique pour payer ses dettes de bar."
    
    mi "Ce 'papa' comme tu dis, c'est celui qui a laissé ta vraie mère se faire massacrer parce qu'il était trop ivre pour appeler la sécurité. C’est un déchet, Mitsuko. Un putain de déchet inutile."

    m "Je... Je suis désolé. Je ne voulais pas t'énerver."

    narration "Elle lui prend le menton avec force pour le forcer à la regarder."

    mi "Ne sois pas désolé, sois lucide. Je t'ai élevé pour être un gagnant, pas pour avoir de la sympathie pour les faibles."

    narration "Elle relâche sa prise et caresse soudainement ses cheveux avec une douceur effrayante."

    mi "Écoute-moi, mon bébé... Je fais tout ça pour toi et Himari. À Tokyo, il restera dans sa chambre, à l'étage, et il fermera sa gueule."

    m "Est-ce qu'il sait au moins qu'on rentre aujourd'hui ?"

    mi "Probablement pas. Et honnêtement, je m'en fous. S'il est par terre dans le salon en train de dormir dans sa crasse, je demanderai au personnel de le traîner dans la cuisine."

    mi "Finis ton jus, chéri. Et ne me reparle plus jamais de cet homme. Pour nous, il est mort en 1998. Tu as compris ?"

    m "... Oui, maman. J'ai compris."

    mi "C’est bien, mon grand garçon. Dors un peu maintenant."

    narration "L'hôtesse de l'air s'approche silencieusement, déposant deux serviettes chaudes parfumées à l'osmanthus."

    mi "Bon, oublions ces bêtises. Regarde-moi cette carte, mon cœur. Je t'ai vu loucher sur le homard tout à l'heure..."

    m "C'est vrai que... maintenant que la pression du concert est retombée, j'ai une faim de loup."

    mi "C'est mon grand garçon, ça ! Hôtesse ? Apportez-nous la dégustation complète pour mon fils. Et rajoutez une portion de caviar Beluga."

    m "Maman, c'est beaucoup trop !"

    # Transition pour montrer que le temps a passé et que la tension est redescendue
    scene bg jet_prive with dissolve
    
    mi "Rien n'est trop beau pour toi, chéri. Mange. Je veux te voir reprendre des couleurs."

    narration "Le personnel commence à dresser la table avec une nappe en lin blanc et des couverts en argent."
    
    narration "Mitsuko commence à manger, et le plaisir du repas semble dissiper la tension de leur précédente dispute."

    m "La bouche presque pleine C'est incroyable. On n'a pas mangé aussi bien pendant toute la semaine à New York."
    
    m "Himari était tellement stressée qu'elle ne voulait que des salades et de l'eau."

    mi "Souriant Ta sœur est une perfectionniste, tout comme moi. Mais elle me manque déjà. Elle a appelé avant qu'on décolle ?"

    m "Oui, juste un message. Elle nous rejoint dans trois jours. Elle m'a dit de te dire qu'elle t'aime et qu'elle a hâte de retrouver son lit... et tes plats faits maison."

    mi "(L'œil brillant d'affection) Ma petite princesse... Je lui préparerai son ragoût préféré dès qu'elle posera le pied à la maison."
    
    mi "Et toi, Mitsuko ? Qu'est-ce que tu as pensé du public américain ? Ils étaient à tes pieds, je l'ai vu depuis les coulisses."

    m "C'était fou, maman. Quand j'ai commencé le solo au piano, j'ai cru que le stade allait s'effondrer. Mais au fond... je préfère le public japonais."

    mi "C'est parce que tu as une sensibilité d'artiste noble, mon bébé. Les Américains aiment le spectacle, mais nous, nous aimons l'âme."
    
    mi "On va faire de 2015 l'année de votre consécration totale. J'ai déjà quelques contrats en tête pour ton prochain album solo."

    m "Déjà ? On vient à peine de finir la tournée mondiale..."

    mi "(Lui caressant la main) Le monde n'attend pas, chéri. Ta maman s'occupe de la paperasse et des requins. Toi, tu n'as qu'à créer."
    
    mi "Dis-moi, tu as vu la nouvelle montre que je t'ai achetée ? Elle est dans ton sac."

    m "Encore un cadeau ? Maman, tu m'en as déjà fait un pour l'ouverture du concert."

    mi "un ton léger mais sans réplique C'est pour marquer le coup. Une montre pour que tu n'oublies jamais que ton temps est précieux, et qu'il m'appartient un peu aussi."

    # Transition vers la scène du film
    scene bg jet_prive 
    with Fade(1.5, 0.5, 1.5) # Un fondu long pour marquer l'installation dans le film
    
    narration "Miki a fait incliner leurs deux sièges. Elle a insisté pour qu'ils partagent la même grande couverture en cachemire, créant une bulle d'intimité totale."

    mi "Regarde, chéri... Ils ont mis ce vieux film français que nous avions commencé l'année dernière. L'histoire du pianiste qui dirige l'Opéra de Paris."

    narration "Elle appuie sur 'Play'. Le générique défile, éclairant leurs visages dans le noir. Miki pose sa tête sur l'épaule de Mitsuko."
    
    narration "Pour Mitsuko, c'est le poids habituel de l'affection de sa mère : protecteur, mais pesant."

    m "Tu penses qu'Ami aurait été fière de moi ? De ce que je suis devenu ?"

    narration "Le corps de Miki se tend imperceptiblement. Elle marque un silence, ses yeux fixés sur les images qui dansent sur l'écran."

    mi "Elle serait éblouie, mon cœur. Mais n'oublie jamais... c'est moi qui t'ai tenu la main quand il n'y avait plus personne. Elle t'a donné la vie, mais c'est moi qui t'ai construit."

    scene bg jet_prive with dissolve
    narration "Sur l'écran, un thriller policier japonais à gros budget touche à sa fin."

    mi "(Enthousiaste) Je le savais ! C'est forcément le majordome. Il a utilisé le poison dans le thé ! Ma théorie tient la route, non ?"

    m "Maman... ta théorie est passionnante, mais elle est pleine de trous."

    m "Je vais utiliser une technique que j'ai vue dans un vieux livre que j'aime beaucoup." 
    # Effet visuel : on peut changer la teinte de l'écran pour montrer la réflexion intense de Mitsuko
    show layer master:
        matrixcolor TintMatrix("#d1e5ff")
    with dissolve

    m "Si je suis le tueur, quel est mon plus gros problème ? Ce n'est pas de tuer, c'est de faire croire que je n'étais pas là."
    
    m "En mettant à la place du tueur, on voit que la nièce n'est pas la complice, elle est le cerveau. Elle a utilisé le majordome comme un pion."

    # On retire l'effet de teinte
    show layer master:
        matrixcolor TintMatrix("#ffffff")
    with dissolve

    narration "Le film révèle le coupable : c'est exactement le scénario décrit par Mitsuko."

    mi "(Sous le choc) C'est... c'est terrifiant, Mitsuko. La précision de ton analyse... j'en ai presque des frissons."

    mi "Promets-moi une chose, mon trésor. N'utilise jamais cette technique contre ta maman, d'accord ?"

    m "(Souriant doucement) Pourquoi je ferais ça ? On est dans la même équipe, non ?"

    # --- ARRIVÉE À TOKYO ---

    scene bg aeroport_tokyo with fade
    narration "Plusieurs heures plus tard..."
    
    # Effet de flashs (blanc rapide)
    show white_flash:
        Solid("#fff")
        alpha 1.0
        linear 0.1 alpha 0.0
    with hpunch 

    narration "Dès que les portes coulissantes s'ouvrent, un mur de flashs aveuglants accueille le duo."

    mi "(Ton assuré) Chaque chose en son temps, messieurs. Priorité au repos."

    narration "Soudain, une lycéenne se glisse sous le bras d'un agent de sécurité."

    "Fan" "Mitsuko-sama ! S'il vous plaît ! Juste un autographe ! Je vous aime plus que tout !"

    narration "Le regard de Miki se durcit. Mais Mitsuko signe le carnet doucement."

    m "Merci pour ton enthousiasme. Mais fais attention, tu aurais pu te blesser. Rentre bien chez toi, d'accord ?"

    scene bg limousine_interieur with slideleft # Transition de glissement pour simuler l'entrée dans la voiture

    mi "(Tranchante) Tu es trop indulgent."
    
    mi "Dans ce monde, l'adoration est à un cheveu de l'obsession. Et l'obsession... c'est ce qui a tué Ami."

    narration "La porte se ferme, étouffant les cris de la foule. La voiture s'élance vers la villa Amano."


label chapitre_1_taxi:

    scene bg taxi_interieur with dissolve
    narration "Pour échapper à la presse, Miki a opté pour la discrétion : un taxi urbain banalisé."
    
    chauffeur "Dites-moi... je vous reconnais, vous. Vous êtes la patronne de Daiki Productions, non ?"
    
    narration "Miki ne répond pas, fixant ostensiblement son téléphone."

    chauffeur "(Ricanant) Vous avez encore de beaux restes, je dois dire. C'est votre 'petit ami' à côté ?"

    mi "(Glaciale) C'est mon fils. Concentrez-vous sur la route."

    chauffeur "On sait tous comment les femmes comme vous montent les échelons. Daiki doit pas être le seul..."

    # Mitsuko intervient : changement d'aura
    show layer master:
        matrixcolor TintMatrix("#b22222") # Teinte rouge pour la menace
    with dissolve

    m "(Voix trop calme) Monsieur, regardez-moi bien."
    
    m "Votre licence vous autorise à transporter des passagers, pas à juger leur honneur. Si j'entends encore votre respiration, je m'assure que vous finissiez votre carrière dans une benne à ordures."

    show layer master:
        matrixcolor TintMatrix("#ffffff")
    with dissolve
    
    narration "Le chauffeur se mure dans un silence total jusqu'à la destination."

# --- ARRIVÉE À LA VILLA AMANO ---

label villa_arrivee:

    scene bg villa_entree with fade
    play audio "glass_break.ogg" # Son d'une bouteille qui roule
    
    narration "La porte s'ouvre sur une odeur rance d’alcool et de tabac."
    
    # Apparition de Daiki dans un état pitoyable
    show daiki_affale 
    mi "(Cri de dégoût) Regarde-toi, Daiki ! Une loque humaine étalée dans son propre poison !"

    d "(Voix pâteuse) Haruka... Déjà là ?!..."

    mi "(Exaspérée) Oui déjà là, espèce d'imbécile..."

    mi "Tu n'as même pas honte ? Tu es censé être l'homme de cette famille, le PDG de cette boîte, et tu n'es qu'une loque humaine étalée dans son propre poison ! Regarde tes enfants, Daiki ! Regarde Mitsuko qui se tient devant toi !"

    m "(Neutre, sans pitié) Maman, tu es trop dure... Il a juste besoin de repos."

    mi "(Regard noir) Trop dure ? Tu te rends compte de ce que tu dis, Mitsuko ? Cet homme a laissé ta mère se faire assassiner parce qu'il était trop ivre pour appeler la sécurité !"

    mi "C'est ça ton rôle de père ? Se droguer et picoler jusqu'à l'inconscience pendant qu'on trime à l'autre bout du monde ? Tu devrais crever de honte ! Un \"homme\" ? Tu ne sais même plus ce que ce mot veut dire."

    d "(Tentant de se lever) Haruka... Je suis désolé... Je voulais juste..."

    mi "(Le coupant violemment) Tu voulais juste quoi ? Te saouler jusqu'à en oublier que tu as une famille ?"

    mi "Tes pardons ne valent rien ! Tu sais qui gère tout ce qu'un homme est censé faire ici ? "

    m "(Soupire d'exaspération baissant le bras de Miya) Mère, ça suffit. Laisse-le tranquille."

    mi "(Se tournant vers Mitsuko) Toi aussi, tu devrais avoir honte de défendre ce raté. Tu es censé être mon fils, et tu te comportes comme son avocat ? Enfin, bref je vais pas tourner autour du pot." 

    narration "Daiki se recroqueville sur lui-même, incapable de répondre, brisé par la vérité crue des mots de Miki. Il baisse la tête, honteux."
    
    mi "Bon, Mitsuko, c’est une cause perdue. Va te reposer dans ta chambre. Je vais appeler le personnel pour qu'ils nettoient cette porcherie... et qu'ils le traînent jusqu'à sa chambre avant que je ne commette un meurtre."
    m "(À contrecœur) D'accord, Mère."

    window hide
    scene black with dissolve
    pause 1.0
    narration "Mitsuko monte les escaliers, jetant un dernier regard triste à son père affalé sur le canapé, avant de disparaître dans le couloir."

    narration "Quant à Miki, Elle jette un dernier regard de mépris absolu à Daiki, qui s'est rendormi ou évanoui, avant de poser sa main sur l'épaule de Mitsuko pour le guider vers l'étage."

    d "Mitsuko... Je peux rentrer dans ta chambre ?"

    m "Oui, Papa, tu peux rentrer !"

    d "(Avec un faible sourire) Merci, mon fils..."

    d "(Murmurant) Je suis désolé..."

    d "Je... je voulais m'excuser pour tout à l'heure. Pour l'état dans lequel vous m'avez trouvé. Ce n'est pas une image qu'un fils devrait avoir de son... de moi. Je suis désolé d'avoir gâché ton retour."

    m "(D'une voi douce et compatissante) Père, je t'en veux pas, je comprends ce que tu traverses, malgré tout, malgré tout ce que Mère dit, je t'aime toujours. Je ne me laisse pas influencer par elle."

    d "(Ému) Merci, Mitsuko... Tu es un garçon exceptionnel. Ta mère a de la chance de t'avoir."

    d "Tu es bien trop mûr pour ton âge, Mitsuko. Trop comme elle... Parfois, je te regarde et j'ai l'impression qu'Ami me juge à travers tes yeux." 

    d "Je suis un raté, je le sais. Mais je voulais que tu saches que je suis fier de ce que tu es devenu, même si je n'y suis pour rien."

    m "(Souriant faiblement) Merci, Papa. Ça me fait plaisir de l'entendre. Elle était comment ma mère biologique, Ami ?"

    d "(Souriant avec nostalgie) Ta mère... était une femme incroyable. Forte, belle, intelligente. Elle avait cette capacité à illuminer une pièce rien qu'en y entrant."

    d " Elle aimait la musique plus que tout, et elle avait un talent fou pour le piano. C'est elle qui m'a appris à apprécier la beauté de la vie, malgré mes défauts."

    m "(Touché) Ça me ressemble un peu, alors. J'espère pouvoir être à la hauteur de son héritage."

    m "(Murmurant) De son héritage ?..."
     
    d "(Hochant la tête) Oui, Mitsuko. Tu portes en toi une partie de ta mère. Ne l'oublie jamais."

    narration "Un silence confortable s'installe entre eux, et soudaiment, Mitsuko prends son père dans ses bras pour le réconforter." 

    d "(Surpris mais ému) Mitsuko..."

    m "(Doucement) Repose-toi, Papa. Demain est un autre jour !"

    d "(Souriant faiblement) Oui, demain est un autre jour. Merci, mon fils."

    narration "Soudain, la porte de la chambre est projetée contre le mur avec une violence inouïe. Miki se tient sur le seuil, le visage déformé par une rage aveugle."

    narration "Elle a dû surprendre la fin de la conversation et son esprit a immédiatement interprété la scène comme une agression."
    mi "(Hurlant sur Daiki) QU'EST-CE QUE TU FAIS ICI ?!"

    d "(Confus) Haruka... Je... Je parlais juste avec Mitsuko..."

    mi "(S'élançant vers lui comme une furie) Tu l'insultes encore ? Tu t'en prends à lui parce que tu es incapable de supporter ta propre médiocrité ? Je t'avais dit de rester dans ton trou !"

    m "... (Ne sachant pas comment réagir, il reste figé)"

    d "Mais non, je t'assure, on discutait calmement..."

    mi "TAIS TOI !"

    with vpunch

    narration "Dans un geste d'une rapidité fulgurante, Miki assène une gifle monumentale à Daiki. Le bruit du choc résonne dans toute la pièce. Daiki vacille, portant la main à sa joue, les yeux écarquillés par le choc et la douleur."

    m "(Choqué) Maman ! Ça suffit ! Il ne faisait rien de mal, on discutait juste !"

    mi "(Hurlant) FERME-LA, TOI ! (Ne l'écoutant même pas, elle saisit Daiki par le col de sa chemise propre) Tu ne l'approches plus ! Tu n'as pas le droit de polluer son esprit avec tes mensonges de pochetron ! Sors d'ici tout de suite !"

    narration "Elle le traîne littéralement vers le couloir. Daiki, affaibli par des années d'abus, ne se défend pas, il se laisse manipuler comme un pantin désarticulé."

    m "Maman, je te dis qu'il s'excusait ! Laisse-le tranquille !"

    mi "Ne le défends pas, Mitsuko ! Tu es trop bon, tu ne vois pas son venin ! Il essaie de te manipuler parce qu'il sait que tu es mon point faible ! Je ne le laisserai pas te détruire comme il a détruit Ami !"

    narration "Elle pousse Daiki hors de la chambre et l'entraîne vers l'escalier, ses cris continuant de résonner dans l'appartement alors qu'elle le force à retourner dans sa solitude. Mitsuko reste seul au milieu de sa chambre, le souffle court."

    narration "Il regarde sa porte ouverte. La violence de sa mère, bien qu'exercée \"pour le protéger\", lui a laissé un goût de cendre dans la bouche. Il réalise que dans cette maison, personne n'est vraiment libre, pas même lui."

    narration "Mitsuko sort de sa chambre et descend lentement les marches. Malgré la violence de la scène précédente, il ne ressent pas de colère envers Miki." 

    penseedemitsuko "Elle fait ça pour moi... Elle pense que c'est pour me protéger. Mais à quel prix ?"

    penseedemitsuko "Je me demande si un jour, je pourrai vraiment être libre ici. Ou si je suis condamné à vivre sous le joug de sa volonté ou de leur volonté..."

    penseedemitsuko "Peut-être que je devrais juste accepter les choses comme elles sont. Après tout, c'est ma famille. Même si elle est dysfonctionnelle..."

    penseedemitsuko "Non, je ne peux pas penser comme ça. Je dois trouver un moyen de m'épanouir malgré tout. Pour Himari, pour moi, pour Père et Mère."

    penseedemitsuko "Je dois être fort. Plus fort que tout ça. Je dois prouver que je suis plus qu'un simple pion dans leur jeu."

    penseedemitsuko "Un jour, je trouverai ma propre voie. Et peut-être que ce jour-là, je pourrai enfin être libre."

    penseedemitsuko "Je dois finir cette troisième année de Lycée déjà... et après, je verrai ce que l'avenir me réserve."

    narration "Mitsuko s'est habitué à cette protection féroce, presque animale. Pour lui, c'est la preuve ultime de son dévouement : elle est le bouclier qui se dresse entre lui et la laideur du monde, même si ce bouclier est parfois tranchant."

    narration "Arrivé en bas, il s'arrête dans l'ombre du couloir. La dispute continue, plus venimeuse que jamais."
    penseedemitsuko "(Soupire) Tout ça parce qu'il est venu me parler... C'est fatiguant à la longue"
    mi "(Jetant un oreiller et une couverture au visage de Daiki) Voilà. C'est ton nouveau lit. Et estime-toi heureux que je ne te foute pas sur le trottoir avec les ordures ménagères."

    d "(Assis sur le bord du canapé, la joue encore rouge) Haruka... s’il te plaît. C’est ma maison aussi. On peut au moins discuter comme des adultes ?"

    mi "(Furieuse) Discuter ? Avec toi ? Tu n'as jamais su discuter comme un adulte ! Tu es un enfant gâté qui se cache derrière ses bouteilles pour éviter de faire face à la réalité !"

    mi "Et concernant ta maison ? Quel culot ! C’est mon entreprise qui paie l'hypothèque, mon sang qui paie les factures. Et \"discuter\" ? Mais regarde-toi ! Il n'y a plus rien en toi qui ressemble à un adulte."

    d "Tu ne peux pas me faire ça... Je suis ton mari..."

    mi "(Se penchant pour lui murmurer à l'oreille, mais assez fort pour que Mitsuko entende) Mon mari ? Tu te crois encore capable de tenir ce rôle ? Ne me fais pas rire, Daiki."

    mi "Entre l'alcool et les cachetons, tu n'es plus qu'une loque impuissante. On sait tous les deux que tu es devenu aussi inutile au lit que dans un bureau. Ta petite bite et ton ego sont au même niveau : ridicules. Tu n'es même plus un homme."



    penseedemitsuko "(Pensant) Maman va trop loin cette fois... Même pour elle."
    penseedemitsuko "Mais le truc, c'est que...c'est ridicule, en dirait une pièce de théâtre le truc... il m'a juste parlé, en dirait il a tué quelqu'un..."
    penseedemitsuko "Je devrais peut-être intervenir... mais en même temps, c'est pas mon rôle de faire la police entre eux... c'est des adultes après tout... Oui des adultes qui se comportent comme des gamins..."
    penseedemitsuko "Ou je devrais peut-être juste aller dans ma chambre et les laisser régler ça entre eux... Ou peut-être que je devrais juste partir d'ici... Oui, partir loin de tout ça..."

    narration "Daiki semble se ratatiner sous l'insulte, l'humiliation finale brisant les dernières bribes de sa dignité. Il ne répond plus, fixant ses pieds nus sur le tapis luxueux."

    mi "(Se redressant, s'adressant à l'ombre où se trouve Mitsuko devant les escaliers) Mitsuko ? Tu es là, mon cœur ? Ne reste pas là à regarder ce spectacle affligeant."
    mi "Monte te coucher. Maman va fermer les lumières mais Himari ne devrait pas tarder à arriver ! Ma princesse est bientôt de retour ! (en faisant un clin d'oeil)"
    m "(Hésitant) D'accord, Mère..."
    narration "Mitsuko sort de l'ombre, croisant le regard fuyant et brisé de Daiki, puis celui, victorieux et aimant, de Miki."

    narration "Miki passe devant Daiki sans un regard, comme s'il n'était qu'un obstacle physique sur son chemin, et pose un baiser tendre sur le front de Mitsuko avant de remonter à l'étage."

    narration "Mitsuko reste un instant seul avec Daiki dans le salon plongé dans une pénombre bleutée."

# --- CHAPITRE 2 : L'ÉQUILIBRE QUI SE FRAGILISE ---

label chapitre_2_complet:
    
    call calendrier_transition

    scene bg villa_entree with fade
    
    narration "2h plus tard, après la dispute entre Miya et Daiki, le bruit d'une voiture s'arrêtant devant le perron fait sortir Miki et Mitsuko de leurs occupations."
    narration "La porte s'ouvre sur une tornade d'énergie et de parfum floral. Himari entre, traînant une petite valise griffée."

    h "(Criant de joie en rentrant dans la villa) JE SUIS RENTRÉE !"

    narration "Elle lâche ses bagages au milieu du hall et se jette littéralement dans les bras de Mitsuko, qui l'accueille avec un rire rare et sincère."

    h "Oh, Onii-chan ! Tu m'as tellement manqué ! Trois jours sans toi, c'était une éternité. New York était immense, mais sans toi pour me rassurer dans les coulisses, j'avais l'impression d'être toute petite."

    m "(Serrant sa sœur) Bienvenue à la maison, Himari-chan. Tu as assuré comme une chef, j'ai vu les vidéos du dernier shooting. Tu étais magnifique."

    h "(Se détachant pour faire une petite moue) Tu dis ça parce que tu es mon frère ! Mais j'ai cru que j'allais m'endormir debout pendant les interviews."

    narration "Miki s'avance à son tour, les yeux brillants de fierté maternelle."

    mi "Ma princesse... Ma précieuse petite fille. Enfin nous sommes au complet. Regarde-toi, tu es rayonnante. New York ne t'a pas trop fatiguée ?"

    h "Un peu, maman... mais voir vos visages, ça efface tout. J'ai apporté plein de cadeaux ! Et j'ai tellement hâte de manger autre chose que des burgers et des salades de traiteur."

    mi "(Lui caressant le visage) Tout est prêt, mon ange. J'ai demandé au chef de préparer tes sushis préférés et le ragoût que tu aimes tant. On va fêter ton retour comme il se doit."

    narration "Himari jette un regard circulaire dans le salon, cherchant quelqu'un d'autre. Son enthousiasme retombe d'un demi-ton, une pointe de tristesse voilant ses yeux clairs."

    h "Et... et Papa ? Il est là ? Il va bien ?"

    narration "Miki et Mitsuko échangent un regard rapide. Le silence qui suit est lourd, mais Himari, dans sa douceur habituelle, semble déjà comprendre la réponse sans qu'on ait besoin de lui expliquer la scène de la veille."

    m "Il est dans sa chambre, Himari. Il se repose. Tu sais comment c'est..."

    h "(Tristement) Oh... je vois. J'irai le voir tout à l'heure. Je lui ai acheté une jolie cravate à la 5ème Avenue, j'espère que ça lui fera plaisir."

    mi "(Reprenant le contrôle) Ne t'occupe pas de ça maintenant, chérie. Viens t'asseoir, raconte-nous tout sur ton shooting pour Vogue. Mitsuko et moi, on veut chaque détail !"

    narration "Ils se dirigent tous les trois vers le salon, formant un tableau familial presque parfait, si l'on oubliait l'ombre de Daiki qui plane quelque part à l'étage."

    scene bg salon_dore with dissolve
    narration "La lumière dorée de la fin de journée traverse les grandes baies vitrées. Himari est assise sur le tapis, déballant des sacs de boutiques de luxe new-yorkaises, tandis que Miki et Mitsuko savourent un thé vert de grande qualité."

    h "(Riant) Et là, le photographe me dit : « Himari-chan, essaie de ressembler à une déesse qui s'ennuie ! ». J'ai pensé à toi, maman, quand tu rentres des réunions avec les actionnaires !"

    mi "(Amusée) Oh, je vois que mes expressions servent enfin à ta carrière. Dans ce milieu, le mépris est souvent confondu avec l'élégance."

    h "(Pensive) N'empêche, j'aurais aimé que Papa voie ça... Il m'a toujours dit que j'avais les yeux de ma mère quand je posais sérieusement. Vous pensez qu'il..."

    play sound "cup_click.ogg"
    narration "Le tintement de la cuillère de Miki contre sa tasse résonne comme un glas. Son sourire s'évapore instantanément."

    mi "(Froide) Himari. Nous avons déjà eu cette discussion. Cet homme ne mérite pas d'être inclus dans nos succès. Ne gâche pas ton retour avec des pensées pour ce parasite."

    h "(Baissant les yeux) Oh... pardon, maman. C'est juste que... enfin, c'est Daiki-san. Je ferai attention, je te le promets."

    # --- LA CRISE DE MITSUKO ---
    play sound "tinnitus.ogg"
    narration "Mitsuko, qui observait la scène en silence, s'apprête à intervenir pour détendre l'atmosphère quand une sensation étrange l'envahit."
    narration "Ce n'est d'abord qu'un léger bourdonnement, comme le chant d'une cigale lointaine, mais en quelques secondes, la fréquence monte jusqu'à devenir insupportable."

    m "(Main à la tempe) ... Urgh."

    h "Onii-chan ? Qu'est-ce qu'il y a ? Tu es tout pâle."

    with vpunch
    narration "Une décharge électrique traverse son cerveau. Le salon tangue. Les voix de Miki et d'Himari deviennent lointaines, déformées."

    mi "(Se levant brusquement) Mitsuko ? Mon cœur, qu'est-ce qui t'arrive ?"

    play sound "cup_shatter.ogg"
    narration "Il s'effondre lourdement au sol, renversant sa tasse de thé qui s'écrase sur le parquet."

    h "(Hurlant) ONII-CHAN !"

    mi "(Précipitée à ses côtés) Mitsuko ! Réponds-moi ! Regarde-moi !"

    m "(Reprenant son souffle) ... Ah... Hah..."

    narration "Miki lui tient la tête contre son sein, ses mains tremblant de terreur."

    mi "(Voix brisée) Il revient ! Tu m'as fait tellement peur ! Je vais appeler l'hôpital, les meilleurs médecins du pays !"

    h "Onii-chan, s'il te plaît, dis quelque chose !"
    
    narration "Son regard croise celui de Miki, et pour la première fois, il ne voit plus seulement sa protectrice, mais une pièce sur un échiquier dont il ignore encore les règles."

    m "(Rauque) Je... je vais bien. C'était juste... une migraine. Rien de grave, maman. Je vous assure."

    # --- LE DÉPART EN CUISINE ---
    mi "(Soupirant de soulagement) Je vais quand même appeler le Dr. Saito. Je vais aller en cuisine te préparer ce bouillon de gingembre que tu aimais tant. Ça te remettra les idées en place."

    m "(Forçant un sourire) Oui, maman. Va cuisiner, ça nous fera du bien à tous."

    narration "Miki s'éloigne vers la cuisine, son pas redevenant ferme et décidé, laissant les jumeaux seuls."

    h "(Chuchotant) Onii-chan... Je vais monter. Je veux lui donner le cadeau avant que maman ne revienne."

    m "Fais attention, Himari. Il n'est pas dans un bon état."

    # --- HIMARI ET DAIKI ---
    scene bg chambre_daiki with dissolve
    narration "Himari toque doucement à la porte de la chambre de Daiki, toujours fermée comme une plaie qu'on refuse de regarder."

    h "Papa ? C'est moi... Himari. Je peux entrer ?"

    d "(Derrière la porte) Himari... Entre, ma chérie."

    narration "La chambre est plongée dans la pénombre. Daiki est assis sur le bord de son lit, les yeux bouffis."

    h "Je suis rentrée de New York. Je t'ai trouvé ça sur la 5ème Avenue. C'est une cravate en soie... je me suis dit qu'elle irait bien avec tes yeux."

    narration "Il déchire le papier avec une lenteur de vieillard. Ses lèvres se mettent à trembler."

    d "(La voix brisée) Elle est... magnifique, Himari. Merci."

    h "Tu l'essaieras pour le prochain gala ? On pourrait y aller ensemble, tous les quatre."

    d "Un gala... Regarde-moi. Je suis une ombre. Un raté qui passe ses journées à attendre que sa femme vienne lui cracher dessus pour se sentir exister."

    h "Ne dis pas ça, Papa..."

    d "Je ne sers à rien dans cette maison. Je ne suis qu'un poids mort. Ta mère a raison... je n'ai même pas été capable de protéger Ami, alors comment pourrais-je être fier de porter une cravate offerte par sa fille ?"

    h "(Les larmes aux yeux) Mais moi, je t'aime, Papa. Peu importe ce que maman dit."

    d "(Sourire amer) Va-t'en maintenant... rejoindre les gagnants en bas. L'odeur de l'échec finit par coller aux vêtements."

    # --- LE DÎNER ---
    scene bg salle_a_manger with fade
    narration "La table est dressée avec une précision chirurgicale. Daiki porte la cravate neuve, bien que le nœud soit de travers."

    mi "(Sourire éclatant) Je suis toute contente que vous soyez tous là ! Il n'y a rien de plus sacré que ces moments où la famille se retrouve."

    h "Ça sent tellement bon, maman ! J'ai l'impression que mon estomac revit enfin."

    narration "Le mal de tête violent de Mitsuko s'est calmé. Une sourde pulsation persiste, mais l'odeur du repas agit comme un baume."
    narration "Il faut l'avouer : en termes de cuisine, personne ne peut égaler Miki. Chaque bouchée est une preuve tangible de l'amour — ou du contrôle — qu'elle porte à son foyer."

    mi "Mitsuko, mon cœur, tu reprends des forces ? J'ai mis un peu plus de shiitakés dans ton bol."

    m "(Hoquant la tête) C'est délicieux, maman. Merci."

    d "(Voix basse) Le voyage n'était pas trop... fatiguant ? Le décalage horaire ne pardonne pas."

    narration "Miki lance un regard acéré à Daiki. Il se fige, les baguettes à mi-chemin de sa bouche."

    mi "Il se remet très bien, Daiki. Nous parlions justement de la prochaine tournée nationale. Le planning est serré, n'est-ce pas Mitsuko ?"

    m "(Le regard fixe) Le planning... Oui."

    mi "La mémoire joue des tours, mon bébé. Et la panique de l'époque a rendu tout le monde confus. Daiki, par exemple, était bien trop occupé à cuver pour se souvenir de l'heure exacte, n'est-ce pas ?"

    d "(Bafouillant) Je... je ne sais plus... Je crois que..."

    mi "Tu es fatigué, Mitsuko. On ne discute pas de tragédies pendant un festin."

    m "Pardonnez-moi. Oublions tout ça. Maman... ce bœuf mijoté est probablement la meilleure chose que j'ai mangée cette année."

    mi "(Visage illuminé) Oh, mon cœur... Savoir que ça te plaît efface toute ma fatigue."

    h "(Chassant les ombres) C'est clair ! Onii-chan a raison. Maman, tu devrais ouvrir un restaurant étoilé !"

    # --- LE SECRET D'HIMARI ---
    mi "Dis-moi, ma princesse... Pendant ce temps aux États-Unis... est-ce qu'il n'y aurait pas un garçon qui aurait réussi à attirer ton attention ?"

    h "(S'étouffant avec son riz) Hein ?! Quoi ?!"

    narration "Elle devient instantanément écarlate, la rougeur montant de son cou jusqu'aux oreilles."

    h "M-maman ! Pourquoi tu demandes ça ? Je n'ai pas le temps pour ça !"

    mi "(Riant) Oh, regarde cette réaction ! On dirait que j'ai touché une corde sensible."

    m "(Amusé) C'est vrai que tu es très nerveuse, tout d'un coup. Quelqu'un du staff ?"

    h "(Gênée) Arrêtez ! Onii-chan, ne t'y mets pas toi aussi ! Il n'y a rien ! Enfin... peut-être... non !"

    mi "C'est bon, ma chérie. Tu as le droit d'avoir ton jardin secret. Je veux juste que tu sois heureuse."

    m "Elle a raison. Mais sache que si ce 'garçon' existe, il devra passer un interrogatoire serré avec moi."

    # --- LE BALCON ---
    scene bg balcon_nuit with dissolve
    h "(Soupirant) Onii-chan... maman est tellement... protectrice. Parfois, j'ai peur de lui dire la vérité."

    m "Je sais. Mais il y a vraiment quelqu'un, n'est-ce pas ?"

    h "Oui. Il s'appelle {b}Otsuka Koichi{/b}. Sa famille gère un petit restaurant. Il ne savait même pas qui j'étais la première fois qu'on a parlé."

    h "Il voit la vraie moi. C'est mon ancre, Onii-chan."

    m "Je comprends pourquoi tu étais si gênée. Maman ferait une syncope. Mais s'il te rend heureuse, il est le bienvenu."

    m "Dis-moi, Himari, sois honnête. Est-ce qu'il y a d'autres garçons qui t'embêtent ?"

    h "(Riant nerveusement) Toujours un peu... Pourquoi ? Tu as peur que quelqu'un me fasse du mal ?"

    m "Je veux juste m'assurer que personne ne vienne briser ta paix. Le monde est plein de prédateurs, Himari."

    # --- BUREAU DE MITSUKO ---
    scene bg bureau_mitsuko with dissolve
    narration "Nuit. 21h00. Mitsuko a ouvert les registres de l'école et les annuaires de Setagaya."

    m "(Murmurant) Voyons voir qui tu es vraiment, Otsuka Koichi..."

    # Résultats
    show text "{size=30}Identité : Otsuka Koichi, 19 ans.\nFamille : Restaurant 'Otsuka-ya'.\nRéputation : Travailleur, boursier, aucune trace de scandale.{/size}" at truecenter with dissolve
    pause 4.0
    hide text

    play sound "door_knock.ogg"
    m "Entre, Himari. Je sais que c'est toi."

    h "Tu es déjà en train de faire ton enquête ? Qu'est-ce que l'inspecteur Mitsuko a trouvé ?"

    m "Coupable d'être un garçon trop parfait. Pour être honnête, Himari... c'est le genre de profil que je pensais disparu de Tokyo."

    h "Je te l'avais dit. Il vit dans une réalité tellement différente de la nôtre... Ça me fait du bien."

    m "Je valide ton choix. Mais maman ne doit rien savoir. Elle serait capable de faire fermer le restaurant de ses parents juste pour l'éloigner de toi."

    h "(Frissonnant) Je sais... Mais avec toi de mon côté, je me sens plus forte."

    # --- FIN DE JOURNÉE ---
    scene bg chambre_mitsuko_nuit with fade
    m "(Seul dans le noir) Profite de ton bonheur, Himari. Je m'occuperai de faire en sorte que personne, pas même maman, ne vienne l'éteindre."

    narration "Mitsuko s'est allongé dans son lit. La journée a été un tourbillon : l'épuisement, Daiki, le malaise, Himari."
    narration "Ses paupières sont lourdes, et il s'enfonce rapidement dans les limbes du sommeil, le bruit de la ville s'estompant."



# --- CHAPITRE 3 : LE RÉVEIL DU JOUEUR ---

    call calendrier_chapitre_3

    scene bg cuisine_villa with fade
    narration "L'odeur du café frais et du pain grillé remplit l'espace. Miki est déjà là, élégante, les yeux rivés sur sa tablette."
    
    play sound "phone_vibration.ogg" loop
    narration "Sur le comptoir, le smartphone de Mitsuko vibre frénétiquement. Des dizaines de notifications illuminent l'écran."
    stop sound

    mi "Bien dormi, mon cœur ? Tu as encore l'air un peu préoccupé. Tes migraines sont parties ?"

    m "Oui, ça va mieux. Maman, pourquoi mon fil d'actualité est inondé de mentions depuis ce matin ?"

    mi "(Sourire professionnel) C'est ce que j'étais en train d'analyser. Une fuite de 'Daiki Productions', sans doute. La presse parle déjà d'un nouveau projet : {b}'L’Envers du Décor'{/b}."

    narration "Mitsuko sent un frisson parcourir son échine. Ce titre s'affiche en hashtag sur son écran, à côté d'une photo de lui prise à son insu."

    m "Une émission de variété ? Ils disent que c'est un concept révolutionnaire sur l'analyse de l'image publique. Les fans spéculent déjà."

    mi "J'hésitais à accepter, c'est intrusif. Mais le buzz est là. Si on refuse, on aura l'air de cacher quelque chose."

    show himari_brioche at left with moveinleft
    h "(La bouche pleine) Une émission ? Encore ? Oh non, maman ! On n'a même pas eu le temps de défaire les valises. On reprend les cours demain, le 5 !"

    mi "Je sais, ma chérie. Mais tout le Japon attend une réponse. Le public décide parfois de l'agenda avant nous."

    m "Les gens sont sadiques... 'Hâte de voir Mitsuko craquer sous la pression des caméras'. Ils ne veulent pas une émission, ils veulent une autopsie."

    show daiki_cafe at right with dissolve
    d "(Voix hésitante) Fais attention, Mitsuko. Ils cherchent toujours la faille. Est-ce qu'on a vraiment envie de montrer 'l'envers' de notre décor ?"

    narration "Un ange passe. Miki lance un regard de marbre à Daiki."

    mi "Ne projette pas tes propres insécurités sur tes enfants, Daiki. Ils n'ont rien à cacher, eux. Ils sont parfaits."

    m "Ça va aller. On a l'habitude. Si c'est déjà viral, autant mener la danse. On a la journée pour préparer nos éléments de langage."

    h "Bon, si Onii-chan dit que c'est ok. Mais à une condition : pizzas ce soir pour notre dernière soirée de liberté !"

    mi "(Riant) Accordé, ma princesse. Profitons de ce 4 février. Demain, la réalité reprend ses droits."

    scene bg chambre_mitsuko with fade
    narration "15h30. Le téléphone à la main, Mitsuko hésite. Le besoin de vérifier si Nobuyuki est en sécurité est trop fort."

    play sound "phone_dial.ogg"
    pause 2.0
    
    n "(Voix surprise) Allô ? Mitsuko-senpai ? Je ne m'attendais pas à ce que tu m'appelles si tôt !"

    m "Oui, c'est moi. Je voulais juste prendre de tes nouvelles. Est-ce que tout va bien ? Rien d'inhabituel ?"

    n "(Riant doucement) À part les journalistes, non, rien. Pourquoi ? Tu as l'air... tendu. Il s'est passé quelque chose ?"

    m "Non, rien de grave. Je m'inquiète peut-être trop pour ma Kouhai préférée. Personne ne t'a contactée pour une émission de télévision ?"

    n "Une émission ? Non, pas du tout. Senpai... ça me touche que tu penses à moi au milieu de ton chaos. Tu me manques, tu sais."

    narration "Mitsuko ferme les yeux, soulagé mais troublé. Les médias préparent le terrain sans même prévenir les concernés."

    m "(Murmure) Fais attention à toi. Vraiment. Promets-moi de m'appeler au moindre doute."

    n "Promis, Mitsuko. Je sais me débrouiller !"

    m "(Cœur battant) Nobuyuki..."

    n "Oui ?"

    m "(Ton timide et doux) ... Je t'aime."

    narration "Silence électrique de l'autre côté du fil."

    n "(Voix tremblante) ... Moi aussi, Mitsuko. Moi aussi."

    play sound "phone_hangup.ogg"
    narration "Ce 'Je t'aime' était une bouée de sauvetage. Mais en regardant le hashtag #EnversDuDecor grimper en tendance, son expression redevient glaciale."

    scene bg bureau_Miki with fade
    narration "16h30. Mitsuko frappe à la porte. Miki est entourée d'écrans boursiers."

    mi "Mitsuko ? Tu as besoin de quelque chose ?"

    m "Non, rien de spécial. Je repensais à ce que tu as traversé... notamment avec ton ex-mari, Hiroshi Nakamura."

    play sound "pen_drop.ogg"
    narration "Le stylo de Miki s'arrête net. Une ombre traverse son regard."

    mi "(Voix sèche) Pourquoi diable s'intéresser à cet individu ? C'est un chapitre clos, Mitsuko. Un homme violent, stérile."

    m "C'est pour mon prochain rôle. Je dois jouer quelqu'un qui a vécu un divorce difficile. Comment s'est-il comporté en 2002 ?"

    mi "(Soupirant) Il a rampé, Mitsuko. Comme tous les faibles. Il a disparu. Tu as lu quelque chose sur des blogs ?"

    m "Non, rien. Juste une recherche de personnage. Merci, maman."

    narration "Il quitte le bureau. Miki croit Nakamura 'éliminé', mais sur les forums, les 'leaks' disent que l'émission va ressortir les fantômes du passé."

# --- SCÈNE : LE POIDS DU SECRET ---

label salon_daiki:

    scene bg salon_villa with dissolve
    narration "17h15. Daiki regarde une chaîne d'info sans le son. Mitsuko s'assoit à côté de lui."

    m "Tu as l'air pensif, Daiki."

    d "(Sursautant) Parfois, le silence de cette maison est plus bruyant que ses cris."

    m "Avant 1998... tu étais proche d'Ami, n'est-ce pas ? Qu'est-ce qui a changé juste avant sa mort ?"

    d "(Voix tremblante) Pourquoi ces questions... maintenant ?"

    m "L'émission va se concentrer sur toi. 'L'Ombre du Patriarche'. Quelqu'un te faisait peur ?"

    d "Ce n'était pas la peur, Mitsuko. C'était... le poids du secret. Ami savait des choses qu'elle n'aurait pas dû savoir. J'étais trop lâche pour la protéger."
    
    d "Ta mère est arrivée et a tout 'nettoyé'. Elle nous a sauvés. Mais le prix était de devenir son prisonnier."

    m "'Des choses qu'elle n'aurait pas dû savoir' ? De quoi parles-tu ?"

    with vpunch
    d "(Paniqué) Ne fouille pas là-dedans ! Si tu retournes l'échiquier, tu pourrais découvrir que le Roi et la Reine ne sont pas ceux que tu crois !"

    narration "Il s'enfuit vers la cuisine. Mitsuko réalise que Daiki n'est pas qu'une victime de l'alcool, c'est une victime du silence de Miki."

# --- SCÈNE : LE SIÈGE VIDE ---

label diner_pizza:

    scene bg salle_a_manger_pizza with fade
    narration "19h30. La soirée pizza promise à Himari. Mitsuko ne veut pas condamner Miki ; elle a été leur rempart."

    mi "Allez, mangez ! Demain, retour au lycée. Je veux que vous soyez brillants."

    h "Miam ! Merci maman. Au moins, on est ensemble."

    narration "Mitsuko remarque que le quatrième siège est vide."

    m "Maman ? Où est Daiki ?"

    mi "(Désinvolte) Je n'en ai aucune idée. Je m'en fiche. Il est probablement dans un bar. S'il n'est pas là pour vous, c'est son problème."

    h "(Inquiète) Mais il n'est pas sorti de l'après-midi..."

    mi "(Tranchante) Laisse tomber, Himari. Profite de ton repas."

# --- SCÈNE : LA PARANOÏA ---

label crise_mitsuko:

    scene bg chambre_mitsuko_nuit with fade
    narration "21h00. Mitsuko cherche le repos, mais les murs semblent l'observer."
    
    show layer master:
        matrixcolor TintMatrix("#ffcccc") # Teinte rouge d'angoisse
    with dissolve

    m "(Murmure) Calme-toi... C'est la fatigue..."

    play sound "lamp_smash.ogg"
    with vpunch
    narration "Dans un accès de rage, il balance sa lampe de chevet contre le mur. Il fouille frénétiquement sous son lit, vérifie le verrou : tout est fermé."

    m "(S'effondrant) Ils sont partout... C'est une blague... C'est une caméra cachée de l'agence... C'est pas réel !"

    stop music fadeout 2.0
    scene black with fade

    scene bg hall_villa_nuit with dissolve
    narration "21h30. Le bruit de la porte d'entrée qui s'ouvre lourdement tire Mitsuko de sa torpeur."
    
    narration "Il descend les marches quatre à quatre. En bas, dans la pénombre du vestibule, Daiki est là."
    
    narration "Il retire ses chaussures avec difficulté, l'air épuisé, mais il est sobre."

    m "(Le souffle court) Daiki... Tu es là."

    show daiki_sobre at center with dissolve
    d "(Surpris) Mitsuko ? Oui... je suis là. Je suis allé marcher. J'avais besoin de voir le ciel, loin de cette maison. Désolé pour le dîner."

    narration "Mitsuko s'arrête à quelques pas de lui. Une vague de soulagement immense l'envahit."
    
    narration "Malgré tout, Daiki reste son père. Le voir rentrer, c'est voir une pièce de sa réalité reprendre sa place."

    m "(Calme) C'est pas grave. Va te coucher. Maman a mis tes affaires sur le canapé... je suis désolé pour ça."

    d "(Souriant tristement) Ne le sois pas. C'est ma place maintenant. Bonne nuit, Mitsuko."

    scene bg salon_nuit with dissolve
    narration "Mitsuko le regarde s'installer maladroitement sur le cuir froid du salon."
    
    narration "En remontant, il jette un œil à sa montre. Demain, le 5 février, le lycée reprend ses droits."

    stop music fadeout 3.0
    scene black with fade
    pause 2.0

    # --- CHAPITRE 4 : LE SIGNAL ---

# --- CHAPITRE 4 : LE SIGNAL ---

label chapitre_4:

    call calendrier_chapitre_4

    scene bg chambre_mitsuko_matin with dissolve
    narration "Mitsuko se réveille en sursaut, le corps trempé de sueur. Il n'a pas fait de cauchemar précis, juste une sensation d'étouffement. Son réveil hurle. 07h30."
    narration "Dans trente minutes, selon les réseaux sociaux, la 'diffusion' de leur vie commence."

    scene bg villa_matin with fade
    narration "Mitsuko s'habille avec des gestes mécaniques."
    narration "07h58. Miki vérifie son agenda. Himari finit de lacer ses chaussures en fredonnant. Daiki, prostré sur le canapé, semble dormir encore. 07h59. Mitsuko retient son souffle. Le silence devient assourdissant."
    narration "08h00. Rien. Le tic-tac continue. Un oiseau chante dehors."

    narration "Mitsuko relâche sa respiration, une pointe d'ironie amère aux lèvres. C'était donc ça ?"

    show layer master:
        matrixcolor TintMatrix("#0000ff")
    with hpunch
    pause 0.2
    show layer master:
        matrixcolor TintMatrix("#ffffff")

    narration "Mais alors qu'il se lève, une décharge électrique traverse son crâne. C'est un coup de poignard fulgurant, une distorsion visuelle où le salon semble se transformer en un plateau de tournage saturé de bleu."

    m "— Argh !"
    h "Onii-chan ! Encore ta migraine ?!"
    mi "Mitsuko ! Tu es tout blanc !"

    narration "Aussi vite qu'il est venu, le malaise s'évapore. Mitsuko redresse la tête."
    m "Je... je vais bien. On doit y aller, ou on va être en retard."
    narration "Il jette un dernier regard vers Daiki. L'homme n'a pas bougé. Il ressemble à une nature morte. Mitsuko en est certain : le signal a été donné."

# --- CAMPUS ---
    scene bg campus_keio with fade
    narration "08h30. Le trajet se fait dans un brouillard mental, mais dès qu'il franchit les portes du campus, la silhouette de Nobuyuki l'apaise."

    n "Senpai ! Tu es là !"
    m "Nobuyuki... Je suis tellement heureux de te voir."

    n "Tu as l'air ailleurs, Mitsuko... Quelque chose ne va pas ?"
    m "Non. Tout va bien maintenant que je suis là."

    show bg hall_ecran_subliminal with flash
    pause 0.2
    scene bg campus_keio
    narration "Mitsuko ne remarque pas que sur l'un des écrans d'affichage, une image de Daiki endormi sur son canapé apparaît pendant une fraction de seconde."
# Scène : Toit du lycée - 5 Février 2015, 12h45

    scene bg_school_rooftop with fade
    play music "audio/school_ambience.mp3" fadein 2.0



    narration "5 Février 2015. 12h45."

    narration "Le vent d'hiver siffle entre les grillages du toit. Un bruit blanc qui couvre presque les murmures incessants des couloirs."

    n "Tu ne manges pas tes tamagoyaki, Mitsuko ? Ils ont l'air meilleurs que d'habitude."

    m "Miki a changé de chef personnel ce matin. Elle dit que l'ancien manquait de 'discipline' dans sa présentation."

    n "C'est typique d'elle... Mais au moins, ça a du goût. Tiens, goûte mon onigiri, c'est moi qui l'ai fait. Il est un peu de travers, mais bon..."

    m "Il est parfait, Nobuyuki. La perfection est ennuyeuse, tu le sais bien."

    narration "Ils partagent ce moment de calme, un îlot de sincérité au milieu d'un océan de faux-semblants. Mais l'illusion est de courte durée."

    # Arrivée des lycéennes
    play sound "audio/door_slam.mp3"
    

    lyceenne1 "Oh, mais regardez qui voilà. Notre petite sainte-nitouche est encore en train de corrompre le Prince avec sa nourriture de pauvre."

    lyceenne2 "C'est pathétique. Dis-moi, Nobu, tu penses vraiment qu'un peu de riz collant va te faire monter en grade ? Tu resteras toujours la traînée du quartier."

    n "..." # Nobuyuki serre ses baguettes, le regard baissé sur son bento.

    lyceenne1 "Hé, je te parle, la pute ! Réponds quand on s'adresse à toi. Tu te sens puissante parce que Mitsuko-sama te regarde par pitié ?"

    m "..." # L'expression de Mitsuko se glace.

    lyceenne2 "Elle doit avoir des talents cachés pour qu'il la garde près de lui... On sait toutes comment les filles comme toi finissent dans le show-business. Tu te vends bien, Nobuyuki ?"

    m "C'est assez."

    m "Votre présence pollue cet endroit. Et votre vocabulaire témoigne d'une éducation que même Daiki Productions aurait honte de financer."

    lyceenne1 "Mais Mitsuko-sama ! On vous protège ! Cette fille est une parasite, elle salit votre aura !"

    m "La seule chose qui salit mon aura ici, c'est votre ignorance. Nobuyuki est ici parce qu'elle possède une dignité que vous ne pourrez jamais acheter, même avec tout l'argent de vos parents."


    m "Si une seule insulte franchit encore vos lèvres, je m'assurerai que vos noms soient blacklistés de toutes les agences de Tokyo. Vous voulez devenir des Personnages ? Je peux faire de vous des figurants effacés en un claquement de doigts."

    lyceenne2 "M-Mais... On... Pardonnez-nous !"

    m "Discutez de votre médiocrité ailleurs. Partez."

    hide lyceenne1
    hide lyceenne2
    with easeoutright

    play music "audio/soft_piano.mp3" fadein 1.5

    narration "Le silence revient, lourd et protecteur. Mitsuko soupire et reprend sa place à côté de Nobuyuki."

    n "Tu as encore utilisé 'la menace Daiki'... Tu sais qu'elles vont se venger sur mes casiers demain."

    m "Qu'elles essaient. Je ferai installer des caméras s'il le faut. Comment va ton onigiri ? Il a refroidi."

    n "C'est pas grave. Merci, Mitsuko. Vraiment. Mais parfois, je me demande si tu ne joues pas un rôle, toi aussi... le rôle du chevalier blanc."

    m "Peut-être. Mais si c'est un rôle, alors je veux le jouer jusqu'à la fin de la saison pour toi. On disait quoi, déjà ? Ah oui, le test d'anglais de la troisième heure."

    n "Ah ! Ne m'en parle pas, j'ai l'impression que le prof a inventé de nouveaux mots juste pour nous couler..."

    m "C'est le principe du lycée, Nobuyuki. Créer des obstacles pour voir qui reste debout."

    narration "Ils reprennent leur discussion, faisant semblant d'oublier que le monde entier, au-delà du toit, attend leur prochaine tragédie."
# Suite de la scène sur le toit
    
    n "On a encore vingt minutes avant la sonnerie... Ça te dit de finir ce paquet de biscuits ? Ils sont un peu secs, mais avec ton thé, ça devrait passer."

    m "Avec plaisir. Le thé vert compense tout. D'ailleurs, tu as fini par regarder l'animé dont tout le monde parlait hier ? Celui avec l'histoire du voyageur temporel ?"

    n "Ah, celui-là ! Oui, j'ai vu les trois premiers épisodes hier soir. C'est sympa, mais je trouve que le héros s'inquiète pour rien. S'il peut retourner en arrière, pourquoi il fait une tête pareille à chaque fois ?"

    m "Peut-être parce que changer le passé est plus fatigant que de le vivre. Moi, j'aime bien le générique de fin. La mélodie au piano est assez complexe, j'ai essayé de la reproduire ce matin avant de partir."

    narration "Mitsuko esquisse un geste des doigts sur le béton, comme s'il jouait sur un clavier invisible. Son regard est doux, absent de toute tension."

    n "À propos de ce matin... Tu as pu voir ton père ? Je me demandais comment il allait."

    m "Daiki ? Oui, je l'ai croisé dans le grand salon. Il était déjà installé dans son fauteuil."

    n "Il... il va bien ? Je sais que c'est difficile pour lui depuis qu'il ne s'occupe plus de la gestion de l'entreprise. Ça ne doit pas être évident de voir Miki-san tout diriger à sa place."

    m "Il va bien, Nobuyuki. Ne t'en fais pas trop pour lui. Il était calme. On a même échangé quelques mots sur le jardin."

    n "C'est vrai ? C'est rare qu'il soit d'humeur à discuter ces derniers temps, non ? Avec l'alcool et... enfin, tu sais. Je m'inquiète juste qu'il se sente trop seul dans cette immense villa pendant que vous êtes tous au travail ou ici."

    m "Il a ses habitudes. Et puis, la maison est pleine de personnel. Il m'a même demandé si j'avais bien révisé mon anglais. C'est dire s'il était lucide."

    n "Tant mieux alors. Je l'ai toujours trouvé gentil, au fond. Il a ce regard un peu triste, mais il a toujours été poli avec moi quand je venais."

    m "C'est juste qu'il est fatigué, Nobu. Le show-business l'a usé plus vite que les autres. Mais ce matin, il avait l'air... en paix. Comme s'il n'avait plus rien à prouver."

    n "C'est peut-être la meilleure chose qui pouvait lui arriver, au final. Se reposer un peu."

    m "Sûrement. Bon, assez parlé de mes parents. Tu m'avais promis de me montrer tes dessins pour le club d'art. Tu les as avec toi ?"

    n "Oh ! Heu... oui, mais ils ne sont pas géniaux. J'ai raté toutes les perspectives sur le bâtiment C..."

    m "Fais voir. Je suis sûr que tu exagères encore."

    narration "Ils se rapprochent pour regarder le carnet de croquis, leurs têtes se frôlant presque. Le soleil de février brille faiblement, mais pour eux, la chaleur est suffisante."
    
    play sound "audio/school_bell.mp3"
    
    n "Déjà la sonnerie... Le temps passe trop vite ici."

    m "C'est parce qu'on ne regarde pas l'heure. Allez, viens. , il ne faut pas qu'on soit en retard, sinon le prof va encore nous faire un discours sur la ponctualité japonaise."

    n "C'est clair ! À tout à l'heure, Mitsuko."

    m "À tout à l'heure."
    scene bg_school_lockers with fade
    play music "audio/tension_school.mp3" fadein 1.0

    narration "14h45. La fin de la quatrième heure."

    narration "Nobuyuki marche seule dans le couloir des deuxièmes années. Elle espérait que les menaces du toit n'étaient que des mots en l'air."

    show nobuyuki neutre at center with dissolve

    n "Encore deux heures de cours... Je devrais peut-être passer au casier prendre mon dictionnaire de kanji."

    # Découverte du casier
    play sound "audio/locker_open_metallic.mp3"
    
    show nobuyuki horreur at center with flash
    
    narration "Le métal du casier a été forcé. Mais ce n'est pas le vol qui glace le sang de Nobuyuki."

    narration "À l'intérieur, ses livres sont déchirés. Sur la porte, des insultes ont été gravées et écrites au marqueur indélébile : 'PUTE', 'SALOPE', 'VIDE-COUILLES DE L'IDOLE'."

    n "N-Non... pas encore..."

    narration "Une feuille est scotchée au centre. On peut y lire : 'Tu veux juste te faire baiser par Mitsuko-sama. Reste à ta place de déchet, Nobu. On te regarde.'"

    show nobuyuki pleurs at center with dissolve

    n "Pourquoi... ? Je n'ai rien fait... Je voulais juste... être avec lui..."

    narration "Elle s'effondre contre les casiers voisins, les larmes brouillant sa vue. Le bruit des autres élèves qui passent en riant devient assourdissant."

    # Intervention du Senpai
    show senpai_conseil inquiet at left with moveinleft

    senpai "Hé ! Qu'est-ce qui se passe ici ? Mademoiselle Fujioka ?"

    narration "Un élève de troisième année, portant le brassard du Conseil des Élèves, s'arrête devant le désastre. Son visage se décompose en lisant les insultes."

    senpai "C'est... c'est ignoble. Qui a fait ça ?"

    n "S-Senpai... je ne sais pas... s'il vous plaît, ne dites rien à Mitsuko..."

    senpai "Ne rien dire ? C'est hors de question. C'est une violation grave du règlement intérieur. On ne peut pas laisser passer un tel degré de violence."

    show senpai_conseil serieux at left with dissolve

    senpai "Écoute-moi, Fujioka-san. Je vais prendre des photos pour le dossier. Je fais remonter ça immédiatement à la Présidente du Conseil des Élèves."

    senpai "Elle est très stricte sur le harcèlement. On va trouver qui a fait ça. Ne reste pas là, va à l'infirmerie te laver le visage, je m'occupe du reste."

    n "Merci... mais j'ai peur que ça ne fasse qu'empirer les choses..."

    senpai "Le Conseil est là pour protéger les élèves, pas pour laisser des fanatiques faire leur loi. Allez, va."

    hide nobuyuki with easeoutleft
    
    narration "Nobuyuki s'enfuit dans le couloir, son cœur battant à tout rompre. Elle ne voit pas que, dans l'ombre d'un pilier, un groupe de lycéennes filme la scène avec leurs téléphones."

    scene bg_school_restroom with fade
    play music "audio/nobu_tension_psychologique.mp3" fadein 1.5

    show nobuyuki pleurs at center with dissolve

    narration "Les parois froides des toilettes sont son seul refuge. Ici, personne ne peut voir la 'variable sentimentale' s'effondrer."

    n "Pourquoi ça ne s'arrête jamais... ? Avant lui... c'était pareil. Et maintenant que je suis avec lui, c'est encore pire."

    narration "Dans un accès de rage impuissante, Nobuyuki retire ses lunettes. Ses mains tremblent. Elle a envie de les fracasser contre le carrelage, de briser cette vitre qui lui permet de voir ce monde si laid."

    n "Je déteste ce visage... je déteste ces lunettes... je déteste être celle que tout le monde regarde pour mieux l'insulter."

    narration "Elle se gratte le visage nerveusement, ses ongles laissant des marques rouges sur ses joues. Puis, le choc laisse place à une lassitude glaciale. Elle se passe de l'eau froide sur les yeux, remet ses lunettes, et ajuste son uniforme."

    stop music fadeout 2.0

    # Transition vers le Bureau du Conseil
    scene bg_student_council_office with wipeleft
    play music "audio/yukari_theme_calme.mp3" fadein 1.0

    show yukari_masuyo serieux at left
    show nobuyuki neutre at right
    with dissolve

    define y = Character("Yukari Masuyo", color="#4b4b4b")

    y "Assieds-toi, Fujioka-san. Le Senpai qui t'a trouvée m'a déjà fait un rapport détaillé. J'ai vu les photos de ton casier."

    n "Désolée de vous déranger pour ça... Yukari-senpai."

    y "Tu ne me déranges pas. Le harcèlement est une gangrène pour l'excellence de cet établissement. Je ne tolérerai pas que des élèves de deuxième année transforment nos couloirs en zone de non-droit sous prétexte qu'elles sont fans d'une idole."

    n "Elles ne s'arrêteront pas... Tant que je serai proche de Mitsuko, elles continueront. Parfois... j'ai juste envie que tout s'arrête. J'ai juste envie de mourir pour ne plus avoir à supporter leurs regards."

    show yukari_masuyo douce at left with dissolve

    y "Ne dis pas ça, Nobuyuki. Ta vie a plus de valeur que l'opinion d'une foule hystérique. Je vais ouvrir une enquête formelle. Je ferai tout mon possible pour que les coupables soient sanctionnées sévèrement."

    y "Tiens. C'est une dispense pour le reste de l'après-midi. Va te reposer à l'infirmerie ou rentre chez toi. Tu n'es pas en état de suivre les cours de fin de journée."

    narration "Yukari lui tend une feuille d'excuse signée du sceau du Conseil des Élèves. Nobuyuki la prend, ses doigts effleurant le papier."

    n "Merci, Senpai... Mais... je pense que je vais quand même aller en cours."

    y "C'est une blague ? Tu viens de dire que tu voulais en finir, et tu veux retourner t'asseoir au milieu de tes bourreaux ?"

    n "Si je me cache, elles auront gagné. Et... je ne veux pas que Mitsuko s'inquiète s'il ne me voit pas sortir à l'heure habituelle."

    y "Tu es bien trop têtue pour ton propre bien. Très bien, mais si tu sens que tu vas craquer, tu viens directement ici. Compris ?"

    n "Compris. Merci encore."

    scene bg_school_gate with fade
    play music "audio/mitsuko_tension.mp3" fadein 1.0

    show yukari_masuyo serieux at left
    show mitsuko calme at right
    with dissolve

    narration "16h30. Les derniers rayons du soleil frappent les vitres du lycée. Devant les grilles, Yukari attend Mitsuko."

    y "Mitsuko. Un instant."

    m "Présidente ? Je te croyais occupée avec les rapports du club de sport."

    y "C'est plus grave que ça. Fujioka-san a été victime d'un vandalisme haineux cet après-midi. Son casier a été dévasté. Les insultes étaient... d'une violence inacceptable."

    show mitsuko colere_froide at right with flash

    m "..." # Un silence pesant s'installe. Les mains de Mitsuko se crispent sur les lanières de son sac.

    y "Elle a refusé de rentrer chez elle. Elle est restée en cours malgré son état. Je l'ai fait surveiller par un membre du conseil, mais c'est à toi qu'elle a besoin de parler."

    m "Merci de m'avoir prévenu, Yukari. Je m'occupe d'elle. Et pour les responsables... ne sois pas trop clémente."

    y "Je ne le serai pas. À demain, Mitsuko."

    hide yukari_masuyo with easeoutleft

    # Retrouvailles avec Nobuyuki
    show nobuyuki neutre at center with moveinright
    show mitsuko doux at left with dissolve

    m "Nobuyuki."

    n "Ah... Mitsuko. Tu es déjà là ? Je... je rangeais juste mes affaires..."

    narration "Mitsuko ne dit rien. Il s'approche et pose simplement ses mains sur les épaules de la jeune fille. Il voit les marques rouges sur ses joues, là où elle s'est grattée."

    m "Yukari m'a tout dit. Ne t'excuse pas, ne dis rien. C'est moi qui suis désolé. Je ne devrais pas te laisser seule un seul instant."

    n "C'est pas grave, je... j'ai l'habitude. C'est juste du marqueur et du papier..."

    m "Non, ce n'est pas rien. On ne va pas rentrer tout de suite à la villa. On a besoin de changer d'air, loin de ce lycée et de ses fantômes."

    stop music fadeout 2.0
    scene black with fade
    pause 1.0

    # Transition vers le restaurant de Ramen
    scene bg_ramen_shop with fade
    play music "audio/jazz_ramen_shop.mp3" fadein 1.5

    show mitsuko calme at left
    show nobuyuki neutre at right
    with dissolve

    n "Attends... Mitsuko ? Tu es sérieux ? On est devant un stand de Ramen de quartier..."

    m "Deux bols de Shoyu Ramen, s'il vous plaît ! Avec un supplément d'œuf pour elle."

    n "Mais... tu es une idole nationale ! Le 'Prince' ! Tu ne peux pas t'asseoir sur un tabouret en plastique et manger dans l'endroit le plus roturier de Tokyo ! Si un fan te voit..."

    m "Qu'ils regardent. Ils verront un lycéen affamé. Et puis, regarde le chef : il est trop occupé par ses bouillons pour savoir qui je suis."

    show nobuyuki rire at right with dissolve

    n "Regarde-toi... avec ton uniforme sur mesure dans ce décor de film noir. C'est tellement absurde que ça en devient drôle."

    m "C'est exactement ce qu'il nous fallait. Moins de protocole, plus de gras et de sel."

    narration "Le chef pose les bols fumants devant eux. L'odeur du bouillon est réconfortante, loin de la cuisine stérile et parfaite de Miki."

    n "Wouah... c'est délicieux ! Je ne pensais pas que tu aimais les choses aussi... populaires."

    m "C'est la première fois depuis longtemps que je ne me sens pas comme une image sur une affiche. Merci d'être là, Nobuyuki. Juste pour ça."

    n "C'est moi qui te remercie. Tu es un drôle de chevalier, Mitsuko. Un chevalier qui combat avec des baguettes."

    narration "Ils rient ensemble, un rire franc qui efface, pour quelques minutes seulement, les insultes gravées sur le métal froid du lycée."

    narration "17h40. Les rues sont désormais plongées dans l'obscurité, seulement percée par la lueur blafarde des lampadaires."

    show mitsuko calme at center with dissolve

    m "Enfin arrivé dans le quartier... Encore dix minutes de marche et je suis à la Villa."

    narration "Mitsuko remonte le col de son manteau. Le calme ici est presque pesant par rapport à l'agitation de Shinjuku. On n'entend que le bruit de ses propres pas sur l'asphalte froid."

    m "Miki va encore me demander pourquoi j'ai traîné. Je lui dirai que j'ai fini un projet à la bibliothèque. Pas besoin qu'elle sache pour les ramens."

    narration "Il tourne à l'angle d'une ruelle sombre, un raccourci qu'il emprunte parfois pour éviter l'avenue principale."

    m "C'est quoi cette odeur ? On dirait que les poubelles n'ont pas été ramassées..."

    narration "Il s'arrête un instant, l'oreille tendue. Un bruit de gouttes d'eau — ou d'un autre liquide — résonne contre une plaque de métal au fond de l'allée."

    m "Il y a quelqu'un ?"

    narration "Il plisse les yeux pour percer l'ombre. Au pied d'une pile de caisses abandonnées, une forme sombre et immobile barre le passage."

    m "Hé... Monsieur ? Ça va ?"

    narration "Mitsuko fait un pas en avant, sortant machinalement son téléphone pour éclairer la zone."

    stop music fadeout 0.5
    
    # L'écran scintille légèrement, le CTC s'agite nerveusement
    pause 1.0
# --- LA RUELLE ---
    scene bg ruelle_sombre with fade
    show layer master:
        matrixcolor TintMatrix("#4b0082")

    narration "17h45. Le ciel a pris une teinte violette, lourde et oppressante. Mitsuko et Nobuyuki marchent côte à côte. Mitsuko est plongé dans un silence de plomb."


    narration "Ils s'engagent dans un raccourci sombre. Soudain, l'odeur change. Métallique, lourde. Mitsuko s'arrête net."
    n "Senpai... qu'est-ce que c'est ? C'est... c'est un mannequin ?"

    narration "Mitsuko écarte les sacs d'un geste frénétique. Le corps bascule, révélant un buste déchiqueté. La chemise est un gouffre de pourpre sombre. Puis, il voit le visage."

    m "Non... Non, non, non..."
    n "Oh mon Dieu ! Mitsuko, on doit partir ! On doit appeler les secours !"

    with hpunch
    m "DAIKI ! PÈRE ! RÉVEILLE-TOI !"

    narration "Il s'effondre dans le sang encore tiède. C'est bien lui. L'homme qu'il a méprisé, mais qu'il aimait d'une façon complexe."
    m "Pourquoi lui ?! Il n'était rien ! Pourquoi ?!"
    n "Mitsuko, s'il te plaît ! Ne le touche pas ! Regarde-moi !"
    m "ME REGARDER ?! Regarde-le, lui ! Quel monstre a pu lui faire ça ? C'est un cauchemar... réveille-moi, je t'en supplie !"

# --- POLICE ---
    scene bg ruelle_police with fade
    narration "18h15 – La police a bouclé le périmètre. Mitsuko est assis à l'arrière d'une ambulance, une couverture de survie sur les épaules."

    show sato_neutre at center with dissolve
    sato "Monsieur Amano... Je suis navré. L'identité est confirmée. Daiki Amano. Poignardé à sept reprises."

    n "Mitsuko... Respire. On va trouver qui a fait ça."
    m "Ils ne trouveront rien. Celui qui a fait ça... c'est quelqu'un qui savait exactement où il serait. C'est quelqu'un qui voulait nous briser."

# --- INTERVENTION MÉTA (SYSTEME) ---

    label prologue_meurtre:
    # 1. On prépare les premiers messages du chat
    $ chat_initial = [
        "{size=14}{color=#44bd32}User84:{/color} DAMN ! Enfin un peu d'action ! Le père était inutile de toute façon, bon débarras !{/size}",
        "{size=14}{color=#00a8ff}IdolWatcher:{/color} Regardez la tête de Mitsuko en gros plan, son expression de douleur est 10/10. Bravo aux maquilleurs !{/size}",
        "{size=14}{color=#e84118}MysteryFan_97:{/color} WHOA ! Déjà un mort ? Qui est le tueur à votre avis ? Je parie sur l'ex-mari !{/size}",
        
        # Vague 2 : Théories sur Miki
        "{size=14}{color=#fd9644}Theory_Crafter:{/color} Oua ça doit être cette pute de Miki le tueur ! Elle voulait se débarrasser du poids mort, c'est trop évident !{/size}",
        "{size=14}{color=#4b7bef}Justice4Ami:{/color} Regardez le sourire de la matriarche ce matin... Elle savait. Elle a tout orchestré pour le buzz.{/size}",
        "{size=14}{color=#eb3b5a}Anti_Haruka_Club:{/color} Miki est une psychopathe, elle est capable de tuer son propre mari pour faire monter les actions.{/size}",
        
        # Vague 3 : Cynisme et Voyeurisme
        "{size=14}{color=#45aaf2}ClipIt_Now:{/size} Le moment où il hurle 'DAIKI ! PÈRE !' est déjà en tendance. Clip de l'année.{/size}",
        "{size=14}{color=#fa8231}Toxic_Panda:{/color} C'est scripté de fou, mais c'est bien fait. J'achète le Season Pass direct.{/size}",
        "{size=14}{color=#eb3b5a}Sasaeng_Girl:{/color} Mitsuko est tellement beau quand il pleure, j'ai fait un screenshot pour mon fond d'écran.{/size}"
    ]

    # 2. On appelle la fonction avec TOUTES les valeurs voulues
    # (Audimat Min, Max, Caméra, Tension, Liste du Chat, Ton Message)
    call call_meta_mode(14500000, 16000000, "RUELLE - CAM 04", 89, chat_initial, "Félicitations ! Le premier meurtre a été validé.\n\nEn tant que Spectateur VIP, vous avez désormais accès au Monde Télévisuel.\n\nAppuyez sur T pour voir les statistiques.")

    narration "Mitsuko, lui, ne voit rien de tout cela. Il ne voit que ses mains sales. Il est seul dans sa tragédie humaine."

    n "Mitsuko ! Arrête ça ! Regarde-moi !"
    m "C’est pas possible... Ça ne peut pas s'arrêter comme ça..."

    play sound "slap.ogg"
    with vpunch
    n "Mitsuko ! Reviens à moi ! S'il te plaît !"
    narration "Le choc brise la barrière de déni. Mitsuko s'effondre en avant contre l'épaule de sa Kouhai. Il pleure enfin, de longs sanglots de déchirement."
    m "(En sanglots) Pourquoi... pourquoi lui... ?"
    n "Je suis là, Mitsuko. Je suis là."
    scene bg_alley_crime_police with flash
    
    narration "Une berline noire dérape à l'entrée de la ruelle dans un crissement de pneus strident. Miki et Himari en sortent, escortées par des policiers."

    show himari panique at center with moveinright
    
    h "PAPA ! OÙ EST PAPA ?! DITES-MOI QUE C'EST UNE ERREUR !"

    narration "Himari court, bousculant les agents, ses cheveux en bataille et le visage déjà ravagé par la panique."

    show mitsuko sang at left
    show nobuyuki neutre at left
    with dissolve

    narration "Lorsqu'elle voit Mitsuko couvert de sang et le sac mortuaire que l'on s'apprête à emmener, elle pousse un cri qui semble déchirer le ciel de Tokyo."

    show himari pleurs at center with dissolve
    
    h "{cps=15}NON ! PAS LUI ! Il allait mieux ! Il m'avait promis d'essayer...{/cps}"

    narration "Elle tombe à genoux, ses mains griffant le goudron froid avec désespoir."

    h "Papa ! Papa, réveille-toi ! Ne nous laisse pas seuls !"

    # Miki entre en scène
    show Miki rigide at right with moveinright

    narration "À quelques mètres de là, Miki reste debout. Elle est d'une pâleur spectrale, une ombre rigide sous un lampadaire blafard."

    narration "Son regard passe de la mare de sang à Mitsuko, puis au corps de son mari. Contrairement à Himari, elle ne crie pas. Elle reste figée comme une statue de glace."

    narration "Mais ses mains, serrées sur son sac à main, tremblent si fort que le cuir craque sous la pression de ses doigts."

    mi "Qui... Qui a osé faire ça ?"

    mi "Qui a osé toucher à ce qui m'appartient ?"

    narration "Mitsuko lève les yeux vers sa mère. À travers ses larmes, il voit l'expression de Miki."

    narration "Ce n'est pas seulement de la tristesse, c'est une fureur froide..."

    n "(Elle a raison... Ce n'est pas une fin.)"

    narration "Nobuyuki, toujours agrippée à Mitsuko, observe cette famille brisée. Elle réalise que la mort de Daiki est le début d'une guerre totale."

    n "(Le calme de Miki... c'est ce qu'il y a de plus effrayant ici.)"

    $ chat_initial = [
    "{size=14}{color=#44bd32}DramaLover_TOKYO:{/color} Regardez la tête de Mitsuko... Le maquillage 'sang' est super réaliste cette saison, bravo à l'équipe technique !{/size}",
    "{size=14}{color=#00a8ff}IdolWatcher:{/color} Himari qui hurle... Un peu trop 'over-the-top' non ? Elle surjoue la tristesse, c'est pas crédible.{/size}",
    "{size=14}{color=#e84118} Sinic:{/color} Le sac mortuaire est déjà là ? Ils n'ont pas perdu de temps pour le placement de produit.{/size}",
    "{size=14}{color=#fd9644}MikiGoat:{/color} Regardez la Reine. Zéro larme. C'est ça qu'on veut voir. Froide comme la glace, elle va tous les briser.{/size}",
    "{size=14}{color=#4b7bef}RealityCheck:{/color} C'est un meurtre ou un suicide ? Si c'est un suicide, c'est naze, j'ai parié sur un tueur en série pour l'épisode 3.{/size}",
    "{size=14}{color=#eb3b5a}GossipGirl_05:{/color} Nobuyuki qui s'accroche à Mitsuko... Elle essaie de gratter du temps d'antenne même pendant un deuil, quelle opportuniste.{/size}",
    "{size=14}{color=#45aaf2}BloodFeast:{/color} Plus de sang ! Montrez le visage dans le sac ! Pourquoi ils floutent ? On a payé pour voir !{/size}",
    "{size=14}{color=#fa8231}Addictos:{/color} La réalisation est folle sur le gros plan de Miki. On sent que le budget a augmenté.{/size}",
    "{size=14}{color=#44bd32}HMMMMMM:{/color} C'est juste un acteur de moins sur le plateau. De toute façon, Daiki ne servait à rien à part picoler.{/size}",
    "{size=14}{color=#00a8ff} User1 :{/color} J'espère que la police va les brusquer un peu. Je veux voir Mitsuko craquer en direct, j'adore quand il pleure.{/size}",
    "{size=14}{color=#e84118}Shadow_Director:{/color} Prochaine étape : Miki prend le contrôle total. C'était tellement prévisible, mais j'adore le spectacle.{/size}",
    "{size=14}{color=#fd9644}User_59:{/color} C'est beau de voir une famille se détruire en HD. Merci la prod.{/size}",
    "{size=14}{color=#4b7bef}Hater_Elite:{/color} Regardez le fils prodige, il est pathétique. Sa 'perfection' vient d'en prendre un coup. 10/10 pour la mise en scène.{/size}",
    "{size=14}{color=#eb3b5a}Producer_Fanboy:{/color} La transition entre le repas de ramen et le cadavre ? Du génie. Ça c'est du divertissement.{/size}"
]
    
    call call_meta_mode2(16000000, 18400000, "RUELLE - CAM 05", 95, chat_initial, "kskrif")

    narration "21h30. L'atmosphère dans la villa est devenue suffocante. Himari a été emmenée dans sa chambre, incapable de s'arrêter de trembler."

    narration "Dans le salon, Mitsuko est assis, les mains enfin lavées, mais la peau encore rougie par le frottement obsessionnel du savon. Nobuyuki est restée à ses côtés, une présence silencieuse et nécessaire."

    narration "Miki fait les cent pas, son téléphone à la main, donnant des ordres brefs pour verrouiller l'accès à la villa et gérer les agences de presse."

    narration "Elle s'arrête devant Mitsuko. Sa voix se fait mielleuse, celle d'une mère qui tente de reprendre le contrôle d'une situation qui lui échappe."

    mi "Mon cœur, je sais que c'est un choc atroce. Je le comprends mieux que quiconque. Mais tu dois reprendre tes esprits, pour ton bien, pour notre image."

    mi "Au fond, cet homme n'avait rien d'un père. Regarde la vérité en face, Mitsuko. Il ne t'a rien donné, il ne t'a rien appris à part la honte et la gêne."

    mi "Sa mort est tragique, certes, mais elle ne change pas ce qu'il était au fond : un poids mort. Un obstacle à ton ascension."

    mi "Nous allons traverser ça ensemble. Nous allons effacer cette tache de notre histoire et faire en sorte que le monde oublie ses frasques une bonne fois pour toutes..."

    narration "Mitsuko se lève brusquement, repoussant la main de sa mère avec une violence qui la fait chanceler."

    m "TAIS-TOI, MAMAN. TAIS-TOI TOUT DE SUITE."

    mi "Mitsuko ? Comment oses-tu me parler sur ce ton... après tout ce que j'ai fait pour te protéger ce soir ?"

    m "J'en ai assez ! Assez de ton mépris ! Tu passes ton temps à cracher sur lui alors qu'il est encore froid dans une morgue ! Tu n'as aucune décence ?"

    m "Qu'il ait été un raté, un alcoolique ou une épave, ça ne change rien : c'est MON PÈRE !"

    m "Que tu le veuilles ou non, que ça entache ton précieux empire ou pas, c'est mon géniteur ! C'est son sang qui coule dans mes veines, Miki ! Pas le tien ! Jamais le tien !"

    narration "Le silence qui suit est terrifiant. Miki semble avoir été frappée physiquement. Elle, qui a tout construit pour être l'unique pilier de Mitsuko, voit le lien du sang se dresser contre elle comme une trahison."

    m "Tu n'as pas le droit de décider qui je dois pleurer ! Tu ne peux pas effacer la réalité avec tes stratégies de manager et tes communiqués de presse !"

    m "Il a été massacré dans une ruelle comme un animal, et tout ce que tu trouves à dire, c'est qu'il était un 'poids mort' ? C'était un être humain ! C'était le seul lien qu'il me restait avec ma naissance !"

    mi "Mitsuko... Je... je voulais seulement t'épargner. Te protéger de sa déchéance pour que tu ne finisses pas comme lui. Je ne pensais pas que tu... que tu tenais à lui à ce point."

    mi "Pardon. Je t'en prie... pardonne-moi. Je ne voulais pas te blesser."

    narration "Elle s'effondre sur un fauteuil, cachant son visage dans ses mains. La femme de fer vient de se briser en réalisant que le meurtre de Daiki a fait sauter le verrou de l'obéissance de son fils."

    n "Mitsuko, s'il te plaît... calme-toi. Ne sois pas trop cruel."

    n "Elle est sous le choc elle aussi, même si elle l'exprime mal. Ne dis pas des choses que tu regretteras plus tard, quand la colère sera retombée."

    narration "Mitsuko respire bruyamment, son torse se soulevant au rythme de sa fureur. Le contact de Nobuyuki agit comme un paratonnerre."

    m "Je monte voir Himari. Elle au moins, elle a encore un cœur qui bat."

    m "Ne me parle plus jamais de lui comme d'un étranger. Plus jamais. Est-ce que c'est clair ?"

    narration "Il quitte le salon sans un regard en arrière. Miki reste seule, réalisant que son 'empire' familial vient de subir un séisme irréparable."

    $ chat_initial = [
    "{size=14}{color=#44bd32} Lunatic:{/color} Oh là là, le twist du lien du sang ! Mitsuko qui remet la matriarche à sa place, j'ai crié devant mon écran !{/size}",
    "{size=14}{color=#00a8ff}IdolWatcher:{/color} Mitsuko qui pète un câble, c'est du jamais vu ! Il est tellement plus humain comme ça, j'adore !{/size}",
    "{size=14}{color=#e84118} Nosinic:{/color} Ptdrr, Miki qui craque, c'est la meilleure scène de la saison. On sent que le budget a été investi dans les acteurs cette fois.{/size}",
    "{size=14}{color=#fd9644} DramaalaSpl:{/color}La mère joue super bien la femme brisée, on y croirait presque. Donnez-lui un prix !{/size}",
    "{size=14}{color=#4b7bef} Justice4Ami:{/color} Mitsuko qui défend son père, c'est beau. On voit qu'il y a encore de l'humanité en lui malgré tout.{/size}",
    "{size=14}{color=#eb3b5a} Anti_Miya_Club:{/color} Nobuyuki est trop mignonne à essayer de calmer le jeu. J'espère qu'elle restera jusqu'au bout, elle fait une super co-star ptdrt {/size}",
    ]

    call call_meta_mode2(18400000, 20000000, "VILLA AMANO - SALON - CAM 7", 100, chat_initial, "kskrif2")

    scene bg_room_himari_night with fade
    
    narration "La chambre d'Himari, d'ordinaire si colorée et joyeuse, ressemble ce soir à une cellule de crise."

    narration "Himari est emmitouflée dans une couverture, ses yeux gonflés par les pleurs. Mitsuko est assis au pied du lit, les mains croisées, tandis que Nobuyuki est assise sur une chaise, un carnet à la main."

    show himari pleurs at center
    show mitsuko sombre at left
    show nobuyuki neutre at right
    with dissolve

    h "C’est impossible… Onii-chan, je n’arrive pas à comprendre. Je l’ai vu ce matin. À 8h pile, il était là, sur le canapé."

    h "Il m’a même fait un petit signe de la main quand je mettais mes chaussures. Il avait l'air... normal."

    m "Je l’ai vu aussi. Il ne bougeait presque pas, mais il était là. Le rapport de police dit qu’il a été tué vers 16h00."

    n "S’il a été tué à 16h00 dans cette ruelle près du lycée, cela veut dire qu’il a dû quitter la villa vers 14h30 ou 15h00."

    n "Mitsuko, ta mère a dit qu’elle ne l’avait pas vu partir. Personne dans le personnel ne l’a vu sortir ? Aucun garde ? Aucune caméra ?"

    m "C’est ça qui me rend fou ! Comment un homme dans son état, aussi surveillé par maman et les domestiques, a pu sortir de cette maison ?"

    narration "Mitsuko frappe du poing sur le rebord du lit avec une violence sourde. Il se lève et commence à faire les cent pas dans la petite pièce."

    m "Comment a-t-il pu traverser la moitié de Tokyo pour se retrouver exactement dans une ruelle sur le chemin de MON lycée ?"

    m "Et le timing ! Les cours reprennent aujourd’hui, le 5 février. C’est le jour où on sort enfin de notre bulle protectrice."

    m "C’est comme si le tueur attendait qu’on ne soit plus là pour l'entourer... ou pire… comme s’il voulait que ce soit moi qui le trouve en rentrant."

    h "Tu penses qu'on le suivait ? Papa ne sortait jamais… il avait peur de tout depuis des années. Il ne serait jamais parti sans une raison majeure."

    h "Pour qu'il sorte de lui-même, il a fallu que quelqu'un l'appelle, qu'on lui promette quelque chose... ou qu'on le force."

    n "Ou alors… quelqu’un de la maison l’a emmené là-bas."

    n "Mitsuko, réfléchis. Qui pouvait commander une voiture sans que Miki-san ne soit alertée immédiatement sur son téléphone ?"

    narration "Mitsuko s'arrête net, le souffle court. L'insinuation de Nobuyuki s'insinue dans son esprit comme un poison."

    m "Je refuse de croire que maman est impliquée, malgré notre dispute. Mais ce meurtre est trop chirurgical, trop bien placé."

    m "Ce qui me rend dingue, c’est cette coïncidence avec la reprise des cours. On était en  salle de classe, à quelques mètres de lui, pendant qu'il rendait son dernier souffle !"

    narration "Il repense au violent mal de tête de 8h00 pile ce matin. Cette synchronicité l'effraie plus que le crime lui-même."

    m "Quelqu’un a planifié ça comme une exécution publique. Ils savaient qu'à 16h, on finirait les cours. Ils savaient quelle ruelle on prendrait."

    m "Tout semble avoir été calculé pour nous briser au moment précis de notre retour à la vie normale."

    h "Onii-chan, tu vas bien ?"

    m "Pardon, Himari-chan, je vais bien. Je cherche juste une logique là où il n'y a que de la cruauté...Malheureusement le monde fonctionne ainsi, on y peut rien."

    m "Mais je vous le jure… ce n'est que le début. Le meurtrier n’a pas seulement tué Daiki, il a utilisé sa mort pour nous envoyer un avertissement ! Enfin... c'est ce que je pense..."

    n "Un avertissement ? Lequel ?"

    m "Que notre nom, notre argent et nos murs ne nous protègent plus. En gros pour résume, on a plus de vie privée. Personne n'est à l'abri dans cette maison. Pas même nous."

    $ chat_initial = [
    "{size=14}{color=#44bd32} Detective_Fan:{/color} Mitsuko qui commence à soupçonner sa mère même il le dit pas directement le petit malicieux ahah, c'est du lourd ! J'adore les retournements de situation ! Ah oui d'ailleurs, voici les résultats du sondage !{/size}",
    "{size=20}SONDAGE EN DIRECT ! LES SPECTATEURS REPONDENT ! - Qui a aidé Daiki à sortir de la Villa ?{/size}",
    "{size=18}1. Miki - 55%{/size}",
    "{size=18}2. Un domestique corrompu - 12%{/size}",
    "{size=18}3. Le tueur (par infiltration) - 34%{/size}",
    "{size=14}{color=#00a8ff}IdolWatcher:{/color} Moi je parie sur le majordome. C'est toujours le majordome dans les histoires de meurtre, non ?{/size}",
    "{size=14}{color=#fd9644} Theory_Crafter:{/color} Désolé IdolWatcher ta théorie c'est de la grosse merde mdrr{/size}",
    "{size=14}{color=#e84118} MysteryFan_97:{/color} Miki est trop évidente. Je pense que c'est un domestique qui a été soudoyé pour faire le sale boulot.{/size}",
    
    ]
    call call_meta_mode2(20000000, 22000000, "VILLA AMANO - CHAMBRE HIMARI - CAM 08", 100, chat_initial, "kskrif3")

    # Scène : Salon de la Villa - 5 février 2015, 23h15
label scene_salon_nuit_medias:

    scene bg_villa_salon_night with fade

    narration "23h15. Nobuyuki jette un regard anxieux à sa montre. Malgré son envie de rester pour soutenir Mitsuko, la réalité de sa propre vie la rattrape."

    show mitsuko sombre at left
    show nobuyuki inquiete at center
    with dissolve

    n "Senpai... je dois vraiment y aller. Mes parents vont s'inquiéter, et je ne veux pas rajouter de stress à cette journée."

    n "Appelle-moi demain, d'accord ? Promets-le-moi."

    m "Va, Nobuyuki. Merci d'être restée. Fais attention sur le chemin du retour."

    hide nobuyuki with easeoutright

    narration "Une fois Nobuyuki partie, un silence pesant retombe sur le salon. Himari est assise sur le bord du canapé, les yeux rivés sur son smartphone. Miki, de son côté, fixe l'écran de sa tablette, le visage blafard."

    show himari pleurs at right
    show Miki rigide at center
    with dissolve

    h "Onii-chan... regarde. On fait la une de Twipper. Partout."

    narration "Mitsuko sort son téléphone. Le mot-clé #MeurtreAmano est en tête des tendances mondiales. En quelques secondes, il est projeté dans une arène de cruauté pure."

    m "C’est pas possible... Regardez ces commentaires."

    narration "Il commence à lire à voix haute, sa voix résonnant avec une amertume glaciale dans le silence de la villa."

    narration "@NewsTokyo_Flash : « Le corps de Daiki Amano retrouvé dans une ruelle. La chute finale pour l'époux de la PDG de Daiki Productions ? L'enquête s'annonce juteuse. »"

    narration "@IdolFan_99 : « Est-ce que c’est mal de dire que Mitsuko est encore plus beau quand il a l'air dévasté ? Regardez la photo de l'ambulance, ce regard perdu... 10/10. »"

    narration "@TheoryHunter : « C'est forcément un coup monté. Le timing est trop parfait pour le retour des cours. C'est du génie marketing ou un règlement de comptes familial. Qui est le prochain ? Miki ? »"

    narration "@DarkTruth_01 : « Enfin débarrassés de l'alcoolique. Un meurtre propre pour une famille qui avait besoin d'un nouveau scénario. J'attends la suite avec impatience. »"

    h "« J’attends la suite » ?! Ils parlent de la mort de papa comme si c’était le dernier épisode d’un drama ! Ils disent que c’est 'esthétique' !"

    mi "C'est la machine médiatique, Himari. Elle ne s'arrête jamais. Les algorithmes se nourrissent de notre sang."

    mi "J'ai déjà lancé mes avocats, mais on ne peut pas faire taire dix millions de personnes qui veulent du spectacle."

    narration "Mitsuko fixe sa mère. Elle semble gérer la situation comme une crise de relations publiques, mais ses mains tremblent sur la tablette."

    m "« Qui est le prochain sur la liste ? »... C'est ce que tout le monde se demande sur le net. Ils ont déjà transformé notre vie en un feuilleton macabre."

    m "Ils parient sur notre mort, maman !"

    mi "C'est pour ça qu'on doit verrouiller la villa. Je vais doubler la sécurité. Personne n'entre, personne ne sort sans mon accord. On ne donnera plus rien à manger à ces vautours."

    m "Doubler la sécurité ? Pour nous protéger des journalistes ou pour nous garder sous contrôle ?"

    m "Regarde ce qui se passe : les gens sur internet savent déjà quel chemin on a pris pour aller à l'lycée. Ils ont des photos de nous que même nous n'avons pas."

    m "Ce n'est pas une intrusion physique, maman... on est déjà exposés. On est déjà dans leur arène..."

    m "Enfin... Je dis mais c'est un peu notre faute aussi, non ? On a toujours vécu sous les projecteurs en tant qu'idole. Peut-être qu'on mérite ce qui nous arrive."

    h "Onii-chan, comment tu peux dire ça ? Qui aurait pu faire ça ? Pourquoi tout le monde nous déteste assez pour rire de la mort de papa ?"

    m "Ils ne nous détestent pas, Himari. C'est pire que ça. Ils nous regardent. On est leur divertissement de 2015… C’est Internet, quoi."

    narration "Il se tourne vers le miroir du salon. Son reflet lui semble étranger, comme s'il voyait à travers ses propres yeux le cadrage d'une caméra invisible."

    m "Je ne suis plus Mitsuko Amano. Je suis juste un personnage dans une série que des millions de gens regardent en buvant du pop-corn."

    m "Et maintenant, ils attendent la suite. Ils veulent voir jusqu'où cette histoire va nous mener... Jusqu'où on peut tomber."

    penseedemitsuko "Est-ce que je vais laisser ces inconnus décider de ma vie ? De notre vie ?"
    penseedemitsuko "Est-ce que je vais les laisser nous détruire pour leur divertissement ?"

    call cal(jour_heure="6 FÉVRIER - 08h00")

    scene bg_cimetiere_day with fade

    narration "Le ciel est bas, d'un gris de plomb qui semble écraser les stèles de granit. Une pluie fine et glacée tombe sur le petit cortège réuni pour les funérailles de Daiki Amano."
    narration "L'ambiance est lourde, saturée par le parfum entêtant des lys blancs qui entourent le cercueil."
    narration "Mitsuko se tient droit, vêtu d'un costume noir impeccable. Son visage est une façade de marbre, mais ses mâchoires contractées trahissent une tension extrême."
    narration "À ses côtés, Himari semble minuscule sous son voile de deuil. Elle tremble de tout son corps, ses mains agrippées à un mouchoir trempé."
    
    pr "Puisse l'âme de Daiki Amano trouver enfin la paix que le tumulte de ce monde lui a refusée. Que le souvenir de l'homme qu'il fut demeure dans le cœur de ses proches."

    h "Adieu, papa... Je t'aimerai toujours. (Dans un sanglot étouffé) Ce n'est pas juste... Onii-chan, pourquoi tout le monde fait comme si c'était normal ? Pourquoi ils parlent de lui comme s'il était déjà oublié ?"

    narration "Mitsuko ne répond pas immédiatement, mais il passe un bras protecteur autour des épaules de sa sœur. Il sent son désespoir traverser le tissu de son manteau."

    m "Parce que dans ce monde, Himari, la vie continue. Même après la mort. Nous devons être forts, pour nous deux. (Prenant sa soeur dans ses bras) Je te le promets, on va surmonter ça ensemble."

    mi "(S'approchant, la voix parfaitement calme) La cérémonie est terminée. Il est temps de passer à l'inhumation. Les journalistes et les caméras de télévision sont massés aux grilles, nous devons quitter les lieux sans créer de scène."
    narration "Mitsuko hoche la tête, serrant un peu plus fort Himari contre lui. Il jette un dernier regard au cercueil, une promesse silencieuse gravée dans son esprit."

    narration "Le cercueil a été descendu. La foule s'est dispersée pour rejoindre les voitures noires. Mitsuko a demandé à rester seul quelques minutes. Himari a été raccompagnée par Nobuyuki, qui l'attend à la lisière du cimetière."

    narration "À côté de la tombe, sur un petit trépied de bois, réside une seule photo. C'est une image de Daiki jeune, datant du début des années 90. Il est souriant, une lueur d'ambition dans les yeux. "
    narration "C'est le Daiki d'avant la mort d'Ami, d'avant que l'alcool et le silence de la villa ne le consument. Mitsuko s'approche de la photo. Son masque se fissure enfin. Une larme solitaire roule sur sa joue."

    m "(La voix brisée, s'adressant à la photo) Regarde-toi... Tu avais le monde à tes pieds. Qu'est-ce qu'ils t'ont fait, papa ? Comment as-tu pu finir ainsi ?"

    m "Je... Je suis désolé. Désolé de ne pas avoir pu te sauver. Désolé de ne pas avoir été là pour toi quand tu avais besoin de moi."

    narration "Il s'agenouille dans la terre humide, ses doigts se crispant sur le bord de la stèle."

    m "D'abord elle... maman Ami en 1998. Elle est partie et elle t'a laissé brisé, une ombre errant dans une maison qui n'était plus la tienne. Et maintenant, c'est ton tour. (Sa voix s'étrangle de colère)."
    m "Pourquoi ? Pourquoi toi ? Qu'est-ce que tu as fait pour mériter ça ?"
    m "Pourquoi dans une ruelle ? Comme un déchet dont on se débarrasse quand il n'est plus utile ?"

    narration "Il pose sa main sur le cadre de la photo pour le protéger de l'averse."

    m "J'aurais voulu que tu te libères. J'attendais que tu te lèves, que tu affrontes enfin maman... que tu redeviennes l'homme de cette photo. Mais tu t'es juste laissé emporter par leur courant."

    narration "Il baisse la tête, ses larmes se mélangeant à l'eau de pluie sur le verre de la photo."

    m "Je ne les laisserai pas transformer ta mort en un simple fait divers qu'on oublie après le journal de vingt heures."
    m "Ils ont cru que tu n'étais rien, mais ils ont oublié que c'est ton sang qui coule en moi. Je vais découvrir qui a guidé ce couteau. Repose-toi, papa."

    narration "Il se relève, essuie son visage d'un geste sec et réajuste son manteau."
    narration "En se retournant pour quitter le cimetière, il aperçoit au loin, derrière un arbre, une silhouette qu'il ne reconnaît pas, mais qui semble le fixer avec une insistance malsaine."

    scene bg_villa_salon_day with fade

    narration "Le silence qui suit le départ de Miki ne dure que quelques secondes. Elle ne quitte pas vraiment la pièce. "

    narration "Ses pas s'arrêtent près de la porte, ses épaules s'affaissent, et soudain, toute la superbe de la Femme de fer s'écroule. Elle fait demi-tour et s'approche de Mitsuko qui est resté assis, la tête basse."

    narration "Sans un mot, elle s'assoit à côté de lui et attire sa tête contre sa poitrine, le serrant avec une force désespérée. Mitsuko, surpris, reste figé un instant avant de sentir ses propres larmes remonter."



    return