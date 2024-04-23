label caso1_investigacion1:
    scene bg salon club detectives with dissolve
    "After Marissa left, Alice and I were still in the clubroom."
    "First, we started by reviewing the letter."
    scene carta_amor with dissolve
    ali "Uhm..."
    ali "The handwriting is very sloppy..."
    pla "Maybe it's nerves, right?"
    ali "It could be..."
    pla "What will that stain mean?"
    ali "It looks as if there was an excess of ink."
    ali "Maybe he kept the tip of the pen on the paper for a long time..."
    pla "Uhm, and right on the name, like he was overthinking it."
    pla "..."
    pla "There's something weird with the handwriting..."
    ali "Uh?"
    scene bg salon club detectives with dissolve
    show alice normal with dissolve
    ali "What do you mean, [pla_name]?"
    show alice sorprendida
    pla "I know!"
    pla "It's... It's..."
    show alice normal
    ali "You forgot it?"
    pla "No... none of that..."
    pla "Ah... I have it on the tip of my tongue..."
    show alice sorprendida
    pla "It was something that had to do with the way of writing... with the inclination..."
    ali "You need to use the {amarillo}Roulette of the Incognito{/amarillo}!"
    pla "The- the roulette of the... what?"
    show alice alegre
    ali "It's a technique my superiors used when they temporarily forgot a word."
    ali "What you have to do is imagine several letters that rotate in circles..."
    ali "Then you are discarding letters one by one until you form a word."
    pla "I don't understand..."
    show alice enojada
    ali "Quick, [pla_name]!" with hpunch
    ali "Close your eyes and do what I just told you!"
    pla "I-okay..."
    pla "Nothing to lose..."
    stop music fadeout 4
    scene bg negro with fade
    tuto "It's time for another minigame."
    tuto "In the {amarillo} Roulette of the Incognito {/amarillo} you will see a series of letters that are spinning in circles."
    tuto "The objective is to select several letters to form a word."
    tuto "If you select a wrong letter, you will lose life..."
    tuto "In this minigame, lives are represented by a percentage."
    tuto "Each incorrect letter subtracts 10%%"
    tuto "If you select a correct letter, it will be added to a panel on the right."
    tuto "Basically, it's like {amarillo}the game of hangman.{/amarillo}"
    tuto "Good luck."


     #-----Inicia minijuego
    $ estadoj="Incog. Roulette"
    $ ruleta_porcentaje=100
    $ ruleta_id=1

     #palabra a descubir
    $ palabra_ruleta="LEFTHANDED"

     #posicion de la letra a averiguar en palabra
    $ posicionenpalabra=0

    python:
        #lo que se mostrara en el panel derecho
        lstLetrasActuales=[]

        for x in xrange(0,len(palabra_ruleta)):
            lstLetrasActuales.append("_")

    $letras1=["Z","Y","E","L","D","A","D","R","O"]
    $letras2=["I","D","Z","F","N","T","M","E","H","B"]

    $ quick_menu_gameplay=True
    $ showMinigameTitle("Roulette of the Incognito ")
    $ quick_menu_bajo=True
    window hide
    play music deduccion fadein 3
    $ change_cursor("target")
    scene bg salon club detectives
    $ renpy.show_screen("timer",185) )#185

    call screen ruleta_incognita(letras1,letras2,"From the way of writing, it can be deduced that the author is...",palabra_ruleta)

label ruleta1_gameover:
    stop music fadeout 3
    $ estadoj="Free"
    # $quick_menu_gameplay=False 
    $ quick_menu_bajo=False
    window show
    show alice normal with dissolve
    pla "I give up."
    ali "I thought you'd try harder."
    show alice pensando at decaer
    ali "So we don't have any more clues..."
    jump caso1_gameover

