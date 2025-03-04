import os

# Einstellungen
REPO_NAME = os.getenv("GITHUB_REPOSITORY", "dein-repository").split("/")[-1]
USERNAME = "T4tze"  
IMAGE_FOLDER = "Wallpaper"
README_FILE = "README.md"

# Header für README
readme_content = """# Meine Wallpapers

Hier findest du eine Sammlung meiner Wallpaper. Vorschau unten:

"""

# Bilder auflisten
if os.path.exists(IMAGE_FOLDER):
    for filename in sorted(os.listdir(IMAGE_FOLDER)):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            image_url = f"https://raw.githubusercontent.com/{USERNAME}/{REPO_NAME}/main/{IMAGE_FOLDER}/{filename}"
            readme_content += f"![{filename}]({image_url})\n\n"
else:
    print(f"Ordner '{IMAGE_FOLDER}' nicht gefunden!")

# README.md speichern
with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(readme_content)

print(f"{README_FILE} wurde aktualisiert!")
