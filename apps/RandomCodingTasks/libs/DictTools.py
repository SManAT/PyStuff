import yaml


class DictTools():
  """ Handle Dictionarys """
  def __init__(self):
    pass

  def write(self, data, filename):
    """ write dict to YAML """
    try:
      with open(filename, 'w') as handle:
        handle.write(yaml.dump(data, indent=4, default_flow_style=False))
    except IOError as e:
      print('Could not save data to yaml file %s: %s' % (filename, str(e)))

  def read(self, filename):
    """ read dict from YAML """
    with open(filename, 'r') as stream:
      try:
        parsed_yaml = yaml.safe_load(stream)
        return parsed_yaml
      except yaml.YAMLError as exc:
        print(exc)
