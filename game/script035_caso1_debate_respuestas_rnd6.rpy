label d1r6_incorrecto_beck:
    jump d1r3_incorrecto_beck

label d1r6_incorrecto_marissa:
    jump d1r0_incorrecto_marissa

label d1r6_incorrecto_alice:
    $change_cursor()
    $clearDebateText()
    $quick_menu_bajo=False
    show alice alegre
    ali "[pla_name], I'm glad to see you're deep into the debate..."
    show alice enojada
    $restCorazones()
    ali "But that argument doesn't help me in anything." with hpunch
    jump inicio_d1r6

label d1r6_incorrecto_neil:
    $change_cursor()
    $clearDebateText()
    $quick_menu_bajo=False
    show neil serio hablando
    nei "[pla_name], what do you want to prove with that argument?"
    show neil serio
    $restCorazones()
    nei "Think before you speak." with hpunch
    jump inicio_d1r6

label d1r6_correcto:
    stop music fadeout 1
    $clearDebateText()
    $change_cursor()
    $addCorazones()
    $showplay_excl("that'sright")
    $quick_menu_bajo=False
    # $quick_menu_gameplay = False
    hide screen debateArgumento
    $hide_gameplay_layout()
    play music tiempo_muerto fadein 2
    pla "¡Alice, eso es!"
    show alice sorprendida
    ali "Uhhh!? What?"
    pla "All this time... we've been wrong!"
    show alice normal
    ali "[pla_name]... what's the matter? I don't understand..."
    show alice sorprendida
    pla "The letter could not have been written to Marissa, {amarillo}but to someone else.{/amarillo}"
    show alice:
        ease .5 mleft
    show marissa sorprendida at mright with dissolve
    mar "What?!" with hpunch
    sea "Wasn't the letter for me?"
    # mar "Pero si ahí está mi nombre..."
    # pla "No, estás en un error..."
    pla "The way the author describes his great love {amarillo} does not match the way you are.{/amarillo}"
    show marissa normal
    show alice normal
    mar "..."
    mar " Now that you mention it... That would make sense..."
    show alice sorprendida at brinquitos
    ali "¡Oh!"
    "It seems that Alice has already finished understanding."
    "Thanks to what Alice said... I understood that the real addressee is..."
    # show screen corazones

    # ##ahora se debe seleccionar un item del bloc de notas, usaremos como id, el titulo del elemento
    # $idevidencia_correcta="Prof. Harrow (profile)"

    # label mostrar_evidencia2:

    #     show marissa normal

    #     if cantidad_corazones==0:
    #         jump evidencia_mostrada2_gameover

    #     call screen notepad("evidenc",jumpto="evidencia_mostrada2") with dissolve

    # label evidencia_mostrada2:
    #     if idevidencia_mostrar==idevidencia_correcta:
    #         jump evidencia_mostrada2_correcto
    #     else:
    #         mar " I don't understand... what does that prove?"
    #         $restCorazones()
    #         pla "Ah, sorry... I made a mistake." with hpunch
    #         jump mostrar_evidencia2

    # label evidencia_mostrada2_gameover:
    #     hide screen corazones
    #     stop music fadeout 1
    #     show marissa preocupada
    #     mar "What are you trying to do, [pla_name]?"
    # pla "The truth is, I don't even know..."
    #     stop music
    #     scene bg negro with dissolve
    #     "Game over"
    #     return

    # label evidencia_mostrada2_correcto:
    #     stop music fadeout 2
    #     hide screen corazones
    #     $showplay_excl("that'sit ")
    #     $addCorazones()
    #     $updateStat("intel","+",1)
    #     $renpy.notify("Inteligencia +1")

    # #presentar evidencia: mary
    # # pla "Mary Harrow...it is Professor Harrow to whom the letter was addressed."
    stop music fadeout 2
    play sound campana
    pla "The math teacher." with flashbulb
    mar "Professor Harrow?"
    show marissa sorprendida
    play sound campana
    mar "¡Oh!" with flashbulb
    mar " The teacher's name is {amarillo}Mary{/amarillo} Harrow.... So the stained name, {amarillo}wasn't mine.[/amarillo}"
    show alice:
        ease .5 left
    show marissa:
        ease .5 right
    show neil sonriendo hablando with dissolve
    nei "Hee... Very well done, [pla_name]... now it would be clear how it was that the letter got to the wrong person..."
    $renpy.choice_for_skipping()
    $renpy.save("checkpoint")
    pla "Yes... the letter got to Marissa..."

    label lacartallegoel:
        if cantidad_corazones==0:
            hide screen corazones
            jump d1_gameover
        show screen corazones
        menu:
            "\"... during classes.\"":
                $restCorazones()
                "Nope... it wasn't that..." with hpunch
                jump lacartallegoel
            "\"... during the stumbling.\"":
                # $addCorazones()
                # pause 1
                hide screen corazones
                pass
            "\"... before the stumbling.\"":
                $restCorazones()
                "Nope... it wasn't that..." with hpunch
                jump lacartallegoel
            "\"... on saturday.\"":
                $restCorazones()
                "Nope... it wasn't that..." with hpunch
                jump lacartallegoel

    pla "When Marissa and Professor Harrow stumbled, they also mistook one particular piece of paper, the letter."
    hide alice with dissolve
    show beck enojado at left with dissolve
    bec "That's very suspicious... Neil, you had something to do with that!" with hpunch
    show neil normal
    nei "Heh, heh, heh... No, it wasn't that at all..."
    nei "I just remembered the moment when I went to help them pick up the papers..."
