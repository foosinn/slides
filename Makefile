marks := $(wildcard */slides/*.md)
htmls := $(marks:.md=.html)


all: $(htmls) reveal.js

%.html: %.md
	pandoc -t revealjs -s -o $(@F) $^ -V revealjs-url=./reveal.js -V theme=white

reveal.js:
	mkdir reveal.js
	curl -L https://github.com/hakimel/reveal.js/archive/master.tar.gz | tar xvzpf - --strip-components=1 -C reveal.js


