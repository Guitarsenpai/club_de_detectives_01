label caso1_debate_rnd3:
    stop music fadeout 1
    hide beck with dissolve
    hide marissa with dissolve
    hide alice with dissolve
    

    $ quick_menu_gameplay = True
    $ estadoj="Debate"      
    $ initDebateVars()

    $ debate_args.append(1)## id del debate
    $ debate_args.append(3)## id de la ronda del debate
    $ debate_args.append(9)## cual id de frase es la correcta
    $ debate_args.append(1)## cual id de argumento es el correcto
    $ argumentos = ["Stumble", "Paper and locker", "Beck Doran (profile)", "Correlation diagram", "Field on weekends"]
    $ show_gameplay_layout(600)
    play music debate


label inicio_d1r3:
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
    show beck pensando with fast_dissolve
    show screen debateCharPanel("beck")

    $ frase_args.append(0)## el id de la frase (desde cero)
    $ frase_args.append("If you guys say...{p}that {amarillo}the stalker is not from Marissa's club... {/amarillo}.")    
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f0)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("beck")##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(3,hard=True)

    $ frase_args.append(1)## el id de la frase (desde cero)
    $ frase_args.append("How could this person give her a letter{p}without her noticing?"). 
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f2)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(4,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 30
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show marissa normal with fast_dissolve
    show screen debateCharPanel("marissa")

    $ frase_args.append(2)## el id de la frase (desde cero)
    $ frase_args.append("I've also wondered about that...")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r0f0)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2,hard=True)

    $ frase_args.append(3)## el id de la frase (desde cero)
    $ frase_args.append("If it's not from the club,{p}{azul}it should be someone close to me...{/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r3f3)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("marissa")##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3.5,hard=True)

    hide screen debateText1
    hide screen debateText2

    $ frase_args.append(4)## el id de la frase (desde cero)
    $ frase_args.append("That person {azul} put the letter in my bag... {/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r0f0)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("marissa")##label de char para resp incorrecta, nombre de char o False
    show screen debateText3(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(2.5,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 30
        linear 0.5 xpan 60
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show alice normal with fast_dissolve
    show screen debateCharPanel("alice")

    $ frase_args.append(5)## el id de la frase (desde cero)
    $ frase_args.append("{azul} Perhaps a friend...{/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r1f4)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("alice")##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2.5,hard=True)

    $ frase_args.append(6)## el id de la frase (desde cero)
    $ frase_args.append("Or a {azul} classmate...{/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r1f2)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("alice")##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2,hard=True)

    $ frase_args.append(7)## el id de la frase (desde cero)
    $ frase_args.append("Or a {azul} ex-boyfriend.{/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f2)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("alice")##label de char para resp incorrecta, nombre de char o False
    show screen debateText3(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 60
        linear 0.5 xpan 0
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show beck sonriendo with fast_dissolve
    show screen debateCharPanel("beck")

    $ frase_args.append(8)## el id de la frase (desde cero)
    $ frase_args.append("I know!")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r0f0)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(2,hard=True)

    show beck pensando

    $ frase_args.append(9)## el id de la frase (desde cero)
    $ frase_args.append("Perhaps the stalker {p}{amarillo} put the letter through the {p}slits of the locker.{/amarillo}.")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r3f9)## qué animacion usar
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
    show marissa sorprendida with fast_dissolve
    show screen debateCharPanel("marissa")

    $ frase_args.append(10)## el id de la frase (desde cero)
    $ frase_args.append("{azul}That makes a lot of sense! {/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r0f0)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("marissa")##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
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
"We're discussing {amarillo}how the letter got to Marissa...{/amarillo}"
    "I think that Alice and I {amarillo}found out something{/amarillo} about it..."
    jump inicio_d1r3
