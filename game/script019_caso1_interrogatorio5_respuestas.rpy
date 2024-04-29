label int5f0:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "To the library?"
    pla "What would you go to do at the library, if at that time there were still classes?"
    show neil pensativo
    nei "It turns out that I had been oriented to bring some books from the library, so I happened to pass through the corridor at that moment."
    "Uhm... There is nothing relevant in what he has said..."
    jump caso1_testimonio5_inicio

label int5f1:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    # pla "Oye Neil..."
    pla "Did you happen to know that girl?"
    nei "..."
    nei "Well… no."
    show neil sonriendo hablando
    nei "{amarillo} It was the first time I saw her... {/amarillo}"
    hide neil with dissolve
    show alice normal with dissolve
    ali "..."
    pla "What's wrong Alice?"
    show alice pensando
    ali "I don't know if I was imagining things..."
    show alice normal
    play sound campana
    ali "But his {amarillo}eyes lit up when you mentioned Marissa.{/amarillo}" with flashbulb
    pla "You're right..."
    hide alice with dissolve
    show neil normal with dissolve
    # nei "¿Qué pasa? ¿De qué están hablando?"
    # pla "Neil..."
    # nei "¿Sí?"
    # pla "Sabes, esa chica a la que ayudaste,{nw}"
    # play sound campana
    # extend " {amarillo}se llama Marissa.{/amarillo}" with flashbulb
    # show neil sorprendido
    # nei "¡...!"
    # nei "¿Ma- Marissa?"
    # show neil sonriendo hablando
    # nei "Es un lindo nombre... je, je, je..."
    # pla "Dime, ¿qué opinas de ella?"
    # show neil pensativo
    # nei "¿De esa chica?"
    # nei "Pues no la conozco..."
    # show neil sonriendo hablando at brinquitos
    # nei "Pero ella es realmente linda... je, je..."
    # "Esto afirma lo que tengo apuntado..."
    jump caso1_testimonio5_inicio

label int5f2:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "What exactly did you do?"
    show neil sorprendido
    nei "What do you mean?"
    nei "What else was I going to do? Obviously I went to help them."
    show neil normal
    nei "I picked up the papers on the floor."
    nei "I don't think any further explanation is needed."

    $ restCorazones()
    pla "I shouldn't have asked something so obvious..." with hpunch
    jump caso1_testimonio5_inicio

label int5f3:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "Where did you go?"
    nei "Have you forgotten what I said?"
    show neil serio hablando
    nei "To the library. Is it a detective's job to ask such obvious questions?"
    hide neil with dissolve
    show alice enojada
    ali "[pl_name]!"
    $ restCorazones()
    pla "I know... my mistake..." with hpunch
    hide alice with dissolve
    jump caso1_testimonio5_inicio

label int5f4:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "Is that so?"
    show neil pensativo
    nei "Uh... are you calling me a liar?"
    if not interr_frase4_refutada:
        pla "No no! Do not misunderstand." with vpunch
        pla "I just meant that... Maybe you did see someone else at that time..."
        nei "Oh really?"
        show neil sonriendo hablando
        nei "Well, if you're so sure... {amarillo}tell me who.{/amarillo}"
        show neil normal
        nei "I don't remember no-one else."
        "I should have {amarillo}something to prove...{/amarillo} that Neil {amarillo}did saw someone else...{/amarillo}"
    else:
        "There is no point, there is nothing more to ask here."
    jump caso1_testimonio5_inicio

label int5f5:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")
    pla "Seriously no one caught your attention?"
    nei "Well, that's what I said."
    $ restCorazones()
    nei "Next question." with hpunch
    "I must be more direct..."
    "{amarillo}Neil had to be interested in someone{/amarillo} when the crash happened, but who?"
    jump caso1_testimonio5_inicio




label int5f0_refutado:
    jump int5_incorrecto
label int5f1_refutado:
    jump int5_incorrecto
label int5f2_refutado:
    jump int5_incorrecto
label int5f3_refutado:
    jump int5_incorrecto


