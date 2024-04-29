label caso1_debate_rnd2:
    stop music fadeout 1
    hide beck with dissolve
    hide marissa with dissolve
    hide alice with dissolve
    

    $ quick_menu_gameplay = True
    $ estadoj="Debate"      
    $ initDebateVars()

    
    $ debate_args.append(1)## id del debate
    $ debate_args.append(2)## id de la ronda del debate
    $ debate_args.append(13)## cual id de frase es la correcta
    $ debate_args.append(3)## cual id de argumento es el correcto
    $ argumentos = ["Scratches in the Locker", "Paper and Locker", "Love Letter", "Feeling of Being Watched", "Suspect Profile"].   
    $ show_gameplay_layout(600)
    play music debate

label inicio_d1r2:
    if cantidad_corazones==0:
        jump d1_gameover

    $ frase_args=[]
    $ change_cursor("target")
    show screen debateArgumento
    $ quick_menu_bajo=True 
    
    ## aqui comienzan a hablar los participantes

    #0-beck 30-marissa 60-alice

    scene bg salon club detectives:
        xpan 0

    ## informacion del hablante
    show beck sonriendo with fast_dissolve
    show screen debateCharPanel("beck")

    $ frase_args.append(0)## el id de la frase (desde cero)
    $ frase_args.append("Even if it is a source of envy...")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f0)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2,hard=True)

    $ frase_args.append(1)## el id de la frase
    $ frase_args.append("Being stalked by women is something that gets tiring.")    
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f1)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2,hard=True)

    $ frase_args.append(2)## el id de la frase
    $ frase_args.append("{amarillo} You feel watched...{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f2)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("beck")##label de char para resp incorrecta, nombre de char o False
    show screen debateText3(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(3.5,hard=True)

    $renpy.choice_for_skipping()

    hide screen debateText1
    hide screen debateText2
    hide screen debateText3

    show beck pensando

    $ frase_args.append(3)## el id de la frase
    $ frase_args.append("{amarillo} They call to your cell phone a lot...{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f0)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("beck")##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2,hard=True)

    $ frase_args.append(4)## el id de la frase
    $ frase_args.append("{azul} They send you so many messages...{/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f4)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("beck")##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2,hard=True)

    $ frase_args.append(5)## el id de la frase
    $ frase_args.append("You know , {amarillo} sometimes you need your space.{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f2)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("beck")##label de char para resp incorrecta, nombre de char o False
    show screen debateText3(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3.5,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 30
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show marissa normal with fast_dissolve
    show screen debateCharPanel("marissa")

    $ frase_args.append(6)## el id de la frase (desde cero)
    $ frase_args.append("I get you.")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r0f0)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2,hard=True)

    $ frase_args.append(7)## el id de la frase (desde cero)
    $ frase_args.append("I also need some time alone.")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f7)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2,hard=True)

    $ frase_args.append(8)## el id de la frase (desde cero)
    $ frase_args.append("If I already feel terrible with a stalker...")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r0f2)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText3(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(2.5,hard=True)

    hide screen debateText1
    hide screen debateText2
    hide screen debateText3

    show marissa apenada

    $ frase_args.append(9)## el id de la frase (desde cero)
    $ frase_args.append("I don't want to imagine your situation...")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r1f12)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText4(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(4,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 30
        linear 0.5 xpan 60
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show alice pensando with fast_dissolve
    show screen debateCharPanel("alice")

    $ frase_args.append(10)## el id de la frase (desde cero)
    $ frase_args.append("A conversation between popular people...")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r0f0)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(2.5,hard=True)

    $ frase_args.append(11)## el id de la frase (desde cero)
    $ frase_args.append("What an envy...")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f11)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2.5,hard=True)
    $renpy.choice_for_skipping()
    $clearDebateText()

    scene bg salon club detectives:
        xpan 60
        linear 0.5 xpan 0
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show beck pensando with fast_dissolve
    show screen debateCharPanel("beck")

    $ frase_args.append(12)## el id de la frase (desde cero)
    $ frase_args.append("Stalkers...{p}{ amarillo} look for ways to get closer to their target {/ amarillo}").
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f0)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("beck")##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3.5,hard=True)

    show beck serio

    $ frase_args.append(13)## el id de la frase (desde cero)
    $ frase_args.append("I assure you, {amarillo}that stalker{p}is in your club!{/amarillo}").    
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r1f12)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("beck")##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(4,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 30
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show marissa preocupada sudor with fast_dissolve
    show screen debateCharPanel("marissa")

    $ frase_args.append(14)## el id de la frase (desde cero)
    $ frase_args.append("In my club!?")    
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r1f0)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2,hard=True)

    show marissa preocupada

    $ frase_args.append(15)## el id de la frase (desde cero)
    $ frase_args.append("That {azul}might have sense ...{/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r1f1)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("marissa")##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(2,hard=True)

    hide marissa with dissolve

    $clearDebateText()
    $change_cursor()
    $ quick_menu_bajo=False
    hide screen debateArgumento
    hide screen debateArgs
    $renpy.choice_for_skipping()
    "Let's see... the goal is to look for characteristics to identify Marissa's stalker..."
    "We already have some... {amarillo}but what do we know about his life at school {/amarillo}?"
    "Is there anything we can be sure of?"    
jump inicio_d1r2
