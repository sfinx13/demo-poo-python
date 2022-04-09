# Simple demo POO python

## Presentation

### Class diagram

![Diagram class UML](/_DOC/diagramme_de_classe_poo_app_python.drawio.png)

### Demo screen app

>![Screenshoot console application](/_DOC/screenshoot_console_app.png)

## Installation
```bash
docker build -t demo-poo-python .
docker run -it demo-poo-python
```

## Tests
### unittest
```
python -m unitest -v
```

### doctest
```
python -m doctest -v library/*.py
```

## Documentation
* https://docs.python.org/3/tutorial/classes.html
* https://docs.python.org/3/library/abc.html
* https://docs.python.org/fr/3/tutorial/modules.html
* https://docs.python.org/3/library/unittest.html
* https://docs.python.org/3/library/doctest.html?highlight=doctest#module-doctest

