import random
import networkx as nx
import matplotlib.pyplot as plt

class QuantumMultiverseSimulator:
    def __init__(self):
        self.world_counter = 1
        self.graph = nx.DiGraph()
        self.graph.add_node(self.world_counter, label="World 1")
        
    def diverge(self, world_id):
        self.world_counter += 1
        new_world_id1 = self.world_counter
        self.world_counter += 1
        new_world_id2 = self.world_counter

        event = random.choice(["Event A", "Event B", "Event C"])

        self.graph.add_node(new_world_id1, label=f"World {new_world_id1} ({event})")
        self.graph.add_node(new_world_id2, label=f"World {new_world_id2} ({event})")
        self.graph.add_edge(world_id, new_world_id1)
        self.graph.add_edge(world_id, new_world_id2)

        return new_world_id1, new_world_id2

    def simulate(self, steps):
        current_worlds = [1]
        for _ in range(steps):
            new_worlds = []
            for world in current_worlds:
                 new_worlds.extend(self.diverge(world))
            current_worlds = new_worlds
    

    def visualize(self):
        pos = nx.spring_layout(self.graph)
        labels = nx.get_node_attributes(self.graph, 'label')
        plt.figure(figsize=(12, 8))
        nx.draw(self.graph, pos, with_labels=True, labels=labels, node_size=700, node_color='skyblue', font_size=10, font_color='black', edge_color='gray')
        plt.title("Quantum Multiverse Simulation")
        plt.savefig("quantum_multiverse_simulation.png")
        plt.close()


if __name__ == "__main__":
    simulator = QuantumMultiverseSimulator()
    simulator.simulate(3)  
    simulator.visualize()
        
