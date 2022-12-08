data = open('06_input').readline().strip()


def find_pos(sl):
    for i in range(sl - 1, len(data)):
        if len(set(data[i-sl+1:i+1])) == sl:
            return i + 1


print(find_pos(4))
print(find_pos(14))
