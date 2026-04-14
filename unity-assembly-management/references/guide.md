# Unity Assembly Management Guide

This skill manages project boundaries using Unity Assembly Definitions (`.asmdef`). It ensures faster compile times and forces architectural stability.

## Core Concepts

### 1. Responsibility over Script Type
Don't organize by folder name (e.g., `Scripts/Managers`). Organize by domain and stability:
- **Core**: Shared interfaces, stable utilities, math (Bottom of the graph).
- **Systems**: Implementation of mechanics (Middle).
- **UI**: Visual layers (Top).
- **Editor**: Tooling and Inspector code (Outside runtime).

### 2. Dependency Flow
Dependencies must flow **inward** toward stable code.
- Runtime assemblies must **NEVER** depend on Editor assemblies.
- Circular dependencies are a design smell and will cause compiler errors.

---

## Option A: The Pro Path (Stable & Scalable)
Use this for large projects or shared libraries.

- **Explicit GUIDs**: Use GUIDs instead of names for references. This prevents breaking when files are renamed.
- **Override References**: Set `Override References` to `true` to explicitly list every DLL dependency, preventing "Assembly Drift."
- **Version Defines**: Use `versionDefines` for cross-package compatibility (e.g., only enable URP code if the URP package is present).
- **No Engine References**: If a utility assembly doesn't need `UnityEngine`, toggle this to significantly speed up its compilation.

## Option B: The Light Path (Fast Iteration)
Use this for early prototypes or small modules.

- **Auto-Referenced**: Keep `Auto-Referenced` enabled so the default `Assembly-CSharp` can see it without extra setup.
- **Standard Names**: Simple naming conventions (`Project.Module`).
- **Standard Folder Split**: Just a single `.asmdef` at the root of a feature folder.

---

## Best Practices
- **Non-Transitive**: Remember that references are not transitive. If A depends on B and B depends on C, A does **not** see C automatically. This is for your protection.
- **Editor Folders**: Once an Assembly Definition is in a parent folder, sub-folders named `Editor` are no longer special. You must create a separate `.asmdef` for them and mark it as "Editor" platform only.
