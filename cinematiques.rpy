image color_red = Solid("#ff0000")
image color_blue = Solid("#0000ff")
image color_green = Solid("#00ff00")
image color_black = Solid("#000000")

default avertissements_nom = 0

image easter_egg_kskrif = "images/kskrif.png"



label sequence_crash_nom_interdit:
    stop music
    # Flashs très rapides
    scene color_red 
    pause 0.05
    scene black
    pause 0.05
    scene color_red
    pause 0.1
    
    show text "{b}{color=#ffffff}VIOLATION DU PROTOCOLE ÉTHIQUE.\nIDENTITÉ NON CONFORME AUX VALEURS DE DAIKI PRODUCTIONS.{/color}{/b}":
        align (0.5, 0.5)
    
    with vpunch # Secousse verticale
    pause 3.0
    
    # Message système final avant fermeture
    $ renpy.quit()

label sequence_crash_refus:
    # On coupe la musique s'il y en a une
    stop music

    # Message d'erreur final
    show text "{b}{color=#ff0000}ERREUR CRITIQUE : ACCÈS RÉGIE REFUSÉ.\nFERMETURE DE LA SALLE VISUAL NOVEL...{/color}{/b}":
        align (0.5, 0.5)
    
    with hpunch # Secousse de l'écran pour l'impact
    pause 0.1

    # Fermeture brutale du jeu
    $ renpy.quit()

screen clause_legale():
    tag menu
    add "black" # Fond noir

    vbox:
        align (0.5, 0.4)
        spacing 30
        xsize 1000

        text _(""):
            color "#FFD700" # Doré
            size 40
            xalign 0.5
            bold True

        text _("Bienvenue au sein de Daiki Productions. Vous avez été sélectionné pour visionner le Film « L’Envers du Décor » depuis notre espace exclusif : la Salle Visual Novel. Contrairement à nos Salles Conventionnelles, l'expérience VIP offre une immersion totale et privilégiée dans le Tokyo de 2015. Afin de garantir l'excellence de cette diffusion et de protéger les droits de propriété intellectuelle liés à cette œuvre, l'accès à la salle est conditionné par la signature du présent contrat de visionnage. En poursuivant, vous reconnaissez votre statut de spectateur VIP et acceptez les conditions générales liées à l'exploitation de cette production. Vous gardez naturellement la liberté de décliner ce protocole d'entrée. Nous vous remercions de votre collaboration et vous souhaitons une séance inoubliable."):
            color "#FFD700"
            justify True
            size 22

    hbox:
        align (0.5, 0.8)
        spacing 100

        # Si on signe, on sort de l'écran et on continue
        textbutton _("Oui et signer la clause"):
            action Return() 
            text_hover_color "#ffffff"
            text_idle_color "#FFD700"

        # Si on refuse, le jeu se ferme
        textbutton _("Refuser"):
            action Jump("sequence_crash_refus") # On appelle le label de crash
            text_hover_color "#ff0000"
            text_idle_color "#FFD700"

