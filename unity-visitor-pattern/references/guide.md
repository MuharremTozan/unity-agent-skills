# Visitor Pattern Guide

The Visitor pattern allows you to add new operations to existing components without modifying their classes. It solves the problem of "logic leakage" where stats and powerup logic clutter your core components.

## Core Concepts
1. **IVisitable**: The component being affected (e.g., PlayerHealth).
2. **IVisitor**: The logic provider (e.g., HealthPowerUp).
3. **Double Dispatch**: The magic flow where the context decides the behavior:
   - Player calls `Accept(visitor)`
   - Component calls `visitor.Visit(this)`

## How to Implement

### Step 1: Define Your Components
Inherit from `VisitableComponent` for any object that should be affected by visitors (Health, Inventory, Mana).

### Step 2: Define Your Visitors
Create a logic class (or ScriptableObject) that implements `IVisitor`. 

### Step 3: Trigger the Interaction
Use the `VisitorTrigger` component or a custom call to `visitable.Accept(yourVisitor)`.

## Pro vs Light Path
- **Pro Path**: Use ScriptableObjects for visitors (`ScriptableVisitor`). This allows designers to create 50 different powerups in the Inspector without touching code.
- **Light Path**: Implement `IVisitor` directly on a simple class or a temporary object for one-off logic.
