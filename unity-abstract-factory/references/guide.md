# Abstract Factory Pattern Guide

This skill implements the Abstract Factory pattern to help you manage the complexity of creating objects, especially families of related objects (like a Knight's full equipment set: Sword + Shield + Armor).

## 1. The Core Idea: Decoupling Creation
Instead of `new Sword()` inside your `Knight` class, you ask a Factory: `factory.CreateWeapon()`. Use `ScriptableObject` factories to make this drag-and-drop in the Unity Inspector.

## 2. Choosing Your Path (Hybrid Design)

### A. The "Pro" Path (Abstract Factory with ScriptableObjects)
Use this when you have interchangeable "themes" or "loadouts".
**Example**: An RPG with `FireMage`, `IceMage`, `Necromancer`. Each needs a distinct Staff, Spell, and Robe.
1.  **Define Interfaces**: `IWeapon`, `IShield`.
2.  **Create Concrete Factories**: `FireWeaponFactory : AbstractFactory<IWeapon>`, `IceWeaponFactory : AbstractFactory<IWeapon>`.
3.  **Use Composition**: Create an `EquipmentFactory` SO that references a `WeaponFactory` and a `ShieldFactory`.
4.  **Drag-and-Drop**: Now you can create a `FireMageKit` asset and assign the fire factories. Your `PlayerSpawner` just needs a reference to `EquipmentFactory`.

### B. The "Light" Path (Simple Prefab Factory)
Use this for simple spawning (bullets, enemies, loot).
1.  Use `SimplePrefabFactory<T>`.
2.  Pass it an array of prefabs in the constructor.
3.  Call `.Create()` to get an instance.

## 3. Benefits
- **Hot-Swapping**: Change an enemy's entire behavior/look by swapping one SO asset in the Inspector.
- **Open/Closed Principle**: Add new weapons (LaserGun) without changing the Player code. Just make a new Factory.
