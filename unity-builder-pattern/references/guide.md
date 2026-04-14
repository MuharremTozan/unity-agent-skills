# Builder Pattern Guide

The Builder Pattern separates the construction of a complex object from its representation, allowing the same construction process to create different representations. This skill provides two distinct approaches:

## 1. The "Light" Path: Generic Fluent Builder
Use this for simple GameObject instantiation where you just want a cleaner syntax than `new GameObject() -> AddComponent -> SetPosition -> SetName`.

### How to Use
1.  Inherit from `FluentBuilder<T>` if you need custom logic, or use it directly (if T is a Component).
2.  Call `.Build()` to get your component.

```csharp
// Example Usage
Enemy enemy = new FluentBuilder<Enemy>("Goblin")
    .WithPosition(spawnPoint.position)
    .WithRotation(spawnPoint.rotation)
    .Build();
```

## 2. The "Pro" Path: Interface Validation Builder
Use this when object construction **must** follow a strict sequence (e.g., MUST add weapon before ammo, MUST add health before shield). This pattern uses interfaces to enforce the order at compile time.

### How to Use
1.  Define your interfaces (`IWeaponStep`, `IHealthStep`, `IFinalStep`).
2.  Implement all interfaces in your `Builder` class.
3.  Each method returns the *next interface* in the chain.

```csharp
// Example Usage
Enemy enemy = EnemyBuilder.Create("Boss")
    .WithWeapon(swordData)      // Returns IHealthStep
    .WithHealth(100f)           // Returns IFinalStep
    .Build();                   // Returns Enemy
```

### Benefits
- **Compile-Time Safety**: You cannot call `.Build()` too early. You cannot set Health before Weapon.
- **Readability**: The fluent API reads like natural language.
- **Immutability**: The resulting object is fully configured before being exposed.
