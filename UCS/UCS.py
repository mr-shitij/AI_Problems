
space = {
     'A': [['B',2],['C',3],['D',4]],
     'B': [['A',2],['C',2]],
     'C': [['A',3],['B',2],['D',2],['E',2]],
     'D': [['A',4],['C',2],['E',3]],
     'E': [['C',2],['D',3],['F',4]],
     'F': [['D',1],['E',4]]    
}

start =['A',0]
goal = 'E'

def successor(node, space):
    return space[node[0]]

def goal_test(node, goal):
    return node == goal

def remove_repeated(children):
    a = []
    for ele in children:
        if ele[0] not in a:
            a.append(ele)
    return a

def add_cost(children, cost):
    for ele in children:
        ele[1] += cost
    return children

def remove_if_found(children, close_list):
    li = []
    for ele in children:
        if ele[0] not in close_list:
            li.append(ele)
    return li

def path(start, goal, hirarchi):
    node = goal
    print("\nUCS:")
    print(f'path from {start} to {goal}:\n', end='')
    while node != None:
        print(f'---->{node}',end='')
        node = hirarchi[node]

def ucs(space,start,goal):
    open_list = [start]
    close_list = []
    hirarchi = {start[0]: None}
    while len(open_list) != 0:
        node = open_list.pop(0)
        close_list.append(node[0])

        print(open_list, " ", end="")
        print(node, " ", node[0], " ",end="")
        print(close_list, " ", end="")
        print(goal_test(node[0], goal), " ", end="")

        if goal_test(node[0], goal):
            path(start, goal, hirarchi)
            exit(0)
        
        
        children = successor(node, space)
        children = add_cost(children, node[1])
        children = sorted(children, key=lambda x:x[1] + node[1])

        print(children)

        op_list = [ele[0] for ele in open_list]
        for child in children:
            if child[0] not in op_list and child[0] not in close_list:
                hirarchi[child[0]] = node[0]
                open_list.append(child)
    return close_list


close_list = ucs(space,start,goal)

node = goal
print(ucs(space,start,goal))
