build:
	python3 -m build
	twine check dist/*

clean:
	rm -rf dist/
