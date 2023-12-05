import random
import matplotlib.pyplot as plt

def random_walk(num_steps,prob_right,num_particles):
    particle_paths=[]                       #vamos criar uma lista principal onde vamos anexar todas as listas dos caminhos percorridos por cada partícula
    for n in range(1,num_particles+1):
        particle_path=[0]
        time=1
        position=0
        while time<=num_steps:
            x=random.uniform(0,1)
            if x<=prob_right:
                position=position+1
            elif x>prob_right:
                position=position-1
            particle_path.append(position)
            time+=1 
        particle_paths.append(particle_path)

    create_plot(num_steps, particle_paths)

    return particle_paths


def create_plot(num_steps,particle_paths):
    time = [x for x in range(len(particle_paths[0]))]

    for particle_path in particle_paths:
        plt.plot(particle_path,time)

    plt.title('Random_Walk - N particles')
    plt.xlabel('Position')
    plt.ylabel('Time')
    plt.show()

num_steps = 100
prob_right = 0.500
num_particles = 60

random_walk(num_steps, prob_right, num_particles)