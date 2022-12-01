depths = [int(depth.strip()) for depth in open('01a_input', 'r').readlines()]
increased = [sum(depths[i+1:i+4]) > sum(depths[i:i+3]) for i in range(0, len(depths) - 3)]  # noqa: E501
print(len([i for i in increased if i]))
