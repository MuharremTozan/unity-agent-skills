# Observer Pattern (Reactive Properties) Guide

The Observer pattern is used to decouple the "Subject" (data producer) from the "Observers" (data consumers/UI). This implementation uses **Reactive Properties** to automate notifications.

## Core Concepts
1. **Observable<T>**: A wrapper class for a variable that triggers events when its value changes.
2. **UnityEvent Integration**: Allows designers to link behavior (like UI updates) directly in the Inspector via drag-and-drop.
3. **Implicit Conversion**: Simplifies syntax so you can treat an `Observable<int>` almost like a regular `int`.

## How to use

### Static/Traditional Events
For global system messages, continue using `unity-event-bus`.

### Reactive Data (The Pro Path)
Use `Observable<T>` for properties that need visual representation or tool-driven behavior.

```csharp
public Observable<float> Speed = new(5.0f);

// Change value (triggers event automatically)
Speed.Value = 10.0f;

// Syntax sugar (Implicit cast)
float currentSpeed = Speed; 
```

## Editor Tooling
This skill includes `ObservableEditorTools` for building custom inspectors that can "wire up" events programmatically in Edit Mode.

```csharp
#if UNITY_EDITOR
ObservableEditorTools.AddPersistentListener(myEvent, MyMethod);
#endif
```
