from storage.block_manager import BlockManager
from storage.contiguous import ContiguousAllocation
from storage.linked import LinkedAllocation
from storage.indexed import IndexedAllocation
from filesystem.directory import Directory
from filesystem.file import File

def test_allocation_strategy(strategy_class, label):
    print(f"\n== Testing {label} Allocation ==")
    bm = BlockManager(total_blocks=16)
    root = Directory()
    strategy = strategy_class()

    file1 = File("fileA.txt", 4, label, strategy.allocate(bm, "fileA.txt", 4))
    assert len(file1.blocks) >= 4, "FileA allocation failed"
    root.create_file("fileA.txt", file1)

    file2 = File("fileB.txt", 5, label, strategy.allocate(bm, "fileB.txt", 5))
    assert len(file2.blocks) >= 5, "FileB allocation failed"
    root.create_file("fileB.txt", file2)

    root.list_contents()
    bm.show_disk()

    print("✅ Test passed!")

# Run all three
test_allocation_strategy(ContiguousAllocation, "Contiguous")
test_allocation_strategy(LinkedAllocation, "Linked")
test_allocation_strategy(IndexedAllocation, "Indexed")
