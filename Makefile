test:
	$(MAKE) clean
	nosetests --all-modules

clean:
	@find . -iname '*.pyc' -delete -o -iname '*.pyo' -delete