nei "It occurred to me that there was a high probability that some paper would get to the wrong owner." nei "It occurred to me that there was a high probability that some paper would get to the wrong owner.
    nei "Knowing now who the letter was addressed to, it will be easier to find a new suspect, won't it, [pla_name]?"

    menu:
        "\"On the contrary.\"":
            nei "¿Huh?"
            nei " Well, if you say so..."
            jump d1_gameover
        "\"That's right.\"":
            $updateStat("carisma","+",1)
            $renpy.notify("Carisma +1")
        "\"Possibly.\"":
            $updateStat("carisma","-",1)
            $renpy.notify("Carisma -1")
            nei "What's with that little confidence?"
        "\"That doesn't help.\"":
            nei "Really?"
            nei "I guess your brain can't handle any more..."
            jump d1_gameover

    show beck:
        ease .5 center
    show neil:
        ease .5 mleft
    show alice normal at left with dissolve

    ali " That would explain why the case seemed so confusing... but then..."
    ali "Who would be our new suspect?"

    # scene bg salon club detectives
    hide alice
    hide beck
    hide marissa
    hide neil

    ## cada elemento es el sprite de un personaje
    $ chars=["images/chars/alice/normal.png","images/chars/neil/normal.png","images/chars/beck/serio.png","gui/empty.png","images/chars/marissa/normal.png"]
    ## cada elemento define a qué etiqueta saltar cuando se selecciona el personaje de la lista anterior
    $ chars_labels=["nuevosospechoso_incorrecto","nuevosospechoso_incorrecto","elec_beck2",False,"nuevosospechoso_incorrecto"]

    label quien_es_nuevosospechoso:
        if cantidad_corazones==0:
            jump d1_gameover
        show screen btnHelpTextBox("If the addressee is the teacher, then the person who wrote the letter is...").
        $ quick_menu_bajo=True
        ## llamamos pantalla de seleccion
        call screen char_select(chars,chars_labels) with dissolve

    label nuevosospechoso_incorrecto:
        hide screen char_select
        pause 1.8
        $ hide_select_chars()
        hide screen btnHelpTextBox
        $ quick_menu_bajo=False
        show screen corazones
        $restCorazones()
        "It's not time for games, it's already clear to me who might have written the letter...." with hpunch
        hide screen corazones
        jump quien_es_nuevosospechoso

    label elec_beck2:
        # show screen corazones
        # $addCorazones()
        pause .4
        hide screen char_select
        pause 1.4
        $ hide_select_chars()
        hide screen btnHelpTextBox
        $ quick_menu_bajo=False
        hide screen corazones
        play music tiempo_muerto fadein 3
        show marissa normal with dissolve
        pla "I believe Beck is the author of the letter..."
        show marissa sorprendida
        mar "Be-Beck!" with hpunch.
        pla "He's in love with Professor Harrow."
        mar "Whaaat!? Beck is in love with her?"
        mar "I-I can't believe it..."
        show marissa normal:
            ease .5 mright
        show beck enojado at mleft with dissolve
        bec "Yeah, I can't believe it either." with hpunch
        bec "That I'm in love with a teacher?"
        bec "That's not possible!"
