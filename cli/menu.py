from filesystem.file import File

def main_menu(root_directory, block_manager, strategy_map, current_allocation):
    while True:
        print("\nMain Menu:")
        print("1. Select Allocation Strategy")
        print("2. Create File")
        print("3. Read File Info")
        print("4. Delete File")
        print("5. Show Disk Usage")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            print("Choose: contiguous | linked | indexed")
            strat = input("Strategy: ").lower().strip()
            if strat in strategy_map:
                current_allocation[0] = strategy_map[strat]
                print(f"✔ Strategy set to {strat}")
            else:
                print("❌ Invalid strategy name.")

        
        elif choice == '2':
            name = input("Enter file name: ").strip()
            if not name or len(name) > 20:
                print("❌ Invalid file name.")
                continue
            if name in root_directory.files:
                print("❌ File with this name already exists.")
                continue

            try:
                size = int(input("Enter file size (in blocks): "))
                if size <= 0:
                    raise ValueError
            except ValueError:
                print("❌ Invalid size. Must be a positive integer.")
                continue

            blocks = current_allocation[0].allocate(block_manager, name, size)
            if blocks:
                file_obj = File(name, size, type(current_allocation[0]).__name__, blocks)
                root_directory.create_file(name, file_obj)
                print(f"✔ File '{name}' created.")
            else:
                print("❌ Failed to allocate file: Not enough contiguous/free blocks.")


        elif choice == '3':
            fname = input("File name: ")
            file = root_directory.files.get(fname)
            if file:
                print(file)
            else:
                print("❌ File not found.")

        elif choice == '4':
            fname = input("File name to delete: ").strip()
            if not fname:
                print("❌ Invalid file name.")
                continue

            file = root_directory.files.get(fname)
            if file:
                block_manager.free_blocks(fname)
                root_directory.delete_file(fname)
                print(f"✔ Deleted '{fname}' and freed blocks.")
            else:
                print("❌ File not found.")


        elif choice == '5':
            block_manager.show_disk()

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid option.")
