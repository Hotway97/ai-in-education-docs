"""Добавляет в DOCX флаг обновления полей Word.

Скрипт вызывается после сборки документа Pandoc и обеспечивает
автоматическое обновление оглавления при открытии файла.
"""

import os
import sys
import zipfile
from pathlib import Path

SETTINGS_PATH = "word/settings.xml"
UPDATE_FIELDS_FLAG = '<w:updateFields w:val="true"/>'
SETTINGS_END_TAG = "</w:settings>"


def add_update_fields_flag(settings_xml):
    """Добавляет в XML настроек Word флаг обновления полей.

    :param settings_xml: содержимое файла word/settings.xml
    :return: XML с флагом обновления полей
    """
    if "<w:updateFields" in settings_xml:
        return settings_xml

    return settings_xml.replace(
        SETTINGS_END_TAG,
        UPDATE_FIELDS_FLAG + SETTINGS_END_TAG
    )


def rebuild_docx(docx_path):
    """Пересобирает DOCX, добавляя флаг обновления полей.

    Исходный файл заменяется новым архивом с изменённым
    файлом word/settings.xml.

    :param docx_path: путь к DOCX-файлу
    """
    temporary_path = docx_path.with_name(docx_path.name + ".tmp")

    with zipfile.ZipFile(docx_path, "r") as source:
        with zipfile.ZipFile(temporary_path, "w", zipfile.ZIP_DEFLATED) as target:
            for archive_entry in source.infolist():
                entry_data = source.read(archive_entry.filename)

                if archive_entry.filename == SETTINGS_PATH:
                    settings_xml = entry_data.decode("utf-8")
                    settings_xml = add_update_fields_flag(settings_xml)
                    entry_data = settings_xml.encode("utf-8")

                target.writestr(archive_entry, entry_data)

    os.replace(temporary_path, docx_path)


def main():
    """Запускает обработку DOCX, переданного аргументом командной строки."""
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 update-fields.py article.docx")

    docx_path = Path(sys.argv[1])
    rebuild_docx(docx_path)
    print(f"DOCX finalized: {docx_path}")


if __name__ == "__main__":
    main()
