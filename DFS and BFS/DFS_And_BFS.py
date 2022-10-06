# Program TO Implement DFS
def get_path(hirachi, goal):
    node = goal
    if node not in hirachi.keys():
        print("No Goal Found ..!!")
        return
    while node is not None:
        print(node + "->")
        node = hirachi[node]


def successor(node, space):
    return space[node]


def goal_test(node, goal):
    return node == goal


def bfs(start, goal, space):
    open_list = [start]
    close_list = []

    hirarchi = {start: None}

    while len(open_list) != 0:
        node = open_list[0]
        del open_list[0]
        close_list.append(node)

        print("N  : ", node)
        print("Open List : ", open_list)
        print("Close List : ", close_list)
        print("Goal Test : ", goal_test(node, goal))
        print("Successor : ", successor(node, space))
        print("Hirachi : ", hirarchi)

        if goal_test(node, goal):
            break

        for ele in successor(node, space):
            if ele not in close_list:
                open_list.append(ele)
                hirarchi[ele] = node

    return hirarchi


def dfs(start, goal, space):
    open_list = [start]
    close_list = []

    hirarchi = {start: None}

    while len(open_list) != 0:
        node = open_list[-1]
        del open_list[-1]
        close_list.append(node)

        print("N  : ", node)
        print("Open List : ", open_list)
        print("Close List : ", close_list)
        print("Goal Test : ", goal_test(node, goal))
        print("Successor : ", successor(node, space))
        print("Hirachi : ", hirarchi)

        if goal_test(node, goal):
            break

        for ele in successor(node, space):
            if ele not in close_list:
                open_list.append(ele)
                hirarchi[ele] = node

    return hirarchi


graph = {
    'S0': ['S1', 'S2'],
    'S1': ['S0', 'S3'],
    'S2': ['S2', 'S4'],
    'S3': ['S3', 'S5'],
    'S4': ['S4', 'S6'],
    'S5': ['S5', 'S7'],
    'S6': ['S7'],
    'S7': ['S6'],
}

open_list = []
start = 'S0'
goal = 'S5'

print("DFS Path : ")
get_path(dfs(start, goal, graph), goal)
print()

print("BFS Path : ")
get_path(bfs(start, goal, graph), goal)
print()
