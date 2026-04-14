# Memento Pattern Guide

The Memento pattern captures and restores an object's internal state without violating encapsulation. In game development, it is primarily used for **Undo/Redo systems**, **Quick-Save/Load**, and **Loadout Presets**.

## Core Components
1. **Originator**: The object that has state you want to save (e.g., Player, Hotbar). It implements `IOriginator<T>`.
2. **Memento**: The data structure (struct) that holds the snapshot.
3. **Caretaker**: The object that keeps track of the history (`StateCaretaker<T>`).

## How to Implement

### Step 1: Define the State Struct
Identify the critical variables that need to be saved.
```csharp
public struct MyState {
    public int Level;
    public string CurrentZone;
}
```

### Step 2: Implement IOriginator
On your target MonoBehaviour, implement the `CreateMemento` and `Restore` methods.

### Step 3: Manage History
Use the `StateCaretaker` to provide Undo/Redo functionality or to store multiple loadouts.

## Why Memento?
- **Decoupling**: The Caretaker doesn't need to know *what* is inside the memento, only that it can store and return it.
- **Simplicity**: No need to write complex "Reverse logic" for every command. Just go back to the previous snapshot.
