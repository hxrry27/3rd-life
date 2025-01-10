import os
import shutil
import zipfile
from pathlib import Path

# Define paths
repo_path = Path.home() / "Documents" / "GitHub" / "3rd-Life"  # Relevant Repo
world_name = "3rd-life-test-world"  # Replace with world name
prism_launcher_instance = Path(os.getenv("APPDATA")) / "PrismLauncher" / "instances" / "1.21.4 CubicOasis" / ".minecraft"
minecraft_datapacks = prism_launcher_instance / "saves" / world_name / "datapacks"
version_file = repo_path / "version.txt"  # File to track versioning

# Function to zip only the desired files
def zip_datapack(source_folder, output_file):
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for item in source_folder.iterdir():
            if item.name == "data" and item.is_dir():
                # Add all contents of the `data` folder
                for root, dirs, files in os.walk(item):
                    for file in files:
                        file_path = Path(root) / file
                        arcname = file_path.relative_to(source_folder)
                        zipf.write(file_path, arcname)
            elif item.name in {"pack.mcmeta", "README.md"}:
                # Add `pack.mcmeta` and `README.md`
                zipf.write(item, arcname=item.relative_to(source_folder))

# Function to increment version based on type
def increment_version(version, update_type):
    major, minor, patch = map(int, version.split("."))
    if update_type == "major":
        major += 1
        minor = 0
        patch = 0
    elif update_type == "minor":
        minor += 1
        patch = 0
    elif update_type == "patch":
        patch += 1
    return f"{major}.{minor}.{patch}"

# Function to get the current version
def get_current_version():
    if version_file.exists():
        with open(version_file, "r") as vf:
            return vf.read().strip()
    return "1.0.0"  # Default starting version

# Function to save the new version
def save_version(version):
    with open(version_file, "w") as vf:
        vf.write(version)

# Main script
try:
    print("Fetching current version...")
    current_version = get_current_version()
    print(f"Current version: {current_version}")

    # Ask the user for the update type
    update_type = input("Enter update type (major, minor, patch): ").strip().lower()
    while update_type not in ["major", "minor", "patch"]:
        print("Invalid input. Please enter 'major', 'minor', or 'patch'.")
        update_type = input("Enter update type (major, minor, patch): ").strip().lower()

    new_version = increment_version(current_version, update_type)
    print(f"Updating version to: {new_version}")

    # Ask the user for the datapack name
    datapack_name = input("Enter the name of the datapack: ").strip()
    while not datapack_name:
        print("Datapack name cannot be empty. Please enter a valid name.")
        datapack_name = input("Enter the name of the datapack: ").strip()

    print("Zipping the datapack...")
    output_zip = repo_path / f"{datapack_name}-v{new_version}.zip"
    zip_datapack(repo_path, output_zip)

    print(f"Datapack zipped at: {output_zip}")

    print("Copying the datapack to Minecraft's datapacks folder...")
    minecraft_datapacks.mkdir(parents=True, exist_ok=True)  # Ensure the folder exists
    shutil.copy(output_zip, minecraft_datapacks / output_zip.name)

    print(f"Saving new version: {new_version}")
    save_version(new_version)

    print(f"Datapack '{datapack_name}' successfully updated to version {new_version} in: {minecraft_datapacks}")
except Exception as e:
    print(f"An error occurred: {e}")