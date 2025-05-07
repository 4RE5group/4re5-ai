import random
from PIL import Image, ImageDraw

image = Image.new('RGB', (200, 200), 'white')
draw = ImageDraw.Draw(image)

epsilon = 0.2

def activation(neuron: list, entry: list) -> int:
    """
    returns the state of the neuron (0 or 1) after applying the activation function
    """
    s = 0
    for i in range(len(neuron)):
        s += neuron[i] * entry[i]

    if  s >= 1 :
        return 1
    else :
        return 0

def single_epoque_learning(neuron, entry, objective) :
    """
    returns the state of [p'1, p'2, p'3 ] edited by the learning function
    with the entry and the objective
    """

    ret = [0]*len(neuron)

    s = activation(neuron,entry)
    for i in range(len(neuron)):
        if s == objective:
            return neuron
        elif s==0 and objective == 1:
            ret[i] = neuron[i] + epsilon * entry[i]
        elif s==1 and objective == 0:
            ret[i] = neuron[i] - epsilon * entry[i]
    
    return ret



def get_random_colors(n):
    return [(random.randint(0, 255) / 255, random.randint(0, 255) / 255, random.randint(0, 255) / 255) for _ in range(n)]

def generate_color(n):
    l = []
    for _ in range(n):
        c = get_random_colors(1)[0]
        g = list(c)
        if c[0] > (180/255) and c[1] < (60/255) and c[2] < (60/255):  # mostly red
            l.append((1, g))
        else:
            l.append((0, g))
    return l

def test_colors(neurons, colors):
    l = 0
    c = 0
    errorRateCount = False
    errorRate = 0


    if type(colors[0]) == tuple and len(colors[0]) == 2:
        # need to check the error rate
        errorRateCount = True

    # just display the colors guesses
    for elem in colors:
        if errorRateCount:
            color = elem[1]
            objTest = elem[0]
        else:
            color = elem

        # Ensure color is a list or tuple with three elements
        # if isinstance(color, (list, tuple)) and len(color) == 3:
        #     r, g, b = color
        # else:
        #     continue  # Skip if color is not in the expected format
        r, g, b = color

        s = activation(neurons, color)
        # count errors
        if errorRateCount and s!=objTest:
            errorRate+=1
        

        if s == 1:
            # success
            draw.rectangle([(l*20, c*20), ((l+1)*20, (c+1)*20)], fill=(int(r*255), int(g*255), int(b*255)), outline="green")
            draw.line([(l*20, c*20), ((l+1)*20, (c+1)*20)], fill="green", width=2)
        else:
            draw.rectangle([(l*20, c*20), ((l+1)*20, (c+1)*20)], fill=(int(r*255), int(g*255), int(b*255)), outline="red")

        l += 1
        if l >= 200/20:
            l = 0
            c += 1
        if c >= 200/20:
            break

    if errorRateCount:
        entryTotal = len(colors)
        print("error rate: ")
        print(" valid:", entryTotal-errorRate)
        print(" errors:", errorRate)
        print(f"total: {entryTotal}  success rate: ~{((entryTotal-errorRate)/entryTotal)*100}%")
    image.show()

def train(neurons, entries, n=10):
    """
    trains the neuron with the entries
    """
    for _ in range(n):
        for entry, objective in entries:
            neurons = single_epoque_learning(neurons, entry, objective)
    return neurons







entry_objectives = [
([1,0,0],1), ([0,1,1],0), ([1,1,0],0),
([1,0,0.2],1), ([0,1,0],0), ([0,0,0],0),
([1,0,1],0), ([0.7,0,0],1), ([0.5,0.5,0.5],0),
([0.9,0.2,0],1), ([0.9,0,0],1), ([1,1,1],0),
([0.2,1,0],0), ([0.8,0.2,0],1), ([0.7,0.1,0.1],1) ]

neuron  = [1,1,1]   #initialisation

# train the neuron
neuron = train(neuron, entry_objectives, n=1000)


# test colors
list_rgb = generate_color(100)
test_colors(neuron, list_rgb)
