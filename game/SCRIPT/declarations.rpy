init -2 python:
    import random
    import operator


define battle_sys=0 ##Sistema de combate a utilizar: 0==FG10, 1==FF13

define start_timer =False
define day =1
define month=4
define weekday = 6
define days_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
define days_of_week = ["Null", "Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday", "Sunday"]
define day_of_week = days_of_week [weekday]
define daytime=0
define daytime_name=["Early Morning", "Morning", "Afternoon", "Evening", "Night"]

define stats_letter= ["F", "D", "D+", "C", "C+", "B", "B+", "A", "A+", "S", "S+"]
define training_points_fn = ["Strenght", "Technique", "Agility"]
define skill_points_fn = ["Strike", "Throw", "Stretch", "Choke", "Aerial Strike", "High Flying"]

define dmg_combo=0.0
define def_const=600.0

define atkOne=False
define atkTwo=False
define p_dmg_done=0
define com_dmg_done=0
define p_moves_first=True
define score=[0,0]
define round = 1

# define p_atk_timer=0
# define p_atk_delay=0
#
# define com_atk_timer=0
# define com_atk_delay=0

#####IMAGES

image red circle ="images/red_circle.png"
