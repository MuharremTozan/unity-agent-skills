# Unity Data Persistence — Reference Guide

Source: [adammyhre/Unity-Inventory-System](https://github.com/adammyhre/Unity-Inventory-System/tree/master/Assets/_Project/Scripts/Persistence)

---

## Mental Model: Data Binding

The key insight from Adam Myhre's system is **"data binding"**: instead of reading/writing at save time, you link a live data object to your MonoBehaviour at load time. From that moment on, the MonoBehaviour writes directly into the same object that will eventually be serialized.

```
SaveLoadSystem.GameData
    └── PlayerData (ISaveable)   ←── Hero.Bind(data) → Hero writes to this directly
    └── InventoryData (ISaveable) ←── Inventory.Bind(data) → Inventory writes to this directly
```

Saving is then trivial: `JsonUtility.ToJson(gameData)` — the data is always current.

---

## Option A: The Pro Path (Full Data Binding)

Use this when you have multiple saveable sub-systems (player, inventory, enemies, etc.).

### Step 1 — Create your data DTOs

```csharp
using Standard.Systems.Persistence;

// One DTO per saveable sub-system
[Serializable]
public class PlayerData : ISaveable {
    [field: SerializeField] public SerializableGuid Id { get; set; }
    public Vector3 position;
    public Quaternion rotation;
}
```

### Step 2 — Add data to GameData

```csharp
[Serializable]
public class GameData {
    public string Name;
    public string CurrentLevelName;
    public PlayerData playerData;       // ← add your DTO here
    public InventoryData inventoryData; // ← and here
}
```

### Step 3 — Implement IBind on your MonoBehaviour

```csharp
using Standard.Systems.Persistence;

public class PlayerEntity : MonoBehaviour, IBind<PlayerData> {
    [SerializeField] SerializableGuid id;
    PlayerData data;

    public SerializableGuid Id {
        get => id;
        set => id = value;
    }

    public void Bind (PlayerData incoming) {
        data = incoming;
        data.Id = id; // stamp the id
        // Restore state from data
        transform.position = data.position;
        transform.rotation = data.rotation;
    }

    void Update () {
        // Write-through: data is always current
        data.position = transform.position;
        data.rotation = transform.rotation;
    }
}
```

### Step 4 — Register bindings in SaveLoadSystem.OnSceneLoaded

In your project's subclass of `SaveLoadSystem`:

```csharp
void OnSceneLoaded (Scene scene, LoadSceneMode mode) {
    if (scene.name == "Menu") return;

    Bind<PlayerEntity, PlayerData>(gameData.playerData);
    // Bind<InventoryMono, InventoryData>(gameData.inventoryData);
}
```

### Step 5 — Call Save/Load

```csharp
// Save current state
SaveLoadSystem.Instance.SaveGame();

// Load a named save
SaveLoadSystem.Instance.LoadGame("MySave");

// New game
SaveLoadSystem.Instance.NewGame("MySave", "Level1");
```

---

## Option B: The Light Path (Simple Key/Value)

Use this when you have a small, flat data structure and no need for per-entity binding.

```csharp
// Define data
[Serializable]
public class GameData {
    public string Name;
    public int score;
    public bool tutorialComplete;
}

// Save
var system = GetComponent<SaveLoadSystem>();
system.gameData.score = 9001;
system.SaveGame();

// Load
system.LoadGame("MySlot");
Debug.Log(system.gameData.score);
```

No `IBind`, no `ISaveable`, no `SerializableGuid` needed.

---

## Swapping the Backend

Because everything is behind `IDataService`, swapping to cloud or encrypted binary is a
one-line change in `SaveLoadSystem.Awake()`:

```csharp
// Local JSON (default)
dataService = new FileDataService(new JsonSerializer());

// Future: Cloud
// dataService = new CloudDataService(new JsonSerializer(), userId);

// Future: Encrypted Binary
// dataService = new FileDataService(new BinarySerializer(encryptionKey));
```

---

## SerializableGuid

Assign in the Inspector to give each persistent entity a stable identity. Alternatives:
- Use `string` GUIDs if `SerializableGuid` feels heavy — watch out for duplicates
- Generate at runtime via `SerializableGuid.NewGuid()` for dynamically spawned entities

---

## Multi-Entity Binding (Lists)

For many enemies, NPCs, or spawn points with individual state:

```csharp
// In GameData:
public List<EnemyData> enemyDatas = new();

// In OnSceneLoaded:
Bind<EnemyMono, EnemyData>(gameData.enemyDatas);
// Each enemy is matched by GUID. Missing entries get fresh data auto-created.
```
