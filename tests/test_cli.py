import os
import sys

import pytest
from click.testing import CliRunner

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from trace_dkey.cmd import cli



@pytest.fixture
def runner():
    return CliRunner()


def test_trace_key(runner):
    input_json = '{"name": "John Doe", "age": 30}'
    expected_output = "[['name']]"

    with runner.isolated_filesystem():
        # Create a temporary test JSON file
        with open("test.json", "w") as file:
            file.write(input_json)

        result = runner.invoke(cli, ["--file", "test.json", "--key", "name"])
        assert result.exit_code == 0
        assert result.output.strip() == expected_output