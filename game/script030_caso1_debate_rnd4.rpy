label caso1_debate_rnd4:
    stop music fadeout 1
    hide beck with dissolve
    hide alice with dissolve
    

    $ quick_menu_gameplay = True
    $ estadoj="Debate"      
    $ initDebateVars()

    $ debate_args.append(1)## id del debate
    $ debate_args.append(4)## id de la ronda del debate
    $ debate_args.append(5)## cual id de frase es la correcta
    $ debate_args.append(1)## cual id de argumento es el correcto
    $ argumentos = ["Field on weekends", "Stumble", "Paper and locker", "Correlation diagram", "Beck Doran (profile)"].    
    $ show_gameplay_layout(600)
    play music debate


label inicio_d1r4:
    if cantidad_corazones==0:
        jump d1_gameover

    $ frase_args=[]
    $ change_cursor("target")
    show screen debateArgumento
    $ quick_menu_bajo=True 
    
    ## aqui comienzan a hablar los participantes

    #0-beck 30-marissa 60-alice

    scene bg salon club detectives:
        xpan 30
        linear 0.5 xpan 0
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show beck pensando with fast_dissolve
    show screen debateCharPanel("beck")

    $ frase_args.append(0)## el id de la frase (desde cero)
    $ frase_args.append("If the {azul} letter did not go into the locker...{/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f0)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("beck")##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2,hard=True)

    $ frase_args.append(1)## el id de la frase (desde cero)
    $ frase_args.append("Then {amarillo}the letter was placed directly in the bag.{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r4f1)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("beck")##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 60
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show alice pensando with fast_dissolve
    show screen debateCharPanel("alice")

    $ frase_args.append(2)## el id de la frase (desde cero)
    $ frase_args.append("{amarillo} The stalker may be from the same classroom as Marissa....{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r4f2)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("alice")##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(3,hard=True)

    $ frase_args.append(3)## el id de la frase (desde cero)
    $ frase_args.append("{azul} He could have slipped the letter{/azul} in an oversight...")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r4f3)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("alice")##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 60
        linear 0.5 xpan 30
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show marissa apenada with fast_dissolve
    show screen debateCharPanel("marissa")

    $ frase_args.append(4)## el id de la frase (desde cero)
    $ frase_args.append("So the stalker {p}{azul}is a friend...{/azul}").
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r4f4)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 60
        linear 0.5 xpan 30
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show alice pensando with fast_dissolve
    show screen debateCharPanel("alice")

    $ frase_args.append(5)## el id de la frase (desde cero)
    $ frase_args.append("Perhaps {azul}the letter did not reach Marissa's bag inside the classroom {/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r4f5)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("alice")##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(3,hard=True)

    $ frase_args.append(6)## el id de la frase (desde cero)
    $ frase_args.append("{amarillo}Something must have occurred{/amarillo} for that to happen...").
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r4f6)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("alice")##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3.5,hard=True)

    hide alice with dissolve

    $clearDebateText()
    $change_cursor()
    $ quick_menu_bajo=False
    hide screen debateArgumento
    hide screen debateArgs
    $renpy.choice_for_skipping()
    "We're still stuck on how the letter could have gotten to Marissa..."
    "There must be something in my notes..."
    jump inicio_d1r4
