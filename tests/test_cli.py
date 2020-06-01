from click.testing import CliRunner
from time_machine_cli import timemachine


def test_get_all_pools():
    runner = CliRunner()
    result = runner.invoke(timemachine, ['pools', 'get'])
    assert ['hybrid'] in result.output
    assert result.exit_code == 0


print(test_get_all_pools())
