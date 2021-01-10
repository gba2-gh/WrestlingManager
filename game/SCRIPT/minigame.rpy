####attack minigame
define last_atk_time = 0
define perf_atk_flag = -1
define atk_flag = 0




label perf_atk:
    python:
        #last_atk_time +=1

        renpy.call_screen("perf_atk_screen", atk_flag, perf_atk_flag)



screen perf_atk_screen(atk_flag, perf_atk_flag ):
        add "red circle" at atk_circle_anim
        textbutton "attack" xalign 0.4 yalign 0.5 action SetVariable("perf_atk_flag", atk_flag)

        text "[atk_flag]"
        text "[perf_atk_flag]" yalign 0.1
        #text "min=[minutes]" yalign 0.2


        timer 1 repeat False action SetVariable("atk_flag", 1)
        timer 2.5 repeat False action SetVariable("atk_flag", -1)
        timer 3  repeat False action Call("extra")


label extra():
    call screen extra()

screen extra():
            text "flag=[perf_atk_flag]"
            #text "min=[minutes]" yalign 0.1





screen perf_atk_timer():
        timer 1 repeat True action [Call("perf_atk")]


transform atk_circle_anim:
    pause 1.0
    xalign 0.5 yalign 0.5
    linear 0.0 zoom 8
    linear 0.9 zoom 0.2


transform pulse_button:
    on hover, idle:
        linear .25 zoom 1.25
        linear .25 zoom 1.0
