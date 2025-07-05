import random

class LinkedAllocation:
    def allocate(self, block_manager, file_name, num_blocks):
        free_blocks = [i for i, b in enumerate(block_manager.blocks) if b is None]
        if len(free_blocks) < num_blocks:
            return None

        selected = random.sample(free_blocks, num_blocks)
        for i in selected:
            block_manager.blocks[i] = file_name
        return selected
