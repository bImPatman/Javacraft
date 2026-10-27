import os
import subprocess
import minecraft_launcher_lib
from pathlib import Path

with open((Path("Downloads") / "version.txt"), "r") as file:
    mcversion = file.read()

# 1. Define the custom path pointing to your Downloads subdirectory
# Change this path if you are on Linux/macOS (e.g., os.path.expanduser("~/Downloads/your_folder"))
downloads_dir = os.path.expanduser(r"~\Downloads")

# 2. Generate minimal demo/test credentials since rd-132211 doesn't require authentication
options = minecraft_launcher_lib.utils.generate_test_options()

try:
    # 3. Compile the exact java execution command targeting your directory
    launch_command = minecraft_launcher_lib.command.get_minecraft_command(
        version=mcversion,
        minecraft_directory=downloads_dir,
        options=options
    )
    
    # 4. Fire up the game instance
    print("Launching Minecraft rd-132211...")
    subprocess.run(launch_command, cwd=downloads_dir)

except minecraft_launcher_lib.exceptions.VersionNotFound:
    print(f"Error: Version rd-132211 was not found inside: {downloads_dir}")

