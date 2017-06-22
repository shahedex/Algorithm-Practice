from collections import deque

def BreadthFirstSearch(start,s):
    search_queue = deque()
    search_queue += graph[start]
    searched = []

    while search_queue:
        pop_item = search_queue.popleft()

        if not pop_item in searched:
            if pop_item == s:
                print(str(s) + " is found.")
                return True
            else:
                search_queue += graph[pop_item]
                searched.append(pop_item)
    return False

graph = {}
graph["1"] = ["0","2"]
graph["0"] = ["7"]
graph["2"] = []
graph["7"] = []
print(graph)
inp = input("Enter the item to be searched : ")
if not BreadthFirstSearch("1",inp) :
    print(str(inp) + " is not found")
