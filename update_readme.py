import os

# Einstellungen
REPO_NAME = "Wallpaper-Vault" 
USERNAME = "T4tze"  
IMAGE_FOLDER = "Wallpaper"
README_FILE = "README.md"

# Header für die README.md
readme_content = """# Here are my Wallpaper 
U cant look at my Wallpapers here:

"""

# Alle Unterordner und Bilder durchsuchen
for root, _, files in os.walk(IMAGE_FOLDER):
    relative_path = os.path.relpath(root, IMAGE_FOLDER)
    if relative_path != ".":
        readme_content += f"## {relative_path}\n\n"
    
    for filename in sorted(files):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            image_url = f"https://raw.githubusercontent.com/{USERNAME}/{REPO_NAME}/main/{root}/{filename}"
            readme_content += f"![{filename}]({image_url})\n\n"

# README.md speichern
with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(readme_content)

print(f"{README_FILE} wurde erfolgreich erstellt!")
