
A simple CLI application using Click and the time machine API from Syneto.


Example usage
-------------

| $ time_machine_cli pools get
| $ time_machine_cli snapshots create --dataset hybrid/your_dataset --snapshot my_snapshot
| $ time_machine_cli datasets delete --name hybrid/my_dataset_name

Testing
-------------

| You can write tests and then run them with
| $ pytest

Just make sure you're tests are in the tests directory.