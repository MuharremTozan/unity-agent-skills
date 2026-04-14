# Interaction System Guide

## Core Concept
This skill provides a **generic, raycast-based interaction system** that works for any game genre.

## Quick Start

### 1. Setup Interactable Object
```csharp
using Standard.Interaction;

public class Door : MonoBehaviour, IInteractable {
    public void Interact(IInteractor interactor) {
        Debug.Log("Door opened!");
        // Your door logic here
    }

    public void InteractAlternate(IInteractor interactor) {
        Debug.Log("Door locked!");
    }
}
```

### 2. Setup Player/AI
- Add `InteractionController` to your player
- Set `Interactable Layer` to match your objects
- Adjust `Interact Distance`

### 3. Layer Setup
1. Create a new Layer: "Interactable"
2. Assign it to all objects with `IInteractable`
3. Reference it in the controller

## Pro Tips
- **E Key**: Primary interaction
- **F Key**: Alternative interaction
- **Raycast Direction**: Uses `transform.forward` (works with both 2D and 3D)
- **Event Integration**: Add event firing in `SetSelectedTarget()` for UI feedback

## Use Cases
- Doors, chests, NPCs (RPG)
- Crafting stations, cooking (Simulation)
- Pickups, switches (Platformer)
- Any clickable object
