from api.time_machine_api import TimeMachineApi


class DatasetsApi(TimeMachineApi):

    def get_datasets(self):
        return super()._get(super().url + 'datasets/')

    def create_dataset(self, name):
        json = {"name": name}
        super()._post(super().url + 'datasets/', json)

    def rename_dataset(self, from_name, rename_to):
        json = {"from_name": from_name, "rename_to": rename_to}
        super()._put(super().url + 'datasets/', json)

    def delete_dataset(self, name):
        json = {"name": name}
        super()._delete(super().url + 'datasets/', json)
