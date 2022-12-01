depths = [int(depth.strip()) for depth in open('01a_input', 'r').readlines()]
increased = [depths[i + 1] > depths[i] for i in range(0, len(depths) - 1)]
print(len([i for i in increased if i]))
