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


def dijkstra(graph, start, end, stations):
    distance = {station: float('inf') for station in stations}
    previous = {station: None for station in stations}
    distance[start] = 0
    
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current in visited:
            continue
            
        visited.add(current)
        
        if current == end:
            break
            
        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                new_dist = current_dist + weight
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    previous[neighbor] = current
                    heapq.heappush(pq, (new_dist, neighbor))
    
    if distance[end] == float('inf'):
        return -1, []
    
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    return distance[end], path

def Question2_from_string(text: str) -> str:
    lines = text.strip().splitlines()
    try:
        m, n = map(int, lines[0].split())
    except:
        return "Invalid first line (m n)"

    if len(lines) < 1 + m + n + 2:
        return "Input not long enough"

    stations = lines[1:1+m]
    edges = lines[1+m:1+m+n]
    start = lines[-2]
    end = lines[-1]

    graph = {station: [] for station in stations}
    for line in edges:
        a, b, w = line.strip().split()
        graph[a].append((b, float(w)))
        graph[b].append((a, float(w)))

    dist, path = dijkstra(graph, start, end, stations)
    if dist == -1:
        return "-1"
    return f"{dist}\n{'  '.join(path)}"