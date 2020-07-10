
import alembic as abc
oarch = OArchive('polyMesh1.abc')
meshObj = OPolyMesh(oarch.getTop(), "meshy")
mesh = meshyObj.getSchema()
uvsamp = OV2fGeomParamSample(uvs, kFacevaryingScope)
nsamp  = ON3fGeomParamSample(normals, kFacevaryingScope)
mesh_samp = OPolyMeshSchemaSample(verts, indices, counts, uvsamp, nsamp)