"Huh? But what's wrong with Beck... now he's going to deny it..."
        show beck:
            ease .5 left
        show marissa:
            ease .5 right
        show alice normal with dissolve
        ali "But you talked to [pla_name] and he deduced that..."
        show beck serio
        bec " That he deduced it? Surely it was just a guess."
        bec "The teacher is someone respectable. And she's a great woman..."
        show beck pensando
        bec "But I'm not interested in her."
        show marissa preocupada sudor
        mar "[pla_name], are you sure Beck likes Professor Harrow?"
        # "Yo sí estoy seguro... pero no contaba con que Beck lo negara rotundamente."
        $renpy.choice_for_skipping()
        $renpy.save("checkpoint")
        "There must be{nw}"
        play sound campana
        extend " {amarillo} something that proves Beck's interest in Professor Harrow....{/amarillo}" with flashbulb
        show marissa normal

        # $quick_menu_gameplay=True

        # ##ahora se debe seleccionar un item del bloc de notas, usaremos como id, el titulo del elemento
        $idevidencia_correcta="Ayuda en matemáticas"

        label mostrar_evidencia2:
            show screen corazones

            if cantidad_corazones==0:
                jump evidencia_mostrada2_gameover

            call screen notepad("evidenc",jumpto="evidencia_mostrada2") with dissolve

        label evidencia_mostrada2:
            if idevidencia_mostrar==idevidencia_correcta:
                jump evidencia_mostrada2_correcto
            else:
                mar "I don't understand... what does that prove?"
                $restCorazones()
                pla "Oh, sorry... I made a mistake." with hpunch
                jump mostrar_evidencia2

        label evidencia_mostrada2_gameover:
            hide screen corazones
            stop music fadeout 1
            show marissa preocupada
            mar "What are you trying to do, [pla_name]?"
            pla "To tell you the truth, I don't even know..."
            jump d1_gameover

        label evidencia_mostrada2_correcto:
            $showplay_excl("that'sit ")
            $addCorazones()
            pause 1
            hide screen corazones
            pass

        # $quick_menu_gameplay=False

        pla "No Beck... there is a proof that you are interested in the teacher."
        bec "Oh yeah? I doubt that very much..."
        # bec "A ver, muestráme esa prueba."
        # pla "No es una prueba física... más bien..."
        stop music fadeout 1
        play sound campana
        pla "So explain to us, {amarillo}why you spend a lot of time in the teacher's lounge. {/amarillo}?" with flashbulb
        show beck sorprendido
        bec "¿Huh?"
        pla "Come on, I mean you get tutoring with Professor Harrow. And not just once..."
        show beck pensando
        bec "What's wrong with that? I'm just worried about my grades..."
        pla "It could also be an excuse to spend more time with her..."
         pla "Besides, that would be a perfect opportunity to leave a letter for the teacher among her papers without her noticing."
        show marissa sorprendida
        mar "Beck..."
        show beck sorprendido
        bec "No... you are in a mistake ..."
        "It looks like Beck still doesn't want to give up..."
        show marissa normal
        show beck serio
        bec "Marissa, it's not what you think..."
        show beck pensando
        bec "I by no means wrote that letter..."
        mar "But Beck..."
        mar "Come to think of it... You're left-handed. Just like the person who wrote the letter."
        bec "So what? That doesn't prove anything..."
        mar "Besides, I saw the stalker on Saturday and..."
        show beck serio
        bec "I wasn't even at school that day!" with hpunch.
       "Beck wasn't at school on Saturday?"
        "There's something to prove otherwise..."
        show alice enojada
        $showplay_excl("that'snottrue ")
        play music debate fadein 4
        "¿Huh?"
        show marissa sorprendida
        ali " T-that's... not true..."
        ali "On weekends there are always soccer games."
        show beck pensando
        show marissa normal
        bec "Oh... well, that..."
        show beck preocupado
        bec " It was just a coincidence."
        pla "There's no reason to keep denying it, Beck..."
        show beck enojado
        bec "I deny it because it's not true."
