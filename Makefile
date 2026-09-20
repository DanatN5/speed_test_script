install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

uninstall:
	uv pip uninstall speed-test-script

reinstall:
	uv tool install --force dist/*.whl
	
package-uninstall:
	uv tool uninstall speed_test_script

lint:
	uv run ruff check
