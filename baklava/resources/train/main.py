$entrypoint
import argparse
import os
from mlsriracha.training import TrainingAdapter

print('Starting mlctl container')

parser = argparse.ArgumentParser(
                description='Accept general args.'
                )
                
# https://gist.github.com/fralau/061a4f6c13251367ef1d9a9a99fb3e8d
parser.add_argument("--set",
    metavar="KEY=VALUE",
    nargs='*',
    help="Set a number of key-value pairs "
        "(do not put spaces before or after the = sign). "
        "If a value contains spaces, you should define "
        "it with double quotes: "
        'foo="this is a sentence". Note that '
        "values are always treated as strings.")

args, remainder = parser.parse_known_args()

def parse_var(s):
    """
    Parse a key, value pair, separated by '='
    That's the reverse of ShellArgs.

    On the command line (argparse) a declaration will typically look like:
        foo=hello
    or
        foo="hello world"
    """
    items = s.split('=')
    key = items[0].strip() # we remove blanks around keys, as is logical
    if len(items) > 1:
        # rejoin the rest:
        value = '='.join(items[1:])
    return (key, value)


def parse_vars(items):
    """
    Parse a series of key-value pairs and return a dictionary
    """
    d = {}

    if items:
        for item in items:
            key, value = parse_var(item)
            d[key] = value
    return d

if args.set is not None:
    # parse the key-value pairs
    param_values = parse_vars(args.set)

    print(f'params= {param_values}')
    data_fields = [
        # mlctl specific
        'sriracha_provider', 
        # Azure ML specific
        'training-data', 'validation-data', 'test-data', 'sriracha_mlflow_tracking_uri']
    for data_field in data_fields:
        if data_field in param_values.keys():
            print(f'{data_field}={param_values[data_field]} found in params')
            os.environ[data_field] = param_values[data_field]

# create training adapter env
ta = TrainingAdapter(os.getenv('sriracha_provider'))
try:
    entrypoint(ta)
    ta.finish()
except TypeError:
    print('User provided function does not support TrainingAdapter')
    entrypoint()