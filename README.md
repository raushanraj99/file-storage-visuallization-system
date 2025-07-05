# 📦 File Storage System Simulator

A command-line simulator for file systems with different block allocation strategies.

## 🚀 Features
- Contiguous, Linked, and Indexed allocation strategies
- File creation, deletion, and disk usage tracking
- Directory and file management
- Persistent state saving between sessions
- Disk block visualization

## 🛠 Technologies
- Python 3.8+
- No external libraries required

## 📁 File Structure
- `storage/`: Allocation logic
- `filesystem/`: File/Directory structure
- `cli/`: CLI interface
- `utils/`: Visualization + persistence
- `tests/`: Strategy testing

## ⚙️ Installation & Setup

```bash
# Clone repo
git clone https://github.com/yourusername/file-storage-simulator.git
cd file-storage-simulator

# Create virtual env (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies (none required)
pip install -r requirements.txt
