import pickle

def save_state(block_manager, root_directory, filename="storage_state.pkl"):
    with open(filename, "wb") as f:
        pickle.dump({
            'blocks': block_manager.blocks,
            'directory': root_directory
        }, f)
    print("✅ State saved.")

def load_state(filename="storage_state.pkl"):
    try:
        with open(filename, "rb") as f:
            data = pickle.load(f)
            return data['blocks'], data['directory']
    except FileNotFoundError:
        print("ℹ️ No previous state found. Starting fresh.")
        return None, None
