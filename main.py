from pathlib import Path
import shutil
import argparse

DOCUMENTS = {'.pdf', '.doc', '.docx', '.txt'}
IMAGES = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
ARCHIVES = {'.zip', '.rar', '.7z'}


def organize_folder(folder: Path) -> None:
    if not folder.exists() or not folder.is_dir():
        raise FileNotFoundError('Pasta inválida.')

    targets = {
        'Documentos': DOCUMENTS,
        'Imagens': IMAGES,
        'Compactados': ARCHIVES,
        'Outros': None,
    }

    for item in folder.iterdir():
        if item.is_dir():
            continue

        destination_name = 'Outros'
        for name, suffixes in targets.items():
            if suffixes and item.suffix.lower() in suffixes:
                destination_name = name
                break

        destination = folder / destination_name
        destination.mkdir(exist_ok=True)
        shutil.move(str(item), str(destination / item.name))


def backup_folder(source: Path, destination: Path) -> None:
    if not source.exists() or not source.is_dir():
        raise FileNotFoundError('Origem inválida.')

    destination.mkdir(parents=True, exist_ok=True)
    final_path = destination / source.name

    if final_path.exists():
        shutil.rmtree(final_path)

    shutil.copytree(source, final_path)


def rename_with_prefix(folder: Path, prefix: str) -> None:
    if not folder.exists() or not folder.is_dir():
        raise FileNotFoundError('Pasta inválida.')

    for index, item in enumerate(sorted(folder.iterdir()), start=1):
        if item.is_file():
            new_name = f"{prefix}_{index}{item.suffix.lower()}"
            item.rename(folder / new_name)


def main() -> None:
    parser = argparse.ArgumentParser(description='Automatizador de tarefas do dia a dia.')
    sub = parser.add_subparsers(dest='command', required=True)

    organize = sub.add_parser('organize')
    organize.add_argument('folder')

    backup = sub.add_parser('backup')
    backup.add_argument('source')
    backup.add_argument('destination')

    rename = sub.add_parser('rename')
    rename.add_argument('folder')
    rename.add_argument('prefix')

    args = parser.parse_args()

    if args.command == 'organize':
        organize_folder(Path(args.folder))
        print('Pasta organizada com sucesso.')
    elif args.command == 'backup':
        backup_folder(Path(args.source), Path(args.destination))
        print('Backup concluído com sucesso.')
    elif args.command == 'rename':
        rename_with_prefix(Path(args.folder), args.prefix)
        print('Arquivos renomeados com sucesso.')


if __name__ == '__main__':
    main()
