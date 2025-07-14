from collections import defaultdict

def find_itinerary(tickets):
    graph = defaultdict(list)
    for src, dst in sorted(tickets)[::-1]:
        graph[src].append(dst)

    res = []
    def dfs(airport):
        while graph[airport]:
            dfs(graph[airport].pop())
        res.append(airport)

    dfs("JFK")
    return res[::-1]

print(find_itinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