pla "What about {amarillo}your encounter with Marissa in the cafeteria on Friday {/amarillo}?"
        bec "What about that?"
        show beck pensando
        bec "It was just a coincidence."
        show marissa preocupada sudor
        mar "But that cafe is not a place you frequently go."
        $renpy.choice_for_skipping()
        $renpy.save("checkpoint")
        bec "I told you..."
        play sound campana
        bec "{amarillo} I got a call on my cell phone from some friends,{/amarillo} to go to the cafe to chat for a while.." with flashbulb
        bec "{amarillo} We were talking about Saturday's match.{/amarillo}"
       "No, that's not true..."
        pla "Are you sure about that?"
        show marissa preocupada
        show alice normal
        show beck serio
        bec "Yes."
        pla " How weird, because..."
        "There's something that proves his contradiction!"
        # $quick_menu_gameplay=True

        # ##ahora se debe seleccionar un item del bloc de notas, usaremos como id, el titulo del elemento
        $idevidencia_correcta="Problemas en red de telefonía"

        label mostrar_evidencia3:
            show screen corazones

            if cantidad_corazones==0:
                jump evidencia_mostrada2_gameover

            call screen notepad("evidenc",jumpto="evidencia_mostrada3") with dissolve


        label evidencia_mostrada3:
            if idevidencia_mostrar==idevidencia_correcta:
                jump evidencia_mostrada3_correcto
            else:
                mar "I don't understand... what do you mean by that?"
                $restCorazones()
                pla "Ah, sorry... I made a mistake." with hpunch
                jump mostrar_evidencia3

        label evidencia_mostrada3_correcto:
            stop music fadeout 1
            $showplay_excl("esoes")
            $addCorazones()
            pause 1
            hide screen corazones
            pass

        # $quick_menu_gameplay=False
        play music tiempo_muerto fadein 1
        
        pla "That's very strange... On Friday, which was when Marissa arrived at the cafe, {amarillo}the phone network was down. {/amarillo}"
        play sound campana
        pla "That Friday, you couldn't call or send messages from your cell phone."
        show marissa sorprendida
        mar "Ah, right..."
        show beck enojado
        bec " No... no... That's not enough to accuse me..." with hpunch
        "Aaaah how stubborn he is!" with vpunch
        show marissa normal
        "Now what lie is he going to tell?"
        stop music fadeout 1
        play sound campana
        bec "{amarillo}  If I were the stalker, Marissa would have identified me from the beginning..{/amarillo}" with flashbulb
        pla "What?"
        show alice sorprendida
        show marissa sorprendida

        mar "I-it's... it's true..."
        mar "I couldn't identify the stalker..."
        mar "I would have quickly recognized Beck..."
        show beck serio
        bec "Do you see it now?"
        bec "It's all been a series of coincidences."
        show beck guino
        bec "I'm not the stalker. And I didn't write that love letter either."

        menu:
            "He is right":
                jump caso1_gameover
            "There is something more...":
                show alice enojada
                ali "[pla_name]! We can't let this opportunity pass us by." with hpunch
                ali "The case is about to be solved."
                show alice pensando
                pla "But... how would we explain the fact that Marissa couldn't identify the stalker?"
                $renpy.choice_for_skipping()
                $renpy.save("checkpoint")
                show alice enojada
                ali "There must be something the stalker used to avoid being identified!" with hpunch
                show alice pensando
                ali "But I can't figure out what it could be..."
                "Uhm..."
                "Something the stalker used..."
                "It could be..."
                $hora=16
                $ruleta2_mas_facil=False

    label ruleta2_inicio:

        #-----Inicia minijuego

        $estadoj="Ruleta Incóg."
        $ruleta_porcentaje=100
        $ruleta_id=2

        #palabra a descubir
        $palabra_ruleta=" HOOD "

        #posicion de la letra a averiguar en palabra
        $posicionenpalabra=0

        python:
            #lo que se mostrara en el panel derecho
            lstLetrasActuales=[]
            #agregamos varios guiones bajos
            for x in xrange(0,len(palabra_ruleta)):
                lstLetrasActuales.append("_")

        if not ruleta2_mas_facil:
            $letras1=["G","P","S","O","H","E","R","A","J","U","E","R","O"]
            $letras2=["I","T","Z","K","D","Ñ","U","M","W","C","P","H","B"]
        else:
            $letras1=["C","S","O","X","U","H"]
            $letras2=["A","O","D","C","A","H"]

        $showMinigameTitle("Roulette of the incognita")
        # $quick_menu_gameplay=True
        $quick_menu_bajo=True
        window hide
        play music deduccion fadein 3
        $change_cursor("target")
        scene bg salon club detectives
        $renpy.show_screen("temporizador",185)#185
        
        call screen ruleta_incognita(letras1,letras2"In order to not be identified, the stalker used the...",palabra_ruleta) with dissolve

        label ruleta2_gameover:
            $quick_menu_bajo=False
            stop music fadeout 3
            $change_cursor()
            if not ruleta2_mas_facil:
                pla "No... I don't know..."
                show alice enojada
                ali "¡[pla_name]!" with hpunch
                ali "You can't give up! We're close to solving the case."
                show alice sorprendida
                pla "Haven't you heard? Why couldn't Marissa identify the stalker?"
                pla "I can't find an explanation for that..."
                show alice enojada
                ali "[pla_name], you are not alone..."
                show alice pensando
                ali "I don't want to be any burden."
                pla "Alice..."
                ali "You just have to think things through."
                show alice enojada
                ali "A good deduction {amarillo}starts from the right questions.{/amarillo}"
                pla "So what should I ask myself then?"
                show alice normal
                ali "Well... the problem is that Marissa didn't identify Beck, right?"
                play sound campana
                ali "So, you have to ask yourself, {amarillo}what would you use to prevent an acquaintance from identifying you {/amarillo}?" with flashbulb
                pla "Uhm... A disguise?"
                show alice:
                    ease .5 mright
                show beck enojado at mleft with dissolve
                bec "You're not going to think I wore a disguise, are you?"
                bec "That's ridiculous."
                show beck sorprendido
                play sound campana
                ali "Maybe {amarillo}something that does the same thing as a disguise.{/amarillo}" with flashbulb.
                "Uhm... a disguise... something like... disguise... clothing... something to cover up..."
                show alice sorprendida
                show sherinford pequeño with dissolve:
                    ypos .300
                    xoffset 10
                    xpos 0.650
                she "Tweet, tweet, tweet!" with hpunch
                ali "Sherinford?"
                hide sherinford with dissolve
                she "Tweet, tweet, tweet!" with hpunch
                bec "Where did that chicken come from?"
                "Sherinford suddenly appeared, flapped his wings vigorously and then began to climb up my body, until he landed on my head."
         ali "Sherinford... Do you want to help too?"
                she ""Tweet!"" with hpunch
                show alice alegre
                ali "Very good! Sherinford will be backing you up too, [pla_name]!"
                ali "Surely he'll pass on some of his intelligence to you."
                "That I'll have more intelligence by having this chicken on top of my head?"
                "I don't think that's going to work..."
                "Well, I'll try one more time..."
                $ruleta2_mas_facil=True
                $quick_menu_bajo=True
                jump ruleta2_inicio
            else:
                jump ruleta1_gameover

    label ruleta2_fin:
        $showplay_excl("that'sit")
        stop music fadeout 3
        $estadoj="Debate"
        $quick_menu_gameplay=False
        $quick_menu_bajo=False
        window show
        show alice sorprendida with dissolve
        play sound campana
        pla "The stalker wore a hood!" with flashbulb
    pla "Beck wore {amarillo}the hood of the sweater{/amarillo} he is wearing to hide his identity."
    if ruleta2_mas_facil:
        pla "Thanks Sherinford, I guess some of your intelligence must have rubbed off on me."
        show sherinford grande behind alice at left with dissolve:
            xoffset -300
            on show:
                linear 1 xoffset 20
        she "Tweet"
        hide sherinford with dissolve
    show alice normal:
        ease 1 right
    show marissa sorprendida at center with dissolve
    show beck pensando at left
    mar "Uh..."
    "Marissa walked over to Beck in a daze, and with the confidence that a friendship brings, she pulled his hood over his head..."
    mar "That's him! That's the shadow I looked at! His silhouette is identical!" with hpunch
    "Beck pulled back his hood, but didn't say a word."
    mar "Why... why did all this happen..."
    pla "I think I can explain it all."
    show alice enojada
    ali "That's the spirit, [pla_name]!".

    $fase_titulo.append("Debate + Acertijo + Ruleta de la incógnita")
    $fase_tipo_vida.append("cantidad")
    $fase_corazones.append(cantidad_corazones)
    $fase_multiplicador.append(20)

    $quick_menu_gameplay=False
    show marissa preocupada
    show alice normal

    play music tiempo_muerto fadein 3

    pla " On Friday, Beck was in the teacher's lounge with Professor Harrow."
    pla "Since he's in love with her, he wrote her a letter, kind of cheesy...."
    pla "But he was aware that he wasn't someone who could impress her."
    pla "A student, proposing to a teacher.... Obviously that carried a lot of insecurity and pressure...."
    pla "That's why Beck probably left the letter among the teacher's papers when they were in the teacher's lounge."
    pla "Earlier that day, Professor Harrow bumped into Marissa."
    pla "In the midst of the confusion, the letter that was the teacher's, ended up with Marissa without her realizing it..."
    # pla "But not until the end of class."
    pla "Beck witnessed part of the scene, but was not yet aware of what really happened."
    pla "Then when Beck and Marissa ran into each other at the coffee shop, that's when beck figured it out, the letter went to the wrong person."
    $quick_menu_gameplay=True
    pla "On Saturday, which is when Beck and Marissa were at school..."
    label beckfinal:
        pla "Beck wanted to break into Marissa's locker..."
        mar "Why would Beck do something like that?"
        pla "Well..."
        menu:
            "He wanted to leave you a letter":
                mar "Huh? Why did Beck want to leave me a letter?"
                $updateStat("intel","-",1)
                $renpy.notify("Inteligencia -1")
                play sound golpe
                pla "Uhm... sorry, I made a mistake..." with hpunch
                jump beckfinal
            "He wanted to recover the letter":
                pass
            "He wanted Marissa's cell phone.":
                mar "My cell phone? Why would Beck want my cell phone?"
                pla "It's clear that..."
                $updateStat("intel","-",1)
                $renpy.notify("Inteligencia -1")
                play sound golpe
                extend " I made a mistake." with hpunch
                jump beckfinal
            "I don't know":
                $updateStat("intel","-",1)
                $renpy.notify("Inteligencia -1")
                play sound golpe
                ali "¡[pla_name]!" with hpunch
                pla "Sorry... now it's clear to me..."
                jump beckfinal
    $quick_menu_gameplay=False
    pla "I think Beck thought you had put the letter in your locker."
    pla "Beck wanted the letter back, without you noticing, he was probably too embarrassed to confess the truth."
    pla "That would also explain why you felt stalked."
    pla "And when you saw him, you couldn't identify him because he was wearing his sweater with the hoodie on."
    pla "In the end, you came to our club thinking that letter was for you, but it was simply Professor Harrow's name stained with ink."
    show beck preocupado
    stop music fadeout 2
    play sound campana
    bec "You're right... it's just as you said... I can't deny it anymore." with flashbulb
    bec "Sorry Marissa, for giving you a hard time..."
    mar "Beck..."
