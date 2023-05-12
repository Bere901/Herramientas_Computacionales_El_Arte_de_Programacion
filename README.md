# Herramientas Computacionales: El Arte de la Programación

```
Equipo:
Azul Nahomi Machorro Arreola
Dana Marian Rivera Oropeza 
Daniela Berenice Hernández De Vicente
Rodrigo López Guerra
```

## Descripción de la Actividad:

En base en códigos previamente realizados, usa tus conocimientos de programación y realiza los cambios necesarios para agregar las funciones que se mencionarán a continuación.

Utilizarás las herramientas de GitHub para poder realizar un trabajo cooperativo, donde se pueda ver el uso de push y pulls alrededor de la actividad.

### Actividad 1. Juego Pintado

```
Encargados:
Azul Nahomi Machorro Arreola
Daniela Berenice Hernández De Vicente
```
**__Instrucciones:__**

> 1.- Copia el código del videojuego Paint. Tomado  del  sitio  Grant  Jenks 
<sub>[Código Base](http://www.grantjenks.com/docs/freegames/paint.html.)

> 2.- Prueba el videojuego individualmente, a través de leer el código entenderán su uso, ya que la documentación es escasa.

> 3.- Junto con el compañero analicen el código y documenten de acuerdo al estándar del Instituto.
    
    A.- Uno de los dos creará un repositorio con el videojuego copiado y se lo compartirá al otro compañero
    B.- Uno de los dos añadirá las siguientes funcionalidades:
        B1. Un color nuevo
        B2. Dibujar un círculo
    C.- El otro compañero añadirá:
        C1. Completar el rectángulo
        C2. Completar el triángulo

> 4.- Asegúrense de haber documentado correctamente el código de acuerdo al estándar del Instituto.

**Código Base**

```
from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    "Draw circle from start to end."
    pass  # TODO

def rectangle(start, end):
    "Draw rectangle from start to end."
    pass  # TODO

def triangle(start, end):
    "Draw triangle from start to end."
    pass  # TODO

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
```

<img src='https://drive.google.com/uc?id=1SediQ9qlt6kMB6Nw8BPVr7CS-i3t9v3d'>

### Actividad 2. Juego de la Víbora

```
Encargados:
Dana Marian Rivera Oropeza 
Rodrigo López Guerra
```

**__Instrucciones:__**

> 1.- Copia el código del videojuego Snake. Tomado  del  sitio  Grant  Jenks 
<sub>[Código Base](http://www.grantjenks.com/docs/freegames/snake.html)

> 2.- Prueba el videojuego individualmente, a través de leer el código entenderán su uso, ya que la documentación es escasa.

> 3.- Junto con el compañero analicen el código y documenten de acuerdo al estándar del Instituto.
    
    A.- Uno de los dos creará un repositorio con el videojuego copiado y se lo compartirá al otro compañero
    B.- Uno de los dos añadirá la siguiente funcionalidades:
        B1. La comida podrá moverse al azar un paso a la vez y no deberá de salirse de la ventana
    C.- El otro compañero añadirá:
        C1. Cada vez que se corra el juego, la víbora y la comida deberán tener colores diferentes entre sí, pero al azar, de una serie de 5 diferentes colores, excepto el rojo.

> 4.- Asegúrense de haber documentado correctamente el código de acuerdo al estándar del Instituto.

**Código Base**

```
from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
```

<img src='https://drive.google.com/uc?id=1DJB0iNogxhdDFSuTEc8SwwwqRVj-0DbN'>

### Actividad 3. Juego del PacMan

```
Encargados:
Azul Nahomi Machorro Arreola
Dana Marian Rivera Oropeza 
```

**__Instrucciones:__**

> 1.- Copia el código del videojuego PacMan. Tomado  del  sitio  Grant  Jenks 
<sub>[Código Base](http://www.grantjenks.com/docs/freegames/pacman.html)

> 2.- Prueba el videojuego individualmente, a través de leer el código entenderán su uso, ya que la documentación es escasa.

> 3.- Junto con el compañero analicen el código y documenten de acuerdo al estándar del Instituto.
    
    A.- Uno de los dos creará un repositorio con el videojuego copiado y se lo compartirá al otro compañero
    B.- Uno de los dos añadirá la siguiente funcionalidades:
        B1. Los fantasmas sean más listos.
    C.- El otro compañero añadirá:
        C1. Cambiar el tablero
        C2. Hacer que los fantasmas vayan mas rápido

> 4.- Asegúrense de haber documentado correctamente el código de acuerdo al estándar del Instituto.

**Código Base**

```
from random import choice
from turtle import *
from freegames import floor, vector

state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(5, 0)
pacman = vector(-40, -80)
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

def world():
    "Draw world using path."
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')

def move():
    "Move pacman and all ghosts."
    writer.undo()
    writer.write(state['score'])

    clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 100)

def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
```

<img src='https://drive.google.com/uc?id=1WZUxD_gTm_CBqTirUp8nqyuYVJHrXNS5'>


### Actividad 4. Juego del Tiro Parabólico

```
Encargados:
Daniela Berenice Hernández De Vicente
Rodrigo López Guerra
```

**__Instrucciones:__**

> 1.- Copia el código del videojuego Cannon. Tomado  del  sitio  Grant  Jenks 
<sub>[Código Base](http://www.grantjenks.com/docs/freegames/cannon.html)

> 2.- Prueba el videojuego individualmente, a través de leer el código entenderán su uso, ya que la documentación es escasa.

> 3.- Junto con el compañero analicen el código y documenten de acuerdo al estándar del Instituto.
    
    A.- Uno de los dos creará un repositorio con el videojuego copiado y se lo compartirá al otro compañero
    B.- Uno de los dos añadirá la siguiente funcionalidades:
        B1. La velocidad del movimiento para el proyectil y los balones sea más rápida.
    C.- El otro compañero añadirá:
        C1. Hacer que el juego nunca termine, de manera que los balones al salir de la ventana se re posicionen.

> 4.- Asegúrense de haber documentado correctamente el código de acuerdo al estándar del Instituto.

**Código Base**

```
from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
```

<img src='https://drive.google.com/uc?id=1VlnGB9SZk4Rzwc9Q7XObWWJqVXypPf13'>

### Actividad 5. Juego de Memoria

```
Encargados:
Azul Nahomi Machorro Arreola
Daniela Berenice Hernández De Vicente
```

**__Instrucciones:__**

> 1.- Copia el código del videojuego Memory. Tomado  del  sitio  Grant  Jenks 
<sub>[Código Base](http://www.grantjenks.com/docs/freegames/memory.html)

> 2.- Prueba el videojuego individualmente, a través de leer el código entenderán su uso, ya que la documentación es escasa.

> 3.- Junto con el compañero analicen el código y documenten de acuerdo al estándar del Instituto.
    
    A.- Uno de los dos creará un repositorio con el videojuego copiado y se lo compartirá al otro compañero
    B.- Entre ambos, deberán de repartirse las siguientes tareas:
        B1. Contar y desplegar el numero de taps
        B2. Detectar cuando todos los cuadros se han destapado
        B3. Central el dígito en el cuadro
        B4. Como un condimento de innovación al juego, Podrías utilizar algo diferente a los dígitos para resolver el juego y que al usuario le ayude a tener mejor memoria ?

> 4.- Asegúrense de haber documentado correctamente el código de acuerdo al estándar del Instituto.

**Código Base**

```
from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
```

<img src='https://drive.google.com/uc?id=1FMPKOSqmBOX7IwtkiG-4hp1GXJbn0-Jq'>


