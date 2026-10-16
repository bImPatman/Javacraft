This project will be devided into their own seperate modules, in order to keep the project neat, and easy to read, debug, and improve on.

```
Minecraft Port
├── TeaVm (Transpiler)
│   ├── Bridges (Things like Vulkan-to-WebGPU) ─────────────┐
|   ├── Patches (Patches Minecraft/library code if needed) ─┼─ MC code and Libraries
│   └── Shims (Things like making time/date work) ──────────┘
├── Fetcher (Fetches files)
│   ├── Minecraft Code Fetcher
│   └── Library Fetcher
└── Runner (Baseline test of the compiled client before transpilation)
    ├── Runner
    └── Compiler
        └── Patches
```

(Work-in-progress)