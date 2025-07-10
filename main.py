from cli.menu import main_menu
from storage.block_manager import BlockManager
from filesystem.directory import Directory
from storage.contiguous import ContiguousAllocation
from storage.linked import LinkedAllocation
from storage.indexed import IndexedAllocation
from utils.persistence import save_state, load_state

blocks, root_directory = load_state()
block_manager = BlockManager()
if blocks:
    block_manager.blocks = blocks
if not root_directory:
    root_directory = Directory()

current_allocation = [ContiguousAllocation()]
strategy_map = {
    "contiguous": ContiguousAllocation(),
    "linked": LinkedAllocation(),
    "indexed": IndexedAllocation()
}

if __name__ == "__main__":
    print("=== File Storage System Simulator ===")
    main_menu(root_directory, block_manager, strategy_map, current_allocation)
