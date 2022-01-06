#######################################
######## VERSION PYTHON 3.9.2 #########
#######################################
#Info programa principal
"""
Costa Rica
Instituto Tecnológico de Costa Rica
Área Académica de Ingeniería en Computadores
Taller de Programación, 2021, Grupo 2
Milton Villegas Lemus
Version Python 3.9.2
Versión del codigo 1.0
Editor: Geovanny García Downing, 2020092224
Entradas: no aplica
Salidas: ventana en ciclo TK
Restricciones: no aplica
Modulos usados: guardar_archivo, leer_archivo, close, cargar_imagen, cargarMP3, reprod_FX, detener_cancion, reprod_cancion, reproducir_salida, limitador, Vnivel1Check, Vnivel2Check, Vnivel3Check, checkPoints, mensajePuntos, cronom, reset_time, pause_time, Vnivel1, Vnivel2, Vnivel3, info_adicional, mejores_puntajes, autodocumentacion
Modulos modificados: Se reutilizó código de la tarea, cargar_imagen, abarcado por José Fernando Morales en el taller
Codigo modificado facilitado por: Jose Fernando Morales
"""
#Importacion de las funciones necesarias para el proyecto
from tkinter import *
from os import path
from time import *
from pygame import mixer
from pygame.constants import USEREVENT
from random import *

#Creación de las 3 fuentes más utilizadas en el proyecto, para mayor facilidad
fnt=("Candara Light",20)
fnt2=("Candara Light",12)
fnt3=("Candara Light",16)

#Variables de tiempo (horas , minutos, sgundos, FLAG)
timeFlag=0 #FLAG tiempo (proceso de cambio de Label)
h=0 
m=0
s=0

#Creación de FLAGS para disparar, mover nave y señal de keyrelease
shootFlag=True
moveFlag=False
keyFlag=True

#Texto de la  ventana de información adicional
about="""
Costa Rica
Instituto Tecnológico de Costa Rica
Área Académica de Ingeniería en Computadores
Taller de Programación, 2021, Grupo 2
Milton Villegas Lemus
Versión 1.0
Geovanny García Downing
"""
#Listas que contienen puntajes y nombres del top 5 puntajes
puntajes=[]
nombres=[]

def guardar_archivo(archivo, i=0): #Función para guardar archivo de texto
    global nombres, puntajes
    try:
        archivo.write(nombres[i]+(str(puntajes[i]).zfill(2))+"\n") #guarda nombrepuntaje en cada linea de texto, los últimos 2 caractéres son números
        guardar_archivo(archivo,i+1)
    except:
        archivo.close()
        
def leer_archivo(archivo, i=1): #Función para leer el archrivo de texto con puntajes y nombre
    global nombres, puntajes
    try:
        line=archivo.readline() #toma los últimos 2 digitos de cada line y los toma como el puntaje, el resto es el nombre
        puntajes.append(int(line[-3:]))
        nombres.append(line[:-3])
        leer_archivo(archivo, i+1)
    except:
        archivo.close()
try:
    archivo=open("puntajes.txt","r+") #apertura de archivo en caso de existir
except:
    archivo=open("puntajes.txt","w+") #apertura de archivo en caso de no existir
leer_archivo(archivo)
##############################################################################################################
                                             # Pantalla Principal #
##############################################################################################################
ventana=Tk() #Creación de ventana y tamaño
ventana.title("WARTEC")
ventana.minsize(600,800) 
ventana.resizable(width=NO, height=NO) 

def close(): #función de cierre de la ventana principal
    global ventana 
    reproducir_salida() #reproduce el efecto Goodbye
    sleep(0.9) #tiempo para que se pueda reproducir el efecto
    ventana.destroy() 

def cargar_img(nombre):
    ruta=path.join("assets",nombre) #crea acceso a la ruta assets dentro de la carpeta del programa
    img=PhotoImage(file=ruta) #importa la imagen
    return img #retorna la imagen

C_app=Canvas(ventana, width=600, height=800) #creación del canvas de la ventana principal
C_app.place(x=0,y=0) 

C_app.fondo=cargar_img("fondo1.png") #se carga imagen para fondo
fondo = C_app.create_image(0,0,anchor=NW, image=C_app.fondo)

def reprod_fx(MP3):
    mixer.init()
    sound=mixer.Sound("assets/"+MP3)
    sound.play()

def detener_cancion(): #función para detener reproducción
    mixer.music.stop()

def reprod_cancion(MP3): #función para reproducir canción
    mixer.init()
    detener_cancion()
    playlist = []
    playlist.append (MP3)
    song=playlist.pop() 
    mixer.music.load (song)  
    mixer.music.queue (song)
    mixer.music.set_endevent (USEREVENT)   
    mixer.music.play(-1)
    
def reproducir_salida(): #función efecto de salida
    reprod_fx("goodbye.mp3")

L_about=Label(ventana, font=fnt, bg="#850458", fg="#ffffff", text="Ingrese su nombre")
L_about.place(x=300,y=150,anchor="center")

#Modificado del código de: Samuel Enrique Molina Bermudez
entry_text = StringVar() #string dinámico
E_nombre= Entry(ventana, width=14, font=fnt, textvariable = entry_text, justify=CENTER)
E_nombre.place(x=200,y=220,anchor="center")

def limitador(entry_text): #limita el texto a 12 caracteres
    if entry_text.get()!="":
        entry_text.set(entry_text.get()[:12])

entry_text.trace("w", lambda *args: limitador(entry_text))

def Vnivel1Check(): #check del box de nombre que no esté vacío y corre nivel 1
    if entry_text.get()=="":
        msgbox=Toplevel()
        msgbox.minsize(200,200)
        L_saludo=Label(msgbox,text="Debe ingresar un nombre",font=fnt2)
        L_saludo.place(x=100, y=100, anchor="center")
    else:
        Vnivel1()

def Vnivel2Check(): #check del box de nombre que no esté vacío y corre nivel 2
    if entry_text.get()=="":
        msgbox=Toplevel()
        msgbox.minsize(200,200)
        L_saludo=Label(msgbox,text="Debe ingresar un nombre",font=fnt2)
        L_saludo.place(x=100, y=100, anchor="center")
    else:
        Vnivel2()

def Vnivel3Check(): #check del box de nombre que no esté vacío y corre nivel 3
    if entry_text.get()=="":
        msgbox=Toplevel()
        msgbox.minsize(200,200)
        L_saludo=Label(msgbox,text="Debe ingresar un nombre",font=fnt2)
        L_saludo.place(x=100, y=100, anchor="center")
    else:
        Vnivel3()

