from turtle import title
from wandering import ComunWandering, Wandering
from track import Track
from location import location

from bokeh.plotting import figure, output_file, show

def walking(location, wandering, steps):
    beginning = location.get_location(wandering)
     
    for _ in range(steps):
        location.move_wandering(wandering)
        
    return beginning.distance(location.get_location(wandering))

def simulate_walk(steps, number_attempts, type_wandering):
    Wandering = type_wandering(name='Alirio')
    origen = location(0,0)
    distances = []
    
    for _ in range(number_attempts):
        track = Track()
        track.add_wandering(Wandering, origen)
        simulations_walk = walking(track, Wandering, steps)
        distances.append(round(simulations_walk, 1))
    return distances

def graph(x, y):
    graphics = figure(title='Camino del errante', x_axis_label='Pasos', y_axis_label='Distacia')
    graphics.line(x. y, legend='Distancia')
    show(graphics)