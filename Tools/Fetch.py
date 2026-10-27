import readchar
import requests
from pathlib import Path

versiondatabase = {}
version = ""

def analysemetadata():
    global versiondatabase
    global clientlist
    for version in versiondatabase["versions"]:
        clientlist.append(version["id"])

clientlist = []
versiondatabase = requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json").json()
analysemetadata()

def search(term, array):
    out = []
    for item in array:
        if term in item:
            out.append(item)
    out.reverse()
    return out

while True:
    style = input("How do you want to get Minecraft?\nYou can paste a download url here, or you can just specifiy the Minecraft version\n(URL, Version) ").lower()
    if "version" in style or "url" in style:
        break

if style == "url":
    url = input("Please specify your url.\n")
else:
    buffer = []
    print("\n" * 75)
    print("🔍 ")
    while True:
        key = readchar.readkey()

        if key in (readchar.key.ENTER, '\r', '\n') and current_text in clientlist:
            version = current_text
            break

        elif key in (readchar.key.BACKSPACE, '\x7f', '\x08'):
            if len(buffer) > 0:
                buffer.pop()

        elif len(key) == 1 and key.isprintable():
            buffer.append(key)

        current_text = "".join(buffer)
        print("\n" * 75)
        print(str("\n".join(search(current_text, clientlist))))
        print("🔍 " + str(current_text))

    for i in versiondatabase["versions"]:
        if i["id"] == version:
            url = i["url"]

    mcjson = requests.get(url).json()
    url = mcjson["downloads"]["client"]["url"]

output_path = Path("Downloads")
output_path.mkdir(parents=True, exist_ok=True)
output_path = output_path / (version + ".jar")

if output_path.is_file():
    print("Minecraft " + str(version) + " is already downloaded. Skipping.")
else:
    import os
    import minecraft_launcher_lib

    # Define your target subdirectory
    TARGET_SUBDIR = os.path.join(os.getcwd(), "Downloads")
    VERSION_ID = version

    print(f"Downloading version, libraries, and assets into: {TARGET_SUBDIR}...")

    # 1. Download the version client jar and all associated libraries
    minecraft_launcher_lib.install.install_minecraft_version(
        version=VERSION_ID,
        minecraft_directory=TARGET_SUBDIR
    )

    # 2. Extract the native libraries required by the version into a 'natives' folder
    natives_directory = os.path.join(TARGET_SUBDIR, "versions", VERSION_ID, "natives")
    print(f"Extracting native binaries into: {natives_directory}...")

    minecraft_launcher_lib.natives.extract_natives(
        version=VERSION_ID,
        minecraft_directory=TARGET_SUBDIR,
        extract_path=natives_directory
    )

    print("Download complete!")

print("Done! Now run\n\npython Tools/Decompile.py")