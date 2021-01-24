init -2 python:
    all_wrestlers=[]
    class manager(store.object):
        def __init__(self):
            self.name = "manager"
            self.exp = 0

    class wrestling_team(store.object):
        def __init__(self, members = []):
            self.members= members
            self.rounds_won =0
            self.atk_target =0
            self.moves_act=[]
            self.tagging_meter=0
            self.support =0
            self.def_flag =False
            self.dmg_cal=0
            self.dmg_combo=0
            self.perf_atk_flag=False

            #momentum
            self.mom_max = 50
            self.mom = 0.0
            self.mom_down_rate =0.1    ### 1 punto por segundo
            self.mom_duration=0.0
            self.mom_bar_lvl =0

        def mom_update(self):
            if self.mom_duration > 0:
                if self.mom >= self.mom_max:
                    self.mom_bar_lvl +=1
                    self.mom_max +=10
                    self.mom =0.0
                    self.mom_duration=0.0
                else:
                    #disminuir barra de momento
                    self.mom_duration -=1 * self.mom_down_rate
            elif self.mom_duration <= 0:
                self.mom = 0.0

    class wrestler(store.object):
        def __init__(self, name,strk_atk, power_atk, sub_atk, aerial_atk, strk_def, power_def, sub_def, aerial_def,    speed, str, tech, agi, img_portrait="", img_battle="" ):
            global all_shoppers
            self.name = name
            self.img_portrait=img_portrait
            self.img_battle=img_battle
            ###skill_stats


            self.def_flag=False
            self.atk_skill_points= [strk_atk, power_atk, sub_atk, aerial_atk ]
            self.def_skill_points =[strk_def, power_def, sub_def, aerial_def ]
            ###training points STA
            self.base_stats= [speed, str, tech, agi]
            ## 0 =F ; 1=D ; 2 =D+ ; 3=C; 4=C+; 5=B; 6=B+; 7=A; 8= A+; 9=S; 10=S+

            self.atk_target = 0
            if str>=tech and str>=agi:
                self.type =0
            if tech>str and tech>=agi:
                self.type =1
            if agi>=tech and agi>=str:
                self.type=2


            #timers
            self.atk_timer=0
            self.atk_delay=0
            #HP
            self.hp_max =100
            self.hp = 100
            self.hp_d = 0
            #ENERGY  ##### Tarda 20s para llegar a 100
            self.energy_max = 100
            self.energy = self.energy_max
            self.energy_fill_rate=0.5   ###filll rate se actualiza cada 0.1s. cada segunod sube 5
            self.energy_combo =0
            #momentum
            self.mom_max = 50
            self.mom = 0.0
            self.mom_down_rate =0.1    ### 1 punto por segundo
            self.mom_duration=0.0
            self.mom_bar_lvl =0

            self.moves=[]
            self.moves_act=[]
            self.rounds_won=0
            self.trust_points=0


            if self not in all_wrestlers:
                all_wrestlers.append(self)

        def restart(self):
            self.energy= self. energy_max###tiempo para el primer ataque
            self.mom=0.0
            self.mom_duration=0.0
            self.mom_max=10
            self.mom_bar_lvl -= 1
            self.hp = self.hp_max
            self.moves_act=[]

        def hp_down(self, amt):
            self.hp -= amt

        def energy_update(self):
            if self.energy < self.energy_max:
                self.energy += self.energy_fill_rate

        def mom_update(self):
            if self.mom_duration > 0:
                if self.mom >= self.mom_max:
                    self.mom_bar_lvl +=1
                    self.mom_max +=10
                    self.mom =0.0
                    self.mom_duration=0.0
                else:
                    #disminuir barra de momento
                    self.mom_duration -=1 * self.mom_down_rate
            elif self.mom_duration <= 0:
                self.mom = 0.0



## 0 =F ; 1=D ; 2 =D+ ; 3=C; 4=C+; 5=B; 6=B+; 7=A; 8= A+; 9=S; 10=S+
init python:
    wagner = wrestler("Wagner",5, 7, 3, 3, 1, 1, 1, 1,      6, 7,4,3, img_portrait= "images/portrait/wagner.png", img_battle="images/char/def_char.png")
    villano = wrestler("Villano",2, 1, 7, 3, 1, 1, 1, 1,    4, 3,8,2,   img_portrait= "images/portrait/villano.png", img_battle="images/char/def_char.png")
    mistico = wrestler("Mistico",2, 1, 4, 6, 1, 1, 1, 1,     2,   2,4,7,  img_portrait= "images/portrait/mistico.png", img_battle="images/char/def_char.png")
    yukiko = wrestler("Yukiko",2, 2, 3, 5, 1, 1, 1, 1,       1, 1,1,3, img_portrait= Transform("images/portrait/yukiko.jpg", zoom=2.2), img_battle="images/char/def_char.png" )
    angel =  wrestler("Angel",2, 1, 4, 6, 1, 1, 1, 1,     2,   2,4,7,  img_portrait= "images/portrait/yukiko.png", img_battle="images/char/angel_char.png")
    mika =  wrestler("Mika",2, 1, 4, 6, 1, 1, 1, 1,     2,   2,4,7,  img_portrait= "images/portrait/yukiko.png", img_battle="images/char/mika_char.png")


    p_team= wrestling_team(members=[angel, wagner, yukiko])
    com_team= wrestling_team(members=[mika, villano, mistico])
