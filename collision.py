import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

initial_pos1 = 1
initial_pos2 = 4
initial_velocity1 = -0.1
initial_velocity2 = 0.1
mass1 = 1.0
mass2 = 1.0
num_frames = 100
box_size = 5

def simulate_collision(initial_pos1,initial_pos2,initial_velocity1,initial_velocity2,mass1,mass2,num_frames,box_size):
    ball1_x=[initial_pos1]
    ball2_x=[initial_pos2]

    if initial_pos1>initial_pos2:    
        initial_pos1,initial_pos2=initial_pos2,initial_pos1
        mass1,mass2=mass2,mass1
        initial_velocity1,initial_velocity2=initial_velocity2,initial_velocity1     #vamos garantir que a bola da esquera é a 1 para simplificar o código

    frame=0    #forma de definirmos cada instante
    while frame<num_frames:
        if initial_pos1<=0.1:                               #estamos a garantir que a bola 1(da esquerda) não ultrapassa a caixa que definimos tendo em conta o raio 
            initial_velocity1=-initial_velocity1
        elif box_size-0.1<=initial_pos2:                    #estamos a garantir que a bola 2(da direita) não ultrapassa a caixa que definimos tendo em conta o raio
            initial_velocity2=-initial_velocity2
        elif initial_pos1>=initial_pos2-0.2:                #quando as bolas "colidirem", ou seja, quando a bola 1 estiver a tocar na 2 ou à sua direita, efetuamos a conservação do momento
            initial_velocity1,initial_velocity2=float((2*mass2*initial_velocity2+initial_velocity1*(mass1-mass2))/(mass1+mass2)),float((2*mass1*initial_velocity1+initial_velocity2*(mass2-mass1))/(mass1+mass2))
        initial_pos1=float(initial_velocity1*frame + initial_pos1) 
        ball1_x.append(initial_pos1)
        initial_pos2=float(initial_velocity2*frame + initial_pos2)
        ball2_x.append(initial_pos2)                         #definimos as fórmulas gerais de velocidade para cada frame e guardamos a posição na lista de posições
        frame+=0.01     

    create_animation(ball1_x, ball2_x, box_size)

def create_animation(positions1,positions2,box_size):
    num_frames=len(positions1)

    fig , ax= plt.subplots()
    ax.set_xlim(0,box_size)
    ax.set_ylim(-0.1,0.1)

    ball1,= ax.plot(positions1[0],0,'bo',markersize=10)
    ball2,= ax.plot(positions2[0],0,'ro',markersize=10)

    def update(frame):
        ball1.set_xdata(positions1[frame])
        ball2.set_xdata(positions2[frame])
        return ball1, ball2
    
    ani = FuncAnimation(fig, update, frames=num_frames , blit=True)
    plt.show()

    plt.close(fig)

    return

simulate_collision(initial_pos1,initial_pos2,initial_velocity1,initial_velocity2,mass1,mass2,num_frames,box_size)
