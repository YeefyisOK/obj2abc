
import alembic as abc
oarch = OArchive('polyMesh1.abc')
meshObj = OPolyMesh(oarch.getTop(), "meshy")
mesh = meshyObj.getSchema()
uvsamp = OV2fGeomParamSample(uvs, kFacevaryingScope)
nsamp  = ON3fGeomParamSample(normals, kFacevaryingScope)
mesh_samp = OPolyMeshSchemaSample(verts, indices, counts, uvsamp, nsamp)
cbox = imath.Box3d()
cbox.extendBy(imath.V3d(1.0, -1.0, 0.0))
cbox.extendBy(imath.V3d(-1.0, 1.0, 3.0))
mesh_samp.setChildBounds(cbox)

mesh.set(mesh_samp);
mesh.set(mesh_samp);

#Read an Alembic archive
iarch = IArchive('polyMesh1.abc')
print "Reading", iarch.getName()

top = iarch.getTop()
top.getName()

meshObj = IPolyMesh(top, "meshy")
mesh = meshObj.getSchema()
N = mesh.getNormalsParam()
uv = mesh.getUVsParam()

obj = top.children[0]
if IPolyMeshSchema.matches(obj):
    meshObj = IPolyMesh(obj, KWrapExisting)

