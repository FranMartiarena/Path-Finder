import pygame
import queue
import time
import tkinter as tk
from tkinter import StringVar
from tkinter import OptionMenu


all_paths = []
all_paths2 = []
invalids = []
obs = []
all_pos = []
contador = 0
repes = []


class StartPoint():

    def __init__(self):
        self.color = (0,255,0)
        self.pos = [sposx,sposy]
        self.path = []

    def add_all_pos(self):
        for x1 in range(rows):
            for y1 in range (rows):
                all_pos.append([x1,y1])

    def add_inv(self):

        for x1 in range(rows):
            for y1 in range (rows):
                if x1 == 0 or y1 == 0 or x1 == rows-1 or y1 == rows-1:
                    invalids.append([x1,y1])

    def draw_obs(self, surface):
        for pos in obs:
            pygame.draw.rect(surface, (0,0,0), ((pos[0])*dis+1, (pos[1])*dis+1, dis-1, dis-1 ))
            pygame.display.flip()



    def message_display(self):
        self.root2= tk.Tk()
        self.info = tk.Canvas(self.root2, width = 300, height = 40)
        self.info.pack()
        label3 = tk.Label(self.root2, text="Define Start Position with first click").pack()
        self.info.create_window(150, 35, window=label3)
        label4 = tk.Label(self.root2, text="Define End Position with second click").pack()
        self.info.create_window(150, 30, window=label4)
        label5 = tk.Label(self.root2, text="Define obstacles with third click and so on").pack()
        self.info.create_window(150, 20, window=label5)
        button2 = tk.Button(text="Let's Play!", command=self.quit).pack()
        self.info.create_window(150, 10, window=button2)
        self.root2.mainloop()

    def invalid_pos(self):
        self.root2= tk.Tk()
        self.info = tk.Canvas(self.root2, width = 300, height = 40)
        self.info.pack()
        label3 = tk.Label(self.root2, text="INVALID POSITION").pack()
        self.info.create_window(150, 35, window=label3)
        button2 = tk.Button(text="Again!", command=self.quit).pack()
        self.info.create_window(150, 10, window=button2)
        self.root2.mainloop()

    def quit(self):
        self.root2.destroy()

    def def_pos(self, surface):
        self.add_inv()
        global  sposx, sposy, eposx, eposy, contador
        surface.fill((255,255,255))
        fases = ["inicial","final","obstaculo"]
        click = False
        drawGrid(surface)
        if contador == 0:
            self.message_display()
            contador += 1
        for fase in range(2):
            corriendo = True
            while corriendo:
                #x, y = pygame.mouse.get_pos()
                #print("Elija la posicion ",fases[fase], "su mouse tiene posicion; ", x//dis, y//dis)
                pygame.init()
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.display.quit()
                        pygame.quit()
                        exit()

                    elif event.type == pygame.MOUSEBUTTONDOWN and fases[fase] == "inicial":
                        sposx, sposy = pygame.mouse.get_pos()
                        sposx = sposx // dis
                        sposy = sposy // dis
                        #print("las pocisiones iniciales son: ", sposx, sposy )
                        if [sposx,sposy] in invalids:
                            print("SOLO SE PUEDE DENTRO DEL RECUADRO NEGRO")
                            self.invalid_pos()
                            invalids.clear()
                            obs.clear()
                            all_paths.clear()
                            main()

                        else:
                            pygame.draw.rect(surface, self.color, ((sposx)*dis+1, (sposy)*dis+1, dis-1, dis-1 ))
                            print("Esta es la posicion inicial: ", sposx, sposy )
                            pygame.display.flip()
                            corriendo = False

                    elif event.type == pygame.MOUSEBUTTONDOWN and fases[fase] == "final":
                        eposx, eposy = pygame.mouse.get_pos()
                        eposx = eposx // dis
                        eposy = eposy // dis
                        if [eposx,eposy] in invalids:
                            print("SOLO SE PUEDE DENTRO DEL RECUADRO NEGRO")
                            self.invalid_pos()
                            invalids.clear()
                            obs.clear()
                            all_paths.clear()
                            main()

                        elif [eposx,eposy] == [sposx,sposy]:
                            print("NO SE PUEDE SOBRE LA POSICION INICIAL")
                            self.invalid_pos()
                            invalids.clear()
                            obs.clear()
                            all_paths.clear()
                            main()
                        else:
                            pygame.draw.rect(surface, EndPoint().color, ((eposx)*dis+1, (eposy)*dis+1, dis-1, dis-1 ))
                            print("Esta es la posicion final: ", eposx, eposy )
                            pygame.display.flip()
                            corriendo = False

        while len(obs) != obstaculos:
            oposx, oposy = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click = 1

                elif event.type == pygame.MOUSEBUTTONUP:
                    click = 0

                if click == 1:
                    oposx = oposx // dis
                    oposy = oposy // dis
                    pygame.draw.rect(surface, (0,0,0), ((oposx)*dis+1, (oposy)*dis+1, dis-1, dis-1 ))
                    pygame.display.flip()

                    if [oposx,oposy] not in invalids:
                        invalids.append([oposx,oposy])
                        obs.append([oposx,oposy])
                        #print("Agregue ",[oposx,oposy]," a ",obs," y a ",invalids)
                    if [oposx,oposy] == [sposx,sposy] or [oposx,oposy] == [eposx,eposy]:
                        print("NO SE PUEDE TAPAR LA ENTRADA NI SALIDA")
                        self.invalid_pos()
                        invalids.clear()
                        obs.clear()
                        all_paths.clear()
                        main()



                    if [sposx+1,sposy] in invalids and [sposx,sposy+1] in invalids  and [sposx-1,sposy] in invalids and [sposx,sposy-1] in invalids:
                        print("EL CUBO ESTA ENCERRADO :(")
                        self.invalid_pos()
                        invalids.clear()
                        obs.clear()
                        all_paths.clear()
                        main()

                    if [eposx+1,eposy] in invalids and [eposx,eposy+1] in invalids  and [eposx-1,eposy] in invalids and [eposx,eposy-1] in invalids:
                        print("EL CUBO ESTA ENCERRADO :(")
                        self.invalid_pos()
                        invalids.clear()
                        obs.clear()
                        all_paths.clear()
                        main()



        self.move(surface)

    def draw_paths(self, surface, sum):
        self.pos = [sposx,sposy]

        #self.draw_obs(surface)

        for move in all_paths[sum]:

            if move[-1] == "L" :
                self.pos[0] -= 1


            elif move[-1] == "R":
                self.pos[0] += 1


            elif move[-1] == "U":
                self.pos[1] -= 1


            elif move[-1] == "D":
                self.pos[1] += 1
            pygame.draw.rect(surface, (0,0,255), (self.pos[0]*dis+1, self.pos[1]*dis+1, dis-1, dis-1))
        #print("Este es el camino: ", all_paths[sum], "que termina en ", self.pos)

        pygame.draw.rect(surface, (255,69,0), (self.pos[0]*dis+1, self.pos[1]*dis+1, dis-1, dis-1))
        pygame.display.flip()



    def draw_correct_path(self, surface, right_path):
        all_paths2.clear()
        surface.fill((255,255,255))
        while True:
            drawGrid(surface)
            self.draw_obs(surface)
            #print(self.pos)
            self.pos = [sposx,sposy]
            #print(self.pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    invalids.clear()
                    obs.clear()
                    all_paths.clear()
                    main()

            for move in right_path[0]:
                if move == "L" :
                    pygame.draw.rect(surface, (255,69,0), (self.pos[0]*dis+1, self.pos[1]*dis+1, dis-1, dis-1))
                    self.pos[0] -= 1
                    pygame.draw.rect(surface, (255,69,0), (self.pos[0]*dis+1, self.pos[1]*dis+1, dis-1, dis-1))
                    #print("Estoy dibujando, ",right_path[0]," y voy por la letra l, que lleva a la posicion ", self.pos)


                elif move == "R":
                    pygame.draw.rect(surface, (255,69,0), (self.pos[0]*dis+1, self.pos[1]*dis+1, dis-1, dis-1))
                    self.pos[0] += 1
                    pygame.draw.rect(surface, (255,69,0), (self.pos[0]*dis+1, self.pos[1]*dis+1, dis-1, dis-1))
                    #print("Estoy dibujando, ",right_path[0]," y voy por la letra r, que lleva a la posicion ", self.pos)


                elif move == "U":
                    pygame.draw.rect(surface, (255,69,0), (self.pos[0]*dis+1, self.pos[1]*dis+1, dis-1, dis-1))
                    self.pos[1] -= 1
                    pygame.draw.rect(surface, (255,69,0), (self.pos[0]*dis+1, self.pos[1]*dis+1, dis-1, dis-1))
                    #print("Estoy dibujando, ",right_path[0]," y voy por la letra u, que lleva a la posicion ", self.pos)


                elif move == "D":
                    pygame.draw.rect(surface, (255,69,0), (self.pos[0]*dis+1, self.pos[1]*dis+1, dis-1, dis-1))
                    self.pos[1] += 1
                    pygame.draw.rect(surface, (255,69,0), (self.pos[0]*dis+1, self.pos[1]*dis+1, dis-1, dis-1))
                    #print("Estoy dibujando, ",right_path[0]," y voy por la letra d, que lleva a la posicion ", self.pos)
                pygame.display.flip()



    def valid_move(self, moves):


        self.pos = [sposx,sposy]


        for move in moves:
            invalids.append(self.pos.copy())#Agrega la posicion actual, para que no la repita

            if move == "L" :
                self.pos[0] -= 1

            elif move == "R":
                self.pos[0] += 1

            elif move == "U":
                self.pos[1] -= 1

            elif move == "D":
                self.pos[1] += 1


        if self.pos in invalids or self.pos in obs:
            return False
        else:
            invalids.append(self.pos.copy())
            all_pos.append(self.pos.copy())
            #self.draw_path(self.pos)
            #self.pos = self.ppos#so as to connect with end
            #print(invalids)
            #print("Este es el recorrido ",moves," que termina en la posicion; ",self.pos)
            return True


    def End(self, surface):
        right_path = []

        #print(self.pos, EndPoint().pos)

        for path in all_paths2:
            self.pos = [sposx, sposy]
            for move in path:

                if move == "L" :
                    self.pos[0] -= 1

                elif move == "R":
                    self.pos[0] += 1

                elif move == "U":
                    self.pos[1] -= 1

                elif move == "D":
                    self.pos[1] += 1

            if self.pos == EndPoint().pos:
                print("Este es el ganador: ", path, "con posicion ",self.pos)
                right_path.append(path)
                self.draw_correct_path(surface, right_path)
            all_paths2.remove(path)

        return False

    def move(self, surface):

        nums = queue.Queue()
        nums.put("")
        add = ""
        put = ""
        sum = 0
        cor = True
        while self.End(surface) == False:
        #for x in range(1000):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()

            add = nums.get()
            #print(self.pos, put)
            for x in ["L","R","U","D"]:
                put = add + x
                if self.valid_move(put):
                    all_paths.append(put)
                    all_paths2.append(put)
                    #self.path.append(put)
                    #print("Este es el recorrido ",put," con posicion ", self.pos)
                    self.draw_paths(surface, sum)
                    nums.put(put)

                    sum += 1

