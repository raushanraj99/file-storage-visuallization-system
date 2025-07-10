class ContiguousAllocation:
    def allocate(self, block_manager, file_name, num_blocks):
        blocks = block_manager.get_block_status()
        total = len(blocks)

        for i in range(total - num_blocks + 1):
            if all(blocks[j] is None for j in range(i, i + num_blocks)):
                for j in range(i, i + num_blocks):
                    blocks[j] = file_name
                return list(range(i, i + num_blocks))
        return None