label caso1_inicio:

    $ dia="Thu."
    $ fecha="February 20"
    $ hora=16#4pm
    $ quick_menu=True
    window show
    # pause 1
    scene bg salon club detectives with dissolve
    play music ambiente2 fadein 4
    "It's been a day since we handed out the flyers..."
    "And no one has arrived yet..."
    "To kill time, I have dedicated myself to reading some novels about detectives."
    "In this room, there are some interesting novels..."
    show alice normal with dissolve
    pla "Uhm... So, {amarillo}the killer is the butler{/amarillo}?"
    "Having reached the climax of the story, I made my conclusion known to Alice."
    "According to her, I needed{nw}"
    play sound campana
    extend " {amarillo}\"deductive training\"{/amarillo}." with flashbulb
    "And Alice was the one who was teaching me..."
    show alice sonriendo
    ali "He, He, He... It is a common mistake to think so."
    pla "A mistake? But if it's clear that the butler is to blame..."
    show alice alegre
    ali "That was the intention of the writer."
    play sound campana
    ali "{amarillo}Do not let yourself be led by false leads.{/amarillo}" with flashbulb
    show alice sonriendo
    pla " False leads?"
    ali "Yes, the authors of mysteries {amarillo} tend to be very tricky.{/amarillo}"
    ali "True clues are not given much emphasis in the stories..."
    ali "And when you least expect it..."

    scene bg alice_objection with dissolve
    show alice_objection with dissolve

    ali "The detective points to the least suspicious person!"

    pla "So… that's the way it is?"
    pla "That sounds unfair..."
    ali "Well..."
    ali "It's just that a detective story where you know who the culprit is, would get boring..."
    ali "Though on second thought..."
    ali "The beauty of a mystery novel, {amarillo} is the mystery itself {/amarillo}. It is not always relevant to know who is to blame..."
    pla "I think I understand..."
    scene bg salon club detectives with dissolve
    show alice normal with dissolve
    pla "..."
    ali "This has been very calm..."
    pla "Yes, you are right."
    ali "..."
    show alice pensando
    ali "There has been no crime..."
    pla "Nor should one be happy because one happens."
    show alice normal
    ali "But... this is not what I want for the club..."
    ali "You think the flyer thing didn't work?"
    pla "Well, I didn't have much hope with that..."
    show alice sorprendida
    ali "Whaaat!?" with hpunch
    pla "Just look..."
    show alice normal
    pla "Several clubs have many activities to offer, without having to depend on anyone, that doesn't seems to be the case here."
    pla "This is a too passive club..."
    pla "I think we're on the same level as the literature club in terms of popularity."
    pla "No... maybe under them yet."
    show alice pensando
    ali "Uhh..."
    ali "That's dissappointing..."
    pla "It is what it is."
    pla "We have to think of an activity for the club..."
    pla "I don't know... something that has to do with the theme... that thing about deductions and things like that..."
    ali "Uhm..."
    ali "Uhhmm..."
    show alice asustada
    ali "UHHHMMMM...."
    show alice sorprendida
    play sound campana
    ali "Oh! A {amarillo}{i}escape room{/i}!{/amarillo}" with flashbulb
    show alice normal
    pla "Escape room? ...An escape room..."
    pla "What's that?"
    ali "It's a game, where you put a group of people in a big room or hall..."
    ali "And they will only be able to get out if they solve the puzzles they find."
    pla "Oh that's interesting..."
    pla "Reminds me of a movie..."
    "Even though that movie was gore..."
    ali "Although the complicated thing is the creation of the riddles..."
    show alice pensando
    ali "I've tried... but I'm not good at creating one that's challenging."
    pla "Uh me neither..."
    pla "If we had {amarillo} a person who likes riddles...{/amarillo}"
    show alice pensando
    ali "What if... {w=1}{nw}"
    show alice sorprendida
    pla "Denied."
    pla "I've already told you that we shouldn't commit a crime and then pretend to solve it."
    ali "Woah! You have read my mind!" with hpunch
    pla "You are so easy to understand..."
    show alice normal
    ali "..."
    ali "Oh!"
    ali "What if it's just a show?"
    ali "We could let the participants solve a fake crime, while we help them with clues."
    pla "Deni...oh...not a bad idea..."
    show alice sonriendo
    ali "He, he, he. I'm great right?"
    pla "But there is a problem."
    pla "If it was a faked crime..."
    pla "There would have to be suspects, right?"
    show alice normal
    ali "Yes. That's obvious."
    show alice sorprendida
    pla "And it is also obvious that we are only two people!" with hpunch
    ali "..."
    show alice pensando
    ali "Oh..."
    ali "We would need more people to do it right..."
    pla "That's how it is..."
    pla "But that's better than nothing... you have to make the effort."
    pla "We cannot sit idly by waiting for a case to fall from the sky..."
    show alice normal
    unk "Excuse me... is there anyone here?"
    pla "Uh?"
    hide alice
    show marissa normal with slow_dissolve
    "..."
    show marissa alegre
    mar "Oh! [pla_name], here you are!"
    pla "Marissa!?"
    show marissa:
        linear .5 mleft
    show alice normal at mright with dissolve
    ali "Do you know her, [pla_name]?"
    pla "Uh, yeah... I met her when I went to the cooking club..."
    show marissa normal
    mar "Hello... uh... Alice?"
    show alice sorprendida
    ali "Huh?" with hpunch
    show marissa alegre hablando
    mar "I'm Marissa, don't you remember? I think we met here a year ago."
    mar "The club helped my older sister in the case of a robbery..."
    show alice pensando
    ali "..."
    show alice sorprendida
    ali "Oh! The case of the gold necklace!"
    show marissa alegre:
        mleft
        brinquitos
    mar "Yes, that same one!"
    "A gold necklace? Wow, that must have been something serious..."
    pla "And what brings you here, Marissa?"
    show alice normal
    show marissa preocupada
    mar "..."
    extend " Can I close the door?"
    pla "Uh?"
    mar "I need help from you guys..."
    show alice alegre:
        mright
        brinquitos
    ali "Ah, a case at last!"
    mar "..."
    show alice pensando
    ali "S- sorry..."
    mar "Don't worry..."
    mar "So... Can I count on you?"
    stop music fadeout 5
    mar "It's something delicate what I'm going to talk about..."
    mar "And I don't want other people to listen to me..."
    "Alice and I exchanged glances, puzzled by Marissa's request."
    "Alice nodded, and then I went to the door to close it."
    ali "You can sit here..."
    show marissa sonrojada
    mar "Thank you."
    pla "So... what did you want to talk about?"
    show marissa preocupada
    show alice normal
    mar "..."
    show marissa apenada
    mar "Well... it's a bit confusing... I don't know where to start..."
    show marissa preocupada
    mar "..."
    mar "Ah... well... the thing is,{nw}"
    play sound campana
    extend " that {amarillo}I received a letter{/amarillo}..." with flashbulb
    show alice sorprendida
    ali "A- a letter?"
    ali "Oh! Is it someone who is blackmailing you?" with hpunch
    show marissa sorprendida
    mar "What?"
    mar "No no..."
    show alice normal
    show marissa preocupada
    play sound campana
    mar "{amarillo}It's a love letter.{/amarillo}" with flashbulb
    ali "..."
    pla "..."
    extend " a love letter?"
    play music ambiente2 fadein 10
    "Suddenly, I felt that all the tension in the air had vanished."
    show marissa preocupada
    mar "Yes. A love letter I received {amarillo}on Friday of the last week{/amarillo}."
    pla "Are love letters still being written today?"
    mar "So it seems..."
    show alice pensando
    ali "Uh... just that..."
    "Alice sounded very disappointed."
    show marissa apenada
    mar "Unfortunately, no."
    "Marissa pulled out a folded sheet of paper and handed it to me."
    mar "That's the letter..."
    scene carta_amor with dissolve
    "Alice came over to my side as I began to read the letter."

    #carta bla bla
    "{amarillo}\"Miss Mar... I am writing this letter to express the great love I feel for you [...]\"{/amarillo}"
    "{amarillo}\"From the first day I met you, I fell in love like a dreamy fool. [...]\"{/amarillo}"
    "{amarillo}\"I love that you are so intelligent and very responsible with what you do.\"{/amarillo}"
    "{amarillo}\"Being the upright and mature person that you are, I hope you come to...\"{/amarillo}"
    "After this it is mentioned that the addressee is invited to go to the cafe that is near the school at five in the afternoon."
    "And there are also many cheesy things that are not worth mentioning for now."

    scene bg salon club detectives with dissolve
    show marissa preocupada at mleft with dissolve
    show alice normal at mright with dissolve
    pla "..."
    pla "I'm no expert on the subject, but..."
    pla "What's wrong with this letter?"
    "Apart from being too cheesy."
    mar "Eh... it's about what it says at the end..."
    show marissa apenada
    mar "In the letter he would make an appointment with me at the {i} café {/ i} that is near the school."
    mar "But when I get to the place..."
    mar "I saw no one."
    mar "I was waiting for a long time, and in the end I left."
    show alice sorprendida
    ali "We-were you stood up?"
    show marissa apenada at decaer
    mar "So it seems..."
    show marissa at reponerse_rapido
    mar "Someone who wrote me that cheesy letter, had to stood me up..."
    show marissa alegre
    mar "Well, it's not like I minded that much, since I was thinking of turning him down..."
    ali "Wow! How direct!" with hpunch
    mar "..."
    show alice normal
    show marissa apenada
    extend " But if that had stopped there, I wouldn't be asking for help now."
    show marissa preocupada
    mar "..."
    # extend " I want you to find out who wrote that letter."
    # show alice sorprendida
    # ali "¿¡Uh!?" with hpunch
    # pla "But... ¿Didn't you say it doesn't matter to you?"
    # show alice normal
    # mar "That's right... but..."
    mar "Since I received that letter..."
    stop music fadeout 5
    mar "I feel that now{nw}"
    play sound campana
    extend " {amarillo}someone is stalking me.{/amarillo}" with flashbulb
    show alice sorprendida
    ali "Huh!? A stalker!?" with hpunch
    show marissa normal
    "So that was it..."
    play music tiempo_muerto fadein 5
    mar "So..."
    extend " I need help to discover {nw}"
    play sound campana
    extend "{amarillo}who was the person who sent me that letter.{/amarillo}" with flashbulb
    mar "I haven't talked about this {amarillo} with anyone, not even with the teachers...{/amarillo}"
    mar "I don't want this to get any further, that's why I ask you for help."
    mar "I know that this club can handle these matters very discreetly."
    "Although now in this club we are only a couple of rookies, and a chicken with a cap..."
    mar "So? Could you help me?"
    pla "Uh..."
    show alice alegre at brinquitos
    ali "Of course! Leave the case to us!"
    show alice normal
    pla "Wait..."
    pla "Marissa, so you just want to know who sent you the letter?"
    show marissa alegre hablando
    mar "Yes. Knowing who it was, I could talk to a teacher to fix this problem properly."
    "I get it, she wants solid evidence to accuse someone."
    show marissa alegre
    mar "You know, things are solved by talking."
    mar "Or by threatening them with someone of higher authority."
    # pla "..."
    pla "I understand..."
    show marissa alegre hablando at brinquitos
    mar "Thank you so much, I knew I could count on you!"
    pla "..."
    hide marissa with slow_dissolve
    show alice normal:
        ease 1.5 center
    ali "... what's wrong, [pla_name]?"
    pla "And what are we going to do now?"
    show alice sorprendida
    pla "You should have some experience in this..."
    show alice pensando
    ali "Uh... well, although it may not seem like it, I'm not popular with guys, so I haven't received any love letters, or anything like that..."
    show alice sorprendida
    pla "Not that!" with hpunch
    pla "I mean, what should we do after accepting a case."
    show alice alegre
    play sound campana
    ali "Oh! That, heh, heh... right..." with flashbulb
    ali "..."
    show alice normal
    extend " ok..."
    ali "First of all, in an investigation it is essential to have a record of the things that are discovered."
    show alice sonriendo
    ali "Wait for me a moment..."
    hide alice with dissolve
    pause 1
    "Alice immediately went to look for something among the drawers of a table."
    "..."
    show alice sonriendo with dissolve
    ali "Here you have."
    play sound notify
    $ renpy.notify("You have received a notebook")
    $ quick_menu_btn_notepad=True
    pause 1.2
    ali "{amarillo}Here you can write down all the clues that you discover...{/amarillo} or whatever you can think of."
    if renpy.variant("pc"):
        show text "{font=gui/fonts/fontawesome.ttf}{size=70}{/size}{/font}":
            xpos 0.750 ypos 0.7
            alpha 0
            linear .8 alpha 1
            block:
                ease .5 yoffset -20
                ease .5 yoffset 0
                repeat 4
            linear .8 alpha 0
    "Alice handed me a notebook and a pen."
    if renpy.variant("pc"):
        hide text
    pla "I understand..."
    hide alice with slow_dissolve
    "Well... the first thing would be to write down what we know so far..."
    tuto "Hello, this is a {nw}"
    play sound campana
    extend " {amarillo}tutorial message.{/amarillo}" with flashbulb
    $ addNote("Marissa Morstan (profile)","Marissa Morstan is a member of the cooking club. She is a very friendly and sociable person, she is also the one who has asked Alice and me to identify the person who is stalking her. That same person also delivered a love letter to her.","marissa")
    tuto "You will be notified every time the {amarillo} notepad is updated.{/amarillo}"
    tuto "You can check it at any time."
    tuto "In addition, this notebook will be used when conducting a {amarillo}interrogation{/amarillo} or even in a {amarillo}school debate.{/amarillo}"
    # tuto "It will even be useful to consult it when you are in the middle of a {amarillo}school debate.{/amarillo}"
    tuto "We'll cover the {amarillo}gameplay{/amarillo} later."
    show alice normal with dissolve
    pla "Done... and what's next?"
    ali "Let's see..."
    ali "Now it's time to listen to the {amarillo}testimony{/amarillo} of our \"client\" about how the events happened, and ask questions to {amarillo}get clues.{/amarillo}"
    pla "I see..."
    show alice:
        ease .5 mright
    show marissa preocupada at mleft with dissolve
    pla "Marissa, then you can tell us about your case in detail."
    show marissa alegre
    mar "Sure..."
    mar "I guess I'll start telling you from the beginning of the day {amarillo} when I received the letter.{/amarillo}"
    show marissa preocupada
    mar "But before that..."
    show marissa apenada
    extend " I would like to drink some water."
    show marissa alegre at brinquitos
    stop music fadeout 3
    mar "I feel like I'll talk too much heh heh heh..."
    pla "Sure..."
    # scene bg negro with slow_dissolve
    # stop music fadeout 3
    # pause 2

    jump caso1_testimonio1
