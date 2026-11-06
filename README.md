# Применение искусственного интеллекта в сфере образования

Статья собирается из Markdown в Word одной командой Pandoc. Оформление хранится в `template.docx` и редактируется через стили Word.

Проект основан на шаблоне [Cionaodh/word-as-code](https://github.com/Cionaodh/word-as-code): сохранена структура `src/`, `images/`, `document.yaml`, `template.docx`, `gost-r-7.0.100-2018.csl` и сборка через Pandoc. Оформление взято из первого примера [true-grue/kisscm](https://github.com/true-grue/kisscm): Times New Roman, A4, титульная шапка, номера страниц и стили заголовков. Содержание заменено на статью И. И. Алексеева, А. Ю. Грибченко, В. С. Дорофеева и А. М. Круглова «Применение искусственного интеллекта в сфере образования».

## Зависимости

Список версий и команд установки — в [DEPENDENCIES.md](DEPENDENCIES.md). Для macOS зависимости можно установить из `Brewfile`.

## Запуск на macOS

Нужны Pandoc, pandoc-crossref и Python 3.

```bash
brew bundle --file=Brewfile
make
```

Результат — `article.docx` в корне проекта. Готовый файл также добавлен в репозиторий.

Очистка:

```bash
make clean
```

## Запуск на Windows

Нужны Windows 10/11 x64, Pandoc **3.12.1** и pandoc-crossref **0.3.26**.

1. Скачайте [Pandoc для Windows](https://github.com/jgm/pandoc/releases/download/3.12.1/pandoc-3.12.1-windows-x86_64.zip).
2. Распакуйте архив. Папку с `pandoc.exe` поместите в проект под именем `pandoc`.
3. Скачайте [pandoc-crossref для Windows](https://github.com/lierdakil/pandoc-crossref/releases/download/v0.3.26/pandoc-crossref-Windows-X64.7z) и положите `pandoc-crossref.exe` в ту же папку.
4. Выполните `build.cmd`.

Если обе программы доступны через `PATH`, папка `pandoc/` не нужна.

## Структура

```text
.
├── src/                     # главы статьи
├── images/                  # рисунки
├── article.docx             # готовый документ
├── bibliography.bib
├── Brewfile
├── build.cmd
├── DEPENDENCIES.md
├── document.yaml
├── gost-r-7.0.100-2018.csl
├── heading-style.lua
├── Makefile
├── README.md
├── template.docx
└── update-fields.py
```

## Как устроен проект

Основная команда:

```bash
pandoc --defaults=document.yaml
```

В `document.yaml` указаны порядок разделов, выходной формат, фильтры и путь к `template.docx`. Pandoc объединяет текст и применяет стили шаблона.

| Файл | Назначение |
| :--- | :--- |
| `src/00_header.md` | УДК, авторы, название, аннотация и ключевые слова |
| `src/00_toc.md` | Поле оглавления Word |
| `src/01_intro.md` | Введение |
| `src/02_technologies.md` | Технологическая основа, формулы, рисунки и таблица технологий |
| `src/03_applications.md` | Применение ИИ и таблица сценариев |
| `src/04_limitations.md` | Ограничения и риски |
| `src/05_conclusion.md` | Заключение |
| `src/06_references.md` | Список литературы и строка авторского права |
| `images/duolingo-screen.png`, `images/chatgpt-screen.png` | Скриншоты интерфейсов |
| `template.docx` | Стили Word в оформлении kisscm: Times New Roman, A4, номера страниц |
| `document.yaml` | Порядок разделов и параметры Pandoc |
| `bibliography.bib` | Источники для автоматического списка литературы |
| `gost-r-7.0.100-2018.csl` | Стиль оформления ссылок и библиографии |
| `heading-style.lua` | Заголовки капсом и разрывы страниц перед главами |
| `update-fields.py` | Включает обновление полей Word при открытии |
| `build.cmd` | Запуск сборки на Windows |
| `Makefile` | Сборка и очистка на macOS/Linux |

## Что добавлено к статье

- обязательные элементы задания: оглавление, формулы, рисунки, таблицы и список литературы;
- две формулы языковой модели;
- два рисунка с интерфейсами Duolingo и ChatGPT;
- две таблицы: технологии и сценарии;
- автоматическая нумерация рисунков и таблиц через `pandoc-crossref`;
- каждая глава, оглавление и список литературы начинаются с новой страницы.

## Стили

| Стиль | За что отвечает |
| :--- | :--- |
| `Normal` | Times New Roman 14 pt, полуторный интервал, выравнивание по ширине |
| `Body Text` | Абзацный отступ 1,25 см |
| `UDC`, `Author` | УДК и сведения об авторах |
| `Title`, `TitleLast` | Две части названия статьи |
| `Abstract`, `Keywords` | Аннотация и ключевые слова |
| `Heading 1`, `Heading 2` | Заголовки разделов |
| `Figure`, `Captioned Figure` | Размещение рисунков |
| `Image Caption`, `Table Caption` | Подписи рисунков и таблиц |
| `Compact`, `Table` | Абзацы в ячейках, сетка и оформление таблиц |

## Оглавление

Оглавление вставлено как поле Word после шапки статьи. Сборка добавляет в DOCX флаг обновления полей, поэтому Word обновляет оглавление при открытии. Если этого не произошло, нажмите `Ctrl+A`, затем `F9`. В оглавление попадают заголовки `Heading 1` и `Heading 2`.

## Источники изображений

Скриншоты взяты с официальных страниц приложений в App Store. Ссылки и оговорка об использовании — в `images/SOURCES.md`. Названия и интерфейсы принадлежат соответствующим правообладателям; изображения используются как иллюстрации в учебном проекте.

## Атрибуция

- Шаблон и структура сборки: [Cionaodh/word-as-code](https://github.com/Cionaodh/word-as-code).
- Стили оформления: [true-grue/kisscm](https://github.com/true-grue/kisscm) (MIT), шаблон переведён на A4.
- Статья: Алексеев И. И., Грибченко А. Ю., Дорофеев В. С., Круглов А. М. «Применение искусственного интеллекта в сфере образования» // Наукосфера. 2024. № 4 (2). DOI: 10.5281/zenodo.11071106.
- CSL-стиль `gost-r-7.0.100-2018.csl`: ГОСТ Р 7.0.100-2018, из шаблона `word-as-code`.
