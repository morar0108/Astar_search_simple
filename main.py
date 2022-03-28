#1) A*


graph = {}


class Node:

    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return f'{self.name}: {self.g}'


def a_star(h, start, end):
    visited = []
    to_visit = []
    start_node = Node(start, None)
    end_node = Node(end, None)

    to_visit.append(start_node)

    while len(to_visit) > 0:
        to_visit.sort()
        current_node = to_visit.pop(0)
        visited.append(current_node)

        if current_node == end_node:
            path = []
            while current_node != start_node:
                path.append(current_node)
                current_node = current_node.parent
            path.append(start_node)
            return path[::-1]

        neighbours = graph.setdefault(current_node.name)
        for key, value in neighbours.items():
            neighbour = Node(key, current_node)
            if neighbour in visited:
                continue
            neighbour.g = current_node.g + get_distance(current_node.name, neighbour.name)
            neighbour.h = h.get(neighbour.name)
            neighbour.f = neighbour.g + neighbour.h
            if add_to_open(to_visit, neighbour):
                to_visit.append(neighbour)


def add_to_open(to_visit, neighbor):
    for node in to_visit:
        if neighbor == node and neighbor.f > node.f:
            return False
    return True


def get_distance(a, b=None):
    links = graph.setdefault(a, {})
    if b is None:
        return links
    else:
        return links.get(b)


def connect(a, b, distance):
    graph.setdefault(a, {})[b] = distance
    graph.setdefault(b, {})[a] = distance


def main():
    connect('Oslo', 'Helsinki', 970)
    connect('Helsinki', 'Stockholm', 400)
    connect('Oslo', 'Stockholm', 570)
    connect('Stockholm', 'Copenhagen', 522)
    connect('Copenhagen', 'Warsaw', 668)
    connect('Warsaw', 'Bucharest', 946)
    connect('Bucharest', 'Athens', 1300)
    connect('Budapest', 'Bucharest', 900)
    connect('Budapest', 'Belgrade', 316)
    connect('Belgrade', 'Sofia', 330)
    connect('Rome', 'Palermo', 1043)
    connect('Palermo', 'Athens', 907)
    connect('Rome', 'Milan', 681)
    connect('Milan', 'Budapest', 789)
    connect('Vienna', 'Munich', 458)
    connect('Prague', 'Vienna', 312)
    connect('Prague', 'Berlin', 354)
    connect('Berlin', 'Copenhagen', 743)
    connect('Berlin', 'Amsterdam', 648)
    connect('Munich', 'Lyon', 753)
    connect('Lyon', 'Paris', 481)
    connect('Lyon', 'Bordeaux', 542)
    connect('Madrid', 'Barcelona', 628)
    connect('Madrid', 'Lisbon', 638)
    connect('Lisbon', 'London', 2210)
    connect('Barcelona', 'Lyon', 644)
    connect('Paris', 'London', 414)
    connect('London', 'Dublin', 463)
    connect('London', 'Glasgow', 667)
    connect('Glasgow', 'Amsterdam', 711)
    connect('Budapest', 'Prague', 443)
    connect('Barcelona', 'Rome', 1471)
    connect('Paris', 'Bordeaux', 579)
    connect('Glasgow', 'Dublin', 306)

    heuristics = {'Amsterdam': 2280, 'Athens': 1300, 'Barcelona': 2670, 'Belgrade': 630, 'Berlin': 1800,
                  'Bordeaux': 2100, 'Budapest': 900, 'Copenhagen': 2250, 'Dublin': 2530, 'Glasgow': 2470,
                  'Helsinki': 2820, 'Lisbon': 3950, 'London': 2590, 'Lyon': 1660, 'Madrid': 3300, 'Milan': 1750,
                  'Munich': 1600, 'Oslo': 2870, 'Palermo': 1280, 'Paris': 2970, 'Prague': 1490, 'Rome': 1140,
                  'Sofia': 390, 'Stockholm': 2890, 'Vienna': 1150, 'Warsaw': 946, 'Bucharest': 0}

    print(a_star(heuristics, 'Bucharest', 'Paris'))


if __name__ == "__main__":
    main()