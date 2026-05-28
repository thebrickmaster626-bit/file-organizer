# File organizer

Uses an LLM to organize a folder of your choice.

## Requirements:

- Python3.13
- Ollama installed and running
- Ollama model Ministral-3:3b (or a model of your choice that supports vision and tool calling) installed

## WARNING (read before using):

The LLM is not perfect, as such a small model and all AIs in general will not perform as intelligent and smart as a
human. Because of this, The LLM may rename documents into strange names or put documents in categories they don't belong
in. The LLM can only access files in a folder of your choice, so it will not ruin system files. It also cannot delete
anything without your explicit consent, but it can still freely rename, move, and create directories

## Notes:

- The process of organizing files will take a while and can be resource-intensive. If you wish to solve this, switch to
  a model that has a smaller parameter size or lower quantization (like q4_K_M rather than q8_0)
- The model is completely local, so if you are worried about sensitive information being passed into the LLM, please
  note it is not sent anywhere.
- However, if you choose to use a cloud model and prefer more privacy, there is a variable in `main.py` called
  `request_permission_to_read_files` and when set to `true` it will always ask before reading files.