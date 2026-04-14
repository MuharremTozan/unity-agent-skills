# YAML Templates (Unity 6)

When performing **Bulk Generation**, use these templates to ensure Unity can parse the files upon refresh.

## 1. ScriptableObject (.asset)
**Note:** The `m_Script` GUID must match the `.meta` file of your C# SO class.

```yaml
%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!114 &11400000
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 0}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {fileID: 11500000, guid: [SCRIPT_GUID], type: 3}
  m_Name: [ASSET_NAME]
  m_EditorClassIdentifier: 
  # Custom Properties Start Here
  maxHealth: 100
  baseSpeed: 5
```

## 2. Guid Locating
Before generating, always find the Script GUID:
1. Locate `Assets/Scripts/Data/YourClassSO.cs.meta`.
2. Extract the `guid` string.
3. Replace `[SCRIPT_GUID]` in the template above.

## 3. The Refresh Ritual
After writing files, you **MUST** call:
`mcp_unityMCP_refresh_unity(scope="assets", wait_for_ready=true)`
Unity will then:
- Assign a new GUID to the `.asset`.
- Generate the `.meta` file.
- Register the asset in the AssetDatabase.
