# Enemy AI State Machine Guide (Adam Myhre Pattern)

This guide covers implementing an AI using the 100% repo-accurate FSM and Detection strategies.

## 1. Core AI Components
- **NavMeshAgent**: Required for AI navigation.
- **PlayerDetector**: Handles detection using `IDetectionStrategy`.
- **Timer (CountdownTimer)**: Critical for handling cooldowns (Detections, Attacks).

## 2. Using the At() Helper
Adam Myhre uses a clean `At()` helper method in the `Enemy` component to wire transitions:

```csharp
void Start() {
    stateMachine = new StateMachine();
    
    // 1. Initialize States
    var wanderState = new EnemyWanderState(this, animator, agent, 10f);
    var chaseState = new EnemyChaseState(this, animator, agent, detector.Player);
    
    // 2. Define Transitions with Helper
    At(wanderState, chaseState, new FuncPredicate(() => detector.CanDetectPlayer()));
    At(chaseState, wanderState, new FuncPredicate(() => !detector.CanDetectPlayer()));

    // 3. Set Initial State
    stateMachine.SetState(wanderState);
}

void At(IState from, IState to, IPredicate condition) => stateMachine.AddTransition(from, to, condition);
```

## 3. The Timer System
The FSM is tightly coupled with `Utilities.Timer`. Always use `Tick(Time.deltaTime)` in your `Update` loops to keep your AI logic heartbeat going.

```csharp
void Update() {
    stateMachine.Update();
    attackTimer.Tick(Time.deltaTime); // Don't forget this!
}
```

## 4. Detection Strategy (Strategy Pattern)
The `PlayerDetector` uses an `IDetectionStrategy`. You can swap `ConeDetectionStrategy` for any other custom implementation.

```csharp
// Example check in a transition predicate
() => detector.CanDetectPlayer() 
```
This returns true if the player is within the cone OR if the `detectionTimer` is still running from a recent detection.
