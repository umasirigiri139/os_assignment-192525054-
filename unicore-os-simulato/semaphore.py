semaphore rw_mutex = 1      // controls exclusive access for a writer
semaphore mutex     = 1      // protects read_count
semaphore queue     = 1      // FIFO fairness gate (prevents writer starvation)
int read_count = 0
 
Reader():
    wait(queue)
        wait(mutex)
            read_count++
            if read_count == 1: wait(rw_mutex)   // first reader locks out writers
        signal(mutex)
    signal(queue)
    ... read the exam record ...
    wait(mutex)
        read_count--
        if read_count == 0: signal(rw_mutex)     // last reader unlocks writers
    signal(mutex)
 
Writer():
    wait(queue)
        wait(rw_mutex)
    signal(queue)
    ... write the exam record ...
    signal(rw_mutex)
