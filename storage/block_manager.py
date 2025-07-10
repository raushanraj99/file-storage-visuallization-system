class BlockManager:
    def __init__(self, total_blocks=64):
        self.total_blocks = total_blocks
        self.blocks = [None] * total_blocks  

    def allocate_blocks(self, file_name, num_blocks):
        free_indices = [i for i, block in enumerate(self.blocks) if block is None]
        
        if len(free_indices) < num_blocks:
            return None  

        allocated = free_indices[:num_blocks]
        for idx in allocated:
            self.blocks[idx] = file_name
        
        return allocated

    def free_blocks(self, file_name):
        for i in range(self.total_blocks):
            if self.blocks[i] == file_name:
                self.blocks[i] = None

    def get_block_status(self):
        return self.blocks

    def show_disk(self):
        print("\nDisk Block Status:")
        for i in range(0, self.total_blocks, 8):
            row = self.blocks[i:i+8]
            print(' '.join(['.' if b is None else 'X' for b in row]))
            
    def disk_summary(self):
        used = len([b for b in self.blocks if b is not None])
        free = len(self.blocks) - used
        print(f"\n🔍 Disk Summary:\nTotal: {len(self.blocks)} | Used: {used} | Free: {free}")

   