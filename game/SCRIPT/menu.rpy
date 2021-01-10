
define not_inset=True
label move_swap:
    python:
        chosen_move_type = strike_moves
        renpy.show_screen("move_swap_screen")
        renpy.call_screen("character_select")
