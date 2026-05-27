import hashlib
from pathlib import Path
import ollama

# Code by Salvatore Nicholson
# Side project created on May 27, 2026

path = "~/Desktop/mesyy"

# p = Path(input("Enter the folder to be organized: ")).expanduser()
p = Path(path).expanduser().resolve()

if (not p.is_dir()) or (not p.exists()):
    raise SystemExit("The folder does not exist or is not a directory")

# List all files and directories
all_files = list(p.iterdir())

for f in range(len(all_files)):
    all_files[f] = all_files[f].resolve()
    if all_files[f].is_dir():
        all_files[f] = all_files[f].name + " (folder)"
    else:
        all_files[f] = all_files[f].name

all_files.sort()
print(all_files)