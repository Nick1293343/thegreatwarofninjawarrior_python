from tkinter import *
import time
import random
def continue_game(nothing):
    global continuing_game, want_to_play, continue_list2
    file = open('m55182va.txt', "r")
    theWords= []
    item = ''
    continue_list = []
    continue_list2 = []
    for line in file:
        line = line.rstrip()
        theWords.append(line)
    for i in theWords:
        item = ''
        for r in i:
            if r != '[': # or r != ']':
                if r != ']':
                    item += str(r)
        continue_list.append(item)
    for i in continue_list:
        continue_list2.append(i.split(', '))
    continuing_game = 1
    play_btn.destroy()
    settings_btn.destroy()
    play_saved_game_btn.destroy()
    window.destroy()
    want_to_play = 1



def Default_key_options(nothing):
    global user_key_option
    user_key_option = False
    default_controls.destroy()
    Custom_controls.destroy()
    initial_screen()
def Custom_key_options(nothing):
    global user_key_option
    user_key_option = True
    default_controls.destroy()
    Custom_controls.destroy()
    initial_screen()
def Customize_controls(nothing):
    global default_controls, Custom_controls
    global difficulty_btn, control_settings_btn
    difficulty_btn.destroy()
    control_settings_btn.destroy()
    default_controls = Button(window, text='DEFAULT CONTROLS\n"p" key = punch\n"k" key = kick', width=50, height=3, bd='10', command=lambda: Default_key_options(nothing))
    default_controls.place(x=450, y=350)
    Custom_controls = Button(window, text='CUSTOM CONTROLS\n"9" key = punch\n"0" key = kick', width=50, height=3, bd='10', command=lambda: Custom_key_options(nothing))
    Custom_controls.place(x=450, y=450)

def hard(nothing):
    global difficulty
    difficulty = 'hard'
    easy_btn.destroy()
    hard_btn.destroy()
    initial_screen()
def easy(nothing):
    global difficulty
    difficulty = 'easy'
    easy_btn.destroy()
    hard_btn.destroy()
    initial_screen()
def choose_difficulty(nothing):
    global easy_btn, hard_btn, difficulty_btn, control_settings_btn
    difficulty_btn.destroy()
    control_settings_btn.destroy()
    easy_btn = Button(window, text='EASY (DEFAULT)', width=50, height=3, bd='10', command=lambda: easy(nothing))
    easy_btn.place(x=450, y=350)
    hard_btn = Button(window, text='HARD', width=50, height=3, bd='10', command=lambda: hard(nothing))
    hard_btn.place(x=450, y=450)

def settings_menue(nothing):
    global difficulty_btn, control_settings_btn
    settings_btn.destroy()
    play_btn.destroy()
    play_saved_game_btn.destroy()
    difficulty_btn = Button(window, text='CHOOSE DIFFICULTY', width=50, height=3, bd='10', command=lambda: choose_difficulty(nothing))
    difficulty_btn.place(x=450, y=350)
    control_settings_btn = Button(window, text='CUSTOMIZE CONTROLS', width=50, height=3, bd='10', command=lambda: Customize_controls(nothing))
    control_settings_btn.place(x=450, y=450)

def next_step(nothing):
    global player1_name, entry1, want_to_play
    player1_name = entry1.get()
    print(player1_name)
    window.destroy()
    want_to_play = 1
def play_game(nothing):
    global next_btn, player1_name, entry1, play_saved_game_btn
    settings_btn.destroy()
    label2 = Label(window, text="ENTER YOUR PLAYER'S NAME")
    label2.config(font=('helvetica', 30))
    canvas.create_window(650, 300, window=label2)
    play_btn.destroy()
    play_saved_game_btn.destroy()
    entry1 = Entry(window)
    canvas.create_window(500, 400,height=50, width=300, window=entry1)
    next_btn = Button(window, text='NEXT', width=20, height=2, bd='10', command=lambda: next_step(nothing))
    next_btn.place(x=780, y=375)

def initial_screen():
    global play_btn, settings_btn, play_saved_game_btn
    The_great_fight_of = canvas.create_image(640, 100, image=img3)
    Ninja_warrior = canvas.create_image(640, 250, image=img2)
    play_btn = Button(window, text='PLAY', width=50, height=3, bd='10', command=lambda: play_game(nothing))
    play_btn.place(x=450, y=350)
    settings_btn = Button(window, text='SETTINGS', width=50, height=3, bd='10', command=lambda: settings_menue(nothing))
    settings_btn.place(x=450, y=450)
    # play_saved_game_btn = Button(window, text='CONTINUE', width=50, height=3, bd='10', command=lambda: continue_game(nothing))
    # play_saved_game_btn.place(x=450, y=550)

