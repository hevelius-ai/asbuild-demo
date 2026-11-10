"""Story S1, count words. Black-box: runs the app as a person would. Standard library and pytest only."""

import subprocess
import sys


def run_app(*args):
    return subprocess.run([sys.executable, "-m", "app", *args], capture_output=True, text=True)


def test_S1_C1_counts_the_words_in_a_file(tmp_path):
    f = tmp_path / "three.txt"
    f.write_text("one two\nthree\n")
    out = run_app("count", str(f))
    assert out.returncode == 0
    assert out.stdout.strip().splitlines()[-1] == "words: 3"


def test_S1_C2_a_missing_file_says_so(tmp_path):
    out = run_app("count", str(tmp_path / "missing.txt"))
    assert out.returncode == 2
    assert "no such file" in out.stderr.lower()