class EndPoint():

    def __init__(self):
        self.color = (255,0,0)
        self.pos = [eposx,eposy]




def drawGrid(surface):

    positions = []


    black = []

    x = 0
    y = 0

    for i in range(rows):
        x = x + dis
        y = y + dis

        pygame.draw.line(surface, (0,0,0), (x,0),(x,width))
        pygame.draw.line(surface, (0,0,0), (0,y),(width,x))


    for x1 in range(rows):
        for y1 in range (rows):
            if x1 == 0 or y1 == 0 or x1 == rows-1 or y1 == rows-1:
                pygame.draw.rect(surface, (0,0,0), (x1*dis+1, y1*dis+1, dis-1, dis-1 ))

    #pygame.draw.rect(surface, StartPoint().color, ((StartPoint().pos[0])*dis+1, (StartPoint().pos[1])*dis+1, dis-1, dis-1 ))
    #pygame.draw.rect(surface, EndPoint().color, ((EndPoint().pos[0])*dis+1, (EndPoint().pos[1])*dis+1, dis-1, dis-1 ))

    pygame.display.flip()





def main():
    global width, rows, running, dis, sposx, sposy, eposx, eposy, oposx, oposy, obstaculos
    sposx = 0
    sposy = 0
    eposx = 0
    eposy = 0
    oposx = 0
    oposy = 0

    width = 500
    #pygame.display.quit()
    dis = width // rows
    win = pygame.display.set_mode((width, width))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
            else:
                StartPoint().def_pos(win)

    pass


