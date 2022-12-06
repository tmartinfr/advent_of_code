lines = open('04_input').readlines()
lr = [tuple([range(int(rs[0]), int(rs[1]) + 1) for r in s if (rs := r.split('-'))]) for l in lines if (s := l.strip().split(',')) ]
print(sum([1 if ((t[0][0] >= t[1][0] and t[0][-1] <= t[1][-1]) or (t[1][0] >= t[0][0] and t[1][-1] <= t[0][-1])) else 0 for t in lr]))
print(sum([1 if any(set(t[0]) & set(t[1])) else 0 for t in lr]))
