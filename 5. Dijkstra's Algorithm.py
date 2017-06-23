def FindLowestCostNode(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

graph = {'start':{'a':6,'b':2},'a':{'fin':1},'b':{'a':3,'fin':5},'fin':{}}
infinity = float('inf')
costs = {'a':6,'b':2,'fin':infinity}
parents = {'a':'start','b':'start','fin':None}
processed = []

node = FindLowestCostNode(costs)
while node is not None:
    cost = costs[node]
    neighbours = graph[node]
    for n in neighbours.keys():
        new_cost = cost + neighbours[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = FindLowestCostNode(costs)
    
print("Shortest path : " +str(costs['fin']))
