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

    print("Downloading Minecraft " + str(version))

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
    with requests.get(url, stream=True) as response:
        response.raise_for_status() # Raise error for bad status codes
        with open(output_path, "wb") as file:
            # Download the file in chunks of 8192 bytes
            for chunk in response.iter_content(chunk_size=8192): 
                if chunk:
                    file.write(chunk)

    print("Download Complete!")

if style == "url":
    input("I don't know the libraries to download. Get them yourself and put them in the /Downloads/libs folder.")
else:
    print("Downloading Libraries!")
    downloaded = 0
    for lib in mcjson["libraries"]:
        liburl = lib["downloads"]["artifact"]["url"]

        output_path = Path("Downloads") / "libs"
        output_path.mkdir(parents=True, exist_ok=True)
        output_path = output_path / (str(lib["downloads"]["artifact"]["url"].split("/")[-1]) + ".jar")

        if output_path.is_file():
            print("Library " + (str(lib["downloads"]["artifact"]["url"].split("/")[-1]) + " is already downloaded. Skipping."))
            continue

        with requests.get(liburl, stream=True) as response:
            response.raise_for_status() # Raise error for bad status codes
            with open(output_path, "wb") as file:
                # Download the file in chunks of 8192 bytes
                for chunk in response.iter_content(chunk_size=8192): 
                    if chunk:
                        file.write(chunk)
        downloaded += 1
        print(str(lib["downloads"]["artifact"]["url"].split("/")[-1]) + " downloaded (" + str(downloaded) + "/" + str(len(mcjson["libraries"])) + ")")

print("Done! Now run\n\npython Tools/Decompile.py")