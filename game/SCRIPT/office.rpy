
label office:
    python:

        renpy.show_screen("calendar_gui")
        renpy.show_screen("office_menu")####funcion para que cambie el menu que mueestra
        renpy.call_screen("characer_select")


screen character_select():
    vbox:
        yalign 0.2
        for w in p_team.members:
            textbutton "[w.name]" ypos y action SetVariable("chosen_w", w )

screen office_menu():
    vbox:
        xalign 0.5 yalign 0.5
        textbutton "Training" action [Hide("third_screen"), Show("training_screen")]
        textbutton "Training Hall" action [Hide("third_screen"), Show("training_hall_screen")]
        textbutton "Special Training" action NullAction()
        textbutton "Promotion" action [Hide("third_screen"), Show("promotion_screen")]
        textbutton "Investigation" action NullAction()
        textbutton "Gallery" action NullAction()
        textbutton "Save and or settings" action NullAction()
        textbutton "Calendar" action NullAction()

###ACTIONS
label training_action(x):
    $t = training_points_fn[x]
    "[chosen_w.name] trained [t]"
    python:
        chosen_w.training_points[x] +=10
        renpy.hide_screen("third_screen")
        renpy.jump("day_tran")

label training_hall_action(x, up_cost):
    $t = skill_points_fn[x]
    "[chosen_w.name] practiced [t]"
    python:
        type=chosen_w.skill_points[x][1]
        chosen_w.training_points[type] -= up_cost
        chosen_w.skill_points[x][0] +=1
        renpy.hide_screen("third_screen")
        renpy.jump("day_tran")

label Wagner_evt:
    "hi"
    $daytime +=1
    jump day_tran

label Mistico_evt:
    "hello"
    $daytime +=1
    jump day_tran


#######OFFICE SCREENS
##THIRD SCREENS

screen training_screen():
    tag third_screen
    vbox:
        xalign 0.8 yalign 0.5
        text "[chosen_w.name]" xalign 0.5 #Luchador seleccionado para entrenar
        vbox:
            for num, stat in enumerate(training_points_fn):
                $points = chosen_w.training_points[num]#
                textbutton "[stat] = [points]" action Call("training_action", num)  ##EN MENU
        textbutton "back" action Hide("third_screen")  ##retorno

screen training_hall_screen():
    tag third_screen
    vbox:
        xalign 0.8 yalign 0.5
        text "[chosen_w.name]" xalign 0.5 #Luchador seleccionado para promociòn
        vbox:
            for num, stat in enumerate(skill_points_fn):
                $flag=False
                $points = chosen_w.skill_points[num][0]#
                $up_cost=points*10#costo de subir habilidad
                $type = chosen_w.skill_points[num][1]
                if chosen_w.training_points[type]>=up_cost:
                    $flag=True
                # if num <=1:
                #     if chosen_w.training_points[0]>=up_cost:
                #         $flag=True
                # elif 1<num<=3:
                #     if chosen_w.training_points[1]>=up_cost:
                #         $flag=True
                # elif 3<num<=5:
                #     if chosen_w.training_points[2]>=up_cost:
                #         $flag=True

                textbutton "[stat] = [points]" action [SensitiveIf(flag), Call("training_hall_action", num, up_cost)]  ##EN MENU



screen promotion_screen():
    tag third_screen
    vbox:
        xalign 0.8 yalign 0.5
        text "[chosen_w.name]" xalign 0.5 #Luchador seleccionado para promociòn

        #Mostrar promociones disponibles
        vbox:
            text "random event 1"
            text "random event 2"
            textbutton "important event!" action Function(renpy.jump, chosen_w.name + "_evt")
        textbutton "back" action Hide("third_screen")  ##retorno
