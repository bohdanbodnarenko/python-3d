import os

import maya.cmds as cmds
from dotenv import load_dotenv

from utils.download_files_from_s3 import download_files_from_s3
from utils.make_stl_from_obj import make_stl_from_obj

load_dotenv()


def import_to_maya_and_export(files_dir_path):
    files = cmds.getFileList(folder=files_dir_path)

    if not files or len(files) == 0:
        cmds.warning('No files found in directory ', files_dir_path)
        return

    files_dir_path = files_dir_path if files_dir_path.endswith('/') else files_dir_path + '/'

    for f in files:
        cmds.file(files_dir_path + f, i=True)

    cmds.select(all=True)
    export_filename = "c:/something.obj"
    cmds.file(export_filename, exportSelected=True, type="OBJ", force=True, es=1,
              op="groups=0; ptgroups=0; materials=0; smoothing=0; normals=0")

    return export_filename


def main():
    cwd = os.getcwd()

    downloaded_files = download_files_from_s3(['Male_Height_02_Rig.fbx'],
                                              'Male/Height_02/', 'fbx',
                                              os.path.join(cwd, 'fbxs'))
    maya_file = import_to_maya_and_export(downloaded_files)
    make_stl_from_obj(maya_file)


if __name__ == '__main__':
    main()
