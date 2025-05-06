import random

def activation(neurones, entrees):
    """
    Programmer une fonction activation(neurone,entree) qui selon
    l’état de neurone = [p1,p2,p3] et les valeurs entree = [e1,e2,e3]
    renvoie s = 1 en cas d’activation et s = 0 sinon.
     s = 1            si           p1e1 + p2e2 + p3e3 ≥ 1
               s = 0            sinon.
    """
    s = sum(neurones[i] * entrees[i] for i in range(len(neurones)))
    return 1 if s >= 1 else 0

def apprentissage(neurones, entree, objectif):
    """
    renvoie l’état [p’1, p’2, p’3 ] ] modiﬁé du neurone après apprentissage
    avec l’entrée et l’objectif (0 ou 1) donné.
    """
    s = activation(neurones, entree)
    if s == objectif:
        return neurones
    else:
        epsilon = 0.2
        for i in range(len(neurones)):
            if s == 0 and objectif == 1:
                neurones[i] += epsilon * entree[i]
            elif s == 1 and objectif == 0:
                neurones[i] -= epsilon * entree[i]
        return neurones

def get_random_colors(n):
    return [(random.randint(0, 255) / 255, random.randint(0, 255) / 255, random.randint(0, 255) / 255) for _ in range(n)]

def generate_color(n):
    l = []
    for _ in range(n):
        c = get_random_colors(1)[0]
        g = list(c)
        if c[0] > 200 / 255:  # Normalize the comparison value
            l.append((1, g))
        else:
            l.append((0, g))
    return l

def train(neurones, obj):
    for objectif, entree in obj:
        neurones = apprentissage(neurones, entree, objectif)
    return neurones

neurones = [1, 1, 1]
entrees = generate_color(200)
data = train(neurones, entrees)

# utilise le perceptron sens inverse
r=255
g=255
b=255
color = [r/255, g/255, b/255]
s = activation(data, color)
if s==1:
    print(f"color {r},{g},{b} is a redish color")
else:
    print(f"color {r},{g},{b} isnt a redish color")