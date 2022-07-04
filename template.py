import os
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server


def rebuild():
    dirname = 'photos'
    photos = os.listdir(dirname)
    print(photos)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    pages_dir = Path(Path.cwd() / 'pages')
    books_per_page = 10
    os.makedirs(pages_dir, exist_ok=True)
    render_pages(template, photos, pages_dir, books_per_page)
    print("Site rebuilt")


def render_pages(template, photos, pages_dir, books_per_page=10):
    rendered_page = template.render(photos=photos)
    filepath = os.path.join(pages_dir, f'index.html')
    with open(filepath, 'w', encoding="utf8") as file:
        file.write(rendered_page)



def main():
    rebuild()
    server = Server()
    server.watch('template.html', rebuild)
    server.serve(root='.', default_filename='pages/index.html')


if __name__ == '__main__':
    main()
