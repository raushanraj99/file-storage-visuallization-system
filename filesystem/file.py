class File:
    def __init__(self, name, size, allocation_type, blocks):
        self.name = name
        self.size = size
        self.allocation_type = allocation_type
        self.blocks = blocks

    def __str__(self):
        return f"{self.name} ({self.size} blocks) → {self.allocation_type}, Blocks: {self.blocks}"
