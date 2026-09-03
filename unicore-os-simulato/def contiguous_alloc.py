def contiguous_alloc(disk, size):
    for start, length in disk.free_runs():
        if length >= size:
            blocks = list(range(start, start + size))
            disk.mark(blocks); return blocks
    return None                                            # no run big enough
 
def linked_alloc(disk, size):
    free_blocks = [i for i, f in enumerate(disk.free) if f]
    if len(free_blocks) < size: return None
    blocks = free_blocks[:size]; disk.mark(blocks); return blocks
 
def indexed_alloc(disk, size):
    free_blocks = [i for i, f in enumerate(disk.free) if f]
    if len(free_blocks) < size + 1: return None            # +1 for the index block
    index_block, data_blocks = free_blocks[0], free_blocks[1:size + 1]
    disk.mark([index_block] + data_blocks)
    return index_block, data_blocks
