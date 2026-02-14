# Naming & Directory Conventions

To keep the Agent (AI) efficiently mapping between Data and Visuals, we follow a path-matching convention.

## Folder Structure
```text
Assets/
  Data/
    Robots/         <- .asset files (RobotSO)
    Skills/         <- .asset files (SkillSO)
  Prefabs/
    Robots/         <- .prefab files (Robot Mono)
    VFX/            <- .prefab files (Visual Effects)
  Scripts/
    Data/           <- SO Class definitions
    Logic/          <- MonoBehaviour implementations
```

## Naming Rules
1. **The Twin Rule**: A Prefab and its corresponding SO Asset should share the exact same name where possible.
   - Example: `Scout.prefab` + `Scout.asset`
2. **Suffix for Scripts**:
   - `ClassNameSO.cs` for the ScriptableObject definition.
   - `ClassName.cs` for the MonoBehaviour.
3. **Breadcrumbs**:
   - Every Log should include the SO name found in `data.name` for traceability.

## Tooling Integration
As an Agent, when searching for the "Visuals" of a data object:
1. Get the name of the `.asset` file.
2. Search in `Assets/Prefabs/` for a `.prefab` with the same name.
3. If not found, check the `m_Script` of the prefab for the linking `[SerializeField]`.
