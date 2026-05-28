from pathlib import Path
import ollama

# Code by Salvatore Nicholson
# Side project created on May 27, 2026

path = "~/Desktop/mesyy"
prompt = Path("PROMPT.md")

# p = Path(input("Enter the folder to be organized: ")).expanduser().resolve()
p = Path(path).expanduser().resolve()

if (not p.is_dir()) or (not p.exists()):
    raise SystemExit("The folder does not exist or is not a directory")

# List all files and directories
all_files = list(p.iterdir())

for i, file in enumerate(all_files):
    all_files[i] = all_files[i].resolve()
    if all_files[i].is_dir():
        all_files[i] = {"name": f"{all_files[i].name} (folder)", "path": str(all_files[i].expanduser().resolve())}
    else:
        all_files[i] = {"name": all_files[i].name, "path": str(all_files[i].expanduser().resolve())}

no_hidden_files = []

for i in all_files:
    if not i["name"].startswith("."):
        no_hidden_files.append(i)

all_files = no_hidden_files

print(all_files)

history = [{"role": "system", "content": prompt.read_text()}]