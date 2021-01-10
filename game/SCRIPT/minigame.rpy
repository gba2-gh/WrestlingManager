label perf_atk:
    python:
        renpy.call_screen("perf_atk_screen")



screen perf_atk_screen():
        timer 0.1 repeat True action SetVariable( "last_atk_time", last_atk_time + 0.1 )
        add "red circle" at atk_circle_anim
        text "perf_time=[perf_atk_time]" yalign 0.6
        text "last_time=[last_atk_time]" yalign 0.7
