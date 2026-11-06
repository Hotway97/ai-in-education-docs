PANDOC ?= pandoc

.PHONY: all clean

all:
	$(PANDOC) --defaults=document.yaml
	python3 tools/finalize_docx.py article.docx

clean:
	rm -f article.docx
