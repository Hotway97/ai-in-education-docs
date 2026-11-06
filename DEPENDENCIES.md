# Зависимости

| Компонент | Версия | Назначение |
|---|---|---|
| Pandoc | 3.8+ (проверено на 3.13) | Сборка Markdown в DOCX |
| pandoc-crossref | 0.3.26a | Нумерация рисунков и таблиц |
| Python | 3.9+ | Скрипт `update-fields.py`, только стандартная библиотека |
| GNU Make | 3.81+ | Запуск сборки через `make` |
| Microsoft Word | любая | Просмотр DOCX и обновление полей, для сборки не требуется |

## macOS

Установка через Homebrew:

```bash
brew bundle --file=Brewfile
```

Или вручную:

```bash
brew install pandoc pandoc-crossref python
```

Сборка:

```bash
make
```

## Windows

Нужны Pandoc 3.12.1 и pandoc-crossref 0.3.26. Их можно положить в локальную папку `pandoc/` или добавить в `PATH`.

Сборка:

```bat
build.cmd
```

Для автоматического обновления оглавления при открытии DOCX нужен Python 3:

```bat
python update-fields.py article.docx
```

## Проверка версий

```bash
pandoc --version
pandoc-crossref --version
python3 --version
make --version
```

## Python-пакеты

Сторонние pip-пакеты не используются. `update-fields.py` работает только со стандартной библиотекой Python, поэтому отдельный `requirements.txt` не нужен.
