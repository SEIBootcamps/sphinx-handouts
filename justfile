git-hooks:
  @echo "Installing pre-commit and other Git hooks..."
  pre-commit install

_sphinx:
  @rm -rf examples/kitchen-sink/_build
  @poetry run sphinx-build -b html -d examples/kitchen-sink/_build/doctrees -n examples/kitchen-sink examples/kitchen-sink/_build/html

build: _sphinx