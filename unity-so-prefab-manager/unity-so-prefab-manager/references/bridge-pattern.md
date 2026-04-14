# The SO-to-Mono Bridge Pattern

## Problem: The "Shared Soul" Bug
In Unity, ScriptableObjects are **assets**. If you have two Robots referencing the same `RobotSO` and you subtract health directly from the SO (e.g., `data.health -= 10`), **both robots will lose health simultaneously**.

## Solution: Local State Shadowing
We shadow the SO's data with local variables on the MonoBehaviour.

### Implementation Checklist
1. **Never** write to an SO at runtime unless you explicitly want to save data across sessions (e.g., Options, Global Progress).
2. **Private Fields, Public Properties**: The SO provides the base values.
3. **Initialization Loop**:
   - `MonoBehaviour.Awake()` runs.
   - It reads `SO.Value`.
   - It sets `localValue = SO.Value`.
   - All gameplay logic (Damage, Healing) modifies `localValue`.

### Example: Damage Calculation
```csharp
public void TakeDamage(float amount) {
    // Modify the local state, NOT the SO
    currentHealth -= amount;
    
    // Use SO for static calculations if needed
    float defenseRatio = data.Armor / 100f; 
    
    if (currentHealth <= 0) Die();
}
```

## Troubleshooting
- **Values not updating in Editor?** Remember that local variables are not visible in the Inspector unless marked `[SerializeField]`.
- **NullReferenceException?** Ensure the SO reference is assigned in the Prefab's Inspector.
- **Data mismatch?** If you change the SO while the game is running, the local instances will NOT update automatically unless you implement a `Reset()` or `OnValidate()` listener.