def checkPoints(Pts, Nombre, I): #guarda el puntaje en la lista
    global puntajes, nombres
    if Pts>0:
        if puntajes!=[]: #si está vacía nada más agrega al final
            try: #si la lista se sale de rango
                puntajes[I]
                if puntajes[I]<=Pts: #compara cada valor con los puntos
                    puntajes=puntajes[:I]+[Pts]+puntajes[I:] #quiebra lista y mete en medio
                    nombres=nombres[:I]+[Nombre]+nombres[I:]
                    try:
                        puntajes[5] #en caso de agregar un extra espacio, se elimina, quedando sólo 5
                        puntajes=puntajes[:-1]
                    except:
                        pass
                    archivo=open("puntajes.txt","w+") #guarda en archivo
                    guardar_archivo(archivo)
                    reprod_fx("congratulations.mp3")
                    return mensajePuntos(Pts,I+1) #i+1 es la posición en la que el jugador quedó y llama a la función que envía mensaje a ganador de nuevo record
                else:
                    return checkPoints(Pts, Nombre, I+1) #llamada recursiva
            except: #si se sale de rango y el i es menor a 5 se agrega al final
                if I<5:
                    nombres+=[Nombre]
                    puntajes+=[Pts]
                    archivo=open("puntajes.txt","w+") #guarda archivo
                    guardar_archivo(archivo)
                    reprod_fx("congratulations.mp3")
                    return mensajePuntos(Pts,I+1) #llama a la función que envía mensaje a ganador de nuevo record
                else:
                    pass
        else:
            nombres+=[Nombre] #agrega al final en caso de vacía
            puntajes+=[Pts]
            archivo=open("puntajes.txt","w+") #guarda en archivo
            guardar_archivo(archivo)
            reprod_fx("congratulations.mp3")
            return mensajePuntos(Pts,I+1)

def mensajePuntos(Pts,Pos): #función que genera mensaje al ganador de nuevo record
    msgbox=Toplevel()
    msgbox.minsize(600,600)
    L_score=Label(msgbox,text=f"Usted se encuentra entre \nlos mejores puntajes,\nobtuvo la posición {Pos} \ncon {Pts} puntos",font=("Candara Light",24))
    L_score.place(x=300, y=300, anchor="center")

def cronom(Label): #función que genera el cronómetro
    global timeFlag, h, m, s
    #Verificamos si los segundos y los minutos son mayores a 60
    if s >= 60:
        s=0
        m+=1
        if m >= 60:
            m=0
            h+=1
    # iniciamos la cuenta progresiva de los segundos
    Label['text'] ="Time: "+str(h)+":"+str(m).zfill(2)+":"+str(s).zfill(2) #modifica dinámicamente el texto del label de tiempo
    s+=1
    timeFlag=Label.after(1000, cronom, (Label)) #llamada recursiva cada 1 segundo

def reset_time(): #resetea las variables de tiempo a 0
    global h, m, s
    h=0
    m=0
    s=0

def pause_time(Label): #pausa el cronómetro
    global timeFlag
    Label.after_cancel(timeFlag)

reprod_cancion("assets\\title2.wav") #reproduce musica de fondo con 
##############################################################################################################
                                                # Nivel 1 #
##############################################################################################################

