from collections import defaultdict

def find_itinerary(tickets):
    graph = defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        graph[a].append(b)

    route = []
    def dfs(airport):
        while graph[airport]:
            dfs(graph[airport].pop())
        route.append(airport)

    dfs("JFK")
    return route[::-1]

print(find_itinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
