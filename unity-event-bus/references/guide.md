# Advanced Event Bus Guide

The Advanced Event Bus is a global, type-safe messaging system for Unity. Unlike Event Channels (which use ScriptableObjects), the Event Bus uses **static generic indices** and **Reflection** to decouple components without any Inspector setup.

## 1. When to Use
- **System-to-System Communication**: High-frequency messaging between core managers.
- **Zero-Setup Architectures**: When you want to add events without creating `.asset` files.
- **Data-Heavy Events**: Sending complex structs through the system with zero garbage collection.

## 2. Core Concepts
- **IEvent**: The message (must be a `struct` or `class`).
- **EventBus<T>**: The static hub for a specific event type.
- **EventBinding<T>**: The connection between your code and the bus.

## 3. How to Implement

### Step 1: Define an Event
```csharp
public struct HealthChangedEvent : IEvent {
    public float CurrentHealth;
}
```

### Step 2: Create and Register a Binding
Inside your MonoBehaviour's `OnEnable`:
```csharp
private EventBinding<HealthChangedEvent> _healthBinding;

void OnEnable() {
    _healthBinding = new EventBinding<HealthChangedEvent>(e => Debug.Log(e.CurrentHealth));
    EventBus<HealthChangedEvent>.Register(_healthBinding);
}
```

### Step 3: Raise the Event
```csharp
EventBus<HealthChangedEvent>.Raise(new HealthChangedEvent { CurrentHealth = 50f });
```

## 4. Performance & Cleanup
- **Structs**: Use `struct` for events to avoid Heap allocations (GC-friendly).
- **Auto-Cleanup**: The `EventBusBootstrapper` automatically clears all static references when you exit Play Mode in the Editor, preventing memory leaks in the Unity Editor.