def Vnivel1():
    """
    Costa Rica
    Instituto Tecnológico de Costa Rica
    Área Académica de Ingeniería en Computadores
    Taller de Programación, 2021, Grupo 2
    Milton Villegas Lemus
    Version Python 3.9.2
    Versión del codigo 1.0
    Editor: Geovanny García Downing, 2020092224
    Entradas: no aplica
    Salidas: ventana en ciclo TopLevel
    Restricciones: no aplica
    Modulos usados: end, back, close, checkBoss, SWAP, boss_move, collision, laser_move, smooth_move, create_laser, move_ship, stop_shoot
    Modulos modificados: Se reutilizó código de la tarea, cargar_imagen, abarcado por José Fernando Morales en el taller
    Codigo modificado facilitado por: Jose Fernando Morales
    """
    global ventana, E_nombre, puntajes
    FLAG=True

    #variables de vida, puntos, vida del boss, entre otras banderas de movimiento y embestida
    pts=0
    life=50
    bolife=30
    bossco=[]
    LRFlag=True
    embestida=True
    notdead=True

    #creación de subventana Nivel 1 de música y características por Toplevel
    ventana.withdraw() #oculta ventana principal
    nivel1=Toplevel() 
    nivel1.title("Nivel 1") 
    nivel1.minsize(600,800)
    nivel1.resizable(width=NO, height=NO)
    reprod_cancion("assets\\boss1.wav")

    def end(): #función que calcula los bonuses en caso de finalizar, no hay bonuses en cierres forzados
        global ventana, h, m, s
        nonlocal pts, nombre, life
        if life==50: #si la vida es 50 entonces se obtiene +10 bonus
            pts+=10
        if h==0 and m==0 and s<=30: #si lo hizo en 30 segs +20 bonus
            pts+=20
        reset_time()
        checkPoints(pts, nombre, 0)
        detener_cancion()
        ventana.deiconify() #reaparece la ventana principal
        nivel1.destroy() #cierra la subventana nivel1
        reprod_cancion("assets\\title2.wav")
    
    def back(): #función del botón BACK
        global ventana
        nonlocal pts, nombre
        reset_time()
        checkPoints(pts, nombre, 0)
        detener_cancion()
        ventana.deiconify() #reaparece la ventana principal
        nivel1.destroy() #cierra la subventana nivel1
        reprod_cancion("assets\\title2.wav")

    def close(): #función de cierre
        nonlocal nivel1, FLAG
        global ventana
        FLAG=False #da la señal para detener animación
        detener_cancion()
        reproducir_salida() #reproduce efecto de salida
        sleep(0.9) #tiempo de ejecución del efecto
        nivel1.destroy() #cierra suventana y luego ventana
        ventana.destroy()

    #Creación canvas del nivel1 
    C_nivel1=Canvas(nivel1, width=600, height=800)
    C_nivel1.place(x=0,y=0)

    #Asiganción fondo subventana
    C_nivel1.fondoT=cargar_img("fondo2.png")
    fondoT = C_nivel1.create_image(0,0,anchor=NW, image=C_nivel1.fondoT)

    #Creación del botón BACK
    C_app.back=cargar_img("back.png") #carga imagen para elbotón
    Btn_back=Button(C_nivel1, text='saludar',image=C_app.back, font=fnt, command=back)
    Btn_back.place(x=600,y=0, anchor=NE)
    
    #obtiene el nombre del entry
    nombre=E_nombre.get()
    
    #Labels con info del jugador
    Label_nombre=Label(C_nivel1, font=fnt3, bg="#850458", fg="#ffffff", text=nombre+"'s score: "+str(pts)+" pts")
    Label_nombre.place(x=0,y=0,anchor=NW)

    Label_life=Label(C_nivel1, font=fnt3, bg="#850458", fg="#ffffff", text=nombre+"'s life: "+str(life)+" pts")
    Label_life.place(x=0,y=50,anchor=NW)

    Label_boss=Label(C_nivel1, font=fnt3, bg="#850458", fg="#ffffff", text="Boss' life: "+str(bolife)+" pts")
    Label_boss.place(x=0,y=100,anchor=NW)

    Label_time=Label(C_nivel1, font=fnt3, bg="#850458", fg="#ffffff")
    Label_time.place(x=600,y=50,anchor=NE)
    cronom(Label_time)#llamada al cronómetro
    
    #Barra de vida
    Label_bar=Label(C_nivel1, font=fnt2, bg="#0bfc03", fg="#0bfc03", text="".zfill(20))
    Label_bar.place(x=300,y=100,anchor="center")

    #carga imagen del boss y la versión dañada y los pone en una lista
    C_nivel1.boss=cargar_img("boss2.png")
    C_nivel1.damage=cargar_img("damage2.png")
    images=[C_nivel1.boss,C_nivel1.damage]

    boss = C_nivel1.create_image(300,200,anchor="center", image=C_nivel1.boss, tags="boss")#crea al boss
    
    def checkBoss(): #checa que ni el boss ni el jugador estén muertos
        nonlocal bolife, life, C_nivel1, life, Label_time, embestida, notdead
        if bolife<=0 or life<=0 and notdead:
            notdead=False
            embestida=None #termina el ciclo recursivo de movimiento
            pause_time(Label_time) #pausa tiempo
            reprod_fx("explo4.mp3") #reproduce explosión 
            msgbox=Toplevel() #mensaje de juego finalizado
            msgbox.minsize(600,600)
            if life==0:
                L_saludo=Label(msgbox,text="JUEGO\nFINALIZADO\nPerdió",font=("Candara Light",30))
                L_saludo.place(x=300, y=300, anchor="center")
            else:
                L_saludo=Label(msgbox,text="JUEGO\nFINALIZADO\nGanó",font=("Candara Light",30))
                L_saludo.place(x=300, y=300, anchor="center")
            def fin(): #llama a la función end luego de 5 segundos
                nonlocal msgbox
                msgbox.destroy()
                end()
            C_nivel1.after(5000,fin) 
        else:
            return True
            
    def SWAP():
        nonlocal embestida, LRFlag, bolife, Label_boss, Label_bar #genera num random para ataque de embestida
        if embestida:
            n=randint(1,10)
            if n%3==0:
                reprod_fx("mothership.mp3") #reproduce efectos
                embestida=False #usé lógica invertida, ataca cuando es falso
                LRFlag=None
                bolife-=1
                Label_boss["text"]="Boss' life: "+str(bolife)+" pts" #dinamiza el label de vida del boss
                Label_bar["text"]="".zfill(int(20-(20/30)*(30-bolife))) #función lineal entre puntos de vida y barra de vida
            def callback():
                SWAP() #cada dos segundos hace llamada recursiva
            C_nivel1.after(2000 , callback)

    def boss_move(i=0,collFlag=True):
        nonlocal C_nivel1, shipco, boss, LRFlag, embestida, bossco, bolife, life, Label_life, nombre, images2
        bossco=C_nivel1.coords(boss) #coordenadas en tiempo real
        shipco=C_nivel1.coords(ship)
        coll=colision(shipco[0],shipco[1],100,88,bossco[0],bossco[1],175,175) #verifica colisión de nave con jefe
        if coll and collFlag and embestida==False and life>0: #si colisiona una vez, se levanta la bandera para que no tome una colisón como varias
            collFlag=False #bandera
            C_nivel1.itemconfig("ship",image=images2[1]) #cambia a nave dañada
            def normal(): #vuelve a nave normal después de medio segundo
                nonlocal C_nivel1, images2
                C_nivel1.itemconfig("ship",image=images2[0])
            C_nivel1.after(500,normal)
            reprod_fx("explo3.mp3") #sonido de choque
            life-=10
            Label_life["text"]=nombre+"'s life: "+str(life)+" pts" #actualización de vida en label vida
            checkBoss()
        if coll==False:#llamada a bandera
            collFlag=True
        if embestida:#movimiento derecha izquiera
            if LRFlag: #flag para evira movimiento en embestida
                C_nivel1.move(boss,i,0)
                def callback():
                    boss_move(3,collFlag)
                C_nivel1.after(5 , callback)
                if bossco[0]>600:
                    LRFlag=False
            else:
                C_nivel1.move(boss,i,0)
                def callback():
                    boss_move(-3,collFlag)
                C_nivel1.after(5 , callback)
                if bossco[0]<0:
                    LRFlag=True
        elif embestida==False and LRFlag!=None: #embestida
            if LRFlag:
                C_nivel1.move(boss,0,i)
                def callback():
                    boss_move(10,collFlag)
                C_nivel1.after(1 , callback)
                if bossco[1]>700:
                    LRFlag=False
            else:
                C_nivel1.move(boss,0,i)
                def callback():
                    boss_move(-2,collFlag)
                C_nivel1.after(1 , callback)
                if bossco[1]<200:
                    embestida=True
                    checkBoss() #final de la embestida, checa si sigen ambos con vida
        elif LRFlag==None: #reinicia movimiento luego de embestida
            def espera():   
                nonlocal LRFlag
                LRFlag=True
                boss_move()
            C_nivel1.after(500, espera)

    def colision(x1,y1,w1,h1,x2,y2,w2,h2): #verifica colisiones mediante comparaciones de rangos en un área coordenadas, ancho y alto
        if x1>x2+w2 or x1+w1<x2 or y1>y2+h2 or y1+h1<y2:
            return False
        else:
            return True
   
   #carga el ship y el ship dañado y los agrega a una lista
    C_nivel1.ship=cargar_img("ship.png")
    ship = C_nivel1.create_image(300,750,anchor="center", image=C_nivel1.ship, tags="ship")
    C_nivel1.laser=cargar_img("laser.png") #carga laser
    C_nivel1.dmgShip=cargar_img("dmgShip.png")
    images2=[C_nivel1.ship,C_nivel1.dmgShip]
    shipco=C_nivel1.coords(ship)

    def laser_mov(i,objeto,collFlag=True): #mueve el laser
        nonlocal C_nivel1, shipco, bossco, bolife, pts, Label_boss, Label_nombre, nombre, images, Label_bar
        lasco=C_nivel1.coords(objeto) #coordenadas en tiempo real
        if colision(lasco[0],lasco[1],50,89,bossco[0],bossco[1],175,175) and collFlag and bolife>0: #verifica colisión
            Label_bar["text"]="".zfill(int(20-(20/30)*(30-bolife))) #actualiza barra de vida
            collFlag=False
            C_nivel1.itemconfig("boss",image=images[1]) # si hay colisoón muestra nave dañada
            def normal():
                nonlocal C_nivel1, images
                C_nivel1.itemconfig("boss",image=images[0]) #vuelve a nave normal
            C_nivel1.after(500,normal)
            reprod_fx("hit2.mp3") #sonido de daño
            bolife-=1 #cambio en vida y puntos
            pts+=1
            Label_boss["text"]="Boss' life: "+str(bolife)+" pts"
            Label_nombre["text"]=nombre+"'s score: "+str(pts)+" pts"
            checkBoss() #checa que sigan vivos
        if lasco[1]>-100:
            C_nivel1.move(objeto,0,i)
            def callback():
                laser_mov(i-0.1 ,objeto,collFlag)
            C_nivel1.after(5 , callback)
    
    def smooth_mov(objeto,i,j): #cree este algoritmo para que el movimiento de la nave fuera más suave
        global moveFlag #bandera, produce movimiento hasta keyrelease
        m=C_nivel1.coords(objeto)
        if ((i==-1 and 550>m[0]) or (i==1 and m[0]>50) or (j==-1 and 751>m[1]) or (j==1 and m[1]>100)) and moveFlag:
            C_nivel1.move(objeto,-i,-j)
            def callback():
                smooth_mov(objeto,i,j)
            C_nivel1.after(2, callback)

    def create_laser(canva,imagen) : #crea un laser cada vez que se dispara
        reprod_fx("metal.mp3") #sonido de disparo
        laser = canva.create_image(shipco[0],shipco[1],anchor="center", image=imagen)
        return laser_mov(0,laser)

    def move_ship(evento):  #verifica lo que toca el usuario en el teclado
        nonlocal C_nivel1, shipco, ship
        global shootFlag, keyFlag, moveFlag
        if keyFlag:
            moveFlag=True #inicia movimiento hasta keyrelease
            if evento.keysym=="Left":
                smooth_mov(ship,1,0)
            elif evento.keysym=="Right":
                smooth_mov(ship,-1,0)
            elif evento.keysym=="Up":
                smooth_mov(ship,0,1)
            elif evento.keysym=="Down":
                smooth_mov(ship,0,-1)
            keyFlag=False #evita varias llamadas por estar presionado
        elif evento.keysym=="space":
            if shootFlag:
                shipco=C_nivel1.coords(ship)
                create_laser(C_nivel1,C_nivel1.laser)
                shootFlag=False #bloquea disparo presionado

    def stop_shoot(evento):
        global shootFlag, moveFlag, keyFlag #modifica ciertas banderas que dependen del keyreleas
        nonlocal life, bolife
        if evento.keysym=="space" and bolife>0 and life>0:
            shootFlag=True #puede disparar luego de soltar mientras esté vivo
        else:
            moveFlag=False #deja de moverse
            keyFlag=True #se puede leer la presion de una tecla
    #uso de las funciones de movimiento y embestida
    boss_move()      
    C_nivel1.after(2000,SWAP)
    #eventos de press y release 
    nivel1.bind('<KeyPress>', move_ship)
    nivel1.bind('<KeyRelease>', stop_shoot)
    #cierre protocolo
    nivel1.protocol("WM_DELETE_WINDOW",close) 

