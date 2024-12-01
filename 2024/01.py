import collections
import sys


left = []
right = []
for line in open(sys.argv[1]).readlines():
    l, r = line.strip().split("   ")
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

total_distance = 0
for t in zip(left, right):
    distance = abs(t[0] - t[1])
    total_distance += distance

print(total_distance)

number_of_times = collections.Counter()
for r in right:
    number_of_times[r] += 1

singularity_score = 0
for l in left:
    singularity_score += l * number_of_times[l]

print(singularity_score)
