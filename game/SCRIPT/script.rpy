define player_team = []
label main_menu:
    return
label start:
    python:
        #renpy.jump("office") #[menu.rpy]
        #renpy.jump("perf_atk")
        #Llamar screen para seleciconar luchador [menu_screens.rpy]
        p_w = renpy.call_screen("select_screen", "Player 1", 100)
        #com_w= renpy.call_screen("select_screen", "com", 1500)
        com_w = villano
        p_w.atk_target=com_w
        com_w.atk_target=p_w

        renpy.jump("battle")




        player_team.append(mistico)
        player_team.append(wagner)
        player_team.append(yukiko)
        chosen_w=player_team[0]
        renpy.jump("move_swap")



        narrator("Cambiar movs?", interact=False)
        result = renpy.display_menu([ ("SI", "move_swap"), ("NO", "battle") ]) #battle en battle.rpy
        renpy.jump(result)
        #renpy.say(narrator, "hi")
    return



#SISTEMA DE CALENDARIO
#Day transition pasar al siguiente dia
label day_tran:
    python:
        day +=1
        if days_in_month[month] < day:
            month +=1
            day = 1
        turn = 0

        if weekday >= 7:
            weekday = 0

        weekday +=1

        day_of_week= days_of_week[weekday]
        daytime = 0
    call screen day_tran_screen

screen day_tran_screen():
    add "images/bg/bg_transition.png"
    text "cambiar dia" xpos 500  ypos 500
    text "[day] / [month]   ([day_of_week])" xpos 500  ypos 600
    timer 1 repeat False action Call("office")



###############TEST
#Prueba de timers
define x=0
define y=0
define y_d=0

screen timer():
    timer 0.1 repeat True action Call("test_label")

label test_label:
    python:
        x=x+1
        if y_d> 0:
            y_d -=1
        elif y_d == 0:
            y=0
    call screen test(x,y,y_d)

label b_seq(inc):
    python:
        y+=inc
        y_d= y
        renpy.call_screen("battle_test")

screen test(x, y, y_d):

    use timer()
    $inc = 10
    vbox:
        bar value AnimatedValue(x, range=100, delay = 5.0 )left_bar Frame("gui/bar_full.png",5,5) right_bar Frame("gui/bar_empty.png",5,5) thumb None xmaximum 400 ymaximum 10
        bar value AnimatedValue(y, range=100, delay = 5.0 )left_bar Frame("gui/bar_full.png",5,5) right_bar Frame("gui/bar_empty.png",5,5) thumb None xmaximum 400 ymaximum 10
        bar value AnimatedValue(y_d, range=100, delay = 5.0 )left_bar Frame("gui/bar_full.png",5,5) right_bar Frame("gui/bar_empty.png",5,5) thumb None xmaximum 400 ymaximum 10
        text "x:[x]"
        text "y:[y]"
        text "y_d:[y_d]"
        textbutton "restar" action [SetVariable("x", x-5), Call("test_label")]
        textbutton "move 1" action [Function(renpy.call, "b_seq", 10)]

screen battle_test():
    use test(x, y, y_d)
    text "battle sequence" xalign 0.5 yalign 0.5

    timer 3 repeat False action [SetVariable("y", y+10), SetVariable("y_d", y+10) ]
    timer 5 repeat False action [Hide("battle_test"),Call("test_label")]
