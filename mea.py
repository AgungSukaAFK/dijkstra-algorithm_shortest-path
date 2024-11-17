def means_ends_analysis(start, goal, graph):
    queue = [[start]] 
    visited = []
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node == goal:
            return path

        if node not in visited:
            visited.append(node)
    
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return None

graph = {
    'A': ['1', '2'],
    '1': [],
    '2': ['3'],
    '3': ['B'],
    'B': []
}
start = 'A'
goal = 'B'
result = means_ends_analysis(start, goal, graph)

if result:
    print(f"Jalur yang ditemukan: {' -> '.join(result)}")
else:
    print("Tidak ada jalur yang ditemukan.")
