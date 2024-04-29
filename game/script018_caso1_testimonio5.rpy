label caso1_testimonio5:
    $ estadoj="Testimony"
    $ interrogatorio_activo=False
    $ initInterrVars()
    #intro testimonio
    $ showMinigameTitle(estadoj)
    play music tiempo_muerto2 fadein 3

    $ interr_frase4_refutada=False

    label caso1_testimonio5_inicio:

        if estadoj=="Interrogation":
            show screen interrogatorio_btns

            if cantidad_corazones==0 or timeup:
                hide screen interrogatorio_btns
                jump int5_gameover

        $ renpy.block_rollback()
        show neil normal with dissolve
        $ interr_fraseid=0
        nei "That day, at ten o'clock, {amarillo} I was on my way to the library.{/amarillo}"
        show neil pensativo
        $ interr_fraseid=1
        nei "Then, I found Professor Harrow and {amarillo}a girl on the floor...{/amarillo}"
        show neil normal
        $ interr_fraseid=2
        nei "I also saw that there were lots of papers scattered on the floor, {amarillo}, so I helped pick them up.{/amarillo}"
        show neil sonriendo hablando
        $ interr_fraseid=3
        nei "After that, {amarillo}I left.{/amarillo}"
        show neil serio hablando
        $ interr_fraseid=4
        if not interr_frase4_refutada:
            nei "And since {amarillo} I didn't see anyone else on my way back, {/amarillo} I have nothing more to tell." ."##refutar con perfil de beck o interrogar, de todas formas no activa bandera, pero aumenta inteligencia en 2

        else:
            nei "And yes, I saw that person named Beck, {amarillo} although I didn't speak to him.{/amarillo}"
        if interr_frase4_refutada:
            show neil serio hablando
            $ interr_fraseid=5
            nei "But that's it, apart from the great height of this Beck guy, {amarillo}no one else particularly caught my attention{/amarillo}."
        hide neil with dissolve
        $ renpy.block_rollback()
        hide screen interrogatorio_btns

        if estadoj=="Testimony":
            stop music fadeout 2
            show alice normal with dissolve
            ali "Uhm..."
            ali "That was fast..."
            pla "Yes... we already know almost everything he has said..."
            "But is he telling the whole truth?"
            hide alice with dissolve


            $ quick_menu_gameplay = True

            $ estadoj="Interrogation"
            $ interrogatorio_activo=True


            $ interr_id=5

            $ interr_frasefinal=4


            $ interr_btn_refutar_disabled=False


            $ initCorazones()


            $ showMinigameTitle(estadoj)


            $ show_gameplay_layout(720)


            show screen interrogatorio_btns

            play music tiempo_muerto2 fadein 3

            jump caso1_testimonio5_inicio
        else:

            $ checkTimeAndJump("int"+str(interr_id)+"_gameover")

            if not interr_frase4_refutada:
                show alice normal with dissolve
                ali "This is not enough..."
                ali "What do we do, [pla_name]?"
                "What do we do? I'm doing most of the work..."
                "But... Seriously, what could I do?"
                "Continue {amarillo}asking{/amarillo} or point out a {amarillo}contradiction{/amarillo}?"
                hide alice with dissolve
            else:
                "Alright, I've already proven a contradiction..."
                "But there is another one that is more important!" with hpunch
            jump caso1_testimonio5_inicio
