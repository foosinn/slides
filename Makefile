slides := $(wildcard */slides/*.md)

all: $(slides)
	pandoc -t revealjs -s -o $(^F:.md=.html) $^ -V revealjs-url=./reveal.js
	ln -sf $^ $(^F)

reveal.js:
	mkdir reveal.js
	curl -L https://github.com/hakimel/reveal.js/archive/master.tar.gz | tar xvzpf - --strip-components=1 -C reveal.js


