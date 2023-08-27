import numpy as np

lv = np.array([0.3, 0.3])
l = 1/2
position = np.array([[0.1, 0.2, 0.3],
                     [0.1, 0.2, 0],
                     [0.7, 0.8, 0.9]])

velocity = np.array([[0.1, 0.2, 0.3],
                     [0.4, 0.5, 0.6],
                     [0.7, 0.8, 0.9]])
#for k in position:
#    a = np.all(np.abs(k[:2] - lv) < lv)



def boundary(position, velocity, l, lv):
    index = np.where((position >= l) | (position <= -l))
    velocity[index] *= -1
    for k in position[index[0]]:
        if np.all(np.abs(k[:2] - lv) < lv):
            position[index[0]] = np.array([0,0,0])
            velocity[index[0]] = np.array([0,0,0])
        array = np.array([position, velocity])      
    return array
#print(boundary(position,velocity,l,lv))


index = np.where(np.all(np.logical_and(position <= 0.3, position >= -0.3), axis=1))
indixe =np.where((position >= l) | (position <= -l))
velocity[indixe] *= -1
for k in position[index[0]]:
    if k[2] <=0 and np.all(np.abs(k[:2] - lv) < lv):
        position[index] = np.array([0,0,0])
        velocity[index] = np.array([0,0,0])
print(position)
