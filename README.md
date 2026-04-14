# Unity Agent Skills 🤖🎮

A collection of high-performance skills designed to extend the capabilities of AI coding agents (like Claude, Cursor, and Windsurf) for professional Unity 6 development.

### What's Inside?
This repository is packed with architectural patterns, specific game systems, and best practices tailored to modern game development in Unity. 

**Patterns & Architectures:**
- **unity-abstract-factory**: Factory pattern for creating families of related objects (ScriptableObject + Prefab instantiation).
- **unity-builder-pattern**: Fluent interfaces for complex GameObject object construction.
- **unity-command-pattern**: Encapsulate actions for queuing, undo/redo, and async execution.
- **unity-composition-pattern**: Implements composition over inheritance using SOs and Tuples.
- **unity-decorator-pattern**: Dynamically modify object behavior (e.g. buffs/debuffs).
- **unity-dependency-injection**: Decouples logic with attributes and reflection (DI approach).
- **unity-memento-pattern**: State capturing for save/load or undo/redo.
- **unity-mvc-pattern**: Model-View-Controller and MVP in Unity.
- **unity-observer-pattern**: Reactive properties using UnityEvents.
- **unity-singleton-pattern**: Safe singleton lifecycle control.
- **unity-so-prefab-manager**: Enforces the "SO-to-Mono" Bridge Pattern between ScriptableObjects and Prefabs to prevent data-sharing bugs.
- **unity-strategy-pattern**: Interchangeable algorithms (hot-swap behaviors without modifying client code).
- **unity-visitor-pattern**: Decoupled operations on object structures (ideal for complex PowerUps).

**Systems & Workflows:**
- **unity-assembly-management**: Manages project boundaries via Assembly Definitions (`.asmdef`) for faster compile times.
- **unity-code-reviewer**: Professional Unity C# Code Reviewer that detects anti-patterns and performance leaks.
- **unity-data-persistence**: Robust Save/Load system utilizing Data Binding and DTOs.
- **unity-ecs-patterns**: Unity ECS data-oriented patterns utilizing DOTS, Jobs, and Burst.
- **unity-event-bus**: Code-driven, reflection-based generic global messaging framework.
- **unity-fsm**: Robust Finite State Machine utilizing the State and Strategy patterns.
- **unity-interaction**: Generic raycast-based interaction framework.
- **unity-ui-data-binding**: Implementation of MVVM-style UI Toolkit data binding.
- **unity-ui-procedural**: Advanced UI construction using C# code instead of UI Builder.

**Planning & Orchestration:**
- **planner**: High-fidelity universal orchestrator to guide agents from vague requests to dependency-aware task execution.

*(To view specific implementation guides and code examples, explore the individual skill directories!)*

### Usage
Install skills directly into your project using the Agent Skills CLI:
```bash
npx skills add MuharremTozan/unity-agent-skills/<skill-name>
```
