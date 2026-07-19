"""
Tests for PythonAnalyzer.
"""

from pathlib import Path
import tempfile
from analyzers.python_analyzer import PythonAnalyzer


def test_analyze_symbols():
    code = """
class MyClass:
    def my_method(self):
        pass

def my_function():
    pass
"""
    # Crear un archivo temporal para probar el analyzer
    with tempfile.NamedTemporaryFile(
        suffix=".py", delete=False, mode="w", encoding="utf-8"
    ) as f:
        f.write(code)
        f.flush()
        path = Path(f.name)

    try:
        analyzer = PythonAnalyzer()
        symbols = analyzer.analyze(path)

        assert "MyClass" in symbols["classes"]
        assert "my_function" in symbols["functions"]
        assert "MyClass.my_method" in symbols["methods"]
    finally:
        path.unlink()  # Limpiar el archivo temporal
