import click
import json
from trace_dkey import trace


@click.command()
@click.option("--file", "-f", required=True, help="Path to the JSON file")
@click.option("--key", "-k", required=False, help="Key to trace in the dictionary")
def cli(file: str, key: str):
    with open(file) as file_obj:
        dictionary = json.load(file_obj)

    print(trace(dictionary, key))