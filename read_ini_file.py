from configparser import ConfigParser
import yaml
#import ruamel.yaml
hash = None
config_file = "test.ini"


def handle_value(val):
    if val == "NONE":
        output = None
    elif val in ["-", "null"]:
        output = val
    elif isinstance(val, list) or isinstance(val, int):
        output = val
    else:
        output = yaml.safe_load(val)
    return output


def config_data_update(input, key, value):
    if isinstance(yaml.safe_load(value), dict):
        value = yaml.safe_load(value)
        for n_k, n_v in value.items():
            input[key] = {n_k : handle_value(n_v)}
    else:
        input[key] = handle_value(value)


def read_config(config_file):
    parser = ConfigParser(defaults=None)
    parser.optionxform = lambda option: option
    parser.read(config_file)
    test_config = {}
    for key, value in parser.items("DEFAULT"):
        test_config[key] = yaml.safe_load(value)
    new_config = {}
    for section in parser.sections():
        section_config = {}
        test_items = list(set(parser.items(section)) -
                          set(parser.items("DEFAULT")))
        for key, value in test_items:
            config_data_update(section_config, key, value)
        new_config[section] = section_config
        # print("new_config is \t", new_config)
    return new_config

# read_config(config_file, "20366")
# read_config(config_file, "18876")
# read_config(config_file, "18739")
# read_config(config_file, "18793")
config_details = read_config(config_file)

# for c_k, c_v in config_details.items():
#     # yaml file writing section
#     pass
# or full dump
# new_config = {}
with open('store_file.yaml', 'w') as yaml_file:
#     yaml.dump(config_details, yaml_file, default_flow_style=True)
#     for key, value in config_details.items():
#         yaml.dump(key,value, yaml_file, default_flow_style=True)
#     data = ruamel.yaml.comments.CommentedMap(config_details)
#     data.yaml_set_comment_before_after_key('test*', before='\n')
#     yaml = ruamel.yaml.YAML()
#     yaml.dump(config_details, yaml_file)
      print yaml.dump(config_details, yaml_file, indent=4, default_flow_style=False, Dumper=yaml.SafeDumper, line_break=3)
        # print(yaml.dump(details))