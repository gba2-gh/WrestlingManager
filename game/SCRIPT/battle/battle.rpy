#label: ataque perfecto, tag, multiplicadores de combo, balancear
label battle:
    python:
        p_w=p_team.members[0]
        com_w=com_team.members[0]
        p_team.atk_target = com_w
        com_team.atk_target = p_w
        #update stamina

        for w in p_team.members:
            w.energy_update()

        for w in com_team.members:
            w.energy_update()

        #update momentum
        p_team.mom_update()
        com_team.mom_update()




        find_moves_act(p_team)
        find_moves_act(com_team)

        #find_moves_act(p_w)   ##Función de ataque automatico, en cuanto eliges el ataque este se realiza. Sistema de combate anterior
        #find_moves_act(com_w)

        ##  FF10 >>
        ##P_W ataca cuando se alcanza attack_delay.
        #####TODO Implementar el mismo sistema para ambos p_w y com_w
        #atk_timer empieza a correr cuando se realiza un ataque
        # if p_w.atk_timer > p_w.atk_delay:
        #     renpy.call("battle_seq", p_w, p_w.moves_act[0])
        #
        # if com_w.atk_timer > com_w.atk_delay:
        #     renpy.call("battle_seq", com_w, com_w.moves_act[0])
        #     #find_moves_act(p_w)
        #     #Find move busca en la lista moves act del personaje y llama a battle_seq
        #     ##<<  FF10


        renpy.call_screen("timer_screen")

#label: CAMBIOS OCURRIDOS AL REALIZAR UN MOVIMIENTO
label battle_seq(team,move):
    python:
        w=team.members[0]
        ###SISTEMA DE COMBATE FF10
        #calcular bonus por triangulo
        #bonus = move_bonus_tri(w, move)##move[0], el ùnico mov en la lista
        uke= team.atk_target
        #disminuir hp de receptor
        dmg_cal= cal_base_dmg(w,uke,move)   ##calcular daño y mom up
        #uke.hp -= dmg_cal[0]
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
        w.atk_timer=0#esto es para ff 10
        last_atk_time=0 #timer de animacion de ataque
        perf_atk_time=0

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
