PANDOC ?= pandoc

.PHONY: all clean

all:
	$(PANDOC) --defaults=document.yaml
	python3 update-fields.py article.docx

clean:
	rm -f article.docx
