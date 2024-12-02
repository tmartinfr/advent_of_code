import sys


reports = []

for line in open(sys.argv[1]).readlines():
    reports.append([int(level) for level in line.strip().split(" ")])

def is_safe(report, allow_alteration=False):
    initial_ascending = None
    for i, level in enumerate(report):
        if i == 0:
            continue
        diff = level - report[i-1]
        ascending = diff > 0
        if initial_ascending is None:
            initial_ascending = ascending
        if ascending != initial_ascending or not 1 <= abs(diff) <= 3:
            if not allow_alteration:
                return False
            for i in range(0, len(report)):
                altered_report = report.copy()
                altered_report.pop(i)
                if is_safe(altered_report):
                    return True
            else:
                return False
    else:
        return True


safe_reports = sum([1 for report in reports if is_safe(report)])
print(safe_reports)

safe_reports = sum([1 for report in reports if is_safe(report, allow_alteration=True)])
print(safe_reports)
