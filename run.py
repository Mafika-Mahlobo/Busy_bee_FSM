from app.environment import Environment
from app.bee import Bee
from app.flower import Flower
from app.threat import Threat

env = Environment(10, 10)
actors = []
for i in range(7):
    actors.append(Bee(environment=env))
    actors.append(Flower())
    actors.append(Threat())

env.load_actors(actors)

while True:
    for agent in env._actors:
        if isinstance(agent, Bee):
            agent.update()
            env.update()
            env.grid
        print()
