"""Copia as pastas configuradas para o destino de backup, uma pasta por dia."""
import json
import shutil
import sys
from datetime import date
from pathlib import Path

CONFIG = Path(__file__).with_name("config.json")


def load_config():
    with CONFIG.open(encoding="utf-8") as handle:
        return json.load(handle)


def remove_old(destination, keep):
    folders = sorted(path for path in destination.iterdir() if path.is_dir())
    for folder in folders[:-keep]:
        print(f"Removendo backup antigo: {folder.name}")
        shutil.rmtree(folder)


def backup(config):
    destination = Path(config["destination"]) / date.today().isoformat()
    failures = []
    for source in config["sources"]:
        source = Path(source)
        print(f"Copiando {source}...")
        try:
            shutil.copytree(source, destination / source.name, dirs_exist_ok=True)
        except OSError as error:
            print(f"ERRO ao copiar {source}: {error}")
            failures.append(source)
    remove_old(Path(config["destination"]), config.get("keep", 7))
    return failures


def main():
    config = load_config()
    failures = backup(config)
    if failures:
        print(f"Backup terminou com {len(failures)} falha(s).")
        return 1
    print("Backup concluído.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
