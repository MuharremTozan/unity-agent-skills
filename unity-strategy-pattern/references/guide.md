# Strategy Pattern Guide

The Strategy Pattern allows you to encapsulate a family of algorithms (e.g., Attack Logic, Spell Casting) and make them interchangeable.

## 1. The Core Idea
Instead of a giant `if/else` or `switch` statement in your PlayerController based on `SpellType`:
```csharp
if (spell == Fireball) CastFireball();
else if (spell == Shield) CastShield();
```
You delegate the logic to an interface:
```csharp
currentSpellStrategy.CastSpell(transform); 
```

## 2. Choosing Your Path (Hybrid Design)

### A. The "Pro" Path (Complex ScriptableObjects)
Use this for robust gameplay mechanics like Abilities, Spells, or AI Behaviors.
1.  **Define Base Class**: `SpellStrategy : ScriptableObject` with an `Execute(user)` method.
2.  **Create Strategies**:
    -   `FireballStrategy`: Handles projectile math, instantiation, and damage data.
    -   `ShieldStrategy`: Handles parent constraints, duration logic.
    -   `OrbitalStrategy`: Handles complex rotation math (sin/cos positioning).
3.  **Assign**: In the Inspector, drag your Strategy asset into the Player's slot.
4.  **Benefits**:
    -   **SRP**: Each spell logic lives in its own file.
    -   **Reusability**: Different enemies can use the same `FireballStrategy` asset.
    -   **Hot-Swapping**: Change a boss's attack pattern mid-fight by swapping the `.asset` reference.

### B. The "Light" Path (Interface + Delegates)
Use this for simple behavior toggles (e.g., `IMovementStrategy` -> `Run` vs `Walk`).
1.  Define a simple interface `IMove`.
2.  Implement `RunStrategy` and `WalkStrategy` as plain C# classes.
3.  Inject into your controller via Constructor or Method Injection.
