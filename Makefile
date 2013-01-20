test:
	$(MAKE) clean
	nosetests --all-modules $(ARGS)

coverage:
	$(MAKE) test ARGS="--with-coverage --cover-package=fysom $(ARGS)"

clean:
	@find . -iname '*.pyc' -delete -o -iname '*.pyo' -delete
