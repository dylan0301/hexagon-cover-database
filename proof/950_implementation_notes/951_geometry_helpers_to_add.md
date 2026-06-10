# Geometry Helpers To Add

Status: Implementation note

Suggested TypeScript types:

```ts
type CEType = "CE0" | "CE1" | "CE2" | "CEDegenerate";

type CVertexConeType = "CType1" | "CType2" | "CTypeDegenerate";
```

Suggested helpers:

```ts
getTrianglePerimeterEdgeOverlaps(...)
classifyCEType(...)
getCVertexConeType(...)
getCoveredMidpoints(...)
isNondegenerateInterval(...)
```

These are specifications only; this folder creates markdown files, not source files.
