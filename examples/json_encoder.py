import natch


@natch.condition(lambda x: isinstance(x, bool))
def encode(data):
    return 'true' if data is True else 'false'


@natch.condition(lambda x: isinstance(x, int))
def encode(data):
    return str(data)


@natch.condition(lambda x: isinstance(x, str))
def encode(data):
    return f'"{data}"'


@natch.condition(lambda x: isinstance(x, list))
def encode(data):
    encoded_segments = list()
    for segment in data:
        encoded_segment = encode(segment)
        encoded_segments.append(encoded_segment)
    inner = ', '.join(encoded_segments)
    return f'[{inner}]'


@natch.condition(lambda x: isinstance(x, dict))
def encode(data):
    inner_split = []
    for key, value in data.items():
        encoded_segment = encode(value)
        inner_split.append(f'"{key}": {encoded_segment}')
    inner = ', '.join(inner_split)
    return f'{{{inner}}}'


data = {'id': -1, 'username': 'ertgl', 'follows': ['neuro-sys'], 'is_active': True}

encoded_data = encode(data)
print(encoded_data)
