install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

uninstall:
	uv pip uninstall speed-test-script
	
package-uninstall:
	uv tool uninstall speed_test_script

run:
	uv run speed_test -- help

lint:
	uv run ruff check
