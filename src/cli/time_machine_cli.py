import click
from pprint import pprint

from api.datasets_api import DatasetsApi
from api.pools_api import PoolsApi
from api.snapshots_api import SnapshotsApi
from api.time_machine_api import TimeMachineApi
from click_help_colors import HelpColorsGroup


@click.group(cls=HelpColorsGroup, help_headers_color='blue', help_options_color='green', help='TimeMachine Api')
@click.option(
    "--verbose",
    "-v",
    default=False,
    is_flag=True,
    show_default=True,
    help="Enable debug output",
)
@click.pass_context
def timemachine(ctx, verbose):
    ctx.obj = TimeMachineApi()


@timemachine.group(help='Pools commands')
@click.pass_context
def pools(ctx):
    ctx.obj = PoolsApi()


@pools.command(help='Get pools list')
@click.pass_obj
def get(api):
    pools = api.get_pools()
    pprint(pools)


@timemachine.group(help='Datasets commands')
@click.pass_context
def datasets(ctx):
    ctx.obj = DatasetsApi()


@datasets.command(help='Get dataset list')
@click.pass_obj
def get(api):
    datasets = api.get_datasets()
    pprint(datasets)


@datasets.command(help='Create a dataset')
@click.option('--name', help='Name of the new dataset')
@click.pass_obj
def create(api, name):
    api.create_dataset(name)
    pprint(api.get_datasets())


@datasets.command(help='Rename a dataset')
@click.option('--from-name', help='Name of the dataset you wish to change')
@click.option('--rename-to', help='New name of the dataset')
@click.pass_obj
def rename(api, from_name, rename_to):
    api.rename_dataset(from_name, rename_to)
    pprint(api.get_datasets())


@datasets.command(help='Delete a dataset')
@click.option('--name', help='Name of the dataset you wish to delete')
@click.pass_obj
def delete(api, name):
    api.delete_dataset(name)
    pprint(api.get_datasets())


@timemachine.group(help='Snapshots commands')
@click.pass_context
def snapshots(ctx):
    ctx.obj = SnapshotsApi()


@snapshots.command(help='Get all snapshots, for all datasets')
@click.pass_obj
def get(api):
    snapshots = api.get_snapshots()
    pprint(snapshots)


@snapshots.command(help='Create a snapshot for a dataset')
@click.option('--dataset', help='Name of the dataset you wish to create a snapshot of')
@click.option('--snapshot', help='Name of the new snapshot')
@click.pass_obj
def create(api, dataset, snapshot):
    api.create_snapshot(dataset, snapshot)
    pprint(api.get_snapshots())


@snapshots.command(help='Rename a snapshot')
@click.option('--from-name', help='Name of the snapshot you wish to change')
@click.option('--rename-to', help='New name of the snapshot')
@click.pass_obj
def rename(api, from_name, rename_to):
    api.rename_snapshot(from_name, rename_to)
    pprint(api.get_snapshots())


@snapshots.command(help='Destroy a snapshot for a dataset')
@click.option('--name', help='Name of the snapshot you wish to destroy')
@click.pass_obj
def delete(api, name):
    api.delete_snapshot(name)
    pprint(api.get_snapshots())


@snapshots.command(help='Clone snapshot into a dataset')
@click.option('--dataset', help='Name of the new dataset where the clone will be saved')
@click.option('--snapshot', help='Name of the snapshot that will be cloned')
@click.pass_obj
def clone(api, dataset, snapshot):
    api.clone_snapshot(dataset, snapshot)
    pprint(api.get_snapshots())


@snapshots.command(help='Rollback dataset to a snapshot')
@click.option('--snapshot', help='Name of the snapshot that we will roll back to')
@click.pass_obj
def rollback(api, snapshot):
    api.rollback_snapshot(snapshot)
    pprint(api.get_snapshots())
