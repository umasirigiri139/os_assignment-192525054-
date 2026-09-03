def le(a, b):
    return all(a[i] <= b[i] for i in range(len(a)))
 
def safety_algorithm(alloc, need, available, procs):
    work = list(available)
    finish = {p: False for p in procs}
    sequence = []
    changed = True
    while changed:
        changed = False
        for p in procs:
            if not finish[p] and le(need[p], work):
                for i in range(4):
                    work[i] += alloc[p][i]
                finish[p] = True
                sequence.append(p)
                changed = True
    return all(finish.values()), sequence, work
 
def request_resource(pid, request, alloc, need, available):
    if not le(request, need[pid]):
        return "REJECTED: exceeds declared maximum claim"
    if not le(request, available):
        return "MUST WAIT: exceeds Available resources"
    # tentatively grant, then re-run safety_algorithm on the new state
    # -> GRANTED if still safe, otherwise roll back and wait
