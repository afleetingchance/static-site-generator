import os
import sys
import shutil

def main():
    if not os.path.exists('./static'):
        print("Error: static directory is required")
        sys.exit(1)
    if not os.path.exists('./public/'):
        os.system('mkdir public')
    
    os.system('rm -rf ./public/*')

    copy_files(os.listdir('./static'), './static', './public')
    
def copy_files(paths, working_dir, dest_dir):
    for path in paths:
        full_path = os.path.join(working_dir, path)
        if os.path.isfile(full_path):
            print(f'Copying... {full_path}')
            shutil.copy(full_path, dest_dir)
        else:
            full_dest_path = os.path.join(dest_dir, path)
            print(f'Going into... {full_path}')
            copy_files(os.listdir(full_path), full_dest_path)

if __name__ == '__main__':
    main()