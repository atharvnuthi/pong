from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.collision import *

#Janela
janW = 720
janH = 480
janela = Window(janW, janH)
janela.set_title("Pong")
#fundo = GameImage("fundo.png")

#Bola
bola = Sprite("assets/bola.png")
bolW = bola.width
bolH = bola.height
bola.set_position(janW/2 - bolW/2, janH/2 - bolH/2)
velx = 0
vely = 0

#Pads
pad1 = Sprite("assets/pad.png")
pad1.set_position(30, janH/2 - pad1.height/2)
pad2 = Sprite("assets/pad.png")
pad2.set_position(janW - pad2.width - 30, janH/2 - pad1.height/2)
velpad = 500
velAI = 400

#Teclado
key = keyboard.Keyboard()

#Jogo em Si
pt1 = 0
pt2 = 0
centro = True
tempo = 0

dim1 = False
dim2 = False
pH1 = pad1.height 
pH2 = pad2.height

#Game Loop
while True:
    janela.set_background_color((0, 0, 0))
    if(key.key_pressed("ESC")):
        break

    bola.x += velx*janela.delta_time()
    bola.y += vely*janela.delta_time()

    #Bola não pode sair do eixo vertical da janela
    if bola.y <= 0:
        bola.y += 1
        vely = vely * -1

    if bola.y >= janH - bolH:
        bola.y -= 1
        vely = vely * -1

    #Colisão da bola com a raquete
    if (bola.collided(pad1) and velx < 0):
        velx *= -1

    if (bola.collided(pad2) and velx > 0):
        velx *= -1

    #Pontuar se a bola sair da tela
    if bola.x < 0:
        pt2 += 1
        if dim1 == False:
            pad1.height /= 2
            pad2.height = pH2
            dim1 = True
            dim2 = False
        centro = True

    if bola.x > janW:
        pt1 += 1
        if dim2 == False:
            pad2.height /= 2
            pad1.height = pH1
            dim2 = True
            dim1 = False
        centro = True

    #Recolocar a bola no centro
    if centro == True:
        bola.set_position(janW / 2 - bolW / 2, janH / 2 - bolH / 2)
        pad1.set_position(30, janH / 2 - pad1.height / 2)
        pad2.set_position(janW - pad2.width - 30, janH / 2 - pad1.height / 2)
        velx = 0
        vely = 0
        velpad = 0

        tempo += 1
        if tempo == 500:
            velx = 500
            vely = 500
            velpad = 500
            centro = False
            tempo = 0

    #Movimentação dos Pads
    if pad1.y >= 0:
        if (key.key_pressed("W")):
            pad1.y -= velpad*janela.delta_time()

    if pad1.y <= janH - pad1.height:
        if (key.key_pressed("S")):
            pad1.y += velpad*janela.delta_time()
    
    if pad2.y >= 0:
        if (key.key_pressed("UP")):
            pad2.y -= velpad*janela.delta_time()
    
    if pad2.y <= janH - pad2.height:
        if (key.key_pressed("DOWN")):
            pad2.y += velpad*janela.delta_time()
    
    #Movimentação da IA
    if velx > 0 and bola.x > janW/2 and bola.x < janW:
        if pad2.y >= 0:
            if bola.y < pad2.y + pad2.height/2:
                pad2.y -= velAI*janela.delta_time()
        if pad2.y <= janH - pad2.height:
            if bola.y > pad2.y + pad2.height/2:
                pad2.y += velAI*janela.delta_time()

    #fundo.draw()
    janela.draw_text(str(pt1), x=((janW/4)*1), y=10, size=35, color=(108, 108, 108), bold=True, italic=True)
    janela.draw_text(str(pt2), x=((janW/4)*3), y=10, size=35, color=(108, 108, 108), bold=True, italic=True)

    pad1.draw()
    pad2.draw()
    bola.draw()
    janela.update()