label ruleta1_fin:

    $ fase_titulo.append("Roulette of the Incognito ")
    $ fase_tipo_vida.append("percentage")
    $ fase_corazones.append(ruleta_porcentaje)
    $ fase_multiplicador.append(5)

    $ showplay_excl("that is")
    stop music fadeout 3
    $ estadoj="Free"
    $ quick_menu_gameplay=False
    $ quick_menu_bajo=False
    window show
    show alice sorprendida with dissolve
    play sound campana
    pla "The author is left-handed!" with flashbulb
    ali "Hey!?"
    ali "Why do you say that?"
    show alice normal
    pla "By the inclination of the letter."
    pla "That inclination seemed strange to me..."
    pla "And it is precisely because someone who writes with their left hand will have the letter tilted to that side..."
    pla "Besides, that would also explain the stain on the letter."
    show alice sorprendida
    ali "Uh!? Really?"
    pla "Yes. By leaving the pen on the paper at a specific point for some time..."
    pla "It would make the ink run, and since you write from left to right..."
    show alice normal
    ali "Someone left-handed would pass the hand with which he writes over the ink..."
    pla "That's how it is."
    ali "..."
    play music ambiente fadein 3
    show alice alegre at brinquitos
    ali "That's incredible! [pla_name], you're so smart!"
    ali "I'm so glad to have you in the club!"
    #actualizamos perfil de sospechoso
    #--nota: actualizar de acuerdo al nombre, usar la posicion del array no es confiable, ya que esta posicion puede variar de acuerdo a cuando se obtiene una pista
    $ updateNote("Suspect Profile",ndesc="\n\nThere are clues that the author of the letter is left-handed.",add=True)
    pla "Ah... come on... it's not that big a deal..."
    pla "..."
    show alice normal
    pla "Time has flown by, it's already going to be five o'clock."
    show alice sorprendida
    ali "Uh, I hadn't realised..."
    show alice normal
    ali "It's time to go out..."
    ali "But first, we should check Marissa's locker..."
    pla "Um, sure..."
    ali "Let's go, Sherinford."
    show sherinford grande behind alice at left with dissolve:
        xoffset -300
        on show:
            linear 1 xoffset 20
    she "Twit, twit, twit!"
    scene bg negro with slow_dissolve
    hide screen quick_menu
    $ quick_menu=False
    window hide
    $ hora=17
    pause 2
    $ quick_menu=True
    window show
    scene bg escuela corredor with slow_dissolve
    show alice normal with dissolve
    show sherinford pequeño at center with dissolve:
        ypos .450
        xoffset 70
    "Together with Alice and her chicken, I went to the corridor of the classrooms, where the lockers are."
    "I had texted Marissa to tell us where her locker was."
    ali "Uhm..."
    "Alice muttered as she checked the locker with a huge magnifying glass."
    ali "Uuuuuhhhmmm..."
    ali " I see..."
    pla "Have you discovered something?"
    show alice sonriendo at brinquitos
    show sherinford pequeño at brinquitos
    ali "Indeed..."
    ali "The scratches on the locker latch are quite uncommon."
    pla "..."
    "Thank you captain obvious, I already saw that without needing a magnifying glass..."
    show alice pensando
    ali "I haven't found any more clues..."
    ali "I think that's all..."
    show alice sorprendida
    pla "Not so fast."
    pla "We should ask ourselves {nw}"
    play sound campana
    extend " {amarillo}why this locker was being tampered with by someone.{/amarillo}" with flashbulb
    ali "Oh! O- of course! Of course I already knew that." with hpunch
    show alice pensando
    ali "I was just testing you..."
    "I really doubt it..."
    pla "Anyway, considering what Marissa told us..."
    show alice normal
    pla "If those scratches appeared on Saturday..."
    pla "We'd have to find out if anyone saw anything suspicious in that time frame."
    ali "I don't think that's easy..."
    ali "{amarillo}On weekends, the students only come for club activities...{/amarillo}"
    ali "And this {amarillo} building generally remains empty...{/amarillo}"
    ali "Even the salons here are kept closed."
    $ addNote("Classrooms on the weekend","Classrooms are closed on weekends, with the exception of the club building.\nTherefore, the building where the lockers are located remains empty.")
    pla "Oh, I didn't know that..."
    pla "So, back to the reason for the tampering..."
    pla "Considering that we are talking about a stalker, did this person want something from Marissa?"
    pla "You know, something like a treasure... Or a prize..."
    show alice pensando
    ali "Uh... I get chills just thinking about it..."
    show alice normal
    play sound campana
    ali "{amarillo}But what was the stalker trying to get out of Marissa's locker?{/amarillo}" with flashbulb
    $ addNote("Is there anything of value in the locker?","What was the person responsible for the tampering looking for in Marissa's locker? Is there anything of value that Marissa keeps in her locker?")
    pla "We'll have to ask Marissa if she kept anything of value..."
    ali "Good idea..."
    show alice sorprendida
    play sound campana
    ali "Oh!" with flashbulb
    pla "Alice?"
    ali "I know! And what if the person responsible was looking to put something in the locker!?"

    hide sherinford with dissolve
    hide alice with dissolve
    "Clearly excited, Alice took a notebook sheet from her backpack."
    pla "What do you have in mind now?"
    ali "[pla_name], I've been thinking about it..."
    ali "How did that letter get into Marissa's bag?"
    ali "I think the stalker wanted to put the letter in the locker, so he picked the lock."
    ali "And seeing that it was very difficult to do it, then..."
    "Alice began trying to get the blade through the cracks in the door."
    "She even tried to get it through the holes in the front."
    "However..."
    show alice pensando with dissolve
    show sherinford pequeño at center with dissolve:
        ypos .450
        xoffset 70
    ali "No- it doesn't go in..."
    she "Twit..."
    "Alice's hypothesis soon fell apart."
    pla "I don't think that was it..."
    pla "Otherwise, {amarillo} Marissa would have told us that she found the letter in the locker, and not in her bag.{/amarillo}"
    ali "Uh...that seems to be...I thought I was right..."
    $ addNote("paper and locker","Alice demonstrated that you can't put a piece of paper in a locker without first opening it.")
    "Alice sounded disappointed, but it wouldn't hurt to write down what she found."
    show alice normal
    # ali "..."
    # pla "¿Qué pasa ahora, Alice?"
    # "Vi que ella de repente se quedó viendo a la nada, sumida en sus pensamientos."
    # ali "¿Cómo estamos seguros de que el acosador realmente no pudo abrir el casillero?"
    # $addNote("¿Cerradura fue forzada?","Alice sugirió que quizás el acosador sí pudo abrir el casillero...")
    # pla "..."
    pla "Well, I think we have enough information for today."
    pla "It's getting late."
    ali "Uh yes... there is nothing more to investigate here."
    pla "Well, I'm leaving."
    show alice pensando
    ali "..."
    if pla_stat["charisma"]>=2:
        show alice pensando
        ali " [pla_name]..."
        pla "What's wrong?"
        ali "Uh... we- well..."
        show alice sonrojada
        ali "{size=25}We should exchange numbers...{/size}"
        pla "What?"
        show alice asustada
        ali "..."
        ali "do- don't make me repeat it..." with hpunch
        "I wouldn't, if she spoke with a more audible voice."
        show alice sonrojada
        ali "I was wondering..."
        extend " if we could exchange numbers..."
        show alice asustada
        ali "D-don't think anything strange!" with hpunch
        show alice sonrojada
        ali "Is that I..."
        pla "I'm not thinking of anything strange... it's okay."
        show alice sorprendida
        ali "Uh!?" with hpunch
        pla "Why do you act like this?"
        show alice pensando
        ali "Uh...no...nothing..."
        stop music fadeout 3
        scene bg negro with dissolve
        pause 1.5
        "Before we said goodbye, I exchanged numbers with Alice."
        $ numero_alice_obtenido=True
    else:
        $ numero_alice_obtenido=False
        extend " bye [pla_name]."
        stop music fadeout 3
        scene bg negro with dissolve
        pause 1.5

    if numero_alice_obtenido:
        hide screen quick_menu
        window hide
        $ quick_menu=False
        $ hora=20 #8 pm
        pause 2
        window show
        $ quick_menu=True
        "..."
        #ring
        "In the night, I received a message from Alice."
        ali "{amarillo}\"Hi, how are you?\"{/amarillo}"
        ali "{amarillo}\"I hope we can solve this case...\"{/amarillo}"
        ali "{amarillo}\"I'm counting on you, [pla_name] :3\"{/amarillo}"

    scene bg negro with slow_dissolve
    hide screen quick_menu
    $ quick_menu=False
    window hide

    $ hora=20 #8 pm
    pause 2

    $ hora=10
    $ dia="Fri"
    $ fecha="February 21"
    $ estadoj="Break time"

    window show
    $ quick_menu=True

    scene bg escuela corredor with dissolve
    "{amarillo}- The next day, during break time... -{/amarillo}"
    play music ambiente2 fadein 5
    "Walking out of my classroom, I met a familiar face."
    show alice alegre with dissolve
    ali "[pl_name]! Good morning!" with hpunch
    pla "Alice... Good morning..."
    "I saw that she was in a very good mood."
    show alice enojada
    ali "Come on! The investigation must continue!" with hpunch
    pla "Uh..."
    pla "I would rather have a break... classes are more demanding this year..."
    ali "How can you say that!?" with hpunch
    ali "You can't let an investigation get too cold or it will go to waste."
    show alice normal
    pla "Ahh... now I'm hungry..."
    "Ignoring my complaints, Alice continued talking."
    ali "I've been thinking a lot about the case last night..."
    ali "From what Marissa has told us..."
    ali "It would be good to establish as a starting point... {nw}"
    play sound campana
    extend "{amarillo}that the stalker is an acquaintance of hers.{/amarillo}" with flashbulb
    pla "Makes sense..."
    "I started walking towards the cafeteria, and Alice was following me as she expounded her ideas."
    ali "So... we have to take advantage of this break time to find out more {amarillo}about Marissa's classmates.{/amarillo}"
    pla "Uh, come on... give me a break..."
    show alice enojada
    ali "[pl_name]!" with hpunch
    extend " There is no time to waste."
    show alice pensando
    ali "If not, the club..."
    ali "It could close..."
    pla "Don't even think about making a scandal of yours."
    ali "Um..."
    pla "..."
    "I stopped walking, and started scratching my head."
    pla "Hah, It's okay..."
    show alice alegre at brinquitos
    ali "Yaaay!"
    extend " Well said!"
    hide alice with dissolve
    "Let's see... Marissa's classroom would be the..."
    pla "..."
    "I saw that Alice was not following me..."
    pla "Alice... you don't want me to go alone, do you?"
    show alice pensando with dissolve
    ali "..."
    ali "Uh- we- well..."
    "The girl began to babble until she found an answer."
    show alice sorprendida
    ali "Oh yeah!" with hpunch
    show alice normal
    ali "Remember how Marissa told us to be discreet?"
    ali "Well... it would be suspicious if we both arrived."
    pla "..."
    extend "oh great."
    show alice sonriendo
    ali "So... do your best to find suspects."
    ali "I will be investigating elsewhere."
    pla "What if we better change places?"
    show alice alegre at brinquitos
    ali "See you later!"
    show alice:
        ease .3 xoffset 90
        ease .5 xoffset -900
    pause 1.5
    hide alice
    # hide alice with dissolve

    "Without finishing listening to me, Alice ran away..."
    "Ah... you will pay me..."
    scene bg negro with dissolve
    pause 1.4
    # "Le envié un mensaje a Marissa, avisándole que iría a su salón para buscar sospechosos."
    # "Ella me contestó de inmediato, y me dijo que no había problema."
    # "Acordamos que yo iría porque supuestamente estoy interesado en el club de cocina."
    # "Y aprovechando el don de Marissa para ser muy sociable... ella me presentaría a sus compañeros de clase."
    scene bg salon clases with dissolve
    pla "Excuse me... is Marissa here?"
    unk "Uh?"
    unk "Marissa, someone is looking for you."
    mar "I'm coming..."
    show marissa alegre hablando with dissolve
    mar "Hello! Uh? [pla_name]?"
    # "Marissa fingió no conocerme, de acuerdo al plan que establecimos en el chat."
    show marissa normal
    pla "Hi, I'm here for the cooking club, I'm interested."
    "As I was saying that, I secretly wink at her."
    show marissa alegre hablando at brinquitos
    mar "Ah, do you want to join the cooking club?"
    "And thank goodness Marissa caught my signal."
    pla "I'm not sure, but I would like to know a few things about the club."
    show marissa alegre
    mar "Sure, no problem!"
    unk "Who is it, Marissa? Do you know him?"
    "One of the girls near her asked very curiously."
    show marissa alegre hablando
    mar "Of course, he is... [pla_name]. A few days ago he went to the club as he was looking for one to join."
    "As expected of someone so popular, Marissa handled the situation matter-of-factly."
    unk "Uh... so it's like that... I see..."
    scene bg negro with dissolve
    "And without being suspicious at all, Marissa was introducing me to all of her friends, and she also told me about the rest of her classmates."
    "It's the only thing that occurred to me in a short time..."
    "However, I discovered some interesting things."
    scene bg salon clases with dissolve
    show marissa alegre hablando with dissolve
    unk "Hey, Marissa... who's that guy?"
    unk "Is he your boyfriend? Ha ha ha."
    show marissa alegre
    mar "Heh heh, don't be kidding."
    show marissa:
        ease .5 mright
    show beck sonriendo at mleft with dissolve
    pause 1
    "Woooa... that guy is so tall!" with vpunch
    show marissa alegre
    mar "[pla_name], this is {amarillo}Beck Doran.{/amarillo} Beck, this is [pla_name]."
    bec "What's up?"
    pla "Nice to meet you..."
    "Beck... I remember Marissa said she ran into him in the cafeteria..."
    mar "[pla_name] came to me because he is interested in the cooking club."
    show beck sorprendido
    bec "Oh really?"
    "The boy looked like he was analyzing me, I hope he doesn't catch our lie..."
    stop music fadeout 4
    show beck serio
    bec "I see..."
    show marissa sorprendida
    mar "..."
    show beck enojado
    bec "I know what the truth is."
    pla "..."
    mar "What?"
    show beck serio
    bec "Your name is... [pla_name], right?"
    bec "You're a smart boy... but I already know your true intentions."
    pla "..."
    pla "I don't know what you're talking about..."
    # "¿Acaso es verdad lo que está diciendo?"
    mar "Beck... what do you mean?"
    show beck enojado
    bec "Marissa... that boy..."
    play music ambiente2 fadein 2
    show beck sonriendo at brinquitos
    bec "He wants to join the club to be surrounded by cute girls!"
    show beck guino
    bec "You're quite the ruffian, [pla_name], ha ha ha."
    pla "..."
    extend " Oh! Ha ha ha..." with hpunch
    "I could only laugh, relieved, hoping he would change the subject."
    show marissa normal
    show beck sonriendo
    bec "Hey [pla_name], let's not play dumb, if the cooking club isn't your thing..."
    play sound campana
    bec "Take a tour by {amarillo}the soccer club.{/amarillo} I assure you that you will have more girls following you heh, heh, heh." with flashbulb
    bec "Well, see you ha ha ha."
    hide beck with dissolve
    show marissa:
        ease .5 center
    "And with that Beck left the room while he was laughing."
    "Also, while he was leaving, some girls went to follow him…"
    pla "... that was close..."
    show marissa alegre at decaer
    mar "So it seems, heh, heh..."
    show marissa alegre hablando at reponerse
    mar "As you could see, that is Beck Doran, he is a member of the soccer club."
    mar "He is quite the celebrity in our classroom."
    pla "..."
    show marissa normal
    mar "[pla_name]?"
    pla "Ah, there's something he told me that caught my attention..."
    pla "What did he mean with that {amarillo}\"I would have more girls following me\"{/amarillo}?"
    mar "Uh... are you interested in that?"
    pla "No no..."
    "Okay, yes..."
    pla "That boy, is he really that popular?"
    show marissa alegre
    mar "Sure, almost every girl in the classroom has him as an idol.{nw}"
    play sound campana
    extend " {amarillo}He's even had female stalkers.{/amarillo}" with flashbulb
    show marissa normal
    pla "Uh!?" with hpunch
    "So that boy has had stalkers..."
    $ addNote("Beck Doran (profile)","Member of the football club. He is a very popular person in his classroom, especially among the girls. According to Marissa, he has had some female stalkers bothering him.","beck")
    "I should talk to him later."
    pla "Oh by the way..."
    $ renpy.choice_for_skipping()
    pla "Marissa, I have something to ask you..."
    tuto "Now, you will need to select an element from the notepad."
    tuto "You just have to click on \"Submit\" under the element to choose."

    $ initCorazones()
    show screen corazones
    $ quick_menu_gameplay=True
    mar "Yeah? What do you want to ask?"

