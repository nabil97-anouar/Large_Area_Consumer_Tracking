from .. import attribute


class JaadType(attribute.ObjectType):
    """Object types for JAAD."""
    PEDESTRIAN = ()


JAAD_ATTRIBUTE_METAS = {
    JaadType.PEDESTRIAN: [
        # Detection
        {'attribute': 'confidence',          'group': 'detection',  'only_on_instance': False, 'is_classification': True,  'is_scalar': True,  'is_spatial': False, 'n_channels': 1},
        {'attribute': 'center',              'group': 'detection',  'only_on_instance': True,  'is_classification': False, 'is_scalar': False, 'is_spatial': True,  'n_channels': 2, 'std': [2.7, 5.9]},
        {'attribute': 'height',              'group': 'detection',  'only_on_instance': True,  'is_classification': False, 'is_scalar': True,  'is_spatial': True,  'n_channels': 1, 'default': 17.5, 'mean': 17.5, 'std': 8.9},
        {'attribute': 'width',               'group': 'detection',  'only_on_instance': True,  'is_classification': False, 'is_scalar': True,  'is_spatial': True,  'n_channels': 1, 'default': 7.7,  'mean': 7.7,  'std': 4.4},
        # Intention
        {'attribute': 'time_to_crossing',    'group': 'intention',  'only_on_instance': True,  'is_classification': False, 'is_scalar': True,  'is_spatial': False, 'n_channels': 1, 'default': -2.4, 'mean': -2.4, 'std': 2.8},
        # Behavior
        {'attribute': 'look',                'group': 'behavior',   'only_on_instance': True,  'is_classification': True,  'is_scalar': True,  'is_spatial': False, 'n_channels': 1, 'default': 0},
        {'attribute': 'walk',                'group': 'behavior',   'only_on_instance': True,  'is_classification': True,  'is_scalar': True,  'is_spatial': False, 'n_channels': 1, 'default': 1},
        {'attribute': 'motion_direction',    'group': 'behavior',   'only_on_instance': True,  'is_classification': True,  'is_scalar': True,  'is_spatial': False, 'n_channels': 2, 'default': 0, 'labels': {0: 'lateral', 1: 'longitudinal'}},
        {'attribute': 'group_size',          'group': 'behavior',   'only_on_instance': True,  'is_classification': True,  'is_scalar': True,  'is_spatial': False, 'n_channels': 4, 'default': 1, 'labels': {0: '1', 1: '2', 2: '3', 3: '4+'}},
        {'attribute': 'reaction',            'group': 'behavior',   'only_on_instance': True,  'is_classification': True,  'is_scalar': True,  'is_spatial': False, 'n_channels': 4, 'default': 0, 'labels': {0: 'none', 1: 'clear_path', 2: 'speed_up', 3: 'slow_down'}},
        # Appearance
        {'attribute': 'gender',              'group': 'appearance', 'only_on_instance': True,  'is_classification': True,  'is_scalar': True,  'is_spatial': False, 'n_channels': 2, 'default': 0, 'labels': {0: 'female', 1: 'male'}},
        {'attribute': 'age',                 'group': 'appearance', 'only_on_instance': True,  'is_classification': True,  'is_scalar': True,  'is_spatial': False, 'n_channels': 3, 'default': 1, 'labels': {0: 'child/young', 1: 'adult', 2: 'senior'}},
      
}
