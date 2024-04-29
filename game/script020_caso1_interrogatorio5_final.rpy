label caso1_interrogatorio5_final:

    $ fase_titulo.append("Neil's interrogation")
    $ fase_tipo_vida.append("amount")
    $ fase_corazones.append(cantidad_corazones)
    $ fase_multiplicador.append(10)

    $ estadoj="Recess"
    pla "So… {amarillo}nobody caught your eye, huh?{/amarillo}"
    show neil pensativo
    nei "Uh...yeah... A-any prob-problem with that?"
    hide neil with dissolve
    show alice sorprendida with dissolve
    ali "He stuttered!" with hpunch
    pla "Yes... it becomes clear that he is attracted to Marissa..."
    pla "I have an idea."
    ali "Huh?"
    pla "Just play along..."
    ali "U-understood..."
    show alice normal:
        ease .5 mright
    show neil pensativo at mleft with dissolve
    play music ambiente3 fadein 3
    pla "Hey Neil, that girl is very grateful for your help..."
    show neil sorprendido
    nei "Whaaat!?" with hpunch
    extend " Se-seriously?"
    pla "Yes, and a lot... she was surprised to find out that chivalrous men still exist..."
    show neil sonriendo hablando
    nei "Heh-heh-heh... I just did what a man had to do..."
    show neil normal
    pla "I happen to know that girl, her name is Marissa."
    show neil sonriendo hablando
    nei "Marissa? Heh heh, she has a cute name."
    pla "Yes, anyway... she asked me to get your cell phone number."
    show neil sorprendido
    nei "Whaaaaat!?" with hpunch
    show neil sonriendo hablando at brinquitos
    nei "Heh, heh, heh... I- I see..."
    show neil normal
    nei "Okay, I guess I should give you my number, heh heh heh..."
    pla "You can write it down here."
    "I offered Neil my pen and notepad."
    $ addNote("Neil's number","Neil has written his cell phone number on my notepad in his own hand. He wrote his number immediately after I told him that Marissa was interested in calling him, this makes me think that Neil is interested in her...{p}{p} Uhm... I don't see that tremor that I saw in the letter...","numneil",True)
    nei "Well, here you have it."
    pla "..."
    nei "The recess will soon be over. I have to go."
    show neil sonriendo hablando
    nei "I'll be waiting for her call."
    nei "Hehehe..."
    hide neil with dissolve
    stop music fadeout 4
    show alice normal:
        ease .5 center
    ali "He has left in a very good mood..."
    show alice sorprendida
    ali "...!" with hpunch
    show alice enojada
    ali "[pl_name]!" with hpunch
    ali "Why did you tell him that Marissa wanted his number!?"
    pla "For this..."
    show alice sorprendida
    "Along with my answer, I showed Alice my notepad."
    ali "So, you wanted Neil's number!?" with hpunch
    show alice pensando
    ali "[pla_name], I didn't know you had those tastes..."
    show alice sorprendida
    pla "You're wrong!" with hpunch
    show alice normal
    ali "So?"
    pla "I asked Neil to write down his cell phone number, {nw}"
    play sound campana
    extend " {amarillo}and with that I found out that Neil is left-handed!{/amarillo}" with flashbulb
    ali "..."
    show alice sorprendida
    ali "Oh! {amarillo} In the stalker's profile we found out that he is left-handed! {/amarillo}"
    pla "Shhh don't say it so loud..."
    $ updateNote("Neil London (profile)",ndesc="\n\nI found out that Neil is left-handed.",add=True)
    show alice alegre at brinquitos
    ali "You're great, [pla_name]!"
    show alice sonriendo

    play music ambiente2 fadein 3
    ali "Uhm... we've come a long way... we should be able to come up with a solution by now."
    show alice alegre at brinquitos
    ali "According to my experience, it's about time to perform{nw}"
    play sound campana
    extend " {amarillo}a school debate.{/amarillo}" with flashbulb
    pla "School debate?"
    show alice sonriendo
    ali "When my superiors had a case where there was a lot of information that didn't seem to fit..."
    ali "They held a debate with almost everyone involved in the case."
    show alice normal
    ali "First, a question was established, and then the members of the debate {amarillo} began to give ideas one by one.{/amarillo}"
    ali "And we also expressed our opinions..."
    ali "In the end, the contradictions surfaced."
    ali "And so we managed to have new important clues to solve the case."
    show alice alegre
    ali "And even... my superiors sometimes caught the culprit in the same debate!" with hpunch
    pla "Uhh..."
    pla "That's a good idea... we need to do something like that."
    show alice sonriendo at brinquitos
    ali "Yeah, it's something that the founder of the club came up with."
    ali "He is a very smart and cunning person."
    pla "..."
    pla "So in that debate, everyone should be involved..."
    show alice pensando
    ali "Yes… we have Marissa, Professor Harrow, Beck, Neil and us..."
    show alice normal
    ali "In total we are six people."
    pla "Is it necessary for everyone to be in the debate?"
    ali "There's no need."
    ali "But if it is established that his presence is important, we would have to call him."
    show alice pensando
    ali "Of course, when we were a recognized club... we had permission from the school management {amarillo}to force any student to join the debate.{/amarillo}"
    pla "Uh... I see..."
    pla "We have to work with what we have..."
    pla "We will have to notify everyone in advance, that maybe we could need to call them to go to the club room..."
    show alice normal
    ali "Yes, you have to prepare everything in time."
    ali "I could take care of cleaning the club room, since it is somewhat messy..."
    pla "Anyway, we'll talk about it more calmly, now I want to go to the cafeteria before the recess is ov..."
    stop music
    play sound campana_escuela
    show alice sorprendida
    pause 4
    ali "The recess has already ended."
    show alice alegre
    ali "See you, [pla_name]!"
    hide alice with dissolve
    pla "Huh!?" with hpunch
    pla "Ah... I feel like I'm going to starve to death..."
    stop music fadeout 3
    scene bg negro with dissolve
    "I sent Marissa a message, summarizing what Alice and I have come up with, and also told her that we would have a discussion tomorrow."
    "She didn't take long to answer, saying that it would be fine for her."

    scene bg negro with slow_dissolve
    hide screen quick_menu
    $ quick_menu=False
    window hide
    pause 2
    $ hora=17
    $ estadoj="Free"
    $ quick_menu=True
    window show
    scene bg escuela edificio principal corredor with dissolve

    play music ambiente fadein 2
    "It's five o'clock in the afternoon."
    "After classes ended, I went to the club room, to arrange with Alice all the necessary to hold a debate."
    "And then, I was passing the main school building, when..."
    show beck sonriendo with dissolve
    pause 1
    pla "Beck?"
    "I ran into Beck, {amarillo}, who had come out of the teachers' lounge.{/amarillo}"
    show beck sorprendido
    bec "Huh? [pla_name]?"
    show beck sonriendo
    bec "What's up? How's the investigation going?"
    pla "Uh... well moving on... hey, were you talking to Professor Harrow?"
    show beck sorprendido
    bec "Hey!? How do you know!?" with hpunch
    pla "Ah... I just said the first thing that came to my mind..."
    hide beck with dissolve
    show mary normal with dissolve
    "And I also saw Professor Harrow..."
    mary "[pla_name]? What a miracle to see you at this hour at school..."
    pla "Yes, I've been a bit busy with club activities."
    show mary pensando
    mary "..."
    mary "I hope you're not forgetting that you have homework to do for tomorrow."
    pla "Of course I haven't forgotten!" with hpunch
    "To tell the truth, I had forgotten, thinking too much about Marissa's case..."
    mary "Ok then, I'm leaving."
    show mary normal
    mary "See you tomorrow, [pla_name]."
    hide mary with dissolve
    show beck sorprendido with dissolve
    bec "..."
    extend " ..."
    extend " ..."
    bec "Am I imagining things, or did you just have a casual chat with Professor Harrow!?" with hpunch
    pla "Uhm... yeah... I guess did..."
    show beck pensando
    bec "How can you talk so calmly with Professor Harrow?"
    pla "Well... uh... she's like a friend of my family..."

    pla "Professor Harrow has been watching my grades ever since I entered this school."
    show beck sorprendido
    bec "Professor Harrow is a friend of your family?"
    show beck pensando
    bec "Oh... how lucky you are..."

    pla "Lucky?"
    pla "I don't think I feel very lucky about it..."
    bec "Oh… how much {amarillo} would I like to receive that kind of attention from Professor Harrow...{/amarillo}"

    pla "What?"
    show beck sorprendido
    bec "Huuuh!? No-no, nothing..." with hpunch
    show beck sonrojado

    bec "..."
    pla "..."

    bec "What? Don't look at me like that..."
    menu:
        "Keep Staring at Beck":
            bec "..."
            show beck pensando
            bec "Sorry [pla_name], but I don't play on that side, I'm only interested in women."
            $ updateStat("charisma","+",2)
            $ renpy.notify("Charisma +2")
            pla "What!? I'm not gay..." with hpunch
            bec "If you say so..."
            "Oh dear..."
        "Keep talking":
            $ updateStat("charisma","-",1)
            $ renpy.notify("Charisma -1")

    show beck preocupado
    bec "Hey... do you happen to know if she has a boyfriend?"
    pla "Are you asking me if Professor Harrow has a boyfriend?"
    show beck sorprendido
    bec "It's not what you think!" with hpunch
    show beck pensando
    bec "I was just thinking out loud, I'm just curious."
    bec "If a person like her has a partner..."
    bec "..."











    show beck sonriendo
    bec "So? Does Professor Harrow have a boyfriend?"
    pla "Well... not that I know of."
    show beck sorprendido
    bec "..."
    show beck sonriendo
    bec "Great!"
    show beck pensando
    bec "Ahem! I mean interesting..." with hpunch
    "Beck seriously sucks at lying..."
    show beck guino
    bec "Well I have to go. See you, [pla_name]!"
    hide beck with dissolve
    "Wasting no time, Beck ran away..."
    $ updateNote("Beck Doran (profile)",ndesc="\n\nI have a suspicion that Beck is in love with Professor Harrow. Wow... who would have thought...",add=True)
    "Should I tell him that Professor Harrow is only interested in intelligent men?"
    "Uhmm... nah. I'm tired, I want to go home now."
    stop music fadeout 2
    scene bg negro with slow_dissolve
    hide screen quick_menu
    $ quick_menu=False
    window hide
    pause 2
    $ dia="Tuesday."
    $ hora=14
    $ fecha="February 25"
    $ quick_menu=True
    window show
    play music ambiente2 fadein 3
    scene bg salon club detectives with dissolve

    jump caso1_predebate
