env:
	python3 -m venv env && env/bin/pip install --upgrade pip wheel setuptools

install:
	. env/bin/activate ; pip install -r requirements.txt

upgrade:
	. env/bin/activate ; pip install --upgrade -r requirements-base.txt

freeze:
	. env/bin/activate ; pip freeze > requirements.txt
