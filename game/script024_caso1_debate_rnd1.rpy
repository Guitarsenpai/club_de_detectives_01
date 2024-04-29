label caso1_debate_rnd1:
    stop music fadeout 1
    hide marissa with dissolve
    hide alice with dissolve


    $ quick_menu_gameplay = True
    $ estadoj="Debate"
    $ initDebateVars()


    $ debate_args.append(1)
    $ debate_args.append(1)
    $ debate_args.append(1)
    $ debate_args.append(3)
    $ argumentos = ["Love Letter","Paper and locker","Beck Doran (profile)","Suspect Profile","Crash"]
    $ show_gameplay_layout(600)
    play music debate


label inicio_d1r1:
    if cantidad_corazones==0:
        jump d1_gameover

    $ frase_args=[]
    $ change_cursor("target")
    show screen debateArgumento
    $ quick_menu_bajo=True



    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 60
    $ renpy.pause(0.5,hard=True)


    show marissa normal with fast_dissolve
    show screen debateCharPanel("marissa")

    $ frase_args.append(0)
    $ frase_args.append("My question is...")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r1f0)
    $ frase_args.append(False)
    $ frase_args.append(False)
    show screen debateText1(debate_args,frase_args)
    $ frase_args=[]
    $ renpy.pause(1.5,hard=True)

    $ frase_args.append(1)
    $ frase_args.append("{azul}Do we have another clue about the author?{/azul}")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r1f1)
    $ frase_args.append(True)
    $ frase_args.append("marissa")
    show screen debateText2(debate_args,frase_args)
    $ frase_args=[]
    $ renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $ clearDebateText()

    scene bg salon club detectives:
        xpan 60
        linear 0.5 xpan 0
    $ renpy.pause(0.5,hard=True)


    show alice normal with fast_dissolve
    show screen debateCharPanel("Alice")

    $ frase_args.append(2)
    $ frase_args.append("Another clue?")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r1f2)
    $ frase_args.append(False)
    $ frase_args.append(False)
    show screen debateText1(debate_args,frase_args)
    $ frase_args=[]
    $ renpy.pause(2,hard=True)

    show alice pensando

    $ frase_args.append(3)
    $ frase_args.append("{amarillo}I think so...{/amarillo}")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r1f3)
    $ frase_args.append(True)
    $ frase_args.append("Alice")
    show screen debateText2(debate_args,frase_args)
    $ frase_args=[]
    $ renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $ clearDebateText()

    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 60
    $ renpy.pause(0.5,hard=True)


    show marissa alegre hablando with fast_dissolve
    show screen debateCharPanel("marissa")

    $ frase_args.append(4)
    $ frase_args.append("Great! And which one is it?")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r1f4)
    $ frase_args.append(False)
    $ frase_args.append(False)
    show screen debateText1(debate_args,frase_args)
    $ frase_args=[]
    $ renpy.choice_for_skipping()
    $ renpy.pause(2,hard=True)

    hide screen debateText1

    $ frase_args.append(5)
    $ frase_args.append("{azul}Is there a secret message in the letter?{/azul}")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r1f2)
    $ frase_args.append(True)
    $ frase_args.append("marissa")
    show screen debateText2(debate_args,frase_args)
    $ frase_args=[]
    $ renpy.pause(1.8,hard=True)

    $ frase_args.append(6)
    $ frase_args.append("{amarillo}Is there anyone with the same handwriting?{/amarillo}")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r0f5)
    $ frase_args.append(True)
    $ frase_args.append("marissa")
    show screen debateText3(debate_args,frase_args)
    $ frase_args=[]
    $ renpy.pause(2,hard=True)

    show marissa at brinquitos

    $ frase_args.append(7)
    $ frase_args.append("{azul}In the end, was the writer's name in the letter?{/azul}")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r1f7)
    $ frase_args.append(True)
    $ frase_args.append("marissa")
    show screen debateText4(debate_args,frase_args)
    $ frase_args=[]
    $ renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $ clearDebateText()

    scene bg salon club detectives:
        xpan 60
        linear 0.5 xpan 0
    $ renpy.pause(0.5,hard=True)


    show alice pensando with fast_dissolve
    show screen debateCharPanel("Alice")

    $ frase_args.append(8)
    $ frase_args.append("Uh...")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r1f8)
    $ frase_args.append(False)
    $ frase_args.append(False)
    show screen debateText1(debate_args,frase_args)
    $ frase_args=[]
    $ renpy.pause(1,hard=True)

    $ frase_args.append(9)
    $ frase_args.append("Um...")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r1f9)
    $ frase_args.append(False)
    $ frase_args.append(False)
    show screen debateText2(debate_args,frase_args)
    $ frase_args=[]
    $ renpy.pause(1,hard=True)

    $ frase_args.append(10)
    $ frase_args.append("Well...")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r1f10)
    $ frase_args.append(False)
    $ frase_args.append(False)
    show screen debateText3(debate_args,frase_args)
    $ frase_args=[]
    $ renpy.pause(1,hard=True)

    $ frase_args.append(11)
    $ frase_args.append("I would say that...")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r1f11)
    $ frase_args.append(False)
    $ frase_args.append(False)
    show screen debateText4(debate_args,frase_args)
    $ frase_args=[]
    $ renpy.pause(1.3,hard=True)
    $ renpy.choice_for_skipping()
    hide screen debateText1
    hide screen debateText2
    hide screen debateText3
    hide screen debateText4

    show alice asustada

    $ frase_args.append(12)
    $ frase_args.append("[pl_name]! Help!")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r1f12)
    $ frase_args.append(False)
    $ frase_args.append(False)
    show screen debateText1(debate_args,frase_args)
    $ frase_args=[]
    $ renpy.pause(3,hard=True)


    hide alice with dissolve
    $ clearDebateText()
    $ change_cursor()
    $ quick_menu_bajo=False
    hide screen debateArgumento
    hide screen debateArgs
    $ renpy.choice_for_skipping()
    "Wow, Marissa has a lot of ideas..."
    "But there is something else we discovered..."
    jump inicio_d1r1