##ahora se debe seleccionar un item del bloc de notas, usaremos como id, el titulo del elemento
    $ idevidencia_correcta="Is there anything of value in the locker?"

    label mostrar_evidencia1:

        show marissa normal

        if cantidad_corazones==0:
            jump evidencia_mostrada1_gameover

        call screen notepad("evidenc",jumpto="evidencia_mostrada1") with dissolve

    label evidencia_mostrada1:
        if idevidencia_mostrar==idevidencia_correcta:
            $ evidencia1_fallida1erintento=False
            jump evidencia_mostrada1_correcto
        else:
            $ evidencia1_fallida1erintento=True
            $ randomnum = renpy.random.randint(1, 5)
            if randomnum==1:
                mar "I do not understand your question..."
            elif randomnum==2:
                show marissa alegre hablando
                mar "You know... Sometimes you say strange things..."
            elif randomnum==3:
                show marissa enojada
                mar "Could you go straight to the point? The break time is very short."
            elif randomnum==4:
                mar "You like to waste time, huh?"
            elif randomnum==5:
                show marissa apenada
                mar "[pla_name]...Hurry up, I want to go buy something in the cafeteria..."
            $ restCorazones()
            pla "Ah, sorry... that wasn't..." with hpunch
            jump mostrar_evidencia1

    label evidencia_mostrada1_gameover:
        $ evidencia_mostrada1_resuelta=False
        hide screen corazones
        stop music fadeout 1
        show marissa preocupada
        mar "What are you trying to do, [pla_name]?"
        $ updateStat("intel","-",1)
        $ renpy.notify("Intelligence -1")
        pla "The truth is that I don't even know..."
        jump evidencia_mostrada1_final

    label evidencia_mostrada1_correcto:
        $ evidencia_mostrada1_resuelta=True
        hide screen corazones
        $ showplay_excl("that is")
        if not evidencia1_fallida1erintento:
            $ updateStat("intel","+",1)
            $ renpy.notify("Intelligence +1")
        pla "Marissa... Do you keep anything of value in your locker?"
        show marissa sorprendida
        mar "Huh?"
        mar "Why do you ask?"
        pla "Well... that would help explain why they would try to open your locker..."
        "I made sure to speak quietly so others wouldn't hear."
        show marissa normal
        mar "Uhm..."
        mar "Well, I don't keep anything of value in my locker."
        mar "I only have books and notebooks there."
        pla "Oh, I understand... thanks, that's what I wanted to know."
        $ removeNote("Is there anything of value in the locker?")
        "Question resolved..."
        jump evidencia_mostrada1_final

