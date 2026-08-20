from app.environment import Environment
from app.bee import Bee
from app.flower import Flower
from app.threat import Threat


print('Welcome to busy bee simulation.')
print('=================================')

try:
    x = int(input('Enter width: '))
    y = int(input('Enter height: '))

    actors = []
    env = Environment(y, x)

    bees = int(input('How many bees?: '))
    threats = int(input('How many threats?: '))
    flowers = int(input('How many flowers?: '))

    for _ in range(bees):
        actors.append(Bee(environment=env))

    for _ in range(threats):
        actors.append(Threat())

    for _ in range(flowers):
        actors.append(Flower())

    env.load_actors(actors)
    while True:
        for agent in env._actors:
            if isinstance(agent, Bee):
                agent.update()
                env.update()
                env.grid
            print()

except:
    print('Invalid input. All answers should be numbers. (e.g, 6)')




