import random

print('hello')
print('starting...')

wall = '[]'
fail = False


def draw_canvas_empty():
    canvas = [[]for x in range(20)]
    for iterator in range(20):
        canvas[iterator] = ['  ' for x in range(21)]
    return canvas


def init_places(canvas : list):
    print('init_places ...')
    entrances = []
    #assignamos unas cordenadas a cada entrada
    [entrances.append([random.randint(2,18),random.randint(2,18)]) for iterable in range(7)]
    draw_places(entrances, canvas) 
    return canvas


def draw_places(entrances : list,canvas):
    i = 1  # i es para tener el E1, E2, E3 , E4
    for entrance in entrances:
        print(entrance)
        # Pintamos el E1 para cada entrada
        print_canvas(entrance[0],entrance[1],canvas, f'E{i}')
        # Empezamos a pintar el area
        area(entrance[0],entrance[1],canvas)
        i += 1
        break

def area(Ex,Ey,canvas):
    global wall
    posible_directions = where_to_draw(Ex,Ey,canvas)
    area = random.randint(10,15)
    print(area)
    while True:
        start_direction = pick_direction(posible_directions)
        print_canvas(Ex+start_direction[0],Ey+start_direction[1],canvas,wall)
        break
        

def print_canvas(x,y,canvas, symbol):
    canvas[x][y] = symbol
    
def pick_direction(directions : list):
    random_index = random.randint(0,directions.__len__()-1)
    return directions[random_index]

    

def where_to_draw(x,y,canvas):
    global fail
    posibilities = [[1,0],[0,1],[-1,0],[0,-1]]
    surroundings = [[1,1],[-1,1],[-1,-1],[1,-1]]
    posibles = []
    for posibilitie in posibilities:
        try:
            if can_draw(x+posibilitie[0],y+posibilitie[1],canvas,posibilitie):
                posibles.append(posibilitie)
            else:
                continue
        except IndexError:
            continue

    return posibles
         


def can_draw(x,y, canvas,direction):
    global fail
    if canvas[x][y] == '  ' and canvas[x+direction[0]][y+direction[1]] == '  ':
        return True
    elif canvas[x][y] == 'E1' or canvas[x][y] == 'E2' or canvas[x][y] == 'E3' or canvas[x][y] == 'E4' or canvas[x][y] == 'E5' or canvas[x][y] == 'E6':
        fail = True
        return False 
    else:
        return False



def draw_canvas(canvas : list):
    print('__'*22)
    for row in canvas:
        print('|',end='')
        for column in row:
            print(column,end='')
        print('|')
    print('--'*22)
    

while True:
    step1 = init_places(draw_canvas_empty())

    if fail:
        continue
    else:
        draw_canvas(step1)
        break

print('finish')