window = Tk()
want_to_play = 0
difficulty = 'easy'
continue_list2 = []
nothing = None
user_key_option = False
easy_btn = None
difficulty_btn = None
control_settings_btn = None
hard_btn = None
play_btn = None
settings_btn = None
leader_board_btn = None
canvas = Canvas(window, width=1280, height=720)
canvas.pack()
img1 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate2/Re37g5.v1.png')
img2 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/ninja_warrior1.png')
img3 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/the great fight of.png')
lava_cave = canvas.create_image(1280/2, 720/2 + 15, image=img1)
window.update()
initial_screen()
next_btn = None
continuing_game = 0
player1_name = ''
entry1 = None
default_controls = None
Custom_controls = None
play_saved_game_btn = Button(window, text='CONTINUE', width=50, height=3, bd='10', command=lambda: continue_game(nothing))
play_saved_game_btn.place(x=450, y=550)


window.mainloop()
while want_to_play != 0:
    def save_and_exit(nothing):
        global coords_of_player1, coords_of_player2, Health_player2, Health_player1,\
            Healthbar_player2, coords_Healthbar_player2, coords_Healthbar_player1, want_to_play
        coords_of_player2 = canvas.coords(player2_stance)
        coords_of_player1 = canvas.coords(player1_stance)
        coords_Healthbar_player1 = canvas.coords(Healthbar_player1)
        coords_Healthbar_player2 = canvas.coords(Healthbar_player2)
        line = [f'{coords_of_player1}\n{coords_of_player2}\n{coords_Healthbar_player1}\n'
                f'{coords_Healthbar_player2}\n{Health_player1}\n{Health_player2}']
        f = open( 'm55182va.txt', 'w')
        f.writelines(line)
        want_to_play = 0
        window.destroy()

    def Boss_key(event):
        global Boss_key_var, pause_btn, fake_doc, click, click2
        if Boss_key_var == 1:
            click = 1
            click2 = 1
            fake_doc = canvas.create_image(width_canvas/2, height_canvas/2 + 200, image=img31)
            pause_btn.destroy()
            Boss_key_var = 0
        elif Boss_key_var == 0:
            click = 0
            click2 = 0
            canvas.delete(fake_doc)
            pause_btn = Button(window, text='II',font=('Arial Black', 20) ,width=3, height=1, bd='10', command=lambda: paused(nothing))
            pause_btn.place(x=380, y= 40)
            Boss_key_var = 1

    def resume(nothing):
        global paused_var
        paused_var = 0
        paused(nothing)


    def paused(nothing):
        global click2, click, paused_var, end_menue_player1, end_menue_player2, rect, resume_btn, reset_btn, pause_btn, exit_btn
        click = 1
        click2 = 1
        if paused_var == 1:
            rect = canvas.create_rectangle(100, 100, 1200, 600, fill='steel blue')
            end_menue_player1 = canvas.create_image(width_canvas/4 - 100, height_canvas/2, image=img24)
            end_menue_player2 = canvas.create_image(width_canvas*3/4 + 100, height_canvas/2, image=img25)
            resume_btn = Button(window, text='RESUME', width=50, height=5, bd='10', command=lambda: resume(nothing))
            resume_btn.place(x=450, y=height_canvas/2 - 135)
            reset_btn = Button(window, text='RESTART', width=50, height=5, bd='10', command=lambda: window.destroy())
            reset_btn.place(x=450, y=height_canvas/2 - 35)
            # pause_btn.place(x=380, y= 10)
            exit_btn = Button(window, text='EXIT', width=25, height=5, bd='10', command=lambda: clicked(want_to_play))
            exit_btn.place(x=450, y=height_canvas/2 + 65)
            save_exit_btn = Button(window, text='SAVE AND EXIT', width=21, height=5, bd='10', command=lambda: save_and_exit(nothing))
            save_exit_btn.place(x=650, y=height_canvas/2 + 65)
            paused_var = 0
        elif paused_var == 0:
            canvas.delete(end_menue_player1)
            canvas.delete(end_menue_player2)
            canvas.delete(rect)
            click = 0
            click2 = 0
            resume_btn.destroy()
            reset_btn.destroy()
            exit_btn.destroy()
            # pause_btn.place(x=380, y= 40)
            paused_var = 1

    def clicked(event):
        global want_to_play
        want_to_play = 0
        window.destroy()
    def game_over():
        global click, click2, player1_stance, player2_stance
        click = 1
        click2 = 1
        pause_btn.destroy()

        if Health_player2 <= 0:
            canvas.delete(Healthbar_player2)
            time.sleep(1)
            canvas.itemconfig(player2_stance, image=img30)
            canvas.move(player2_stance, 0, 60)
            window.update()
            time.sleep(1)
        elif Health_player1 <= 0:
            canvas.delete(Healthbar_player1)
            time.sleep(1)
            canvas.itemconfig(player1_stance, image=img29)
            canvas.move(player1_stance, 0, 60)
            window.update()
            time.sleep(1)
        for r in range(4):
            game_over_image = canvas.create_image(width_canvas/2, height_canvas/2, image=img22)
            time.sleep(0.5)
            window.update()
            canvas.delete(game_over_image)
            game_over_image2 = canvas.create_image(width_canvas/2, height_canvas/2, image=img23)
            time.sleep(0.5)
            window.update()
            canvas.delete(game_over_image2)
        if Health_player2 <= 0:
            you_won = canvas.create_image(width_canvas/2, height_canvas/2, image=img32)
            window.update()
            time.sleep(2)
        if Health_player1 <= 0:
            you = canvas.create_image(width_canvas/2, height_canvas/2-100, image=img33)
            lose = canvas.create_image(width_canvas/2, height_canvas/2+100, image=img34)
            window.update()
            time.sleep(2)
        canvas.create_rectangle(100, 100, 1200, 700, fill='steel blue')
        end_menue_player1 = canvas.create_image(width_canvas/4 - 100, height_canvas/2, image=img24)
        end_menue_player2 = canvas.create_image(width_canvas*3/4 + 100, height_canvas/2, image=img25)
        exit_btn = Button(window, text='EXIT', width=50, height=5, bd='10', command=lambda: clicked(want_to_play))
        exit_btn.place(x=450, y=height_canvas/2 + 30)
        btn2 = Button(window, text='play again', width=50, height=5, bd='10', command=lambda: window.destroy())
        btn2.place(x=450, y=height_canvas/2 - 170)

    def player_ramming1():                  # Collision detection
        global coords_of_player1, coords_of_player2, player1_ramming
        if coords_of_player1[0] >= coords_of_player2[0]-30:
            player1_ramming = 1

    def player_ramming2():                  # Collision detection
        global coords_of_player1, coords_of_player2, player2_ramming
        if coords_of_player2[0] <= coords_of_player1[0]-30:
            player2_ramming = 1

    def player_going_out2():                # Collision detection
        global coords_of_player1, coords_of_player2, player2_going_out
        if coords_of_player2[0] >= width_canvas-70:
            player2_going_out = 1
    def player_going_out1():                # Collision detection
        global coords_of_player1, coords_of_player2, player1_going_out
        if coords_of_player1[0] <= 70:
            player1_going_out =1

    def cheat_code3(event):
        global coords_of_player1, coords_of_player2, Health_player2, click, click2, player2_going_out, coords_Healthbar_player1, coords_Healthbar_player2, one_percent_health_player2, Healthbar_player2, left_key, up_key, down_key, right_key
        left_key = True
        if click == 0 and up_key == True and down_key == True and right_key == True and left_key == True:
            click = 1
            click2 = 1
            coords_of_player1 = canvas.coords(player1_stance)
            coords_of_player2 = canvas.coords(player2_stance)
            canvas.itemconfig(player1_stance, image=img17)
            time.sleep(00.3)
            window.update()
            canvas.itemconfig(player1_stance, image=img18)
            time.sleep(00.3)
            window.update()
            time.sleep(00.3)
            canvas.itemconfig(player1_stance, image=img19)
            window.update()
            canvas.itemconfig(player1_stance, image=img20)
            time.sleep(00.3)
            window.update()
            super_wave = canvas.create_oval(coords_of_player1[0]-20, coords_of_player1[1]-20, coords_of_player1[0]+20, coords_of_player1[1]+20, fill='red2')
            time.sleep(0.3)
            canvas.itemconfig(player1_stance, image=img2)
            while True:
                coords_of_superwave = canvas.coords(super_wave)
                canvas.move(super_wave, 5, 0)
                time.sleep(0.0001)
                window.update()
                if coords_of_superwave[2] == coords_of_player2[0]:          # Collision detection
                    break
            canvas.delete(super_wave)
            canvas.itemconfig(player2_stance, image=img11)
            for i in range(15):
                coords_of_player2 = canvas.coords(player2_stance)
                if player2_going_out == 1:
                    player2_going_out = 0
                    canvas.move(player2_stance,-10,0)
                    break
                time.sleep(0.1)
                canvas.move(player2_stance, 20, 0)
                window.update()
                player_going_out2()

            canvas.itemconfig(player2_stance, image=img3)
            Health_player2 -= 33

            for i in range(33):
                canvas.delete(Healthbar_player2)
                Healthbar_player2 = canvas.create_rectangle(coords_Healthbar_player2[0], coords_Healthbar_player2[1], coords_Healthbar_player2[2] + one_percent_health_player2, coords_Healthbar_player2[3], fill='red2')
                window.update()
                time.sleep(0.01)
                coords_Healthbar_player1 = canvas.coords(Healthbar_player1)
                coords_Healthbar_player2 = canvas.coords(Healthbar_player2)
            click = 0
            click2 = 0
            up_key = False
            down_key = False
            right_key = False
            left_key = False
            if Health_player2 <= 0:
                game_over()
            computer_player()
    def cheat_code2(event):
        global right_key
        right_key = True
        canvas.bind("<Left>", cheat_code3)
        computer_player()
    def cheat_code1(event):
        global down_key
        down_key = True
        canvas.bind("<Right>", cheat_code2)
        computer_player()

    def cheat_code(event):
        canvas.bind("<Down>", cheat_code1)
        global up_key
        up_key = True
        computer_player()

    def computer_player():
        if Health_player2 >= 0:
            global attacks, distance_btw_th_players, click2, number_attacks_done, defendnumber, state_player2, state_player1, Health_player1, player2_going_out, coords_of_player2, coords_of_player1, player2_ramming, Healthbar_player1, coords_Healthbar_player1, coords_Healthbar_player2
            if distance_btw_th_players > -200:
                player2_attack = attacks[random.randint(0, 4)]
                if player2_attack == 'punch' and click2 == 0:
                    if defendnumber == 0:
                        click2 = 1
                        state_player2 = 'punch'
                        canvas.itemconfig(player2_stance, image=img12)
                        canvas.move(player2_stance, -10, 10)
                        window.update()
                        time.sleep(0.25)
                        canvas.move(player2_stance, 10, -10)
                        if (state_player1 == 'stance' or state_player1 == 'run' or state_player1 == 'squat') and distance_btw_th_players > -148:            # Collision detection
                            Health_player1 -= 10
                            canvas.delete(Healthbar_player1)
                            Healthbar_player1 = canvas.create_rectangle(coords_Healthbar_player1[0], coords_Healthbar_player1[1], coords_Healthbar_player1[2] + 10*one_percent_health_player1, coords_Healthbar_player1[3], fill='green')
                            coords_Healthbar_player1 = canvas.coords(Healthbar_player1)
                            coords_Healthbar_player2 = canvas.coords(Healthbar_player2)

                        canvas.itemconfig(player2_stance, image=img3)
                        state_player2 = 'stance'
                        number_attacks_done += 1
                        click2 = 0
                        if Health_player1 <= 0:
                            game_over()
                    else:
                        click2 = 1
                        canvas.itemconfig(player2_stance, image=img12)
                        canvas.move(player2_stance, -10, 10)
                        window.update()
                        time.sleep(0.25)
                        canvas.move(player2_stance, 40, -10)
                        canvas.itemconfig(player2_stance, image=img3)
                        click2 = 0
                        number_attacks_done += 1
                        defendnumber = 0
                elif player2_attack == 'kick' and click2 == 0:
                    if defendnumber == 0:
                        click2 = 1
                        state_player2 = 'kick'
                        canvas.itemconfig(player2_stance, image=img13)
                        canvas.move(player2_stance, 0, -30)
                        window.update()
                        time.sleep(0.3)
                        canvas.move(player2_stance, 0, 30)
                        if (state_player1 == 'stance' or state_player1 == 'run' or state_player1 == 'jump') and distance_btw_th_players > -144:             # Collision detection
                            Health_player1 -= 10
                            canvas.delete(Healthbar_player1)
                            Healthbar_player1 = canvas.create_rectangle(coords_Healthbar_player1[0], coords_Healthbar_player1[1], coords_Healthbar_player1[2] + 10*one_percent_health_player1, coords_Healthbar_player1[3], fill='green')
                            coords_Healthbar_player1 = canvas.coords(Healthbar_player1)
                            coords_Healthbar_player2 = canvas.coords(Healthbar_player2)
                        canvas.itemconfig(player2_stance, image=img3)
                        number_attacks_done += 1
                        defendnumber = 0
                        state_player2 = 'stance'
                        click2 = 0
                        if Health_player1 <= 0:
                            game_over()
                    else:
                        click2 = 1
                        canvas.itemconfig(player2_stance, image=img13)
                        canvas.move(player2_stance, -10, -10)
                        window.update()
                        time.sleep(0.3)
                        canvas.move(player2_stance, 40, 10)
                        canvas.itemconfig(player2_stance, image=img3)
                        number_attacks_done += 1
                        click2 = 0

                elif player2_attack == 'jump' and click2 == 0:
                    click2 = 1
                    state_player2 = 'jump'
                    canvas.itemconfig(player2_stance, image=img14)
                    for i in range(10):
                        time.sleep(0.005)
                        canvas.move(player2_stance, 0, -10)
                        window.update()
                    for i in range(10):
                        time.sleep(0.005)
                        canvas.move(player2_stance, 0, 10)
                        window.update()

                    canvas.itemconfig(player2_stance, image=img3)
                    click2 = 0
                    state_player2 = 'stance'
                # elif player2_attack == 'defend:':
                #     coords_of_player1 = canvas.coords(player1_stance)
                #     coords_of_player2 = canvas.coords(player2_stance)
                #     distance_btw_th_players = coords_of_player1[0] - coords_of_player2[0]
                #     if distance_btw_th_players < -175:
                #         click2 = 1


                if number_attacks_done % 5 == 0:
                    canvas.itemconfig(player2_stance, image=img11)
                    state_player2 = 'run'
                    for i in range(3):
                        coords_of_player2 = canvas.coords(player2_stance)
                        time.sleep(0.2)
                        canvas.move(player2_stance, 20, 0)
                        window.update()
                        player_going_out2()
                        if player2_going_out == 1:              # Collision detection
                            player2_going_out = 0
                            canvas.move(player2_stance,-10,0)
                            break
                    canvas.itemconfig(player2_stance, image=img3)
                    state_player2 = 'stance'

            else:
                if click2 == 0:
                    canvas.itemconfig(player2_stance, image=img10)
                    state_player2 = 'run'
                    for i in range(5):
                        coords_of_player2 = canvas.coords(player2_stance)
                        coords_of_player1 = canvas.coords(player1_stance)
                        player_ramming2()
                        if player2_ramming == 1:                 # Collision detection
                            canvas.move(state_player2, 10, 0)
                            player2_ramming = 0
                            break
                        time.sleep(0.2)
                        canvas.move(player2_stance, -20, 0)
                        window.update()
                    canvas.itemconfig(player2_stance, image=img3)
                    state_player2 = 'stance'

    def defend(event):
        global distance_btw_th_players, coords_of_player1, coords_of_player2, click, defendnumber
        if click == 0:
            click = 1
            canvas.itemconfig(player1_stance, image=img15)
            window.update()
            time.sleep(0.5)
            canvas.itemconfig(player1_stance, image=img2)
            window.update()
            click = 0
            coords_of_player1 = canvas.coords(player1_stance)
            coords_of_player2 = canvas.coords(player2_stance)
            distance_btw_th_players = coords_of_player1[0] - coords_of_player2[0]
            if distance_btw_th_players > -175:
                defendnumber = 1
            computer_player()

    def leftKey(event):
        global distance_btw_th_players, coords_of_player1, coords_of_player2, state_player1, player1_going_out
        global click
        if click == 0:
            click = 1
            state_player1 = 'run'
            canvas.itemconfig(player1_stance, image=img7)
            for i in range(10):
                coords_of_player1 = canvas.coords(player1_stance)
                time.sleep(0.02)
                canvas.move(player1_stance, -5, 0)
                window.update()
                player_going_out1()
                if player1_going_out == 1:                                                                              # Collision detection
                    player1_going_out = 0
                    canvas.move(player1_stance,10,0)
                    break
            canvas.itemconfig(player1_stance, image=img2)
            click = 0
            state_player1 = 'stance'
            coords_of_player1 = canvas.coords(player1_stance)
            coords_of_player2 = canvas.coords(player2_stance)
            distance_btw_th_players = coords_of_player1[0] - coords_of_player2[0]
            computer_player()
            #player_going_out()

    def rightKey(event):
        global distance_btw_th_players, coords_of_player1, coords_of_player2, state_player1, player1_ramming
        global click
        if click == 0:
            click = 1
            state_player1 = 'run'
            canvas.itemconfig(player1_stance, image=img4)
            for i in range(10):
                coords_of_player2 = canvas.coords(player2_stance)
                coords_of_player1 = canvas.coords(player1_stance)
                player_ramming1()
                if player1_ramming == 1:                                                                                # Collision detection
                    canvas.move(state_player1, 30, 0)
                    player1_ramming = 0
                    break
                time.sleep(0.02)
                canvas.move(player1_stance, 5, 0)
                window.update()
            canvas.itemconfig(player1_stance, image=img2)
            click = 0
            state_player1 = 'stance'
            coords_of_player1 = canvas.coords(player1_stance)
            coords_of_player2 = canvas.coords(player2_stance)
            distance_btw_th_players = coords_of_player1[0] - coords_of_player2[0]
            # print(distance_btw_th_players)
            computer_player()
    def downKey(event):
        global distance_btw_th_players,coords_of_player1, coords_of_player2, state_player1
        global click
        if click == 0:
            click = 1
            state_player1 = 'squat'
            canvas.itemconfig(player1_stance, image=img6)
            canvas.move(player1_stance, 0, 30)
            window.update()
            time.sleep(0.25)
            canvas.move(player1_stance, 0, -30)
            canvas.itemconfig(player1_stance, image=img2)
            click = 0
            state_player1 = 'stance'
            coords_of_player1 = canvas.coords(player1_stance)
            coords_of_player2 = canvas.coords(player2_stance)
            distance_btw_th_players = coords_of_player1[0] - coords_of_player2[0]
            # print(distance_btw_th_players)
            computer_player()


    def upkey(event):
        global distance_btw_th_players, coords_of_player1, coords_of_player2, state_player1
        global click
        if click == 0:
            click = 1
            state_player1 = 'jump'
            canvas.itemconfig(player1_stance, image=img5)
            for i in range(20):
                time.sleep(0.01)
                canvas.move(player1_stance, 0, -5)
                window.update()
            for i in range(20):
                time.sleep(0.01)
                canvas.move(player1_stance, 0, 5)
                window.update()

            canvas.itemconfig(player1_stance, image=img2)
            click = 0
            state_player1 = 'stance'
            coords_of_player1 = canvas.coords(player1_stance)
            coords_of_player2 = canvas.coords(player2_stance)
            distance_btw_th_players = coords_of_player1[0] - coords_of_player2[0]
            # print(distance_btw_th_players)
            computer_player()
    def punchkey(event):
        global distance_btw_th_players, coords_of_player1, coords_of_player2, state_player2, Health_player2, state_player1, Healthbar_player2, coords_Healthbar_player2, coords_Healthbar_player1, click2
        global click
        if click == 0:
            click = 1
            state_player1 = 'attack'
            canvas.itemconfig(player1_stance, image=img8)
            canvas.move(player1_stance, 20, 0)
            window.update()
            time.sleep(0.25)
            canvas.move(player1_stance, -20, 0)
            if (state_player2 == 'stance' or state_player2 == 'run') and distance_btw_th_players > -129:                # Collision detection
                Health_player2 -= 10
                canvas.delete(Healthbar_player2)
                Healthbar_player2 = canvas.create_rectangle(coords_Healthbar_player2[0], coords_Healthbar_player2[1], coords_Healthbar_player2[2] + 10*one_percent_health_player2, coords_Healthbar_player2[3], fill='red2')
                coords_Healthbar_player1 = canvas.coords(Healthbar_player1)
                coords_Healthbar_player2 = canvas.coords(Healthbar_player2)

            canvas.itemconfig(player1_stance, image=img2)
            click = 0
            if Health_player2 <= 0:
                game_over()

            state_player1 = 'stance'
            coords_of_player1 = canvas.coords(player1_stance)
            coords_of_player2 = canvas.coords(player2_stance)
            distance_btw_th_players = coords_of_player1[0] - coords_of_player2[0]
            computer_player()


    def kickkey(event):
        global distance_btw_th_players, coords_of_player1, coords_of_player2, Health_player2, state_player1, state_player2, Healthbar_player2, coords_Healthbar_player2, coords_Healthbar_player1
        global click
        if click == 0:
            click = 1
            state_player1 = 'attack'
            canvas.itemconfig(player1_stance, image=img9)
            canvas.move(player1_stance, 20, -20)
            window.update()
            time.sleep(0.3)
            canvas.move(player1_stance, -20, 20)
            if (state_player2 == 'stance' or state_player2 == 'run') and distance_btw_th_players > -135:                # Collision detection
                Health_player2 -= 10

                canvas.delete(Healthbar_player2)
                Healthbar_player2 = canvas.create_rectangle(coords_Healthbar_player2[0], coords_Healthbar_player2[1], coords_Healthbar_player2[2] + 10*one_percent_health_player2, coords_Healthbar_player2[3], fill='red2')
                coords_Healthbar_player1 = canvas.coords(Healthbar_player1)
                coords_Healthbar_player2 = canvas.coords(Healthbar_player2)

            elif state_player2 == 'jump' and distance_btw_th_players > -145:                                            # Collision detection
                Health_player2 -= 10

            canvas.itemconfig(player1_stance, image=img2)
            click = 0
            if Health_player2 <= 0:
                game_over()

            state_player1 = 'stance'
            coords_of_player1 = canvas.coords(player1_stance)
            coords_of_player2 = canvas.coords(player2_stance)
            distance_btw_th_players = coords_of_player1[0] - coords_of_player2[0]
            # print(distance_btw_th_players)
            computer_player()


    window = Tk()
    width_canvas = 1280
    height_canvas = 720
    direction = None
    paused_var = 1
    nothing = 0
    click = 0
    click2 = 0
    player1_going_out = 0
    player2_going_out = 0
    player1_ramming = 0
    player2_ramming = 0
    defendnumber = 0
    number_attacks_done = 0
    if continuing_game == 0:
        Health_player1 = 100
        Health_player2 = 100
    if continuing_game == 1:
        Health_player1 = int(continue_list2[4][0])
        Health_player2 = int(continue_list2[5][0])
    state_player1 = 'stance'
    state_player2 = 'stance'
    canvas = Canvas(window, width=width_canvas, height=height_canvas, bg='black')
    canvas.pack()
    img1 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate2/Re37g5.v1.png')
    img2 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/stance.png')
    img3 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/stancep2.v4 (2).png')
    img4 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/runplayer1.png')
    img5 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/jump.png')
    img6 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/squat.png')
    img7 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/backwards.png')
    img8 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/punch.png')
    img9 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/kick3.png')
    img10 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/runplayer2.png')
    img11 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/backwardsplayer2.png.png')
    img12 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/punchplayer2.png')
    img13 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/kickplayer2.png')
    img14 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/jumpplayer2.png')
    img15 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/defend.png')
    img16 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/hp.png')
    img17 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/cheat code1.png')
    img18 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/cheat code2.png')
    img19 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/cheat code4.png')
    img20 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/cheat code5.png')
    img21 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/pixelated-3 (2).png')
    img22 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/game over.png')
    img23 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/game over.v1.png')
    img24 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/end menue player1.png')
    img25 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/end menue player2.png')
    img26 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/pixelated-1.png')
    img27 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/pixelated-2.png')
    img28 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/pixelated_fight.png')
    img29 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/player1_dead.png')
    img30 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/player2_dead.png')
    img31 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/fake_document.png')
    img32 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/you_won.png')
    img33 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/you.png')
    img34 = PhotoImage(file='C:/Users/VEDANT AGRAWAL/Desktop/karate/lose.png')

    lava_cave = canvas.create_image(width_canvas/2, height_canvas/2 + 15, image=img1)
    if continuing_game == 0:
        player1_stance = canvas.create_image(width_canvas/4, height_canvas*3/4 + 20, image=img2)
        player2_stance = canvas.create_image(width_canvas*3/4, height_canvas*3/4 + 10, image=img3)
    elif continuing_game == 1:
        player1_stance = canvas.create_image(continue_list2[0][0], continue_list2[0][1], image=img2)
        player2_stance = canvas.create_image(continue_list2[1][0], continue_list2[1][1], image=img3)
    Healthbarplayer1 = canvas.create_image(width_canvas/4, height_canvas/5 - 80, image=img16)
    Healthbarplayer2 = canvas.create_image(width_canvas*3/4, height_canvas/5 - 80, image=img16)
    canvas.create_text(width_canvas/4+ 60, height_canvas/5 - 50, text=f'{player1_name[:10].upper()}', font=('Arial Black', 15), fill='yellow')
    canvas.create_text(width_canvas*3/4+ 60, height_canvas/5 - 50, text=f'BUDDHU', font=('Arial Black', 15), fill='yellow')
    coords_of_player1 = canvas.coords(player1_stance)
    coords_of_player2 = canvas.coords(player2_stance)
    if continuing_game == 0:
        Healthbar_player1 = canvas.create_rectangle(302, 52, 459, 82, fill= 'green')
        Healthbar_player2 = canvas.create_rectangle(942, 52, 1099, 82, fill= 'red')
    if continuing_game == 1:
        Healthbar_player1 = canvas.create_rectangle(continue_list2[2][0], continue_list2[2][1], continue_list2[2][2], continue_list2[2][3], fill= 'green')
        Healthbar_player2 = canvas.create_rectangle(continue_list2[3][0], continue_list2[3][1], continue_list2[3][2], continue_list2[3][3], fill= 'red')
    pause_btn = Button(window, text='II',font=('Arial Black', 20) ,width=3, height=1, bd='10', command=lambda: paused(nothing))
    pause_btn.place(x=600, y= 40)
    start_3 = canvas.create_image(width_canvas/2, height_canvas/2, image=img21)
    window.update()
    time.sleep(0.5)
    canvas.delete(start_3)
    start_2 = canvas.create_image(width_canvas/2, height_canvas/2, image=img27)
    window.update()
    time.sleep(0.5)
    canvas.delete(start_2)
    start_1 = canvas.create_image(width_canvas/2, height_canvas/2, image=img26)
    window.update()
    time.sleep(0.5)
    canvas.delete(start_1)
    start_fight = canvas.create_image(width_canvas/2, height_canvas/2, image=img28)
    window.update()
    time.sleep(0.5)
    canvas.delete(start_fight)
    distance_btw_th_players = coords_of_player1[0] - coords_of_player2[0]
    if continuing_game ==0:
        canvas.itemconfig(player2_stance, image=img10)
        for i in range(15):
            time.sleep(0.1)
            canvas.move(player2_stance, -20, 0)
            window.update()
        canvas.itemconfig(player2_stance, image=img3)
    coords_Healthbar_player1 = canvas.coords(Healthbar_player1)
    coords_Healthbar_player2 = canvas.coords(Healthbar_player2)
    one_percent_health_player1 = (coords_Healthbar_player1[0] - coords_Healthbar_player1[2])/100
    if difficulty == 'hard':
        one_percent_health_player2 = (coords_Healthbar_player2[0] - coords_Healthbar_player2[2])/200
    else:
        one_percent_health_player2 = (coords_Healthbar_player2[0] - coords_Healthbar_player2[2])/100
    canvas.bind("<a>", leftKey)
    canvas.bind("<d>", rightKey)
    canvas.bind("<w>", upkey)
    canvas.bind("<s>", downKey)
    canvas.bind("<space>", upkey)
    if user_key_option == False:
        canvas.bind('<p>', punchkey)
        canvas.bind("<k>", kickkey)
    else:
        canvas.bind("<9>", punchkey)
        canvas.bind("<0>", kickkey)
    canvas.bind("<r>", defend)
    canvas.bind("<Up>", cheat_code)
    canvas.bind("<Escape>", Boss_key)
    canvas.focus_set()
    attacks = ['punch', 'kick', 'jump', 'punch', 'kick']
    player2_attack = None
    end_menue_player1 = None
    end_menue_player2 = None
    rect = None
    resume_btn = None
    reset_btn = None
    exit_btn = None
    fake_doc = None
    up_key = None
    down_key = None
    right_key = None
    left_key = None
    Boss_key_var = 1







    window.mainloop()