##############################################################################################################
                                                # Nivel 2 #
##############################################################################################################

def Vnivel2():
    """
    Costa Rica
    Instituto Tecnológico de Costa Rica
    Área Académica de Ingeniería en Computadores
    Taller de Programación, 2021, Grupo 2
    Milton Villegas Lemus
    Version Python 3.9.2
    Versión del codigo 1.0
    Editor: Geovanny García Downing, 2020092224
    Entradas: no aplica
    Salidas: ventana en ciclo TopLevel
    Restricciones: no aplica
    Modulos usados: end, back, close, checkBoss, boss_move, collision, laser_move, smooth_move, create_laser, move_ship, stop_shoot, shooting, laser_attack 
    Modulos modificados: Se reutilizó código de la tarea, cargar_imagen, abarcado por José Fernando Morales en el taller
    Codigo modificado facilitado por: Jose Fernando Morales
    """
    global ventana, E_nombre, puntajes
    FLAG=True

    #variables de vida, puntos, vida del boss, entre otras banderas de movimiento y embestida
    pts=0
    life=50
    bolife=40
    bossco=[]
    movimiento=True
    notdead=True

    #creación de subventana nivel 2 de música y características por Toplevel
    ventana.withdraw() #oculta ventana principal
    nivel2=Toplevel() 
    nivel2.title("Nivel 2") 
    nivel2.minsize(600,800)
    nivel2.resizable(width=NO, height=NO)
    reprod_cancion("assets\\boss2.wav")

    def end(): #función que calcula los bonuses en caso de finalizar, no hay bonuses en cierres forzados
        global ventana, h, m, s
        nonlocal pts, nombre, life
        if life==50: #si la vida es 50 entonces se obtiene +10 bonus
            pts+=10
        if h==0 and m==0 and s<=30: #si lo hizo en 30 segs +20 bonus
            pts+=20
        reset_time()
        checkPoints(pts, nombre, 0)
        detener_cancion()
        ventana.deiconify() #reaparece la ventana principal
        nivel2.destroy() #cierra la subventana nivel1
        reprod_cancion("assets\\title2.wav")

    def back(): #función del botón BACK
        global ventana, h, m, s
        nonlocal pts, nombre, life
        if life==50:
            pts+=10
        if h==0 and m==0 and s<=30:
            pts+=20
        reset_time()
        checkPoints(pts, nombre, 0)
        detener_cancion()
        ventana.deiconify() #reaparece la ventana principal
        nivel2.destroy() #cierra la subventana nivel2
        reprod_cancion("assets\\title2.wav")

    def close(): #función de cierre
        nonlocal nivel2, FLAG
        global ventana
        FLAG=False #da la señal para detener animación
        detener_cancion()
        reproducir_salida() #reproduce efecto de salida
        sleep(0.9) #tiempo de ejecución del efecto
        nivel2.destroy() #cierra suventana y luego ventana
        ventana.destroy()

    #Creación canvas del nivel2 
    C_nivel2=Canvas(nivel2, width=600, height=800)
    C_nivel2.place(x=0,y=0)

    #Asiganción fondo subventana
    C_nivel2.fondoT=cargar_img("fondo3.png")
    fondoT = C_nivel2.create_image(0,0,anchor=NW, image=C_nivel2.fondoT)

    #Creación del botón BACK
    C_app.back=cargar_img("back.png") #carga imagen para elbotón
    Btn_back=Button(nivel2, text='saludar',image=C_app.back, font=fnt, command=back)
    Btn_back.place(x=600,y=0, anchor=NE)

    nombre=E_nombre.get()

    #Labels con info del jugador
    Label_nombre=Label(C_nivel2, font=fnt3, bg="#850458", fg="#ffffff", text=nombre+"'s score: "+str(pts)+" pts")
    Label_nombre.place(x=0,y=0,anchor=NW)

    Label_life=Label(C_nivel2, font=fnt3, bg="#850458", fg="#ffffff", text=nombre+"'s life: "+str(life)+" pts")
    Label_life.place(x=0,y=50,anchor=NW)

    Label_boss=Label(C_nivel2, font=fnt3, bg="#850458", fg="#ffffff", text="Boss' life: "+str(bolife)+" pts")
    Label_boss.place(x=0,y=100,anchor=NW)

    Label_time=Label(C_nivel2, font=fnt3, bg="#850458", fg="#ffffff")
    Label_time.place(x=600,y=50,anchor=NE)
    cronom(Label_time)#llamada al cronómetro
    
    #Barra de vida
    Label_bar=Label(C_nivel2, font=fnt2, bg="#0bfc03", fg="#0bfc03", text="".zfill(20))
    Label_bar.place(x=300,y=100,anchor="center")

    #carga imagen del boss y la versión dañada y los pone en una lista
    C_nivel2.boss=cargar_img("boss3.png")
    C_nivel2.damage=cargar_img("damage3.png")
    images=[C_nivel2.boss,C_nivel2.damage]

    boss = C_nivel2.create_image(300,200,anchor="center", image=C_nivel2.boss, tags="boss")#crea al boss
    
    def checkBoss(): #checa que ni el boss ni el jugador estén muertos
        nonlocal bolife, life, C_nivel2, life, Label_time, movimiento, notdead
        if bolife<=0 or life<=0 and notdead:
            notdead=False
            movimiento=None #termina el ciclo recursivo de movimiento
            pause_time(Label_time) #pausa tiempo
            reprod_fx("explo4.mp3") #reproduce explosión 
            msgbox=Toplevel() #mensaje de juego finalizado
            msgbox.minsize(600,600)
            if life==0:
                L_saludo=Label(msgbox,text="JUEGO\nFINALIZADO\nPerdió",font=("Candara Light",30))
                L_saludo.place(x=300, y=300, anchor="center")
            else:
                L_saludo=Label(msgbox,text="JUEGO\nFINALIZADO\nGanó",font=("Candara Light",30))
                L_saludo.place(x=300, y=300, anchor="center")
            def fin(): #llama a la función end luego de 5 segundos
                nonlocal msgbox
                msgbox.destroy()
                end()
            C_nivel2.after(5000,fin) 
        else:
            return True

    def boss_move():
        nonlocal C_nivel2, shipco, boss, movimiento, bossco, nombre, images2
        bossco=C_nivel2.coords(boss) #coordenadas en tiempo real
        shipco=C_nivel2.coords(ship)
        if movimiento:#movimiento derecha izquiera
            C_nivel2.coords(boss,randint(100,500),200)
            bossco=C_nivel2.coords(boss)
            def callback():
                boss_move()
            C_nivel2.after(2000 , callback)
    
    def colision(x1,y1,w1,h1,x2,y2,w2,h2): #verifica colisiones mediante comparaciones de rangos en un área coordenadas, ancho y alto
        if x1>x2+w2 or x1+w1<x2 or y1>y2+h2 or y1+h1<y2:
            return False
        else:
            return True
   
   #carga el ship y el ship dañado y los agrega a una lista
    C_nivel2.ship=cargar_img("ship.png")
    ship = C_nivel2.create_image(300,750,anchor="center", image=C_nivel2.ship, tags="ship")
    C_nivel2.laser=cargar_img("laser.png") #carga laser
    C_nivel2.dmgShip=cargar_img("dmgShip.png")
    images2=[C_nivel2.ship,C_nivel2.dmgShip]
    shipco=C_nivel2.coords(ship)

    def shooting(): #cada 1 segundo dispara 3 lasers
        nonlocal C_nivel2, life, bolife
        if life>0 and bolife>0:
            def shoot3(i=0):
                if i<3:
                    create_laser(C_nivel2,C_nivel2.laser,False)
                def repeat2():
                    nonlocal i
                    shoot3(i+1)
                C_nivel2.after(100,repeat2)
            shoot3()
            def repeat():
                shooting()
            C_nivel2.after(1000,repeat)

    def laser_attack(i,objeto,collFlag=True): #mueve el laser
        nonlocal C_nivel2, shipco, bossco, life, pts, nombre, images, Label_life
        shipco=C_nivel2.coords(ship)
        lasco=C_nivel2.coords(objeto) #coordenadas en tiempo real
        if colision(lasco[0],lasco[1],50,89,shipco[0],shipco[1],100,88) and collFlag and life>0: #verifica colisión
            collFlag=False
            C_nivel2.itemconfig("ship",image=images2[1]) # si hay colisión muestra nave dañada
            def normal():
                nonlocal C_nivel2, images
                C_nivel2.itemconfig("ship",image=images2[0]) #vuelve a nave normal
            C_nivel2.after(500,normal)
            reprod_fx("hit2.mp3") #sonido de daño
            if life==2:
                life=0
                checkBoss()
            else:
                life-=3
            Label_life["text"]=nombre+"'s life: "+str(life)+" pts"
         #checa que sigan vivos
        if lasco[1]<900:
            C_nivel2.move(objeto,0,i)
            def callback():
                laser_attack(i+0.1 ,objeto,collFlag)
            C_nivel2.after(5 , callback)

    def laser_mov(i,objeto,collFlag=True): #mueve el laser
        nonlocal C_nivel2, shipco, bossco, bolife, pts, Label_boss, Label_nombre, nombre, images, Label_bar, movimiento
        lasco=C_nivel2.coords(objeto) #coordenadas en tiempo real
        if colision(lasco[0],lasco[1],50,89,bossco[0],bossco[1],175,89) and collFlag and bolife>0: #verifica colisión
            Label_bar["text"]="".zfill(int(20-(20/40)*(40-bolife))) #actualiza barra de vida
            collFlag=False
            C_nivel2.itemconfig("boss",image=images[1]) # si hay colisoón muestra nave dañada
            def normal():
                nonlocal C_nivel2, images
                C_nivel2.itemconfig("boss",image=images[0]) #vuelve a nave normal
            C_nivel2.after(500,normal)
            reprod_fx("hit2.mp3") #sonido de daño
            bolife-=1 #cambio en vida y puntos
            pts+=1
            Label_boss["text"]="Boss' life: "+str(bolife)+" pts"
            Label_nombre["text"]=nombre+"'s score: "+str(pts)+" pts"
            if movimiento:
                checkBoss() #checa que sigan vivos
        if lasco[1]>-100:
            C_nivel2.move(objeto,0,i)
            def callback():
                laser_mov(i-0.1 ,objeto,collFlag)
            C_nivel2.after(5 , callback)
    
    def smooth_mov(objeto,i,j): #cree este algoritmo para que el movimiento de la nave fuera más suave
        global moveFlag #bandera, produce movimiento hasta keyrelease
        m=C_nivel2.coords(objeto)
        if ((i==-1 and 550>m[0]) or (i==1 and m[0]>50) or (j==-1 and 751>m[1]) or (j==1 and m[1]>100)) and moveFlag:
            C_nivel2.move(objeto,-i,-j)
            def callback():
                smooth_mov(objeto,i,j)
            C_nivel2.after(2, callback)

    def create_laser(canva,imagen,uso=True) : #crea un laser cada vez que se dispara
        if uso:
            reprod_fx("metal.mp3") #sonido de disparo
            laser = canva.create_image(shipco[0],shipco[1],anchor="center", image=imagen)
            return laser_mov(0,laser)
        else:
            reprod_fx("bigsmall.mp3") #sonido de disparo
            laser = canva.create_image(bossco[0],bossco[1],anchor="center", image=imagen)
            return laser_attack(0,laser)

    def move_ship(evento):  #verifica lo que toca el usuario en el teclado
        nonlocal C_nivel2, shipco, ship
        global shootFlag, keyFlag, moveFlag
        if keyFlag:
            moveFlag=True #inicia movimiento hasta keyrelease
            if evento.keysym=="Left":
                smooth_mov(ship,1,0)
            elif evento.keysym=="Right":
                smooth_mov(ship,-1,0)
            elif evento.keysym=="Up":
                smooth_mov(ship,0,1)
            elif evento.keysym=="Down":
                smooth_mov(ship,0,-1)
            keyFlag=False #evita varias llamadas por estar presionado
        elif evento.keysym=="space":
            if shootFlag:
                shipco=C_nivel2.coords(ship)
                create_laser(C_nivel2,C_nivel2.laser)
                shootFlag=False #bloquea disparo presionado

    def stop_shoot(evento):
        global shootFlag, moveFlag, keyFlag #modifica ciertas banderas que dependen del keyreleas
        nonlocal life, bolife
        if evento.keysym=="space" and bolife>0 and life>0:
            shootFlag=True #puede disparar luego de soltar mientras esté vivo
        else:
            moveFlag=False #deja de moverse
            keyFlag=True #se puede leer la presion de una tecla
    #uso de las funciones de movimiento y embestida
    boss_move()      
    C_nivel2.after(1000,shooting)
    #eventos de press y release 
    nivel2.bind('<KeyPress>', move_ship)
    nivel2.bind('<KeyRelease>', stop_shoot)
    #cierre protocolo
    nivel2.protocol("WM_DELETE_WINDOW",close) 
    
