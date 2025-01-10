import os
import shutil
import zipfile
from pathlib import Path
import platform

# Define paths
repo_path = Path.home() / "Documents" / "GitHub" / "Repo-Name"
world_name = "<3rd-life-test-world>"  # Replace with your world name
datapack_zip_name = "3rd-life-rehashed.zip"  # Name for the zip file

# Determine the .minecraft folder location based on the OS
def get_minecraft_datapacks_folder(world_name):
    system = platform.system()
    if system == "Windows":
        minecraft_folder = Path(os.getenv("APPDATA")) / ".minecraft"
    elif system == "Darwin":  # macOS
        minecraft_folder = Path.home() / "Library" / "Application Support" / "minecraft"
    else:
        raise OSError("Unsupported operating system.")
    return minecraft_folder / "saves" / world_name / "datapacks"

# Paths
minecraft_datapacks = get_minecraft_datapacks_folder(world_name)

# Zip the datapack folder
def zip_folder(source_folder, output_file):
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=source_folder)
                zipf.write(file_path, arcname)

# Run the script
try:
    print("Zipping the datapack...")
    output_zip = repo_path / datapack_zip_name
    zip_folder(repo_path, output_zip)

    print("Copying the datapack to Minecraft's datapacks folder...")
    shutil.copy(output_zip, minecraft_datapacks)

    print(f"Datapack successfully updated in: {minecraft_datapacks}")
except Exception as e:
    print(f"An error occurred: {e}")
