"""Story S2, count lines. Black-box: runs the app as a person would. Standard library and pytest only."""

import subprocess
import sys


def run_app(*args):
    return subprocess.run([sys.executable, "-m", "app", *args], capture_output=True, text=True)


def test_S2_C1_shows_the_number_of_lines_in_a_file(tmp_path):
    f = tmp_path / "three.txt"
    f.write_text("one\ntwo\nthree\n")
    out = run_app("lines", str(f))
    assert out.returncode == 0
    assert out.stdout.strip().splitlines()[-1] == "lines: 3"


def test_S2_C2_an_empty_file_shows_zero_lines(tmp_path):
    f = tmp_path / "empty.txt"
    f.write_text("")
    out = run_app("lines", str(f))
    assert out.returncode == 0
    assert out.stdout.strip().splitlines()[-1] == "lines: 0"
