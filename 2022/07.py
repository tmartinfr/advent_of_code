tree = {}

for b in [s for block in open('07_input').read().split("$ ") if (s := block.strip().split("\n"))]:
    cmd = b.pop(0)
    match cmd[:2]:
        case "cd":
            dst = cmd[3:]
            match dst:
                case "/":
                    cur = [tree]
                case "..":
                    cur.pop()
                case other:
                    cur.append(cur[-1][dst])
        case "ls":
            for prefix, name in [line.split(" ") for line in b]:
                treepos = cur[-1]
                match prefix:
                    case "dir":
                        treepos[name] = {}
                    case other:
                        treepos[name] = int(prefix)


def count_size(tree, ss):
    size = 0
    for k, v in tree.items():
        if isinstance(v, dict):
            ds = count_size(tree[k], ss)
            size += ds
            ss.append(ds)
        else:
            size += v
    return size


ss = []
root_size = count_size(tree, ss)
print(sum([s for s in ss if s <= 100_000]))

unused_space = 70_000_000 - root_size
need_space = 30_000_000 - unused_space
for s in sorted(ss):
    if s >= need_space:
        print(s)
        break
