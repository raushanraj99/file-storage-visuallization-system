import random

class IndexedAllocation:
    def allocate(self, block_manager, file_name, num_blocks):
        free_blocks = [i for i, b in enumerate(block_manager.blocks) if b is None]
        if len(free_blocks) < num_blocks + 1:
            return None

        selected = random.sample(free_blocks, num_blocks + 1) 
        index_block = selected[0]
        data_blocks = selected[1:]

        block_manager.blocks[index_block] = f"{file_name}_index"
        for i in data_blocks:
            block_manager.blocks[i] = file_name

        return [index_block] + data_blocks
