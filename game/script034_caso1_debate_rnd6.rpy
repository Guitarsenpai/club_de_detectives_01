label caso1_debate_rnd6:
    stop music fadeout 1
    hide neil with dissolve
    hide beck with dissolve
    

    $ quick_menu_gameplay = True
    $ estadoj="Debate"      
    $ initDebateVars()

    $ debate_args.append(1)## id del debate
    $ debate_args.append(6)## id de la ronda del debate
    $ debate_args.append(15)## cual id de frase es la correcta
    $ debate_args.append(3)## cual id de argumento es el correcto
    $ argumentos = ["Neil London (profile)", "Correlation diagram", "Field on weekends", "Prof. Harrow (profile)", "Paper and locker", "Stumble"].
    $ show_gameplay_layout(600)
    play music debate


label inicio_d1r6:
    if cantidad_corazones==0:
        jump d1_gameover

    $ frase_args=[]
    $ change_cursor("target")
    show screen debateArgumento
    $ quick_menu_bajo=True 
    
    ## aqui comienzan a hablar los participantes

    #0-neil 20-beck 50-marissa 60-alice

    scene bg salon club detectives:
        xpan 30
        linear 0.5 xpan 0
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show neil normal with fast_dissolve
    show screen debateCharPanel("neil")

    $ frase_args.append(0)## el id de la frase (desde cero)
    $ frase_args.append("First, I recommend that...")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f0)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2.4,hard=True)

    $ frase_args.append(1)## el id de la frase (desde cero)
    $ frase_args.append("you take another look to the letter").
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f1)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2.2,hard=True)

    $ frase_args.append(2)## el id de la frase (desde cero)
    $ frase_args.append("{amarillo} Perhaps there may be new clues there.{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f2)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("neil")##label de char para resp incorrecta, nombre de char o False
    show screen debateText3(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 60
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show alice normal with fast_dissolve
    show screen debateCharPanel("alice")

    $ frase_args.append(3)## el id de la frase (desde cero)
    $ frase_args.append("{azul} But there's nothing else on the letter...{/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f1)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("alice")##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(2,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 60
        linear 0.5 xpan 50
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show marissa normal with fast_dissolve
    show screen debateCharPanel("marissa")

    $ frase_args.append(4)## el id de la frase (desde cero)
    $ frase_args.append("Also, you have said that the author was{p}{amarillo} a left-handed person...{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f4)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("marissa")##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $ frase_args.append(5)## el id de la frase (desde cero)
    $ frase_args.append("If it wasn't Neil, who wrote the letter?")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f5)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 50
        linear 0.5 xpan 0
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show neil normal with fast_dissolve
    show screen debateCharPanel("neil")

    $ frase_args.append(6)## el id de la frase (desde cero)
    $ frase_args.append("It would be better to...")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f6)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2,hard=True)

    $ frase_args.append(7)## el id de la frase (desde cero)
    $ frase_args.append("{amarillo} focus on the content of the letter.{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f7)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("neil")##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 50
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show marissa normal with fast_dissolve
    show screen debateCharPanel("marissa")

    $ frase_args.append(8)## el id de la frase (desde cero)
    $ frase_args.append("What could there be {p}hidden in the {p}content?")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r1f0)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(3,hard=True)

    $ frase_args.append(9)## el id de la frase (desde cero)
    $ frase_args.append("{azul}Maybe a secret code?{/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r1f1)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("marissa")##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 20
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show beck serio with fast_dissolve
    show screen debateCharPanel("beck")

    $ frase_args.append(10)## el id de la frase (desde cero)
    $ frase_args.append("Seeing the way it was written...")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f10)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(2.5,hard=True)

    hide screen debateText1

    $ frase_args.append(11)## el id de la frase (desde cero)
    $ frase_args.append("Perhaps the author {amarillo}is a poet....{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r1f8)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("beck")##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2.5,hard=True)

    $ frase_args.append(12)## el id de la frase (desde cero)
    $ frase_args.append("Since he does not have an outstanding figure...").
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r4f4)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText3(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2,hard=True)

    $ frase_args.append(13)## el id de la frase (desde cero)
    $ frase_args.append("{amarillo} That's his only way to pick up girls.{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f13)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("beck")##label de char para resp incorrecta, nombre de char o False
    show screen debateText4(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 20
        linear 0.5 xpan 60
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show alice pensando with fast_dissolve
    show screen debateCharPanel("alice")

    $ frase_args.append(14)## el id de la frase (desde cero)
    $ frase_args.append("{amarillo} There's something in the letter that doesn't match...{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f1)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("alice")##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(3,hard=True)

    $ frase_args.append(15)## el id de la frase (desde cero)
    $ frase_args.append("{azul} It's as if it were about another person....{/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f2)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("alice")##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(3,hard=True)

    show alice normal

    $ frase_args.append(16)## el id de la frase (desde cero)
    $ frase_args.append("{azul}Is Neil not the stalker?{/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r0f0)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("alice")##label de char para resp incorrecta, nombre de char o False
    show screen debateText3(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2.7,hard=True)

    show alice pensando

    $ frase_args.append(17)## el id de la frase (desde cero)
    $ frase_args.append("{amarillo} Everything is so confusing...{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f5)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("alice")##label de char para resp incorrecta, nombre de char o False
    show screen debateText4(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    hide alice with dissolve
    $clearDebateText()
    $change_cursor()
    $ quick_menu_bajo=False
    hide screen debateArgumento
    hide screen debateArgs
    $renpy.choice_for_skipping()
    "Just as Neil said, I should read the letter again and {amarillo}understand the contents{/amarillo} of it better."
    "I don't want to trust him, but if he says there is something else in the letter... I must confirm it!"
    jump inicio_d1r6
