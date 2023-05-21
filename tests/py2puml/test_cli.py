from argparse import HelpFormatter
from io import StringIO
from subprocess import run, PIPE
from typing import List
from pytest import mark
from py2puml.asserts import assert_multilines
from py2puml.py2puml import py2puml
from subprocess import PIPE, STDOUT, run
from hypothesis import given, strategies as st
from tests import __version__, __description__, TESTS_PATH
from subprocess import run, PIPE
from pytest import mark
import sys
from pathlib import Path
import sys
from argparse import Namespace
from unittest import mock
from pathlib import Path

from py2puml.cli import run as runcli

@mark.parametrize(
    'entrypoint', [
        ['py2puml'],
        ['python', '-m', 'py2puml']
    ]
)
def test_cli_consistency_with_the_default_configuration(entrypoint: List[str]):
    command = entrypoint + ['py2puml/domain', 'py2puml.domain']
    cli_stdout = run(command,
        stdout=PIPE, stderr=PIPE,
        text=True, check=True
    ).stdout

    puml_content = py2puml('py2puml/domain', 'py2puml.domain')

    assert ''.join(puml_content).strip() == cli_stdout.strip()

def test_cli_on_specific_working_directory():
    command = ['py2puml', 'withrootnotincwd', 'withrootnotincwd']
    cli_process = run(command,
        stdout=PIPE, stderr=PIPE,
        text=True, check=True,
        cwd='tests/modules'
    )

    with open(TESTS_PATH / 'puml_files' / 'withrootnotincwd.puml', 'r', encoding='utf8') as expected_puml_file:
        assert_multilines(
            # removes the last return carriage added by the stdout
            [line for line in StringIO(cli_process.stdout)][:-1],
            expected_puml_file
        )

@mark.parametrize(
    'version_command', [
        ['-v'],
        ['--version']
    ]
)
def test_cli_version(version_command: List[str]):
    '''
    Ensures the consistency between the CLI version and the project version set in pyproject.toml
    which is not included when the CLI is installed system-wise
    '''
    command = ['py2puml'] + version_command
    cli_version = run(command,
        stdout=PIPE, stderr=PIPE,
        text=True, check=True
    ).stdout

    assert cli_version == f'py2puml {__version__}\n'

@mark.parametrize(
    'help_command', [
        ['-h'],
        ['--help']
    ]
)
def test_cli_help(help_command: List[str]):
    '''
    Ensures the consistency between the CLI help and the project description set in pyproject.toml
    which is not included when the CLI is installed system-wise
    '''
    command = ['py2puml'] + help_command
    help_text = run(command,
        stdout=PIPE, stderr=PIPE,
        text=True, check=True
    ).stdout.replace('\n', ' ')

    assert __description__ in help_text

def test_cli_missing_required_argument():
    command = ['py2puml']
    cli_process = run(command,
        stdout=PIPE, stderr=PIPE,
        text=True
    )

    assert cli_process.returncode == 2
    assert 'the following arguments are required: path, module' in cli_process.stderr

def test_cli_invalid_argument_type():
    command = ['py2puml', 'py2puml/domain', 'invalid_argument']
    cli_process = run(
        command,
        stdout=PIPE,
        stderr=PIPE,
        text=True,
    )

    assert cli_process.returncode == 1

@mark.parametrize(
    'entrypoint', [
        ['py2puml'],
        ['python', '-m', 'py2puml']
    ]
)
def test_cli_with_invalid_module(entrypoint):
    command = entrypoint + ['py2puml/domain', 'invalid_module']
    cli_process = run(command,
        stdout=PIPE, stderr=PIPE,
        text=True
    )

    assert cli_process.returncode == 1
    assert 'ModuleNotFoundError: No module named' in cli_process.stderr

def test_cli_help_with_version():
    command = ['py2puml', '-h', '-v']
    cli_process = run(command, stdout=PIPE, stderr=PIPE, text=True)
    assert 'usage: py2puml' in cli_process.stdout

def test_cli_with_non_ascii_module_name():
    command = ['py2puml', 'py2puml/domain', 'æøå']
    cli_process = run(command,
        stdout=PIPE, stderr=PIPE,
        text=True
    )

    assert cli_process.returncode == 1
    assert 'ModuleNotFoundError: No module named' in cli_process.stderr

def test_cli_with_valid_path_and_invalid_module():
    command = ['py2puml', 'py2puml/domain', 'invalid_module']
    cli_process = run(command,
        stdout=PIPE, stderr=PIPE,
        text=True
    )

    assert cli_process.returncode == 1
    assert 'ModuleNotFoundError: No module named' in cli_process.stderr

def test_cli_with_valid_path_and_missing_module_argument():
    command = ['py2puml', 'py2puml/domain']
    cli_process = run(command,
        stdout=PIPE, stderr=PIPE,
        text=True
    )

    assert cli_process.returncode == 2
    assert 'the following arguments are required: module' in cli_process.stderr

@mark.parametrize(
    'entrypoint,expected_output', [
        (['py2puml'], 'usage: py2puml [-h] [-v] path module\n'),
        (['python', '-m', 'py2puml'], 'usage: __main__.py [-h] [-v] path module\n'),
    ]
)
def test_cli_with_no_arguments(entrypoint, expected_output):
    cli_process = run(entrypoint,
        stdout=PIPE, stderr=PIPE,
        text=True, input='\n'
    )
    assert cli_process.returncode == 2
    assert expected_output in cli_process.stderr

def test_path_append():
    current_working_directory = str(Path.cwd().resolve())

    # Append the current working directory to sys.path
    sys.path.append(current_working_directory)

    # Check if the current working directory is added to sys.path
    assert current_working_directory in sys.path

class TestCLI:

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=Namespace(path='.', module=None))
    def test_adds_current_directory_to_path(self, mock_parse_args):
        current_working_directory = str(Path.cwd().resolve())

        with mock.patch.object(sys, 'path', []):
            runcli()

        assert current_working_directory in sys.path