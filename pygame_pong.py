import turtle

wn = turtle.Screen() #crea una ventana
wn.title("pong by viky")#Le pone nombre a la ventana
wn.bgcolor("black")#cambia el color de fondo 
wn.setup(width=800,height=600)
wn.tracer(0)#no updatea la ventana (hace que el juego sea mas rapido porque la setapea una vez y listo)


#SCORE creo las variables que guardan los tantos
score_a = 0
score_b = 0


#Paleta A 
paddle_a = turtle.Turtle()#class name
paddle_a.speed(0)#speed of animation (0) la setea a lo mas rapido
paddle_a.shape("square")#le da forma 
paddle_a.color("white")#le da color
paddle_a.shapesize(stretch_wid=5,stretch_len=1)#cambia el cuadrado original ensanchandolo asi queda un rectangulo
paddle_a.penup()#hace que no dibuje una linea por donde se mueve
paddle_a.goto(-350,0)#inicializa mi objeto en un lugar en la pantalla

#Paleta B
paddle_b = turtle.Turtle()#class name
paddle_b.speed(0)#speed of animation (0) la setea a lo mas rapido
paddle_b.shape("square")#le da forma 
paddle_b.color("white")#le da color
paddle_b.shapesize(stretch_wid=5,stretch_len=1)#cambia el cuadrado original ensanchandolo asi queda un rectangulo
paddle_b.penup()#hace que no dibuje una linea por donde se mueve
paddle_b.goto(350,0)#inicializa mi objeto en un lugar en la pantalla


#Pelota
ball = turtle.Turtle()#class name
ball.speed(0)#speed of animation (0) la setea a lo mas rapido
ball.shape("square")#le da forma 
ball.color("white")#le da color
ball.penup()#hace que no dibuje una linea por donde se mueve
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5 #cada vez que se mueve se mueve por 0.5 pixeles 

#ANOTADOR 

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()#no queremos que se vea solo que se vean los numeros que escribe
pen.goto(0,260)#la ubica al centro arriba
pen.write("Player A: 0   Player B: 0",align ="center", font=("Courier",24,"normal"))#le agrega el score inicial


#FUNCIONES 

def paddle_a_up():
    y = paddle_a.ycor() #esta funcion de turtle obtiene la coordenada y del objeto en la ventana
    if(y + 20 < 260):
        y += 20
    paddle_a.sety(y)#le asigna a la coord y el valor "y"

def paddle_a_down():
    y = paddle_a.ycor() #esta funcion de turtle obtiene la coordenada y del objeto en la ventana
    if(y - 20 > -260):
        y -= 20
    paddle_a.sety(y)#le asigna a la coord y el valor "y"

def paddle_b_up():
    y = paddle_b.ycor() #esta funcion de turtle obtiene la coordenada y del objeto en la ventana
    if(y + 20 < 260):
        y += 20
    paddle_b.sety(y)#le asigna a la coord y el valor "y"

def paddle_b_down():
    y = paddle_b.ycor() #esta funcion de turtle obtiene la coordenada y del objeto en la ventana
    if(y - 20 > -260):
        y -= 20
    paddle_b.sety(y)#le asigna a la coord y el valor "y"

#KEYBOARD BINDING
wn.listen()#le dice a la ventana que "escuche" teclado
wn.onkeypress(paddle_a_up,"w")#cuando el usuario use la tecla "w" llama a la funcion paadle_a_up 
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#Main game loop 

while True:
    wn.update()

    #Moving the ball 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #border check

    #coordenada y 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    #coordenada x 
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1 #que arranque para el lado contrario al que se fue
        score_a += 1
        pen.clear()#primero limpia la pantalla de lo que escribio antes si no lo escribe arriba
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b),align ="center", font=("Courier",24,"normal"))#le agrega el score inicial

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1 
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b),align ="center", font=("Courier",24,"normal"))#le agrega el score inicial
  

    #COLISIONES 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)#la dibuja un poco mas atras
        ball.dx *= -1 #cambia la direccion en el eje x

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
    
