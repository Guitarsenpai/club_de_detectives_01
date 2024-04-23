label caso1_testimonio2:
    $ estadoj="Testimony"
    $ interrogatorio_activo=False
    $ initInterrVars()
    #intro testimonio
    $ showMinigameTitle(estadoj)
    play music tiempo_muerto2 fadein 3

    label caso1_testimonio2_inicio:

        if estadoj=="Interrogation":
            show screen interrogatorio_btns
            ## si se realizaron todas las preguntas necesarias...
            if fraseInterr[0] and fraseInterr[1] and fraseInterr[2] and fraseInterr[3]:
                jump caso1_iterrogatorio2_final

        if cantidad_corazones==0 or timeup:
            hide screen interrogatorio_btns
            jump int2_gameover

        $ renpy.block_rollback()
        show mary normal with dissolve
        $ interr_fraseid=0
        mary "{amarillo}On Friday of last week{/amarillo}, after speaking {amarillo} with a student{/amarillo} in the teachers' lounge..."
        $ interr_fraseid=1
        mary "{amarillo}Following my schedule,{/amarillo} I went to Miss Morstan's classroom to give classes."
        $ interr_fraseid=2
        show mary pensando
        mary "But as I approached the entrance, {amarillo} she bumped into me.{/amarillo}"
        $ interr_fraseid=3
        show mary hablando
        mary "{amarillo}Papers went flying{/amarillo}, it was a disaster. It's a good thing {amarillo}someone came to help.{/amarillo}"
        $ interr_fraseid=4
        show mary pensando
        mary "After I collected my documents. I imposed a punishment on Marissa."
        $ interr_fraseid=5
        show mary normal
        mary "Later, {amarillo}I gave my classes normally.{/amarillo}"
        $ interr_fraseid=6
        mary "{amarillo}That's all.{/amarillo}"
        $ renpy.block_rollback()

        hide screen interrogatorio_btns

        if estadoj=="Interrogation":
            stop music fadeout 2

            mary "Okay, drop your questions."
            mary "I don't have all the time in the world."
            mary "I will give you {amarillo}five minutes{/amarillo} to clarify all your doubts."
            pla "Huh!?" with hpunch
            "Five minutes?"
            "I must hurry!"

            ## desactivamos opciones irrelevantes del quick menu, y el menu normal
            $ quick_menu_gameplay = True

            $ estadoj="Interrogation"
            $ interrogatorio_activo=True

            ## variables del interrogatorio
            $ interr_id=2
            ##para establecer cual es la última frase y así desactivar el botón de siguiente
            $ interr_frasefinal=6

            #en este interrogatorio, como no se necesita refutar, se desactiva el botón
            $ interr_btn_refutar_disabled=True

            #variables bandera
            $ fraseInterr={0:0,1:1,2:2,3:3,4:4}
            $ fraseInterr[0]=False
            $ fraseInterr[1]=False
            $ fraseInterr[2]=False
            $ fraseInterr[3]=False
            $ fraseInterr[4]=False


            $ initCorazones()


            $ showMinigameTitle(estadoj)


            $ show_gameplay_layout(300)

            show screen interrogatorio_btns

            play music tiempo_muerto2 fadein 3

            jump caso1_testimonio2_inicio
        else:

            $ checkTimeAndJump("int"+str(interr_id)+"_gameover")
            "For some reason, I feel like there's something here that could be important in the investigation..."
            "I need to ask the right questions!" with hpunch
            jump caso1_testimonio2_inicio
