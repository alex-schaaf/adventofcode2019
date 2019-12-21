with open("06/input.txt", "r") as f:
    orbit_codes = [l.rstrip() for l in f.readlines()]


def find_path(graph:dict, start:str, end:str):
    path = [start]
    if start == end:
        return path
    for k, v in graph.items():
        if start in v:
            path.append(
                find_path(graph, k, end)
            )
    return path

def get_graph(orbit_codes):
    graph = {}
    edges = set()
    nodes = set()
    for edge in orbit_codes:
        e1, e2 = edge.split(")")
        edges.add((e1, e2))
        nodes.add(e1)
        nodes.add(e2)
        if e1 in graph.keys():
            graph[e1].append(e2)
        else:
            graph[e1] = [e2]

    return graph, nodes, edges


def flatten(L):
    """https://www.reddit.com/r/learnpython/comments/5yxgd4/flatten_a_nested_list_using_recursion_simplify/"""
    return [L] if not isinstance(L, list) else [x for X in L for x in flatten(X)]


from tqdm import tqdm

graph, nodes, edges = get_graph(orbit_codes)
counter = 0
for node in tqdm(nodes):
    L = find_path(graph, node, "COM")
    counter += len(flatten(L)) - 1

print(f"Result #1: {counter}")