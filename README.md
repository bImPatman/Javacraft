Disclaimer: This repository does not contain any copyrighted material, including Minecraft.
# Minecraft-Transpiler
This is a custom Minecraft to JS/WASM transpiler made with teavm.

Now, you may be thinking that this is just any other transpiler setup, such as eaglercraft.

Instead of rewriting all of the libraries that Minecraft depends on, this project instead focuses on reimplementing that natives.

The reason being that replicating the execution of the target library is difficult and complex.
Replicating a native changes the approach derastically, and might make this project a lot for feasable.

Even though this project is focused on creating web-based natives, it includes the functionality to re-create the libraries (bridges), natives (shims), and lets you patch everything from Minecraft to the libraries.

Directory structure:
```
Javacraft/
├── Documentation/ (Contains documentation)
├── Run/ (Created when testing a patched jar)
├── Out/ (Where all output files are stored)
│   ├── Java/
│   └── Web/
│       ├── Javascript/
│       └── WASMGC/
├── Tools/
│   └── Fetch.py (Fetches Minecraft and libraries)
├── Patches/
├── Shims/
├── Bridges/
├── src/
├── Downloads/
├── build.gradle
├── LICENSE
└── README.md
```