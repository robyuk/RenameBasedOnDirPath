from pathlib import Path

root_dir=Path('files')
file_paths=root_dir.glob("*/*/*")

for path in file_paths:
  if path.is_file():
    print(path)
    parent_folder=path.parts[-2]
    grandparent_folder=path.parts[-3]
    print(grandparent_folder,parent_folder)
    new_filename=grandparent_folder + '-' + parent_folder + '-' + path.name
    print(new_filename)
    new_filepath=path.with_name(new_filename)
    path.rename(new_filepath)