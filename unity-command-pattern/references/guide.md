# Command Pattern Guide

The Command Pattern encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

## 1. The Core Architecture
- **Command**: An object wrapping a method.
- **Invoker**: The object that calls `Execute()` (and manages queuing/history).
- **Receiver**: The object that the command acts upon (e.g., Player).

## 2. Choosing Your Path (Hybrid Design)

### A. The "Pro" Path (Async Combo System)
Use this for systems where order and timing matter (Combos, Spells, Turn-Based Actions).
1. **Interfaces**: Commands implement `ICommand` which returns a `Task`.
2. **Invoker**: Use `CommandInvoker` to `await` each command. This ensures an "Attack" finishes its animation before a "Jump" begins.
3. **Parameterization**: Pass the target/parameters in the constructor of the Command object.

### B. The "Light" Path (ScriptableObject Actions)
Use this for simple, data-driven interactions like UI buttons or context-menu actions.
1. **Template**: Create a `CommandSO` asset.
2. **Execution**: Pass the target `GameObject` as a parameter to the `Execute(target)` method.
3. **Usage**: Drag the asset into a UnityEvent field (like `Button.onClick`).

## 3. Advanced Usage: Undo/Redo
To support Undo, keep a `Stack<ICommand>` in your Invoker. Each command must implement an `Undo()` method that reverses the action performed in `Execute()`.
