import os
import re
import sys
import shutil

from block_helpers import markdown_to_html_node

def main():
    if not os.path.exists('./static'):
        print("Error: static directory is required")
        sys.exit(1)
    if not os.path.exists('./docs/'):
        os.system('mkdir docs')

    basepath = sys.argv[1] if len(sys.argv) > 1 else '/'
    print(basepath)
    
    os.system('rm -rf ./docs/*')

    copy_files(os.listdir('./static'), './static', './docs')
    generate_pages_recursive('./content', 'template.html', './docs', basepath)

    
def copy_files(paths, working_dir, dest_dir):
    for path in paths:
        full_path = os.path.join(working_dir, path)
        if os.path.isfile(full_path):
            print(f'Copying... {full_path} to {dest_dir}')
            shutil.copy(full_path, dest_dir)
        else:
            full_dest_path = os.path.join(dest_dir, path)
            os.system(f'mkdir {full_dest_path}')
            print(f'Going into... {full_path}')
            copy_files(os.listdir(full_path), full_path ,full_dest_path)

def extract_title(markdown_text):
    match = re.match(r'\# (.*?)\n', markdown_text)
    if match:
        return match.group(1)
    
    raise Exception('No title found')

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    paths = os.listdir(dir_path_content)

    for path in paths:
        full_path = os.path.join(dir_path_content, path)
        full_dest_path = os.path.join(dest_dir_path, path)

        if os.path.isfile(full_path):
            dest_filename, _ = os.path.splitext(full_dest_path)
            generate_page(full_path, template_path, f'{dest_filename}.html', basepath)
        else:
            generate_pages_recursive(full_path, template_path, full_dest_path, basepath)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    
    with open(from_path, 'r') as file:
        markdown = file.read()
    with open(template_path, 'r') as file:
        template = file.read()

    html_content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace('{{ Title }}', title)
    template = template.replace('{{ Content }}', html_content)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    if not os.path.exists(dest_path):
        create_directory_from_path(dest_path)
        os.system(f'touch {dest_path}')

    with open(dest_path, 'w') as file:
        file.write(template)
        
def create_directory_from_path(path):
    dir = os.path.dirname(path)
    if os.path.exists(dir) and os.path.isdir(dir):
        return
    else:
        os.makedirs(dir)

if __name__ == '__main__':
    main()