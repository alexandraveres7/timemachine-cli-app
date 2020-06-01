from time_machine_api import TimeMachineApi


class PoolsApi(TimeMachineApi):

    def get_pools(self):
        return super()._get(super().url + 'pools/')
