from collections import deque
import heapq

def bfs_distance(graph, start, stations):
    visited = {station: False for station in stations}
    distance = {station: -1 for station in stations}
    
    queue = deque()
    queue.append(start)
    visited[start] = True
    distance[start] = 0

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

    return distance

def Question1_from_string(text: str) -> str:
    lines = text.strip().splitlines()
    try:
        m, n = map(int, lines[0].split())
    except:
        return "Invalid first line (m n)"

    if len(lines) < 1 + m + n + 1:
        return "Input not long enough"

    stations = lines[1:1+m]
    edges = lines[1+m:1+m+n]
    start = lines[-1]

    graph = {station: [] for station in stations}
    for line in edges:
        a, b = line.strip().split()
        graph[a].append(b)
        graph[b].append(a)

    distance = bfs_distance(graph, start, stations)

    result = ""
    for s in stations:
        result += f"{s}: {distance[s]}\n"
    return result.strip()