##############################################################################################################
                                                # Nivel 3 #
##############################################################################################################

def Vnivel3():
    """
    Costa Rica
    Instituto Tecnológico de Costa Rica
    Área Académica de Ingeniería en Computadores
    Taller de Programación, 2021, Grupo 2
    Milton Villegas Lemus
    Version Python 3.9.2
    Versión del codigo 1.0
    Editor: Geovanny García Downing, 2020092224
    Entradas: no aplica
    Salidas: ventana en ciclo TopLevel
    Restricciones: no aplica
    Modulos usados: end, back, close, checkBoss, SWAP, boss_move, collision, laser_move, smooth_move, create_laser, move_ship, stop_shoot, shooting, laser_attack
    Modulos modificados: Se reutilizó código de la tarea, cargar_imagen, abarcado por José Fernando Morales en el taller
    Codigo modificado facilitado por: Jose Fernando Morales
    """
    global ventana, E_nombre, puntajes
    FLAG=True

    #variables de vida, puntos, vida del boss, entre otras banderas de movimiento y embestida
    pts=0
    life=50
    bolife=50
    bossco=[]
    LRFlag=True
    embestida=True
    shootFlag2=True
    notdead=True

    #creación de subventana nivel3 de música y características por Toplevel
    ventana.withdraw() #oculta ventana principal
    nivel3=Toplevel() 
    nivel3.title("Nivel 3") 
    nivel3.minsize(600,800)
    nivel3.resizable(width=NO, height=NO)
    reprod_cancion("assets\\boss3.wav")

    def end(): #función que calcula los bonuses en caso de finalizar, no hay bonuses en cierres forzados
        global ventana, h, m, s
        nonlocal pts, nombre, life
        if life==50: #si la vida es 50 entonces se obtiene +10 bonus
            pts+=10
        if h==0 and m==0 and s<=30: #si lo hizo en 30 segs +20 bonus
            pts+=20
        reset_time()
        checkPoints(pts, nombre, 0)
        detener_cancion()
        ventana.deiconify() #reaparece la ventana principal
        nivel3.destroy() #cierra la subventana nivel1
        reprod_cancion("assets\\title2.wav")

    def back(): #función del botón BACK
        global ventana, h, m, s
        nonlocal pts, nombre, life
        if life==50:
            pts+=10
        if h==0 and m==0 and s<=30:
            pts+=20
        reset_time()
        checkPoints(pts, nombre, 0)
        detener_cancion()
        ventana.deiconify() #reaparece la ventana principal
        nivel3.destroy() #cierra la subventana nivel3
        reprod_cancion("assets\\title2.wav")

    def close(): #función de cierre
        nonlocal nivel3, FLAG
        global ventana
        FLAG=False #da la señal para detener animación
        detener_cancion()
        reproducir_salida() #reproduce efecto de salida
        sleep(0.9) #tiempo de ejecución del efecto
        nivel3.destroy() #cierra suventana y luego ventana
        ventana.destroy()

    #Creación canvas del nivel3 
    C_nivel3=Canvas(nivel3, width=600, height=800)
    C_nivel3.place(x=0,y=0)

    #Asiganción fondo subventana
    C_nivel3.fondoT=cargar_img("fondo4.png")
    fondoT = C_nivel3.create_image(0,0,anchor=NW, image=C_nivel3.fondoT)

    #Creación del botón BACK
    C_app.back=cargar_img("back.png") #carga imagen para elbotón
    Btn_back=Button(nivel3, text='saludar',image=C_app.back, font=fnt, command=back)
    Btn_back.place(x=600,y=0, anchor=NE)

    nombre=E_nombre.get()

    #Labels con info del jugador
    Label_nombre=Label(C_nivel3, font=fnt3, bg="#850458", fg="#ffffff", text=nombre+"'s score: "+str(pts)+" pts")
    Label_nombre.place(x=0,y=0,anchor=NW)

    Label_life=Label(C_nivel3, font=fnt3, bg="#850458", fg="#ffffff", text=nombre+"'s life: "+str(life)+" pts")
    Label_life.place(x=0,y=50,anchor=NW)

    Label_boss=Label(C_nivel3, font=fnt3, bg="#850458", fg="#ffffff", text="Boss' life: "+str(bolife)+" pts")
    Label_boss.place(x=0,y=100,anchor=NW)

    Label_time=Label(C_nivel3, font=fnt3, bg="#850458", fg="#ffffff")
    Label_time.place(x=600,y=50,anchor=NE)
    cronom(Label_time)#llamada al cronómetro
    
    #Barra de vida
    Label_bar=Label(C_nivel3, font=fnt2, bg="#0bfc03", fg="#0bfc03", text="".zfill(20))
    Label_bar.place(x=300,y=100,anchor="center")

    #carga imagen del boss y la versión dañada y los pone en una lista
    C_nivel3.boss=cargar_img("boss1.png")
    C_nivel3.damage=cargar_img("damage1.png")
    images=[C_nivel3.boss,C_nivel3.damage]

    boss = C_nivel3.create_image(300,200,anchor="center", image=C_nivel3.boss, tags="boss")#crea al boss
    
    def checkBoss(): #checa que ni el boss ni el jugador estén muertos
        nonlocal bolife, C_nivel3, life, Label_time, embestida, notdead
        if bolife<=0 or life<=0 and notdead:
            notdead=False
            embestida=None #termina el ciclo recursivo de movimiento
            pause_time(Label_time) #pausa tiempo
            reprod_fx("explo4.mp3") #reproduce explosión 
            msgbox=Toplevel() #mensaje de juego finalizado
            msgbox.minsize(600,600)
            if life==0:
                L_saludo=Label(msgbox,text="JUEGO\nFINALIZADO\nPerdió",font=("Candara Light",30))
                L_saludo.place(x=300, y=300, anchor="center")
            else:
                L_saludo=Label(msgbox,text="JUEGO\nFINALIZADO\nGanó",font=("Candara Light",30))
                L_saludo.place(x=300, y=300, anchor="center")
            def fin(): #llama a la función end luego de 5 segundos
                nonlocal msgbox
                msgbox.destroy()
                end()
            C_nivel3.after(5000,fin) 
        else:
            return True
            
    def SWAP():
        nonlocal embestida, LRFlag, bolife, Label_boss, Label_bar, shootFlag2 #ataca cada 6 segundos
        if bolife>0:    
            reprod_fx("mothership.mp3") #reproduce efectos
            embestida=False #usé lógica invertida, ataca cuando es falso
            shootFlag2=False
            LRFlag=None
            def callback():
                SWAP() #cada dos segundos hace llamada recursiva
            C_nivel3.after(6000 , callback)

    def boss_move(i=0,collFlag=True):
        nonlocal C_nivel3, shipco, boss, LRFlag, embestida, bossco, bolife, life, Label_life, nombre, images2, shootFlag2
        bossco=C_nivel3.coords(boss) #coordenadas en tiempo real
        shipco=C_nivel3.coords(ship)
        coll=colision(shipco[0],shipco[1],100,88,bossco[0],bossco[1],100,175) #verifica colisión de nave con jefe
        if coll and collFlag and embestida==False and life>0: #si colisiona una vez, se levanta la bandera para que no tome una colisón como varias
            collFlag=False #bandera
            C_nivel3.itemconfig("ship",image=images2[1]) #cambia a nave dañada
            def normal(): #vuelve a nave normal después de medio segundo
                nonlocal C_nivel3, images2
                C_nivel3.itemconfig("ship",image=images2[0])
            C_nivel3.after(500,normal)
            reprod_fx("explo3.mp3") #sonido de choque
            life-=10
            if life<0:
                life=0
            Label_life["text"]=nombre+"'s life: "+str(life)+" pts" #actualización de vida en label vida
            checkBoss()
        if coll==False:#llamada a bandera
            collFlag=True
        if embestida:#movimiento derecha izquiera
            if LRFlag: #flag para evira movimiento en embestida
                C_nivel3.move(boss,i,0)
                def callback():
                    boss_move(3,collFlag)
                C_nivel3.after(5 , callback)
                if bossco[0]>600:
                    LRFlag=False
            else:
                C_nivel3.move(boss,i,0)
                def callback():
                    boss_move(-3,collFlag)
                C_nivel3.after(5 , callback)
                if bossco[0]<0:
                    LRFlag=True
        elif embestida==False and LRFlag!=None: #embestida
            if LRFlag:
                C_nivel3.move(boss,0,i)
                def callback():
                    boss_move(3,collFlag)
                C_nivel3.after(1 , callback)
                if bossco[1]>700:
                    LRFlag=False
            else:
                C_nivel3.move(boss,0,i)
                def callback():
                    boss_move(-2,collFlag)
                C_nivel3.after(1 , callback)
                if bossco[1]<200:
                    checkBoss()
                    if randint(0,1)==0:
                        C_nivel3.coords(boss,300,200)
                        embestida=True
                        shootFlag2=True
                    else:
                        C_nivel3.coords(boss,randint(100,500),200)
                        embestida=False
                        LRFlag=None
        elif LRFlag==None: #reinicia movimiento luego de embestida
            def espera():   
                nonlocal LRFlag
                LRFlag=True
                boss_move()
            C_nivel3.after(500, espera)

    def colision(x1,y1,w1,h1,x2,y2,w2,h2): #verifica colisiones mediante comparaciones de rangos en un área coordenadas, ancho y alto
        if x1>x2+w2 or x1+w1<x2 or y1>y2+h2 or y1+h1<y2:
            return False
        else:
            return True
   
   #carga el ship y el ship dañado y los agrega a una lista
    C_nivel3.ship=cargar_img("ship.png")
    ship = C_nivel3.create_image(300,750,anchor="center", image=C_nivel3.ship, tags="ship")
    C_nivel3.laser=cargar_img("laser.png") #carga laser
    C_nivel3.dmgShip=cargar_img("dmgShip.png")
    images2=[C_nivel3.ship,C_nivel3.dmgShip]
    shipco=C_nivel3.coords(ship)
    
    def shooting(): #cada 1 segundo dispara 3 lasers
        nonlocal C_nivel3, life, shootFlag2, bolife
        if life>0 and shootFlag2 and bolife>0:
            def shoot3(i=0):
                if i<3:
                    create_laser(C_nivel3,C_nivel3.laser,False)
                def repeat2():
                    nonlocal i
                    shoot3(i+1)
                C_nivel3.after(100,repeat2)
            shoot3()
        if life>0:
            def repeat():
                shooting()
            C_nivel3.after(1000,repeat)

    def laser_attack(i,objeto,collFlag=True): #mueve el laser
        nonlocal C_nivel3, shipco, bossco, life, pts, nombre, images, Label_life
        shipco=C_nivel3.coords(ship)
        lasco=C_nivel3.coords(objeto) #coordenadas en tiempo real
        if colision(lasco[0],lasco[1],50,89,shipco[0],shipco[1],100,88) and collFlag and life>0: #verifica colisión
            collFlag=False
            C_nivel3.itemconfig("ship",image=images2[1]) # si hay colisión muestra nave dañada
            def normal():
                nonlocal C_nivel3, images
                C_nivel3.itemconfig("ship",image=images2[0]) #vuelve a nave normal
            C_nivel3.after(500,normal)
            reprod_fx("hit2.mp3") #sonido de daño
            if life==2 or life==1:
                life=0
                checkBoss()
            else:
                life-=3
            Label_life["text"]=nombre+"'s life: "+str(life)+" pts"
         #checa que sigan vivos
        if lasco[1]<900:
            C_nivel3.move(objeto,0,i)
            def callback():
                laser_attack(i+0.1 ,objeto,collFlag)
            C_nivel3.after(5 , callback)

    def laser_mov(i,objeto,collFlag=True): #mueve el laser
        nonlocal C_nivel3, shipco, bossco, bolife, pts, Label_boss, Label_nombre, nombre, images, Label_bar
        lasco=C_nivel3.coords(objeto) #coordenadas en tiempo real
        if colision(lasco[0],lasco[1],50,89,bossco[0],bossco[1],100,175) and collFlag and bolife>0: #verifica colisión
            Label_bar["text"]="".zfill(int(20-(20/50)*(50-bolife))) #actualiza barra de vida
            collFlag=False
            C_nivel3.itemconfig("boss",image=images[1]) # si hay colisoón muestra nave dañada
            def normal():
                nonlocal C_nivel3, images
                C_nivel3.itemconfig("boss",image=images[0]) #vuelve a nave normal
            C_nivel3.after(500,normal)
            reprod_fx("hit2.mp3") #sonido de daño
            bolife-=1 #cambio en vida y puntos
            pts+=1
            Label_boss["text"]="Boss' life: "+str(bolife)+" pts"
            Label_nombre["text"]=nombre+"'s score: "+str(pts)+" pts"
            checkBoss() #checa que sigan vivos
        if lasco[1]>-100:
            C_nivel3.move(objeto,0,i)
            def callback():
                laser_mov(i-0.1 ,objeto,collFlag)
            C_nivel3.after(5 , callback)
    
    def smooth_mov(objeto,i,j): #cree este algoritmo para que el movimiento de la nave fuera más suave
        global moveFlag #bandera, produce movimiento hasta keyrelease
        m=C_nivel3.coords(objeto)
        if ((i==-1 and 550>m[0]) or (i==1 and m[0]>50) or (j==-1 and 751>m[1]) or (j==1 and m[1]>100)) and moveFlag:
            C_nivel3.move(objeto,-i,-j)
            def callback():
                smooth_mov(objeto,i,j)
            C_nivel3.after(2, callback)

    def create_laser(canva,imagen,uso=True) : #crea un laser cada vez que se dispara
        if uso:
            reprod_fx("metal.mp3") #sonido de disparo
            laser = canva.create_image(shipco[0],shipco[1],anchor="center", image=imagen)
            return laser_mov(0,laser)
        else:
            reprod_fx("bigsmall.mp3") #sonido de disparo
            laser = canva.create_image(bossco[0],bossco[1],anchor="center", image=imagen)
            return laser_attack(0,laser)

    def move_ship(evento):  #verifica lo que toca el usuario en el teclado
        nonlocal C_nivel3, shipco, ship
        global shootFlag, keyFlag, moveFlag
        if keyFlag:
            moveFlag=True #inicia movimiento hasta keyrelease
            if evento.keysym=="Left":
                smooth_mov(ship,1,0)
            elif evento.keysym=="Right":
                smooth_mov(ship,-1,0)
            elif evento.keysym=="Up":
                smooth_mov(ship,0,1)
            elif evento.keysym=="Down":
                smooth_mov(ship,0,-1)
            keyFlag=False #evita varias llamadas por estar presionado
        elif evento.keysym=="space":
            if shootFlag:
                shipco=C_nivel3.coords(ship)
                create_laser(C_nivel3,C_nivel3.laser)
                shootFlag=False #bloquea disparo presionado

    def stop_shoot(evento):
        global shootFlag, moveFlag, keyFlag #modifica ciertas banderas que dependen del keyreleas
        nonlocal life, bolife
        if evento.keysym=="space" and bolife>0 and life>0:
            shootFlag=True #puede disparar luego de soltar mientras esté vivo
        else:
            moveFlag=False #deja de moverse
            keyFlag=True #se puede leer la presion de una tecla
    #uso de las funciones de movimiento y embestida
    boss_move()      
    C_nivel3.after(6000,SWAP)
    C_nivel3.after(1000,shooting) 
    #eventos de press y release 
    nivel3.bind('<KeyPress>', move_ship)
    nivel3.bind('<KeyRelease>', stop_shoot)
    #cierre protocolo
    nivel3.protocol("WM_DELETE_WINDOW",close) 

