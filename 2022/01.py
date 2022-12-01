l = [[int(n) for n in segment.strip().split("\n")] for segment in open('01_input', 'r').read().split("\n\n")]
l_total = [sum(s) for s in l]
print(max(l_total))
print(sum(sorted(l_total)[-3:]))