label evidencia_mostrada1_final:
    $ quick_menu_gameplay=False
    pla "Well, I think I should go now."
    pla "See you Marissa..."
    stop music fadeout 1
    show marissa sorprendida:
        ease .5 mright
    show mary normal at mleft with dissolve
    play sound campana
    pla "...!" with flashbulb
    show mary hablando
    mary "Marissa Morestan..."
    mar "Whoa!" with hpunch
    mar "Pro- pro- Professor Harrow!"
    show mary normal
    mary "..."
    mary "[pla_name]? I didn't expect to see you here..."
    pla "Hello, Professor Harrow..."
    "Professor Harrow was at the entrance of the room. As always, with an intimidating aura..."
    "And I saw that Marissa suddenly became nervous, like a deer in the headlights of a car."
    "What's going on here?"
    show mary hablando
    mary "Marissa... come with me."
    mar "Aaaahhh!" with hpunch
    mary "Marissa."
    show marissa at brinquitos
    mar "Iiiihh!" with hpunch
    show mary normal
    "Marissa let out a strange wail, like a small animal, as the teacher walked further into the room."
    "The girl, who until recently had a friendly attitude, is now showing a nervous side."
    "This is what causes, Professor Harrow's wrath..."
    show marissa apenada at decaer
    "As if she had accepted a terrible fate, Marissa took her bag and head down, headed towards the exit."
    pla "Wait... Professor Harrow..."
    show marissa normal at reponerse
    pla "Why are you taking Marissa?"
    show mary hablando
    mary "I don't have to give details. It's none of your business."
    play music ambiente3 fadein 4
    show mary normal
    show marissa apenada
    mar "[pl_name]! Save meeeee!" with hpunch
    pla "..."
    pla "Professor Harrow..."
    pla "I'd appreciate it if you could tell me what's going on..."
    show mary hablando
    mary "I just have to talk to Marissa about her academic performance last year, that's all."
    show mary normal
    show marissa sorprendida
    mar "I- I- lie! You're only taking me because you're still angry about {amarillo}that stumble{/amarillo}!" with hpunch
    play sound campana
    pla "That stumble?" with flashbulb
    extend " You haven't told me, Marissa."
    # "Eso es algo que no me ha contado Marissa..."
    show marissa preocupada
    mar "Oh really? Uh i forgot..."
    "I should investigate more..."
    show marissa normal
    pla "Professor Harrow, I'd like to ask you a few questions."
    show mary sorprendida
    mary "Huh? What is this about?"
    pla "It's... because of my club's activities..."
    show mary normal
    "I made sure to keep my voice low as I said it."
    "Although anyway, I probably already look suspicious for trying to find out what happened between them..."
    mary "..."
    show mary pensando
    extend " I understand."
    mary "We can talk in the teachers' lounge."
    pla "Thank you so much..."
    stop music fadeout 2.5
    scene bg negro with dissolve
    pause 2
    scene bg salon maestros dia with fade
    show mary normal with dissolve
    # show marissa preocupada at mright with dissolve
    pla "So, could you tell me what happened the day of that \"stumble\"?"
    # hide marissa with dissolve
    # show mary:
    #     ease .5 center
    mary "Alright..."
    #reiniciamos corazones, si antes se acabaron corazones, al tratar de preguntar a marissa si tenia algo de valor, esto evitara que el interrogatorio se termine (por que corazones=0)
    $ initCorazones()
    jump caso1_testimonio2
