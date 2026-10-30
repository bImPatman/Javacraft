import subprocess
import sys
import os
from pathlib import Path

def run_vineflower(jar_path, input_path, output_dir):
    """
    Runs the Vineflower decompiler on a specified input file or directory.
    
    :param jar_path: Path to the vineflower.jar file
    :param input_path: Path to the .class, .jar, or directory to decompile
    :param output_dir: Directory where decompiled .java files should be saved
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Build the command: java -jar vineflower.jar <input> <output>
    command = [
        "java", 
        "-jar", jar_path,
        input_path,
        output_dir
    ]
    
    try:
        # Execute the command and capture output
        result = subprocess.run(
            command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True, 
            check=True
        )
        print("Decompilation completed successfully!")
        return result.stdout
        
    except subprocess.CalledProcessError as e:
        print(f"Error during decompilation (Exit Code {e.returncode}):", file=sys.stderr)
        print(e.stderr, file=sys.stderr)
        return None

print("Getting paths...")
with open((Path("Downloads") / "version.txt")) as file:
    version = file.read()
print("Using " + version + "...")
libraries = []
for file in (Path("Downloads") / "libraries").rglob("*"):
    if file.is_file():
        libraries.append(file)
Path("src/main").mkdir(parents=True, exist_ok=True)
print("Decompiling Minecraft...")
run_vineflower(".\\Downloads\\vineflower.jar", ("Downloads\\versions\\" + version + "\\" + version + ".jar"), ".\\src\\main\\java\\")
print("Decompiling libraries")
for i in libraries:
    path = str(".".join(str(i).split("\\")[-1].split(".")[:-1]))
    (Path("src") / path).mkdir(parents=True, exist_ok=True)
    run_vineflower(".\\Downloads\\vineflower.jar", str(i), ".\\src\\" + path)
    print("Done Decompiling " + path)
