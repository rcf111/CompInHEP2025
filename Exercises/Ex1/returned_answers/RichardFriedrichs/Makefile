SRC = $(basename $(wildcard *.tex))
PRE = $(addsuffix .ps, $(SRC))
OUT = $(addsuffix .pdf, $(SRC))

all:
	$(MAKE) -i tex
	$(MAKE) bib
	$(MAKE) mf
	$(MAKE) tex
	$(MAKE) tex
	$(MAKE) dvips
	$(MAKE) pdf

tex:
	latex $(SRC)

bib:
	bibtex $(SRC)

mf:
	mf "\mode=localfont; input graph1.mf;"
	mf "\mode=localfont; input graph2.mf;"

dvips:
	dvips $(SRC) -o
pdf:
	ps2pdf $(PRE) $(OUT)

RM = $(sort $(wildcard *.dvi *.log *.fls *.gz *.blg *.bbl *.xml *-blx.bib *.fdb_latexmk *.aux graph* *~))
clean:
	rm -r $(RM)

cleanAll:
	$(MAKE) clean
	rm -rf *.ps 
	rm -rf *.pdf