label splashscreen:
    # --- PHASE 1 : PRÉVENTION ET SÉCURITÉ ---
    $ avertissements_nom = 0
    scene black
    pause 1.0

    # Titre d'avertissement
    show text "{size=50}{color=#ff4444}{b}AVERTISSEMENT : CONTENU MATURE (18+){/b}{/color}{/size}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve

    # Texte de prévention (Affiché seul pour une lecture claire)
    show text "{size=28}L’Envers du Décor est un thriller psychologique traitant de sujets graves et matures.\nBien que l'œuvre ne comporte aucune scène sexuelle explicite,\nle récit aborde des thématiques lourdes telles que :\n\n- Les violences sexuelles et le viol (mentions et conséquences psychologiques)\n- Le harcèlement et l'aliénation\n- Le suicide et les troubles de la santé mentale\n\nCe jeu est destiné à un public capable d'aborder ces sujets avec recul.\nLa discrétion du spectateur est conseillée.{/size}" at truecenter with dissolve
    
    # On attend un clic pour être sûr que l'utilisateur a lu
    pause
    hide text with dissolve

    # Menu de consentement (Apparaît sur écran noir propre)
    menu:
        "Souhaitez-vous commencer l'expérience ?"
        
        "Je suis majeur et j'accepte le contenu.":
            pause 0.5
        "Quitter le jeu.":
            $ renpy.quit()

    # --- PHASE 2 : IMMERSION (TON SLOGAN) ---
    scene black
    with Pause(1.0)

    # Animation de ton slogan "Votre pire cauchemar..."
    show text "{size=40}{color=#ffffff}Votre pire cauchemar est leur meilleur programme.{/color}{/size}":
        align (0.5, 0.5)
        alpha 0.0
        linear 1.5 alpha 1.0
    with Pause(2.5)

    show text "{size=40}{color=#ffffff}Votre pire cauchemar est leur meilleur programme.{/color}{/size}":
        align (0.5, 0.5)
        linear 1.0 alpha 0.0
    with Pause(1.0)
    
    # 2. Le Flash et la mire ERROR
    scene white with Dissolve(0.1)
    scene mire_error with Pause(1.2) # Ton image de barres colorées


    call screen clause_legale 

    # 4. Fin de la séquence
    scene black with Dissolve(1.0)
    with Pause(3.5)

    # --- PHASE 4 : SAISIE DU NOM ET EASTER EGG ---
    scene black with dissolve
    label .saisie_nom:
        # Fenêtre de saisie pour le Spectateur VIP
        $ player_name = renpy.input("Veuillez saisir votre nom de Spectateur VIP pour finaliser l'accès :", length=20).strip()

        # Si le nom est vide
        if player_name == "":
            $ player_name = "Spectateur Anonyme"

        # --- CAS CRITIQUE : ADOLF HITLER (CRASH) ---
        if "adolf" in player_name.lower() or "hitler" in player_name.lower():
            jump sequence_crash_nom_interdit

        # --- CAS INSULTES : RÉACTION DE LA RÉGIE ---
        elif any(word in player_name.lower() for word in ["merde", "connard", "salope", "zizi", "fesse", "caca", "prout", "nique ta race", "nique ta mère"]):
            $ avertissements_nom += 1
            
            # Vérification de la récidive (Crash si 2ème tentative)
            if avertissements_nom >= 2:
                show text "{b}{color=#ff0000}RÉCIDIVE DÉTECTÉE.\nEXPULSION IMMÉDIATE DU SPECTATEUR DE LA SALLE VIP.{/color}{/b}":
                    align (0.5, 0.5)
                with hpunch
                pause 2.5
                $ renpy.quit()

            # Première infraction : Message de la Régie
            show text "{size=30}{color=#ff0000}ALERTE : Langage inapproprié détecté.\nLe Plateau de Télévision exige le respect de ses invités.{/color}{/size}":
                align (0.5, 0.5)
            with hpunch
            pause 3.0
            hide text with dissolve

            # Choix aléatoire entre l'humiliation ou la seconde chance
            $ random_choice = renpy.random.randint(1, 2)

            if random_choice == 1:
                # Option A : Identité imposée
                $ noms_ridicules = ["Spectateur Malpoli", "Petit Rigolo", "Candidat Docile", "Erreur de Casting", "Petit con", "Spectateur Rebelle"]
                $ player_name = renpy.random.choice(noms_ridicules)
                show text "{size=30}{color=#FFD700}Identité réattribuée par la Régie : [player_name].{/color}{/size}":
                    align (0.5, 0.5)
                pause 3.0
                hide text with dissolve
            else:
                # Option B : On redemande
                show text "{size=30}{color=#ffffff}Une seconde chance vous est accordée.\nVeuillez décliner une identité conforme aux valeurs du Plateau de Télévision.{/color}{/size}":
                    align (0.5, 0.5)
                pause 3.0
                hide text with dissolve
                jump .saisie_nom
        elif player_name.lower() == "kskrif":
            scene black
            show easter_egg_kskrif:
                align (0.5, 0.5)
                alpha 0.0
                linear 0.5 alpha 1.0
            
            with Pause(10.0)
            
            hide easter_egg_kskrif with dissolve
            pause 1.0

        # --- CAS NORMAL ---
        else:
            show text "{size=30}{color=#ffffff}Bienvenue [player_name] !\nPréparation de la Salle Visual Novel en cours...{/color}{/size}":
                align (0.5, 0.5)
                alpha 0.0
                linear 1.0 alpha 1.0
            pause 2.0
            hide text with dissolve


    # --- PHASE 5 : TRANSITION VERS LE MENU ---
    scene black with dissolve
    pause 3.0

    return 