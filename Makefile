PYTHON := $(shell command -v python3 2> /dev/null)


ifndef PYTHON
    $(error "Python3 is not installed! See README.md")
endif


test:
	python3 -m unittest
