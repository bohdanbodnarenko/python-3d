import pymesh
from os import listdir

MODELS_PATH = 'models/'

operations = ['union', 'intersection']
engines = ['cork']


# TODO check why still "Input mesh is not PWN!" error
def resolve_self_intersection(mesh):
    self_intersection = pymesh.detect_self_intersection(mesh)
    if len(self_intersection):
        print(self_intersection)
        return pymesh.resolve_self_intersection(mesh)
    else:
        return mesh


for operation in operations:
    for engine in engines:
        model_names = listdir(MODELS_PATH)

        mesh1 = resolve_self_intersection(pymesh.load_mesh(MODELS_PATH + model_names.pop()))
        mesh2 = resolve_self_intersection(pymesh.load_mesh(MODELS_PATH + model_names.pop()))

        boolmesh = pymesh.boolean(mesh1, mesh2, operation=operation, engine=engine)

        for model in model_names:
            print(f'Merging with {model}')
            mesh = resolve_self_intersection(pymesh.load_mesh(MODELS_PATH + model))
            boolmesh = pymesh.boolean(boolmesh, mesh, operation=operation)

        fn = f"result-{operation}-{engine}-export.stl"
        pymesh.save_mesh(fn, boolmesh)
