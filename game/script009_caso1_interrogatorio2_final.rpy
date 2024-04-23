label caso1_iterrogatorio2_final:
label caso1_iterrogatorio2_final:

    $ fase_titulo.append("Interrogation of Prof. Harrow")
    $ fase_tipo_vida.append("amount")
    $ fase_corazones.append(cantidad_corazones)
    $ fase_multiplicador.append(10)

    stop music fadeout 2
    hide screen interrogatorio_btns
    $quick_menu_gameplay = False
    $hide_gameplay_layout()
    $estadoj="Free"
    pla "Thank you very much Professor Harrow."
    $ addNote("Professor Harrow (profile)","A strict and very responsible person with her work, that's Professor Mary Harrow. Also, she likes order and efficiency.{P}{p}When she gets angry, she is very scary. I've known her for a long time since she's a friend of my family, so I've gotten used to her intimidating look.","Mary")
    pla "I think that's all I needed to know."
    show mary pensando
    mary "I understand."
    show mary hablando
    mary "Fine, you should go now. I have to talk to Marissa..."
    show mary:
        ease .5 mleft
    show marissa apenada at mright with dissolve
    mar "Oooooooooooooooooo..." with hpunch
    "Poor Marissa..."
    scene bg escuela edificio principal corredor with fade
    "This is getting more and more confusing..."
    "Now, new details have emerged... and {amarillo}a suspect...{/amarillo}"
    "Can we solve this mystery?"
    if numero_alice_obtenido:
        "By the way..."
        "How will Alice have fared?"
        "I haven't heard from her."
        "I sent her a message telling her that I found new leads of the case, but she hasn't replied to me..."
    "The break time will soon be over..."
    "When classes are over I will go to the club."
    scene bg negro with slow_dissolve
    hide screen quick_menu
    $ quick_menu=False
    window hide
    pause 2
    $ hora=14
    $ quick_menu=True
    window show
    scene bg escuela corredor clubes dia with dissolve
    pause 2
    "To my surprise, I found the detective club room completely closed."
    if numero_alice_obtenido:
        "I've been banging on the door, but no one has answered."
        "I also dialed Alice but she did not answer."
    "Where could she be?"
    show hatty sonriendo with dissolve
    pause 1
    "..."
    play music ambiente fadein 4
    hat "Huh!? You are..."
    hat "That boy from the other time."
    pla "Hello."
    show hatty alegre
    hat "Hey what's up! What are you doing in the front of the literature club?" with hpunch
    pla "What?"
    show hatty pensando
    hat "What's with that confused face?"
    pla "Um... Hatty, this is the detective club..."
    show hatty asustada
    hat "Huh!?" with hpunch
    hat "I have made a mistake..."
    show hatty pensando at decaer
    hat "Where can she be..."
    show hatty at reponerse
    pla "Who are you looking for? If it can be known..."
    hat "I'm looking for my sister..."
    hat "She had told me that she was going to the literature club to fill out a form..."
    "Uh..."
    hat "Ah... what a nuisance, I just have to tell her that I'll be late home..."
    "Hatty began to mutter to herself, as she looked at her cell phone."
    hat "Just today {nw}"
    play sound campana
    extend " {amarillo} the telephone network also had to go down...{/amarillo}" with flashbulb
    "Huh?"
    show hatty sonriendo
    hat "What's wrong, [pla_name]?"

    menu:
        "\"It's nothing\"":
            $ updateStat("intel","-",1)
            $ renpy.notify("Intelligence -1")
            pla "It's nothing."
            hat "Uhm... ok..."
        "\"Is the phone network down?\"":

            $ updateStat("intel","+",1)
            $ renpy.notify("Intelligence +1")
            pla "Is the phone network down?"
            hat "That's how it is..."

    show hatty pensando
    hat "Don't you find it curious?"
    play sound campana
    hat "{amarillo}On Friday of last week the network was also down.{/amarillo}" with flashbulb
    pla "It's that so? On Friday of last week..."
    pla "So you can't call your sister?"
    show hatty molesta
    hat "Yes... although the tone sounds, the calls do not connect, the internet does not work, nor can I send text messages..."
    pla "So you couldn't call or text last Friday either?"
    hat "Yes... that's why it's funny, today is also Friday..."
    hat "And the problem lasted all day, surely today is the same..."
    $ addNote("Phone network problems","On Friday of last week (when Marissa received the letter), and also on Friday the 21st, the phone network was down. Therefore it has been impossible to call or send messages from the cell phone in those days.")
    pla "I see... I hadn't noticed."
    show hatty sonriendo
    hat "Huh? Why are you noting that down?"
    pla "Uh, well... I'm in the middle of an investigation..."
    hat "An investigation?"

    # pla "¿Estás buscando a tu hermana?"
    # hat "Sí. Ella se unió al club de literatura, y pensé que este era el salón."
    # pla "Sí estás buscando ese club, está allá..."
    # "Le señalo a Hatty a donde tiene que ir."
    # hat "Oh, ya veo... gracias."
    # hat "..."
    # hat "Así que este es el club de detectives..."
    # hat "¿Qué pasa? ¿No hay nadie adentro?"
    # pla "Eso parece..."
    # hat "¿Y qué me cuentas del club?"
    # "¿Eh? Parece que ella está interesada en el club..."
    # pla "Uhm... bueno..."
    # pla "Estamos en medio de una investigación."
    # hat "Ooohhh..."

    hat "And who are you investigating?"
    pla "I can't tell you. It is confidential information."
    show hatty molesta
    hat "Uhh..."
    extend " now I'll be curious."
    pla "Well, if you're willing to know, you're always welcome at the club."
    pla "We are looking for new members."
    hat "Uh..."
    show hatty alegre at brinquitos
    hat "Interesting. I'll keep it in mind. He he."
    show hatty pensando
    hat "..."
    hat "Hey... [pla_name]... I'm embarrassed to say it... but..."
    hat "Where is the literature club?"
    "Wow, her sense of direction is terribly wrong..."
    pla "Well, the literature club is in the first room of this corridor..."
    hat "Oh, I've gone too far then..."
    show hatty alegre
    hat "Well, see you [pla_name]."
    hide hatty with dissolve
    # "Y al final, Hatty se fue con los ánimos decaídos..."
    "That girl needs to have a map all day..."
    # "..."
    "Uhm... what should I do..."
    if numero_alice_obtenido:
        "Since Alice hasn't answered me, I have nothing to do here..."
    "There is still time."
    "And with what I've discovered so far..."
    play sound campana
    "It would be a good idea to talk to {amarillo}Beck Doran.{/amarillo}" with flashbulb
    "If anyone knows about stalkers, it's probably him."
    $ quick_menu_btn_notepad=False
    $ addstate=True
    label beck_esta_en_club_de:
        "If I'm not wrong... Beck is in the club of..."
        menu:
            "Sports":
                "No...That's for sure, but from a specific sport..."
                $ addstate=False
                jump beck_esta_en_club_de
            "Baseball":
                "No... That's not..."
                $ addstate=False
                jump beck_esta_en_club_de
            "Soccer":
                if addstate:
                    $ updateStat("intel","+",1)
                    $ renpy.notify("Intelligence +1")
                $ quick_menu_btn_notepad=True
                "The football club..."

    "So... probably at this hour... Beck would be on the school field..."
    "Ok, let's go there..."
    stop music fadeout 5
    scene bg escuela campo deporte tarde with slow_dissolve
    "Arriving at the school field, I noticed that there was a game in progress..."
    play music partido_futbol fadein 6
    "..."
    "Huh!?" with hpunch
    "Examining the place, I saw that someone was hiding behind a tree."
    "Uh..."
    "With cautious steps, I approached that tree..."
    "And the surprise was..."
    stop music fadeout 2
    show alice sorprendida
    ali "...!" with hpunch
    pla "Alice?"
    ali "Aaahh!" with hpunch
    play music ambiente3 fadein 3
    ali "[pla_name]? Wha- what are you doing here?"
    pla "That's what I should ask..."
    pla "What are you doing hiding here? You look like a stalker..."
    show alice asustada
    ali "Oh! Of course not!" with hpunch
    ali "I am investigating!" with hpunch
    pla "Investigating what?"
    show alice pensando
    ali "To all those people..."
    show alice normal
    ali "Marissa had said that she came to school on Saturday, right?"
    show alice pensando
    play sound campana
    ali "{amarillo}Well, that day there was a soccer game.{/amarillo}" with flashbulb
    show alice normal
    pla "Oh really? I had no idea..."
    show alice pensando
    ali "Yes... I remembered that one of my superiors was a soccer fanatic, and he said that here they play school league games on the weekends."
    show alice normal
    ali "So I thought the stalker would often come onto the field..."
    $ addNote("Field on weekend","On the weekends, school league games are played at the school, that's what Alice told me.")
    pla "..."
    pla "Not bad..."
    ali "And why did you come here?"
    # pla "¿No has recibido mi mensaje? Te lo envié en la hora de receso."
    # ali "Uhm... no... no he recibido nada."
    # "Me lo imaginaba, entonces la red telefónica realmente está fallando..."
    pla "In my case, I came here to try to talk to a stalker expert."
    show alice sorprendida
    ali "Huh!?" with hpunch
    ali "A stalker expert?"
    pla "Have you seen all those girls in the audience?"
    unk "That, come on! We have to win!"
    unk "Aahh! Beck! Score another goal!"
    show alice normal
    ali "Uh... yeah..."
    "Even though this seemed to be a practice match, there were several girls cheerleading…"
    pla "Well, when I went to Marissa's classroom, I found out that one of her classmates is often stalked by women."
    show alice sorprendida
    ali "Oh really!?" with hpunch
    pla "Yes, his name is Beck Doran... the same one with the ball..."
    pla "I thought it would be a good idea to talk to him about the case."
    ali "You're sure?"
    ali "Marissa didn't want too many people to find out about her problem..."
    pla "I know... But I think we can get more information if we talk to him."
    show alice normal
    ali "Uh...well, okay."
    "..."
    ali "..."
    show alice sorprendida
    pla "Do you plan to stay there?"
    ali "Well yes..."
    pla "Let me tell you, that makes you look very suspicious."
    pla "Come on, let's watch the game for a while."
    ali "..."
    show alice sonrojada
    ali "... Alright..."
    if not numero_alice_obtenido:
        pla "Hey, Alice... I think we should exchange numbers."
        show alice sorprendida
        ali "Huh!?"
        show alice sonrojada
        ali "The truth… is that I was thinking about that too..."
        pla "Great."
        "Alice and I exchanged numbers."
        "Even if the phone network is failing today, it is always good to have the number of your colleagues."
    stop music fadeout 4
    scene bg negro with dissolve
    pause 1.4
    $hora=15
    scene bg escuela corredor afuera tarde with dissolve
    pause 1
    "After the match ended, Alice and I kept a close eye on where Beck was headed."
    "We waited for the opportune moment to speak with him."
    "Beck had already left some locker rooms that were near the field."
    "And when nobody was around anymore, that's when we got closer."
    show beck serio with dissolve
    pause 1
    show beck sorprendido
    bec "Hey?"
    pla "Hi Beck..."
    bec "You are... the boy who was talking to Marissa..."
    bec "What was your name?"
    pla "[pla_name]. And this girl who is accompanying me is Alice Baskerville."
    bec "Who?"
    show alice pensando at right with dissolve
    "I saw that Alice was hiding behind me."
    bec "What's wrong? It seems to be scared..."
    pla "Alice... come on, stop hiding..."
    ali "Uh..."
    show beck:
        ease .5 mleft
    pause .5
    show alice:
        ease .5 mright
    ali "{size=25}H- hello...{/size}"
    show beck pensando
    bec "So? What do you want?"
    show beck guino
    bec "Don't tell me... you regretted it and now you want to join the soccer club?"
    pla "Uh no. I already have a club."
    play sound campana
    pla "Alice and I are from the detective club." with flashbulb
    show beck sorprendido
    bec "Whaat!?" with hpunch
    bec "B-but... weren't you about to join Marissa's club?"
    pla "It was just an excuse to investigate."
    bec "Investigate?"
    bec "Wh- what are you investigating?"
    pla "We can't tell you. It's confidential."
    hide alice with dissolve
    show beck pensando:
        ease .5 center
    bec "Uh... well, I haven't gotten into any trouble, so bye..."
    pla "Wait!" with hpunch
    pla "It's not a case involving you. But you could have been {amarillo}witness to something...{/amarillo}"
    show beck sorprendido
    bec "Huh?"
    pla "We want to know what happened {amarillo} on Friday of last week.{/amarillo}"
    bec "On Friday?"
    pla "I just need to ask you a few questions, it won't be long."
    bec "..."
    show beck pensando
    bec "Well... and what do you want to know?"
    pla "To begin with, could you tell us what happened that day?"
    bec "Uh... I'm not comfortable with this..."
    show beck preocupado
    bec "Will I get in trouble if I say something wrong?"
    pla "I doubt it... we just want to know more about that day."
    show beck pensando
    bec "..."
    extend " alright."
    pla "Thank you so much."
    bec "Ok... let's see..."
    jump caso1_testimonio3
    
