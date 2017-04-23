# import necessary packages
from visual import *
from visual.graph import *

display(title='Moving cart (Andrew Lavery)', background=color.white)
graph1 = gdisplay(title='Cart x vs t (Andrew Lavery)', background=color.white, foreground=color.black, xtitle='time (s)', ytitle='x (m)', )
graph1 = gcurve(color=color.red)

track = box(pos=(0,-.025,0), size=(2,.05,.1), color=color.green)
barrier = box(pos=(.95,.2,0), size=(.1,.4,.1), color=color.red)
cart = box(pos=(-.95,0.025,0), size=(.1,.05,.05), color=color.blue)
cart.velocity = vector(.5,0,0)
cart.trail = curve(color=color.magenta)

t = 0
dt = 0.01

while t < 4.00:
    if (cart.pos.x + .05) > (barrier.pos.x - .05):
        cart.velocity = cart.velocity * -1
    cart.pos = cart.pos + cart.velocity * dt
    cart.trail.append(pos=cart.pos)
    graph1.plot(pos=(t,cart.pos.x))
    t = t + dt
    rate(100)
    