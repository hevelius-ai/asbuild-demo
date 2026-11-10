import subprocess
import sys


def test_version_prints_the_version():
    out = subprocess.run([sys.executable, "-m", "app", "version"], capture_output=True, text=True)
    assert out.returncode == 0
    assert out.stdout.strip() == "0.1.0"
