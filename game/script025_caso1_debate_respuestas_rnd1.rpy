label d1r1_incorrecto_marissa:
    jump d1r0_incorrecto_marissa

label d1r1_incorrecto_alice:
    $ change_cursor()
    $ clearDebateText()
    $ quick_menu_bajo=False
    show alice enojada
    ali "[pla_name]..."
    $ restCorazones()
    ali "Don't contradict me, I know there's something else we found out about the author of the letter..." with hpunch
    show alice pensando
    ali "But I don't remember exactly what it is..."
    jump inicio_d1r1

label d1r1_correcto:
    stop music fadeout 1
    $ clearDebateText()
    $ change_cursor()
    $ addCorazones()
    $ showplay_excl("that'strue")
    $ quick_menu_bajo=False
    # $quick_menu_gameplay = False
    hide screen debateArgumento
    $ hide_gameplay_layout()
    play music tiempo_muerto fadein 2
    pla "Yeah, we found another lead."
    play sound campana
    pla "{amarillo}The author of the letter is left-handed.{/amarillo}" with flashbulb
    show marissa preocupada sudor
    mar "He's left-handed? Wow, that does help to identify him..."
    mar "I'm curious, how did you know?"
    show marissa normal
    pla "I noticed the slant of the lettering."
    pla "Right-handed people do not leave that kind of inclination when writing."
    show marissa:
        ease .5 mleft
    show alice sorprendida at mright with dissolve
    ali "Oh, right!"
    ali "I forgot to say it..."
    show alice pensando
    ali "It's just that Marissa started saying a lot of things and I got nervous..."
    show marissa preocupada sudor
    mar "Huh!? S- sorry..."
    show marissa preocupada
    mar "I was kind of excited..."
    ali "..."
    pla "Anyway, if the author of the letter is left-handed, that would also explain the stains on the paper."
    mar "The hand with which he writes would pass over the fresh ink..."
    show marissa alegre hablando at brinquitos
    show alice normal
    mar "Wow! That is incredible! Just as expected from the detective club!"
    show alice sonrojada
    ali "..."
    "For a moment, I saw a slight smile on Alice's face..."
    show alice normal
    pla "And with this clue, the list of suspects would be narrowed down a lot..."
    "Although that's not enough..."
    show marissa normal
    mar "Well, now we are clear about the personality and a special characteristic of the person in question..."
    mar "But… I do not understand."
    mar "How a person who wrote a letter with nerves and also felt insecure..."
    mar "Got to the point of stalking me?"
    show alice pensando
    ali "..."
    pla "Honestly, that's something we can't understand..."
    pla "Marissa, when you asked us for help, you said to be discreet on this one..."
    show alice normal
    show marissa preocupada
    mar "That's right, I wouldn't want this to spread like a rumor..."
    pla "Uh, yeah... but I think we need to get other people involved."
    show alice normal
    mar "Yeah?"
    pla "You know, I'm thinking Beck could help us better understand this stalker."
    mar "..."
    stop music
    play sound campana
    show marissa preocupada sudor
    mar "Oh! Beck has {amarillo}experience dealing with stalkers{/amarillo}!" with flashbulb
    mar "..."
    show marissa alegre
    mar "No problem!"
    show marissa alegre hablando
    mar "I've known Beck for the past year, and I'm sure he's not someone who goes around starting rumors."
    mar "And he can understand how I feel about it..."
    pla "Perfect then, I'll go for him."
    $quick_menu_gameplay=False
    scene bg negro with dissolve
    "I ran towards the school field, it didn't take me long to find Beck, who was on the side of the field chatting with some friends."
    "I told him that we needed his help to solve Marissa's problem."
    "And he agreed to go with me to the club room."
    play music ambiente fadein 3
    scene bg salon club detectives with dissolve
    show beck preocupado with dissolve
    pause 1
    show beck:
        ease .5 mleft
    show marissa alegre hablando at mright with dissolve
    mar "Hi Beck."
    bec "Hey Marissa..."
    bec "[pla_name] was telling me along the way..."
    bec "About how you got a love letter, and after that you started getting stalked..."
    show marissa normal
    mar "Yeah... that's right..."
    show beck pensando
    bec "Marissa, you should have asked me for help."
    bec "It can be dangerous to deal with a stalker."
    mar "I know..."
    mar "But that's why I asked the detective club for help."
    mar "I know from experience that they are discreet, besides..."
    mar "I only asked that the stalker be identified."
    mar "With enough evidence I will ask a teacher, even the principal, for help."
    bec "..."
    bec "Well... Getting to that point..."
    show beck preocupado
    bec "And do you have any suspect?"
    "Marissa's and Beck's gazes flicked to me, then to Alice, searching for answers…"
    show beck sorprendido
    show marissa sorprendida
    pla "Uh... well, we do have a suspect..."
    bec "Oh really!?"
    bec "Who is it?"
    show beck preocupado
    show marissa normal
    pla "I would prefer not to say it for now, not until I have enough information."
    pla "And that's why I called you."
    show beck:
        ease .5 left
    show marissa:
        ease .5 center
    show alice pensando at right with dissolve
    ali "I- I agree with [pla_name]..."
    ali "The best thing is not to launch accusations without a solid base..."
    ali "T- that's what my superiors taught me..."
    bec "Hum..."
    show alice normal
    bec "Well... and what do you need to know?"
    pla "About your experience."
    show beck sorprendido
    bec "My experience?"
    pla "We all know that you are someone very popular."
    pla "A person who is constantly in the company of other people..."
    pla "I think in this room, you're the only one who has experience dealing with stalkers."
    show beck pensando
    bec "..."
    # bec "¡Ah, cierto!"
    bec "So I'm the expert in being stalked..."
    bec "I don't like how it sounds..."
    show beck guino
    bec "But you're right."
    $ quick_menu_gameplay=True
    $ renpy.choice_for_skipping()
    $ renpy.save("checkpoint")
    bec "Well, it's time for the voice of experience to speak."
    jump caso1_debate_rnd2
