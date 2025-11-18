# AI suggested testing `read_pulse_file` because it reads and processes external data,
# which is a key part of the pipeline. I created a unit test to make sure the function
# reads at least three lines from `pulse.txt`.

from pulse_tools import read_pulse_file

def test_read_pulse_file():
    assert read_pulse_file("pulse.txt") >= 3

