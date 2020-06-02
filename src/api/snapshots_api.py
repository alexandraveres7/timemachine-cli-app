from api.time_machine_api import TimeMachineApi


class SnapshotsApi(TimeMachineApi):

    def get_snapshots(self):
        return super()._get(super().url + 'snapshots/')

    def create_snapshot(self, dataset_name, snapshot_name):
        json = {"dataset": dataset_name, "snapshot": snapshot_name}
        super()._post(super().url + 'snapshots/', json)

    def rename_snapshot(self, from_name, rename_to):
        json = {"from_name": from_name, "rename_to": rename_to}
        super()._put(super().url + 'snapshots/', json)

    def delete_snapshot(self, name):
        json = {"name": name}
        super()._delete(super().url + 'snapshots/', json)

    def clone_snapshot(self, dataset, snapshot_name):
        json = {"dataset": dataset, "snapshot": snapshot_name}
        super()._put(super().url + 'snapshots/clone', json)

    def rollback_snapshot(self, snapshot):
        json = {"name": snapshot}
        super()._put(super().url + 'snapshots/rollback', json)