root= tk.Tk()
ask_display = tk.Canvas(root, width = 400, height = 300)
ask_display.pack()
entry1 = tk.Entry (root)
ask_display.create_window(200, 100, window=entry1)
label1 = tk.Label(root, text="Type the amount of obstacles to put:")
ask_display.create_window(200, 50, window=label1)
label2 = tk.Label(root, text="Select the grid's size:")
ask_display.create_window(200, 150, window=label2)
def get_input():
    global rows, obstaculos
    x1 = int(entry1.get())
    x2 = variable.get()
    #if type(x1) is float or type(x1) is str:
        #label2 = tk.Label(root, text=type(x1))
        #ask_display.create_window(200, 250, window=label2)
    #else:
    label2 = tk.Label(root, text="")
    ask_display.create_window(200, 250, window=label2)
    obstaculos = int(x1)
    if x2 == "Small" and x1 < 29:
        rows = 10
        root.destroy()
    elif x2 == "Medium" and x1 < 150:
        rows = 20
        root.destroy()
    elif x2 == "Large(slower)" and x1 < 400:
        rows = 50
        root.destroy()
    else:
        label2 = tk.Label(root, text="Number of obstacles exceeded")
        ask_display.create_window(200, 250, window=label2)


variable = StringVar(root)
variable.set("Small")
menu = OptionMenu(root, variable, "Small", "Medium", "Large(slower)")
ask_display.create_window(200, 200, window=menu)
button1 = tk.Button(text='Submit', command=get_input)
ask_display.create_window(200, 275, window=button1)
root.mainloop()


main()
