label caso1_debate_rnd5:
    stop music fadeout 1
    hide neil with dissolve
    hide beck with dissolve
    hide marissa with dissolve
    

    $ quick_menu_gameplay = True
    $ estadoj="Debate"      
    $ initDebateVars()

    $ debate_args.append(1)## id del debate
    $ debate_args.append(5)## id de la ronda del debate
    $ debate_args.append(8)## cual id de frase es la correcta
    $ debate_args.append(3)## cual id de argumento es el correcto
    $ argumentos = ["Paper and locker", "Correlation diagram", "Field on weekends", "Neil's number", "Stumble"].  
    $ show_gameplay_layout(600)
    play music debate


label inicio_d1r5:
    if cantidad_corazones==0:
        jump d1_gameover

    $ frase_args=[]
    $ change_cursor("target")
    show screen debateArgumento
    $ quick_menu_bajo=True 
    
    ## aqui comienzan a hablar los participantes

    #0-neil 30-beck 60-alice

    scene bg salon club detectives:
        xpan 30
        linear 0.5 xpan 0
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show beck enojado with fast_dissolve
    show screen debateCharPanel("beck")

    $ frase_args.append(0)## el id de la frase (desde cero)
    $ frase_args.append("{amarillo}You were around {/amarillo} when {p}Marissa and the teacher tripped...").
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f0)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("beck")##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(3.5,hard=True)

    $ frase_args.append(1)## el id de la frase (desde cero)
    $ frase_args.append("You took advantage of that moment {/amarillo}{p} to put a letter in her purse {/amarillo}.")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r0f2)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("beck")##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3.5,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 30
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show neil sorprendido with fast_dissolve
    show screen debateCharPanel("neil")

    $ frase_args.append(2)## el id de la frase (desde cero)
    $ frase_args.append("Huh? That I did what?!")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r5f2)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(2.3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 30
        linear 0.5 xpan 0
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show beck serio with fast_dissolve
    show screen debateCharPanel("beck")

    $ frase_args.append(3)## el id de la frase (desde cero)
    $ frase_args.append("Also...")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r0f5)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2,hard=True)

    $ frase_args.append(4)## el id de la frase (desde cero)
    $ frase_args.append("{amarillo} Then you started stalking her..{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f0)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("beck")##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 30
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show neil sorprendido with fast_dissolve
    show screen debateCharPanel("neil")

    $ frase_args.append(5)## el id de la frase (desde cero)
    $ frase_args.append("That I've been stalking her!?")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f0)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2.5,hard=True)

    show neil pensativo

    $ frase_args.append(6)## el id de la frase (desde cero)
    $ frase_args.append("{azul} That is a lie.{/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r5f6)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("neil")##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(2.5,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 30
        linear 0.5 xpan 0
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show beck enojado with fast_dissolve
    show screen debateCharPanel("beck")

    $ frase_args.append(7)## el id de la frase (desde cero)
    $ frase_args.append("{amarillo}¡ Yes you did!{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f0)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("beck")##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2.5,hard=True)

    $ frase_args.append(8)## el id de la frase (desde cero)
    $ frase_args.append("{azul} There is evidence that you are interested{p} in Marissa.{/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r4f1)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("beck")##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3.5,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 30
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show neil pensativo with fast_dissolve
    show screen debateCharPanel("neil")

    $ frase_args.append(8)## el id de la frase (desde cero)
    $ frase_args.append("Oh yeah? And what is that evidence?")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f0)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 30
        linear 0.5 xpan 0
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show beck pensando with fast_dissolve
    show screen debateCharPanel("beck")

    $ frase_args.append(9)## el id de la frase (desde cero)
    $ frase_args.append("Uhm...")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f0)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2,hard=True)

    show beck preocupado

    $ frase_args.append(10)## el id de la frase (desde cero)
    $ frase_args.append("Is there evidence, [pla_name]?")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r5f10)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
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

    $ frase_args.append(11)## el id de la frase (desde cero)
    $ frase_args.append("Only [pla_name] is asked...")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r5f11)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(4,hard=True)





    hide alice with dissolve
    $clearDebateText()
    $change_cursor()
    $ quick_menu_bajo=False
    hide screen debateArgumento
    hide screen debateArgs
    $renpy.choice_for_skipping()
    "If I said that Neil is suspected of being Marissa's stalker..."
    "It's because I have evidence to prove it..."
    jump inicio_d1r5