##############################################################################################################
                                                # About #
##############################################################################################################
def info_adicional():
    """
    Costa Rica
    Instituto Tecnológico de Costa Rica
    Área Académica de Ingeniería en Computadores
    Taller de Programación, 2021, Grupo 2
    Milton Villegas Lemus
    Version Python 3.9.2
    Versión del codigo 1.0
    Editor: Geovanny García Downing, 2020092224
    Entradas: no aplica
    Salidas: ventana en ciclo TopLevel
    Restricciones: no aplica
    Modulos usados: back, close
    """
    global ventana, about
    ventana.withdraw() #oculta ventana principal
    info=Toplevel() #creción de subventana de información adicional y características por Toplevel
    info.title("Información Adicional")
    info.minsize(600,800)
    info.resizable(width=NO, height=NO)
    
    def back(): #función del botón BACK
        global ventana
        ventana.deiconify() #reaparece ventana principal
        info.destroy() #cierra ventana de info

    def close(): #función de cierre
        nonlocal info
        global ventana
        reproducir_salida() #reproduce efecto de salida Goodbye
        sleep(0.9) #tiempo de reproducción efecto
        info.destroy() #cierra subventana y luego ventana
        ventana.destroy()
    
    #Creación canvas de subventana Info   
    C_info=Canvas(info, width=600, height=800)
    C_info.place(x=0,y=0)

    #Asignación fondo de subventana Info
    C_info.fondoI=cargar_img("fondo1.png")
    fondoI = C_info.create_image(0,0,anchor=NW, image=C_info.fondoI)

    #Creación botón BACK
    C_app.back=cargar_img("back.png") #Carga imagen para botón
    Btn_back=Button(info, text='saludar',image=C_app.back, font=fnt, command=back)
    Btn_back.place(x=600,y=0, anchor=NE)

    #Label con el texto de info adicional (about)
    L_about=Label(info,font=fnt, bg="#ffffff", fg="#000000", text=about)
    L_about.place(x=300, y=380, anchor="center")

    info.protocol("WM_DELETE_WINDOW",close) 