label int5f4_refutado:
    hide screen interrogatorio_btns

    if interr_item_notepad_select==lstNotepad_titulo.index("Marissa Morstan (profile)") and not interr_frase4_refutada:
        $ showplay_excl("wait")
        "No wait..."
        "Neil said that he didn't see anyone else on the way, but {amarillo} it's obvious that he ran into Marissa {/amarillo} and Professor Harrow, because he went to help them."
        "So there has to be {amarillo}a third person...{/amarillo}"
        "Ugh, thank goodness Alice didn't scold me."
        hide neil with dissolve
        show alice enojada with dissolve
        $ restCorazones()
        ali "[pla_name]..." with hpunch
        "You shouldn't claim victory ahead of time..."
        hide alice with dissolve
        jump caso1_testimonio5_inicio

    elif interr_item_notepad_select==lstNotepad_titulo.index("Beck Doran (profile)") and not interr_frase4_refutada:
        $ showplay_excl("that is not true")
        pla "Are you sure about that?"
        show neil pensativo
        nei "Uhm... yeah..."
        pla "And what about Beck?"
        show neil serio
        nei "Beck? Who is that?"
        "Ah right... he doesn't know him..."
        pla "He is a boy who studies in the same classroom as the girl you helped..."
        pla "And that person, {nw}"
        play sound campana
        extend "{amarillo}was in the corridor when you went to help pick up the papers.{/amarillo}" with flashbulb
        show neil sorprendido
        nei "Huh!?"
        show neil pensativo
        nei "Uhmm... {amarillo}is he a tall boy with brown hair?{/amarillo}"
        $ checkTimeAndJump("int"+str(interr_id)+"_gameover")
        menu:
            "Yes":
                pla "Yeah..."
                nei "Huh..."
                show neil serio hablando
                nei "No wait... the only person I know who is tall and have {amarillo} brown hair {/amarillo} did not go to school that day."
                nei "And he's not called \"Beck.\""
                $ restCorazones()
                "Ah...I screwed up...I should check my notepad, {amarillo} I think I misunderstood his question.{/amarillo}" with hpunch
            "No":
                if not interr_frase4_refutada:
                    $ updateStat("intel","+",1)
                    $ renpy.notify("Intelligence +1")
                pla "No, the person I'm telling you about is tall, but he has red hair."
                show neil serio
                nei "Uhm...someone tall and red-haired..."
                play sound campana
                show neil sorprendido
                nei "Oh! I already remember!" with flashbulb
                show neil normal
                nei "Now that I've made an effort to remember..."
                nei "Yes, I think I saw that person at that time."
                play sound campana
                nei "But how important is that?" with flashbulb
                nei "I didn't talk to him at all, I just went on my way."


                show neil sonriendo hablando
                nei "Heh, heh, heh... I think the recess will be over soon..."
                nei "I should go now..."
                pla "Oh! Wait!" with hpunch
                pla "There is still something else..."
                $ checkTimeAndJump("int"+str(interr_id)+"_gameover")
                nei "Well... what else do you need to know?"
                if not interr_frase4_refutada:
                    tuto "The interrogated phrases have been updated. {amarillo}Another contradiction has appeared.{/amarillo}"
                $ interr_frase4_refutada=True
                $ interr_frasefinal=5
        jump caso1_testimonio5_inicio
    else:
        jump int5_incorrecto


label int5f5_refutado:
    hide screen interrogatorio_btns

    if interr_item_notepad_select==lstNotepad_titulo.index("Marissa Morstan (profile)") or interr_item_notepad_select==lstNotepad_titulo.index("Neil London (profile)"):
        $ quick_menu_gameplay = False
        $ hide_gameplay_layout()
        stop music fadeout 1
        $ showplay_excl("that is not true")
        jump caso1_interrogatorio5_final
    else:
        jump int5_incorrecto



label int5_incorrecto:
    hide screen interrogatorio_btns
    $ showplay_excl("wait")

    show neil serio
    nei "And what's that supposed to mean?"
    $ restCorazones()
    "Oh, nothing actually…" with hpunch
    jump caso1_testimonio5_inicio

label int5_gameover:
    hide screen interrogatorio_btns
    $ hide_gameplay_layout()
    stop music fadeout 1.0
    show neil pensativo
    nei "On second thought..."
    show neil normal
    nei "You wouldn't be able to solve a case. So this is a waste of time."
    pla "But we solved your riddle!"
    show neil pensativo
    nei "So what?"
    nei "Maybe it was pure luck."
    nei "Also… it was a riddle that even a child could solve."
    show neil normal
    nei "I'm sorry I have to go."
    hide neil with dissolve
    "No… no… Wait!" with hpunch
    jump caso1_gameover
