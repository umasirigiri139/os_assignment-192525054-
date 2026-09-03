def scan(reqs, start, max_cyl=199):
    left  = sorted([r for r in reqs if r < start])
    right = sorted([r for r in reqs if r >= start])
    order = right + [max_cyl] + list(reversed(left))     # sweep up, then reverse
    movement, cur = 0, start
    for nxt in order:
        movement += abs(nxt - cur); cur = nxt
    return movement
 
def cscan(reqs, start, max_cyl=199):
    left  = sorted([r for r in reqs if r < start])
    right = sorted([r for r in reqs if r >= start])
    order = right + [max_cyl, 0] + left                   # sweep up, wrap to 0
    movement, cur = 0, start
    for nxt in order:
        movement += abs(nxt - cur); cur = nxt
    return movement