##############################################################################################################
                                                # Puntajes #
##############################################################################################################
def mejores_puntajes():
    """
    Costa Rica
    Instituto Tecnológico de Costa Rica
    Área Académica de Ingeniería en Computadores
    Taller de Programación, 2021, Grupo 2
    Milton Villegas Lemus
    Version Python 3.9.2
    Versión del codigo 1.0
    Editor: Geovanny García Downing, 2020092224
    Entradas: no aplica
    Salidas: ventana en ciclo TopLevel
    Restricciones: no aplica
    Modulos usados: back, close, tablero,
    """
    global puntajes, nombres, ventana, about
    ventana.withdraw() #oculta ventana principal
    info=Toplevel() #creción de subventana de información adicional y características por Toplevel
    info.title("Información Adicional")
    info.minsize(600,800)
    info.resizable(width=NO, height=NO)
    
    def tablero(Puntajes,I): #retorna un texto con los puntajes, nombres y posiciones
        if Puntajes==[]:
            return ""
        else:
            return f"{I+1}. {nombres[I]} \t\t---> {Puntajes[0]}\n" + tablero(Puntajes[1:],I+1)

    def back(): #función del botón BACK
        global ventana
        ventana.deiconify() #reaparece ventana principal
        info.destroy() #cierra ventana de info

    def close(): #función de cierre
        nonlocal info
        global ventana
        reproducir_salida() #reproduce efecto de salida Goodbye
        sleep(0.9) #tiempo de reproducción efecto
        info.destroy() #cierra subventana y luego ventana
        ventana.destroy()
    
    #Creación canvas de subventana Info   
    C_info=Canvas(info, width=600, height=800)
    C_info.place(x=0,y=0)

    #Asignación fondo de subventana Info
    C_info.fondoI=cargar_img("fondo1.png")
    fondoI = C_info.create_image(0,0,anchor=NW, image=C_info.fondoI)

    #Creación botón BACK
    C_app.back=cargar_img("back.png") #Carga imagen para botón
    Btn_back=Button(info, text='saludar',image=C_app.back, font=fnt, command=back)
    Btn_back.place(x=600,y=0, anchor=NE)

    #Label con el texto de info adicional (about)
    L_about=Label(info,font=fnt, bg="#ffffff", fg="#000000", text=tablero(puntajes,0))
    L_about.place(x=300, y=380, anchor="center")

    info.protocol("WM_DELETE_WINDOW",close) 

