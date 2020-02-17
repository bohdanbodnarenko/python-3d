import pymesh


def make_stl_from_obj(filename: str) -> str:
    def resolve_self_intersection(mesh):
        self_intersection = pymesh.detect_self_intersection(mesh)
        if len(self_intersection):
            print(self_intersection)
            return pymesh.resolve_self_intersection(mesh)
        else:
            return mesh

    mesh = resolve_self_intersection(pymesh.load_mesh(filename))
    fn = filename.replace('.obj', '.stl')
    pymesh.save_mesh(fn, mesh)
    return fn


if __name__ == '__main__':
    make_stl_from_obj('something.obj')
