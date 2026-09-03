def round_robin(procs, quantum=4):
    queue = deque(); remaining_bt = {p[0]: p[3] for p in procs}
    t = 0; gantt = []
    while queue or not_yet_arrived_remaining:
        pid = queue.popleft()
        run = min(quantum, remaining_bt[pid])
        gantt.append((pid, t, t + run))
        t += run
        remaining_bt[pid] -= run
        enqueue_newly_arrived_processes(t)
        if remaining_bt[pid] > 0:
            queue.append(pid)          # not finished -> back of queue
        else:
            completion[pid] = t        # finished
