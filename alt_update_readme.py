import os

# Einstellungen
REPO_NAME = "Wallpaper-Vault" 
USERNAME = "T4tze"  
IMAGE_FOLDER = "Wallpaper"
README_FILE = "README.md"

# Header für die README.md
readme_content = """
# Wallpaper-Vault
All images here are taken from the internet. If you have cool wallpapers to share, feel free to send them!  

If you want any image removed, please contact me at *********  
#
"""

# Alle Unterordner und Bilder durchsuchen
for root, _, files in os.walk(IMAGE_FOLDER):
    relative_path = os.path.relpath(root, IMAGE_FOLDER)
    if relative_path != ".":
        readme_content += f"<details>\n  <summary><b>{relative_path}</b></summary>\n\n"
    
    for filename in sorted(files):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            image_url = f"https://raw.githubusercontent.com/{USERNAME}/{REPO_NAME}/main/{root}/{filename}"
            readme_content += f"  <img src=\"{image_url}\" width=\"300\">\n\n"
    
    if relative_path != ".":
        readme_content += "</details>\n\n"

# README.md speichern
with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(readme_content)

print(f"{README_FILE} wurde erfolgreich erstellt!")
