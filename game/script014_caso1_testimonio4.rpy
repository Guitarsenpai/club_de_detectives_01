label caso1_testimonio4:
    $ estadoj="Testimony"
    $ interrogatorio_activo=False
    $ initInterrVars()

    $ showMinigameTitle(estadoj)
    play music tiempo_muerto2 fadein 3

    label caso1_testimonio4_inicio:

        if estadoj=="Interrogation":
            show screen interrogatorio_btns
            ## si se realizaron todas las preguntas necesarias...
            if fraseInterr[0] and fraseInterr[2] and fraseInterr[4]:
                jump caso1_interrogatorio4_final

        if cantidad_corazones==0 or timeup:
            hide screen interrogatorio_btns
            jump int4_gameover

        $ renpy.block_rollback()
        show marissa alegre hablando with dissolve
        $ interr_fraseid=0
        mar "Before math class, {amarillo} I was chatting with my friends in the classroom.{/amarillo}"
        show marissa normal
        $ interr_fraseid=1
        mar "Almost at the end of the hour, {amarillo} I received a call.{/amarillo}"
        $ interr_fraseid=2
        show marissa normal
        mar "So, I rushed out and {amarillo} then was when I bumped into the teacher...{/amarillo}"
        $ interr_fraseid=3
        show marissa apenada
        mar "{amarillo}Professor Harrow's papers went flying{/amarillo}, and I {amarillo}dropped some notebooks.{/amarillo}"
        $ interr_fraseid=4
        show marissa at decaer
        mar "It didn't take long for me to start packing things up, that teacher is terrifying, {amarillo}shortly after, someone came to help.{/amarillo}"
        $ interr_fraseid=5
        show marissa enojada at reponerse
        mar "Despite having apologized, the teacher {amarillo} punished me.{/amarillo}"
        $ interr_fraseid=6
        show marissa normal
        mar "I didn't return to the {amarillo} classroom until the math class was over.{/amarillo}"
        $ renpy.block_rollback()

        hide screen interrogatorio_btns

        if estadoj=="Testimony":
            stop music fadeout 2
            hide marissa with dissolve

            show alice normal with dissolve
            ali "Wow, she must have had a terrible time..."
            ali "I feel lucky that I didn't see Professor Harrow upset..."
            pla "Yeah... Anyway, let's see what we can find out..."
            show alice sonriendo
            ali "Yeah!"
            hide alice with dissolve

           ## desactivamos opciones irrelevantes del quick menu, y el menu normal
            $ quick_menu_gameplay = True

            $ estadoj="Interrogation"
            $ interrogatorio_activo=True


            $ interr_id=4

            $ interr_frasefinal=6


            $ interr_btn_refutar_disabled=True


            $ fraseInterr={0:0,1:1,2:2,4:4}
            $ fraseInterr[0]=False
            $ fraseInterr[1]=False
            $ fraseInterr[2]=False
            $ fraseInterr[4]=False


            $ initCorazones()


            $ showMinigameTitle(estadoj)


            $ show_gameplay_layout(400)


            show screen interrogatorio_btns

            play music tiempo_muerto2 fadein 3

            jump caso1_testimonio4_inicio
        else:

            $ checkTimeAndJump("int"+str(interr_id)+"_gameover")
            hide marissa with dissolve
            "Marissa has told me some things that I already knew..."
            "But, there are others that I need more information about."
            "I need to ask the right questions!" with hpunch
            jump caso1_testimonio4_inicio
