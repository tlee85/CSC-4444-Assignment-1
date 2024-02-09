import heapq


def uniform_cost_search(start, goals, graph, costs):
    answer = {node: {'cost': float('inf'), 'path': []} for node in goals}
  
    queue = [(0, start, [start])]
   
    visited = set()
    
    while queue:
    
        cost, node, path = heapq.heappop(queue)
        
 
        if node in goals and cost < answer[node]['cost']:
            answer[node]['cost'] = cost
            answer[node]['path'] = path
        
 
        visited.add(node)
        
      
        for neighbor, edge_cost in graph[node].items():
      
            total_cost = cost + costs[(node, neighbor)]
           
            if neighbor not in visited and (total_cost, neighbor) not in [(item[0], item[1]) for item in queue]:
                heapq.heappush(queue, (total_cost, neighbor, path + [neighbor]))
           
            elif (total_cost, neighbor) in [(item[0], item[1]) for item in queue] and total_cost < [item[0] for item in queue][[(item[0], item[1]) for item in queue].index((total_cost, neighbor))]:
                queue[[item[0] for item in queue].index((total_cost, neighbor))] = (total_cost, neighbor, path + [neighbor])
                heapq.heapify(queue)
    
    return answer
 

if __name__ == '__main__':
     
 
    graph, cost = [{} for i in range(30)], {}
 

    graph[0][4] = 1
    graph[0][5] = 1
    graph[0][16] = 1
    graph[2][1] = 1
    graph[3][1] = 1
    graph[4][2] = 1
    graph[4][3] = 1
    graph[4][5] = 1
    graph[5][8] = 1
    graph[5][18] = 1
    graph[6][3] = 1
    graph[6][7] = 1
    graph[8][16] = 1
    graph[8][17] = 1
    graph[16][17] = 1
    graph[18][6] = 1
    

    cost[(0, 4)] = 3
    cost[(0, 5)] = 9
    cost[(0, 16)] = 1
    cost[(2, 1)] = 2
    cost[(3, 1)] = 2
    cost[(4, 2)] = 1
    cost[(4, 3)] = 8
    cost[(4, 5)] = 2
    cost[(5, 8)] = 3
    cost[(5, 18)] = 2
    cost[(6, 3)] = 3
    cost[(6, 7)] = 2
    cost[(8, 16)] = 4
    cost[(8, 17)] = 4
    cost[(16, 17)] = 15
    cost[(18, 6)] = 1
    
  
    start = 0
    
  
    goal = [7]
    
    min_cost_info = uniform_cost_search(start, goal, graph, cost)

    for node, info in min_cost_info.items():
        print(f'Minimum cost from {start} to {node} is {info["cost"]}')
        print(f'Path: {info["path"]}')