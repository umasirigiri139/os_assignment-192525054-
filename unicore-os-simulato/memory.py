def fifo(refs, frames):
    memory, faults = [], 0
    for r in refs:
        if r not in memory:
            faults += 1
            if len(memory) >= frames: memory.pop(0)
            memory.append(r)
    return faults
 
def lru(refs, frames):
    memory, faults = [], 0
    for r in refs:
        if r in memory:
            memory.remove(r); memory.append(r)          # mark as most-recent
        else:
            faults += 1
            if len(memory) >= frames: memory.pop(0)      # evict least-recently-used
            memory.append(r)
    return faults
 
def optimal(refs, frames):
    memory, faults = [], 0
    for idx, r in enumerate(refs):
        if r not in memory:
            faults += 1
            if len(memory) >= frames:
                future = refs[idx + 1:]
                victim = max(memory, key=lambda m: future.index(m) if m in future else float("inf"))
                memory.remove(victim)
            memory.append(r)
    return faults
