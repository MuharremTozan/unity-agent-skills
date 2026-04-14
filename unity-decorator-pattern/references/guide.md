# Decorator Pattern Guide

The Decorator Pattern allows you to add responsibilities to individual objects dynamically, without affecting other objects. In Unity, this is often used for Buffs/Debuffs or Weapon Upgrades (e.g., Fire Damage + Ice Damage + Sword Base).

## 1. The Core Idea: Wrapping
Instead of subclassing `FireSword`, `IceSword`, `FireIceSword`, you wrap the base object:
```csharp
IStatProvider damage = new SwordBase(10f); // Base: 10
damage = new FireDamage(damage);           // Adds +5 => 15
damage = new PercentageBuff(damage, 0.2f); // Adds 20% => 18
```
The client code just calls `damage.GetValue()` and doesn't care how many layers deep the wrapping goes.

## 2. Choosing Your Path (Hybrid Design)

### A. The "Pro" Path (ScriptableObject Decorators - Card Game Style)
Use this for robust data-driven RPG stats or Card Games.
1.  Define a `CardDefinition` SO.
2.  Define a `CardDecorator` SO that holds a reference to another `CardDefinition` at runtime (or uses a `Decorate(Card c)` method).
3.  **Example**: Implementing a Card Game where playing a "Fire" card onto a "Dragon" card boosts its attack.
    -   The `CardDecorator` class wraps the `Card` instance.
    -   Calls to `Play()` on the decorator execute effects *and then* call `Play()` on the wrapped card.

### B. The "Light" Path (Runtime Stat Modifiers - RPG Style)
Use this for simple math modifiers (Powerups, Potions).
1.  **Interface**: Create `IStatProvider` with `GetValue()`.
2.  **Base**: `StatBase` holds the initial float.
3.  **Decorators**: `StatModifier` classes take an `IStatProvider` in the constructor.
4.  **Usage**:
    ```csharp
    var health = new StatBase(100f);
    health = new FlatModifier(health, 50f); // +50 Potion
    Debug.Log(health.GetValue()); // 150
    ```
