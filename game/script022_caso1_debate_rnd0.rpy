label caso1_debate_rnd0:
    stop music fadeout 1


    $ quick_menu_gameplay = True

    $ estadoj="Debate"

    $ showMinigameTitle(estadoj,2)


    $ initDebateVars()
    $ initCorazones()


    $ debate_args.append(1)



    $ debate_args.append(0)

    $ debate_args.append(10)

    $ debate_args.append(1)

    $ argumentos = ["Neil London (profile)","Suspect Profile","Love Letter","Mysterious shadow"]


    $ show_gameplay_layout(600)

    play music debate


label inicio_d1r0:

    if cantidad_corazones==0 or timeup:
        jump d1_gameover

    $ frase_args=[]

    $ change_cursor("target")

    show screen debateArgumento

    $ quick_menu_bajo=True





    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 60

    $ renpy.pause(0.5,hard=True)


    show alice pensando with fast_dissolve
    show screen debateCharPanel("Alice")


    $ frase_args.append(0)

    $ frase_args.append("I suggest that...")

    $ frase_args.append("phrase")

    $ frase_args.append(d1r0f0)

    $ frase_args.append(False)

    $ frase_args.append(False)

    show screen debateText1(debate_args,frase_args)

    $ frase_args=[]

    $ renpy.pause(0.8,hard=True)


    $ frase_args.append(1)

    $ frase_args.append("we have to set...")

    $ frase_args.append("phrase")

    $ frase_args.append(d1r0f1)

    $ frase_args.append(False)

    $ frase_args.append(False)

    show screen debateText2(debate_args,frase_args)

    $ frase_args=[]

    $ renpy.pause(2,hard=True)

    show alice normal


    $ frase_args.append(2)

    $ frase_args.append("the {amarillo}personality of the author{/amarillo} of the letter.")

    $ frase_args.append("phrase")

    $ frase_args.append(d1r0f2)

    $ frase_args.append(False)

    $ frase_args.append(False)

    show screen debateText3(debate_args,frase_args)

    $ frase_args=[]

    $ renpy.choice_for_skipping()

    $ renpy.pause(3.8,hard=True)

    $ clearDebateText()

    hide alice with fast_dissolve
    hide screen debateCharPanel


    scene bg salon club detectives:
        xpan 60
        linear 0.5 xpan 0

    $ renpy.pause(0.5,hard=True)


    show marissa normal with fast_dissolve
    show screen debateCharPanel("marissa")

    $ frase_args.append(3)
    $ frase_args.append("The personality?")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r0f3)
    $ frase_args.append(False)
    $ frase_args.append(False)
    show screen debateText1(debate_args,frase_args) 
    $ frase_args=[]
    $ renpy.pause(2,hard=True)

    $ frase_args.append(4)
    $ frase_args.append("Uhm... well {amarillo}he seems like a romantic guy.{/amarillo}")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r0f4)
    $ frase_args.append(False)
    $ frase_args.append(False)
    show screen debateText2(debate_args,frase_args) 
    $ frase_args=[]
    $ renpy.choice_for_skipping()
    $ renpy.pause(4,hard=True)

    hide screen debateText1
    hide screen debateText2

    show marissa apenada

    $ frase_args.append(5)
    $ frase_args.append("If only he had given me the letter...")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r0f5)
    $ frase_args.append(False)
    $ frase_args.append(False)
    show screen debateText1(debate_args,frase_args) 
    $ frase_args=[]
    $ renpy.choice_for_skipping()
    $ renpy.pause(5,hard=True)

    hide screen debateText1
    hide screen debateCharPanel


    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 60

    $ renpy.pause(0.5,hard=True)


    show alice normal with fast_dissolve
    show screen debateCharPanel("Alice")

    $ frase_args.append(6)
    $ frase_args.append("Well, aside from the stalking fact...")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r0f6)
    $ frase_args.append(False)
    $ frase_args.append(False)
    show screen debateText1(debate_args,frase_args) 
    $ frase_args=[]
    $ renpy.choice_for_skipping()
    $ renpy.pause(2,hard=True)

    hide screen debateText1
    hide screen debateCharPanel


    scene bg salon club detectives:
        xpan 60
        linear 0.5 xpan 0

    $ renpy.pause(0.5,hard=True)


    show marissa normal with fast_dissolve
    show screen debateCharPanel("marissa")

    $ frase_args.append(7)
    $ frase_args.append("Then...")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r0f7)
    $ frase_args.append(False)
    $ frase_args.append(False)
    show screen debateText1(debate_args,frase_args) 
    $ frase_args=[]
    $ renpy.pause(2,hard=True)

    show marissa alegre hablando

    $ frase_args.append(8)
    $ frase_args.append("Maybe he's a {azul} nervous boy...{/azul}")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r0f8)
    $ frase_args.append(True)
    $ frase_args.append("marissa")
    show screen debateText2(debate_args,frase_args) 
    $ frase_args=[]
    $ renpy.pause(2,hard=True)

    $ frase_args.append(9)
    $ frase_args.append("{amarillo}Or unsure of himself...{/amarillo}")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r0f9)
    $ frase_args.append(True)
    $ frase_args.append("marissa")
    show screen debateText3(debate_args,frase_args) 
    $ frase_args=[]
    $ renpy.pause(2,hard=True)

    $ renpy.choice_for_skipping()

    $ frase_args.append(10)
    $ frase_args.append("{azul}Or a bit of both{/azul},{p}consequences of being{p}in love I guess...")
    $ frase_args.append("phrase")
    $ frase_args.append(d1r0f10)
    $ frase_args.append(True)
    $ frase_args.append("marissa")
    show screen debateText4(debate_args,frase_args) 
    $ frase_args=[]

    $ renpy.pause(1,hard=True)

    show marissa alegre at brinquitos

    $ renpy.pause(3.3,hard=True)

    hide marissa with dissolve

    if cantidad_corazones==0 or timeup:
        jump d1_gameover
    $ clearDebateText()
    $ change_cursor()
    $ quick_menu_bajo=False
    $ renpy.choice_for_skipping()
    hide screen debateArgumento
    hide screen debateArgs
    "The first thing to clarify is about the personality of the author of the letter..."
    "I must review my notes, and show whether Alice or Marissa {amarillo}made a mistake in something...{/amarillo}"
    "Or if one of them {amarillo}has said something right.{/amarillo}"

    jump inicio_d1r0
