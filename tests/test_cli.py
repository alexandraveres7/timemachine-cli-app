from cli.time_machine_cli import timemachine
from click.testing import CliRunner

runner = CliRunner()


def test_pools_get():
    response = runner.invoke(timemachine, ['pools', 'get'])
    assert response.exit_code == 0
    assert "[{'name': 'hybrid'}]" in response.output


def test_datasets_get():
    response = runner.invoke(timemachine, ['datasets', 'get'])
    assert response.exit_code == 0
    assert "[{'name': 'hybrid'}, {'name': 'hybrid/picasso'}]" in response.output


def test_dataset_create():
    response = runner.invoke(timemachine, ['datasets', 'create', '--name', 'new'])
    assert response.exit_code == 0
    assert [{'name': 'hybrid'}, {'name': 'hybrid/picasso'}, {'name': 'hybrid/new'}]


def test_snapshots_get():
    response = runner.invoke(timemachine, ['snapshots', 'get'])
    assert response.exit_code == 0
    assert "[{'name': 'hybrid/picasso@cina'}]" in response.output