mar "If only you had told me..."
    show beck pensando
    bec "I'm really sorry, ...I was so nervous and embarrassed.... I wasn't thinking clearly."
    "Marissa took a deep breath, letting go of a weight she was carrying..."
    "Then, she pulled the letter out of her purse and handed it to Beck."
    show marissa alegre
    mar "Here, you'll have to work on your lack of confidence if you want to try again..."
    show beck sonrojado
    bec "...yes..."
    $estadoj="Free"
    play music ambiente fadein 4
    #marisa se dirige a neil
    mar "Uhm... Neil?"
    hide beck with dissolve
    show neil sorprendido at left with dissolve
    nei "Y-yes!?" with hpunch
    mar "Do you really like me?"
    show neil sonriendo hablando
    nei "Yes! I fell in love with you at first sight!" with hpunch.
    "Wow...how direct."
    show marissa sonrojada
    mar "I understand."
    mar "But, I'm sorry, I'm not interested in having a boyfriend."
    show neil sorprendido
    nei "What!?" with hpunch
    # nei "Ya veo..."
    show marissa alegre hablando at brinquitos
    play sound campana
    mar "But we could be friends, and we can also get to know each other better..." with flashbulb
    nei "Re- really?"
    "That means hope."
    show neil sonriendo hablando
    nei "He, he, he..."
    "And there he goes, Neil started smiling like an idiot again."
    hide neil with dissolve
    show marissa:
        ease .5 mleft
    show alice:
        ease .5 mright
    mar "[pla_name], Alice..."
    show marissa at brinquitos
    mar "Thanks for helping me!"
    show marissa sonrojada
    mar "Though in the end it was just my mistake..."
    show alice sorprendida
    ali "Do- don't worry!" with hpunch
    ali "It's what the club does, this club is about helping people!"
    show marissa alegre
    mar "Heh, heh, heh. It's a great club."
    show marissa alegre hablando
    mar "You'll see, I'll tell my friends that you guys are great."
    mar "If anyone has a problem, I'll tell them to come to this club!"
    ali "Really?"
    show alice alegre at brinquitos
    ali "That'd be great!"
    hide marissa with dissolve
    show alice normal
    show beck preocupado at mleft with dissolve
    bec "Hey, [pla_name], I want to apologize for acting like a jerk."
    show beck pensando
    bec "I feel bad for asking, but..."
    show beck preocupado
    bec "Could you keep this a secret?"
    pla "Sure, we won't tell anyone about this..."
    ali "I-I won't say anything either."
    show beck sonrojado
    bec "Seriously, thank you..."
    hide alice with dissolve
    show neil pensativo at mright with dissolve
    show beck pensando
    bec "I owe you an apology too..."
    bec "Sorry for wanting to blame you for everything."
    nei "It's okay."
    bec "I hope you won't tell anyone what happened..."
    nei "Well, I'm not a member of this club, so I don't have any obligation to keep your secret..."
    show beck:
        ease .5 left
    show neil:
        ease .5 right
    show marissa normal with dissolve
    mar "Neil..."
    show neil sorprendido
    nei "Aaahh! It was a joke!" with hpunch
    nei "I won't tell anyone, trust me."
    show marissa alegre
    mar "Good to know."
    hide neil with dissolve
    hide beck with dissolve
    show marissa alegre hablando
    mar "Well, it's time to go."
    mar "And don't think it's goodbye."
    mar "Can we still be friends?"
    show marissa:
        ease .5 mleft
    show alice pensando at mright with dissolve
    ali "Huh? A friend..."
    show alice sonrojada
    "Alice smiled lightly, as her face blushed."
    pla "Sure, we'll be friends after all."
    show marissa alegre at brinquitos
    mar "Great, see you, Alice, [pla_name]!"
    hide marissa with dissolve
    show beck pensando at mleft with dissolve
    show alice normal
    bec "I'm leaving too."
    show beck guino 
    bec "Ah, I'll talk to my friends at the club, too. As long as you guys keep your word."
    pla "Sure, our lips will be sealed."
    bec "I hope so, goodbye."
    hide beck with dissolve
    show neil pensativo at mleft with dissolve
    nei "Ah... well done."
    show neil sonriendo hablando
    nei "You have shown that you really belong to a detective club."
    nei "Well, I'm off too."
    hide neil with dissolve
    show alice normal:
        ease .5 center
    "And without another word, Neil left."
    "Alice and I were left in silence."
    "I for my part lay down on a bench, tired from all the work done."
    pla "Ah... my head hurts."
    ali "You've been thinking a lot... it's normal..."
    pla "Well, I hope I won't think any more for the rest of the week."
    $quick_menu_btn_notepad=False
   "Then I left my notebook on the table."
    pla "Well, that's it for today, I'm going home."
    show alice alegre
    ali "Yes, good job, [pla_name]."
    hide alice with dissolve
    "I went in search of my backpack, and as I was already heading to the door..."
    stop music fadeout 3
    show katherine normal with dissolve
    "..."
    extend " ¿huh?"
    "No... I can't believe it... another case..."
    unk "Are you a member of this club?"
    pla "Uh, yes... I'm [pla_name]."
    unk "I see."
    show katherine:
        ease .5 mleft
    show alice sorprendida at mright with dissolve
    ali "¿Huh?" with hpunch
    show alice pensando at temblor
    extend " ... uh..."
    pla "Alice, what's wrong?"
    "Suddenly, she started shaking, clearly nervous."
    pla "Excuse me, who are you?"
    unk "Wow, how disappointing, you don't even know who I am..."
    unk "As expected from this useless club."
    pla "Huh?" with hpunch.
    "What did she say?"
    hide alice
    show alice pensando at mright
    ali "[pla_name],{nw}"
    play sound campana
    extend "she is the president of the student co-committee...." with flashbulb
    play music investigacion fadein 4
    pla "The-the pre-president of the student co-committee!?" with hpunch.
    unk "Is it customary to stutter in this club?"
    kat "I am, {amarillo}Katherine Hyde.{/amarillo}"
    show katherine enojada
    kat "Record that name in that thing you call brain."
    "But what the hell is wrong with her..."
    pla "And why did the president of the student committee come to this club?"
    "I said that looking serious, I couldn't be nice to her."
    kat "Isn't it obvious {nw}"
    play sound campana
    show alice sorprendida
    extend " {amarillo} I'm closing this club.{/amarillo}" with flashbulb
    pla "¿¡Huh!?" with hpunch
    pla "But there's still a long way to go before the time limit..."
    show katherine normal
    kat "Why put off until tomorrow what you can do today?"
    kat "The previous president was very soft on the clubs, but that's over."
    "Is this the beginning of a dictatorship?!" with hpunch
    # kat "Desde mi primer año en este cargo, pondré mano dura a aquellos que no se atienen al reglamento."
    show alice pensando:
        ease .5 right
    show katherine:
        ease .5 center
    show henry sonriendo at left with dissolve
    play sound campana
    "And now what?" with flashbulb.
    "Someone else showed up at the club."
    pla Hey, you're the one from last time..."
    unk "Hey, how's it going boy?"
    play sound campana
    kat "{amarillo}Principal  Okamoto{/amarillo}..." with flashbulb
    pla "Pri-principal!?"
    kat "What, you didn't know he's the principal?"
    pla "Uhm... no..."
    "I'm embarrassed to admit it. Wow, I missed so much on the first day of school..."
    "First, I meet the new student committee president."
    "And now I'm learning that this man is the new principal of the school..."
    show henry tranquilo
    hen "Henry Okamoto, nice to meet you, boy, I was already guessing you didn't know who I was."
    "Henry... ¿Okamoto?"
    show henry alegre
    hen "Oh, and if you're wondering, my father is Japanese, but I grew up and was born in this country."
    "Huh? It seems as though he's read my mind..."
    show henry tranquilo
    hen "And Miss Hyde... I was wondering where you were going in such a hurry..."
    hen "And it looks like I got it right."
    kat "I guess you must be aware that this is not a school-recognized club."
    hen "Yes, it doesn't have enough members."
    kat "Then there's nothing more to talk about, this room needs to be de-occupied for other clubs that do need it."
    pla "W-wait!" with hpunch
    show katherine enojada
    kat "Any objections?"
    pla "Uh... well..."
    "As I was babbling, I noticed that Alice was still not speaking..."
    show henry sonriendo
    hen "There, there, no need to be rude either."
    show henry tranquilo
    hen "They still have two months to get enough members."
    hen "I see no reason to rush things."
    kat "But director... they're just wasting time..."
    hen "How can you be so sure of that?"
    kat "Well... I..."
    show henry sonriendo
    play sound campana
    hen "You've been watching them?" with flashbulb
    pla "What?"
    show katherine enojada
    kat " I- I- I was just doing my job."
    hen "Did they ever break the rules?"
    kat "..."
    kat "No."
    show henry tranquilo
    hen "There you go, now who's been wasting their time?"
    "Uh, that must have hurt."
    kat "..."
    kat "Whatever."
    kat "As soon as I see any of you do anything inappropriate..."
    kat "I'm closing this club immediately!" with hpunch
    hide katherine with dissolve
    show henry:
        ease .5 mleft
    show alice:
        ease .5 mright
    pla "What the heck is wrong with that girl..."
    show henry serio
    play sound campana
    hen "I think she has something against the club." with flashbulb
    pla "¿Huh?"
    show henry alegre
    hen "Oh, don't mind me, I was just talking to myself heh, heh, heh."
    show henry tranquilo
    hen "Well, I have to go."
    hen "I hope you manage to keep this club afloat."
    hide henry with dissolve
    show alice:
        ease .5 center
    "And with a slight bow, the director withdrew from the salon...."
    "So much has happened in such a short time..."
    "Ah... I think this headache is getting worse..."
    pla "Alice?"
    ali "So- sorry... I froze..."
    show alice at decaer
    ali "As soon as I think that the club might close..."
    ali "I get very nervous..."
    show alice at reponerse
    pause .7
    show sherinford pequeño at center with dissolve:
        ypos .450
        xoffset 60
    she "Tweet..."
    pla "Bah, don't give that self-sufficient president a mind."
    pla "Let's do our best, and you'll see we'll have enough members for the club."
    show alice sonrojada
    ali "[pla_name]..."
    show alice sonriendo
    ali "Thank you for staying in the club."
    scene bg negro with slow_dissolve
    "Even though we managed to solve our first case together..."
    "Alice and I were still the only members of the detective club."
    "And we have two months to turn the situation around."
    "I've had a good time in this club, and now I'm committed to helping."
    "I'm not going to let this club close!"
    $noInteract()

    stop music fadeout 3
    hide screen quick_menu
    $quick_menu=False
    window hide
    $ renpy.pause(3,hard=True)

    # show text "{size=70}Fin del primer caso.{/size}" at truecenter
    # with dissolve
    # pause 3
    # hide text
    # with dissolve

    $renpy.choice_for_skipping()
    play sound caso_resuelto
    show text "{size=70}¡Primer caso resuelto!{/size}":
        center
        ypos .9
    show alice chibi:
        center
        ypos .7
        zoom .6
    # with dissolve
    $ renpy.pause(4,hard=True)
    hide text
    with dissolve
    hide alice with dissolve

    if _return:
        $persistent.hikikomoriholmes_unlocked=True
    $persistent.extras_unlocked = True

    call screen casoFinDetalles()
    if persistent.skipcredits:
        show screen btnSkipCredits()
    
    #inicio creditos
    $renpy.music.play(audio.creditos, channel='music', loop=False, fadeout=2.0, synchro_start=False, fadein=1.5, tight=None, if_changed=False)

    $ renpy.pause(3,hard=True)

    show text "{size=30} Concept and script{/size}{p}{size=70}Danny Garay{/size}" at truecenter with dissolve:
        xalign .5
    $ renpy.pause(2,hard=True)
    hide text

    show text "{size=30} Character artwork (sprites){/size}{p}{size=70}Tokudaya{/size}" at truecenter with dissolve:
        xalign .5
    $ renpy.pause(2,hard=True)
    hide text

    show text "{size=30} Additional illustrations{/size}{p}{size=70}Danny Garay{/size}" at truecenter with dissolve:
        xalign .5
    $ renpy.pause(2,hard=True)
    hide text

    show text "{size=30} scene backgrounds {/size}{p}{size=50}loo.sakura.ne.jp{p}Pixabay.com{p}LindaHicks{p}Wokandapix{p}Ajalfalro{p}Uncle Mugen{/size}" at truecenter with dissolve:
        xalign .5
    $ renpy.pause(4,hard=True)
    hide text

    show text "{size=30} Background music {/size}{p}{size=50}Amacha{p}Kevin Macleod{p}Eric Matyas{p}Vibe Mountain{p}Asher Fulero{p}Dead Seed{p}Silent Partner{/size}" at truecenter with dissolve:
        xalign .5
    $ renpy.pause(4,hard=True)
    hide text

    show text "{size=30} Sound effects {/size}{p}{size=60}Freesound.org{p}Taira Komori{/size}" at truecenter with dissolve:
        xalign .5
    $ renpy.pause(3,hard=True)
    hide text

    show text "{size=30} Programming and design {/size}{p}{size=70}Danny Garay{/size}" at truecenter with dissolve:
        xalign .5
    $ renpy.pause(2,hard=True)
    hide text

    show text "{size=30} Beta players (sin ningún orden en particular){/size}{p}{size=40}Pablo Canché, Alexis Sánchez, Marcos Lopez, Davar Osorio, Danny Huerta, Iván Medina, Bill García, Williams Chia, Deivid Navarro, Juan Cruz, Matías Barraza, Jeremy Garrido, Sebas BZ, José Veintimilla, Daniel Castro, Juan Vicente, Michel Hernández, Juan Manuel, Ramiro Segovia.{/size}" at truecenter with dissolve:
        xalign .5
    $ renpy.pause(6,hard=True)
    hide text

    show text "{size=30} Game engine {/size}{p}{size=70}Ren'Py{/size}" at truecenter with dissolve:
        xalign .5
    $ renpy.pause(2,hard=True)
    hide text

    $ renpy.pause(1,hard=True)

    label fin_creditos:
        if persistent.skipcredits:
            hide screen btnSkipCredits with dissolve
        show logo at truecenter with dissolve
        $ renpy.pause(1,hard=True)
        show text "{size=70}¡Thank you for playing!{/size}" with dissolve:
            xalign .5
            ypos .8
        $ renpy.pause(5,hard=True)
        hide logo with dissolve
        hide text with dissolve
        stop music fadeout 3
        $ renpy.pause(4,hard=True) 

        $noInteract(False)

    $persistent.skipcredits=True
    return


