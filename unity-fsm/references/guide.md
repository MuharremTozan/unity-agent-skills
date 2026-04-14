# Finite State Machine Guide (Adam Myhre Pattern)

This guide explains how to implement the Object-Oriented Finite State Machine as used in Adam Myhre's 3D Platformer project.

## 1. Core Architecture
The machine uses the **State** and **Strategy** patterns. All file templates can be found in `assets/code/`.

- **IState**: Core interface for state logic.
- **StateMachine**: manages a dictionary of `StateNode` objects and handles transitions.
- **IPredicate**: Defines the condition strategy for transitions.

## 2. Setting Up States
Create a base state to share common references like the controller and animator.

```csharp
namespace Platformer {
    public abstract class BaseState : IState {
        protected readonly PlayerController player;
        protected readonly Animator animator;

        protected BaseState(PlayerController player, Animator animator) {
            this.player = player;
            this.animator = animator;
        }

        public virtual void OnEnter() { }
        public virtual void Update() { }
        public virtual void FixedUpdate() { }
        public virtual void OnExit() { }
    }
}
```

## 3. Implementing Transitions
Transitions are added in the `Awake` method of your main controller.

```csharp
void SetupStateMachine() {
    stateMachine = new StateMachine();

    // Initialize States
    var locomotionState = new LocomotionState(this, animator);
    var jumpState = new JumpState(this, animator);

    // Define Transitions
    stateMachine.AddTransition(locomotionState, jumpState, new FuncPredicate(() => jumpTimer.IsRunning));
    stateMachine.AddTransition(jumpState, locomotionState, new FuncPredicate(() => grounded && !jumpTimer.IsRunning));

    // Set Initial State
    stateMachine.SetState(locomotionState);
}
```

## 4. Updates
Ensure you call the machine's update methods in Unity's lifecycle:

## 5. Hybrid Usage (ActionState)
For simple states that don't need a full class, use `ActionState` to reduce boilerplate.

```csharp
void SetupSimpleMachine() {
    var stateMachine = new StateMachine();

    // Create a state on the fly with lambdas
    var idleState = new ActionState(
        onEnter: () => animator.Play("Idle"),
        onUpdate: () => Debug.Log("Idle...")
    );

    // Combine with complex class states
    var complexState = new MyComplexCustomState(this, animator);

    stateMachine.SetState(idleState);
}
```
