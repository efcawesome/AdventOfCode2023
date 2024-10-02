import math

with open("Day8Input.txt") as f:
    fr = f.readlines()
    instructions = fr[0].strip()
    nodes = [x.strip() for x in fr[2:]]

node_dict = {}


def format_nodes():
    for node in nodes:
        node_dict[node.split(" = ")[0]] = [node.split(" = ")[1].strip("(").strip(")").split(", ")[0], node.split(" = ")[1].strip("(").strip(")").split(", ")[1]]


def nodes_end_in_z(node_list, range):
    for i in range:
        if node_list[i][2] != "Z":
            return False

    return True


def puzzle1():
    format_nodes()
    print(node_dict)

    steps = 0
    curr_node = "AAA"

    while curr_node != "ZZZ":
        for instruction in instructions:
            index = 0

            if instruction == "R":  # interpret instruction
                index = 1

            curr_node = node_dict[curr_node][index]
            steps += 1

            if curr_node == "ZZZ":
                break

    print(steps)


def puzzle2():
    format_nodes()

    curr_nodes = []

    for node in node_dict:  # get A nodes
        if node[2] == "A":
            curr_nodes.append(node)

    index_list = []
    for instruction in instructions:
        if instruction == "R":
            index_list.append(1)
        else:
            index_list.append(0)

    repeat_amounts = []
    for i in range(len(curr_nodes)):
        steps = 0
        while curr_nodes[i][2] != "Z":
            for index in index_list:
                curr_nodes[i] = node_dict[curr_nodes[i]][index]
                steps += 1

                if curr_nodes[i][2] == "Z":
                    break

        repeat_amounts.append(steps)

    print(math.lcm(*repeat_amounts))


puzzle2()

