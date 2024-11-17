import heapq

def dijkstra(graph, start, end):
    queue = [(0, start)]  # (cost, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # print(f"Memproses node {current_node} dengan jarak {current_distance}")

        if current_node == end:
            print("\n")
            print(f"Tujuan {end} ditemukan dengan jarak {current_distance}")
            print("\n")
            break

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
                # print(f"  Menemukan tetangga {neighbor} dengan jarak baru {distance}")

    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path = path[::-1]  

    if distances[end] == float('inf'):
        return f"Tidak ada jalur dari {start} ke {end}."
    else:
        return f"Jalur terpendek dari {start} ke {end} adalah {' -> '.join(path)} dengan total jarak {distances[end]}."

# Contoh pemanggilan fungsi
if __name__ == "__main__":
    # Contoh graf
    graph_data = {
        'P13': {'P7': 3, 'P12': 4},
        'P7': {'P13': 3, 'P9': 2},
        'P12': {'P13': 4, 'P9': 4, 'T12': 5},
        'P9': {'P7': 2, 'P8': 3, 'P12': 4, 'P10': 8},
        'P8': {'P9': 3},
        'T12': {'P12': 5, 'P11': 3},
        'P11': {'T12': 3, 'P10': 5},
        'P10': {'P9': 8, 'P11': 5}
    }
    start_node = 'P13'
    end_node = 'T12'

    # Panggil fungsi dan tampilkan hasil
    print(dijkstra(graph_data, start_node, end_node))
