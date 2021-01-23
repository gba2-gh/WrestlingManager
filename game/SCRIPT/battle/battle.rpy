#label: ataque perfecto, tag, multiplicadores de combo, balancear
label battle:
    python:
        #ACTUALIZA LUCHADOR ACTIVO Y RECEPTOR ACTIVO
        p_w=p_team.members[0]
        com_w=com_team.members[0]
        p_team.atk_target = com_w
        com_team.atk_target = p_w

        #Actualizar STAMINA para cada luchador
        for w in p_team.members:
            w.energy_update()
        for w in com_team.members:
            w.energy_update()

        #Actualizar MOMENTUM del equipo
        p_team.mom_update()
        com_team.mom_update()

        #Atacar cuando haya ataques en lista moves_act del equipo. El jugador tiene preferencia
        find_moves_act(p_team)
        find_moves_act(com_team)

        renpy.call_screen("timer_screen")

#label: CAMBIOS OCURRIDOS AL REALIZAR UN MOVIMIENTO
label battle_seq_uno(team, move):
    python:
        w=team.members[0]
        if team.perf_atk_flag:
            w.energy -= move.energy_cost *.7
            team.perf_atk_flag=False
        else:
            w.energy -= move.energy_cost
        last_atk_time = 0
        renpy.call_screen("battle_seq_screen_uno", team, move)


#label: CAMBIOS OCURRIDOS AL REALIZAR UN MOVIMIENTO#######BORRAR
label battle_seq(team,move):
    python:
        #Atacante y receptor
        w=team.members[0]
        uke= team.atk_target
        #CALCULAR DAÑO Y SUMARLO AL COMBO
        dmg_cal= cal_base_dmg(w,uke,move)   ##calcular daño y mom up
        dmg_combo += dmg_cal[0]
        #Energy del atacante disminuye
        w.energy -=move.energy_cost
        #w.energy_combo=0
        #aumentar momentum del atacante
        team.mom += dmg_cal[1]
        team.mom_duration += move.duration   #Bonus delay: entre menor el lvl de la carta màs tiempo tarda la barra de momentum en comenzar a bajar
        #remover ataque utilizado
        team.moves_act.remove(move)
        #reiniciar timer de ataque
        last_atk_time=0 #timer de animacion de ataque
        perf_atk_time=0
        if team.def_flag:
            uke.energy -= (move.energy_cost / 2)#BORRAR
            team.mom -= (dmg_cal[1]/2)
            team.mom_duration -= (move.duration/2)
            uke.def_flag=False

        ##Condiciòn de victoria, activan flag para rendir
        if uke.hp <= uke.hp_max * 0.3:
            renpy.call_screen("battle_seq_screen", team, move, True, dmg_cal, dmg_combo)#rendir
        else:
            renpy.call_screen("battle_seq_screen", team, move, False, dmg_cal, dmg_combo)#continua la lucha


######################################################################################
######################################################################################
######################################################################################
######################################################################################
label pin_try(w, type):
    python:
        if random.randint(1,100) <= 70:
            w.rounds_won +=1
            if w.rounds_won == 2:
                renpy.call_screen("victory_screen", w)
            else:
                renpy.call_screen("pin_try_screen", True, w, type)
        else:
            renpy.call_screen("pin_try_screen", False, w, type)

label round_over:
    python:
        p_w.restart()
        com_w.restart()
        round +=1
    call screen round_over_screen

label match_over:
    python:
        p_w.restart()
        p_w.rounds_won =0
        com_w.restart()
        com_w.rounds_won =0
        round =0
        renpy.jump("start")
