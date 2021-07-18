from vpython import *
#GlowScript 3.1 VPython

from vpython import *
scene = display( width = 600, height = 600, center = vector(0,0,0))

lamp = local_light(pos=vector(0,0,0), color=color.orange)
G = 6.67 *pow(10,-11)
userspin = True

ME = 5.973 *pow(10,24)
MM = 7.347 *pow(10,22)
MMa = 6.39 *pow(10,23)
MS = 1.989 *pow(10,30)
REM = 384400000
RSE = 149600000000
RMS = 227900000000
FEM = G*(ME*MM)/pow(REM,2)
FES = G*(MS*ME)/pow(RSE,2)
FEMa = G*(MMa*MS)/pow(RMS,2)

wM = sqrt(FEM/(MM * REM))
vM = wM * REM
print("Angular velocity of the Moon with respect to the Earth: ",wM," rad/s")
print("Velocity v of the Moon: ",vM/1000," km/s")

wE = sqrt(FES/(ME * RSE))
wMa = sqrt(FEMa/(MMa * RMS))
vE = 10*wE * RSE
vMa = 10*wMa * RMS
print("Angular velocity of the Earth with respect to the Sun: ",wE," rad/s")
print("Velocity v of the Earth: ",vE/1000," km/s")


theta0 = 20

def positionMoon(t):                                     
    theta = theta0 + wM * t
    return theta

def positionMars(t):                                     
    theta = theta0 + wMa * t
    return theta

def positionEarth(t):
    theta = theta0 + wE * t
    return theta


def fromDaysToS(d):
    s = d*24*60*60
    return s

def fromStoDays(s):
    d = s/60/60/24
    return d

def fromDaysToh(d):
    h = d * 24
    return h

print("\nSimulation Earth-Moon-Sun motion\n")
days = 365
seconds = fromDaysToS(days)
print("Days: ",days)
print("Seconds: ",seconds)

v = vector(384,0,0)
E = sphere(pos = vector(1500,0,0), color = color.blue, radius = 60, make_trail=True)
Ma = sphere(pos = vector(2300,0,0), color = color.orange, radius = 30, make_trail=True)
M = sphere(pos = E.pos + v, color = color.white,radius = 10, make_trail=True)
S = sphere(pos = vector(0,0,0), color = color.yellow, radius=700)

t = 0
thetaTerra1 = 0
dt = 5000
dthetaE = positionEarth(t+dt)- positionEarth(t)
dthetaM = positionMoon(t+dt) - positionMoon(t)
dthetaMa = positionMars(t+dt) - positionMars(t)
print("delta t:",dt,"seconds. Days:",fromStoDays(dt),"hours:",fromDaysToh(fromStoDays(dt)),sep=" ")
print("Variation angular position of the Earth:",dthetaE,"rad/s that's to say",degrees(dthetaE),"degrees",sep=" ")
print("Variation angular position of the Moon:",dthetaM,"rad/s that's to say",degrees(dthetaM),"degrees",sep=" ")

while t < seconds:
    rate(500)
    thetaEarth = positionEarth(t+dt)- positionEarth(t)
    thetaMoon = positionMoon(t+dt) - positionMoon(t)
    thetaMars = positionMars(t+dt) - positionMars(t)
    E.pos = rotate(E.pos,angle=thetaEarth,axis=vector(0,1,0))
    Ma.pos = rotate(Ma.pos,angle=thetaMars,axis=vector(0,1,0))
    v = rotate(v,angle=thetaMoon,axis=vector(0,1,0))
    M.pos = E.pos + v
t += dt