#Creación botón Jugar que abre subventana Nivel 1
Btn_jugar=Button(ventana, text='Jugar',font=fnt,command=Vnivel1Check, bg="#850458", fg="#ffffff")
Btn_jugar.place(x=400,y=220,anchor="center")    
    
#Creación botón para abrir subventana Nivel 1
Btn_nivel1=Button(ventana, text='Nivel 1',font=fnt,command=Vnivel1Check, bg="#850458", fg="#ffffff")
Btn_nivel1.place(x=300,y=320,anchor="center")

#Creación botón para abrir subventana Nivel 2
Btn_nivel2=Button(ventana, text='Nivel 2',font=fnt,command=Vnivel2Check, bg="#850458", fg="#ffffff")
Btn_nivel2.place(x=300,y=420,anchor="center")

#Creación botón para abrir subventana Nivel 3
Btn_nivel3=Button(ventana, text='Nivel 3',font=fnt,command=Vnivel3Check, bg="#850458", fg="#ffffff")
Btn_nivel3.place(x=300,y=520,anchor="center")

#Creación botón para abrir subventana Puntajes
Btn_pt=Button(ventana, text='Mejores Puntajes',font=fnt,command=mejores_puntajes, bg="#850458", fg="#ffffff")
Btn_pt.place(x=300,y=620,anchor="center")

#Creación botón para abrir subventana Información Adicional
Btn_info=Button(ventana, text='Información Adicional',font=fnt,command=info_adicional, bg="#850458", fg="#ffffff")
Btn_info.place(x=300,y=720,anchor="center")

ventana.protocol("WM_DELETE_WINDOW", close)
ventana.mainloop()

def autodocumentacion():
    print("Nivel 1")
    print(Vnivel1.__doc__)
    print("Nivel 2")
    print(Vnivel2.__doc__)
    print("Nivel 3")
    print(Vnivel3.__doc__)
    print("Puntajes")
    print(mejores_puntajes.__doc__)
    print("About")
    print(info_adicional.__doc__)