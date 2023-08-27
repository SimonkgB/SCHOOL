#for trinket



GlowScript 3.1 VPython

################################
scene.autoscale=False
scene.range=300
scene.background = color.black
################################
B=sphere(radius=8,pos=vec(0,0,0),color=color.green)
#Initialtilstand
t=0
v=50
dt=0.05
eps = 1e-3

#While-løkke
while 1000>t:
  rate(100)
  a=-9.81
  v += a*dt
  B.pos.y += v*dt
  t += dt
  if (B.pos.y + 0.5) < eps and v < 0:
    v=-v*0.8
