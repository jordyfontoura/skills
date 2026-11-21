"""Copia as pastas configuradas para o destino de backup, uma pasta por dia."""
import json
import logging
import shutil
import sys
from datetime import date
from logging.handlers import RotatingFileHandler
from pathlib import Path

CONFIG = Path(__file__).with_name("config.json")
LOG_FILE = Path(__file__).with_name("backup.log")

logger = logging.getLogger("backup")


def setup_logging():
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=1_000_000, backupCount=5, encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def load_config():
    with CONFIG.open(encoding="utf-8") as handle:
        return json.load(handle)


def remove_old(destination, keep):
    folders = sorted(path for path in destination.iterdir() if path.is_dir())
    for folder in folders[:-keep]:
        logger.info("Removendo backup antigo: %s", folder.name)
        shutil.rmtree(folder)


def backup(config):
    destination = Path(config["destination"]) / date.today().isoformat()
    failures = []
    for source in config["sources"]:
        source = Path(source)
        logger.info("Copiando %s...", source)
        try:
            shutil.copytree(source, destination / source.name, dirs_exist_ok=True)
        except OSError as error:
            logger.error("Falha ao copiar %s: %s", source, error)
            failures.append(source)
    remove_old(Path(config["destination"]), config.get("keep", 7))
    return failures


def main():
    setup_logging()
    logger.info("Iniciando backup.")
    try:
        config = load_config()
        failures = backup(config)
    except Exception:
        logger.exception("Backup interrompido por erro inesperado.")
        return 1
    if failures:
        logger.error("Backup terminou com %d falha(s).", len(failures))
        return 1
    logger.info("Backup concluído.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
