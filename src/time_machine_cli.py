import click
from pprint import pprint

from datasets_api import DatasetsApi
from pools_api import PoolsApi
from snapshots_api import SnapshotsApi
from src.time_machine_api import TimeMachineApi
from click_help_colors import HelpColorsGroup, HelpColorsCommand


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


@datasets.command(help='Delete a dataset')
@click.option('--name', help='Name of the dataset you wish to delete')
@click.pass_obj
def delete(api, name):
    api.delete_dataset(name)


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
@click.option('--dataset-name', help='Name of the dataset you wish to create a snapshot of')
@click.option('--snapshot-name', help='Name of the new snapshot')
@click.pass_obj
def create(api, dataset_name, snapshot_name):
    api.create_snapshot(dataset_name, snapshot_name)
    pprint(api.get_snapshots())


@snapshots.command(help='Rename a snapshot')
@click.option('--from-name', help='Name of the snapshot you wish to change')
@click.option('--rename-to', help='New name of the snapshot')
@click.pass_obj
def rename(api, from_name, rename_to):
    api.rename_snapshot(from_name, rename_to)


@snapshots.command(help='Destroy a snapshot for a dataset')
@click.option('--name', help='Name of the snapshot you wish to destroy')
@click.pass_obj
def delete(api, name):
    api.delete_snapshot(name)


@snapshots.command(help='Clone snapshot into a dataset')
@click.option('--dataset', help='Name of the new data set where the clone will be saved')
@click.option('--snapshot', help='Name of the snapshot that will be cloned')
@click.pass_obj
def clone(api, dataset, snapshot):
    api.clone_snapshot(dataset, snapshot)


@snapshots.command(help='Rollback dataset to a snapshot')
@click.option('--snapshot', help='Name of the snapshot that we will roll back to')
@click.pass_obj
def rollback(api, snapshot):
    api.rollback_snapshot(snapshot)
