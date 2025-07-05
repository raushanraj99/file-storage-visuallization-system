def show_disk(blocks, blocks_per_row=8, show_names=True):
    total = len(blocks)
    print("\n📦 Disk Blocks (X = used, . = free):\n")
    
    for i in range(0, total, blocks_per_row):
        row = blocks[i:i + blocks_per_row]
        if show_names:
            print(" | ".join([f"{b if b else '.' :^10}" for b in row]))
        else:
            print(" ".join(['X' if b else '.' for b in row]))

def disk_summary(blocks):
    used = len([b for b in blocks if b is not None])
    free = len(blocks) - used
    print(f"\n🔍 Disk Summary:\nTotal: {len(blocks)} | Used: {used} | Free: {free}")
