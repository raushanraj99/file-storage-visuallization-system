from filesystem.file import File

class Directory:
    def __init__(self, name='root'):
        self.name = name
        self.files = {} 
        self.subdirectories = {}  

    def create_file(self, file_name, file_obj):
        if file_name in self.files:
            raise Exception("File already exists.")
        self.files[file_name] = file_obj

    def delete_file(self, file_name):
        if file_name in self.files:
            del self.files[file_name]
        else:
            raise Exception("File not found.")

    def add_subdirectory(self, folder_name):
        if folder_name in self.subdirectories:
            raise Exception("Folder already exists.")
        self.subdirectories[folder_name] = Directory(folder_name)

    def get_subdirectory(self, folder_name):
        return self.subdirectories.get(folder_name, None)

    def list_contents(self):
        print(f"\n📁 Directory: {self.name}")
        for folder in self.subdirectories:
            print(f"[D] {folder}")
        for file in self.files.values():
            print(f"[F] {file}")

    def find_path(self, path: str):
        parts = path.strip('/').split('/')
        current = self
        for part in parts:
            if part in current.subdirectories:
                current = current.subdirectories[part]
            else:
                raise Exception(f"Folder '{part}' not found.")
        return current
