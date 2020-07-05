import pytest
from torch.nn import GRU as _GRU
from neuralpy.layers import GRU


def test_gru_should_throws_type_error():
    with pytest.raises(TypeError) as ex:
        x = GRU()

# Possible values
input_sizes = [1, '', 0.8]
hidden_sizes = [2, '', 0.2]
num_layerses = [1, '', 0.8]
biases = [False, True, 2]
batch_firsts = [False, 0.2, 2]
dropouts = [1, None, 0.5]
bidirectionals = [False, True, 2]
names = [False, 12, True]


@pytest.mark.parametrize(
    "input_size, hidden_size, num_layers,\
    bias, batch_first, dropout, bidirectional,name",
    [
        (0.3, 0.3, 0.3, 0.54, 4, 4.6, 5, False),
        (False, 3, 0.3, 0.54, 4, 4.6, 5, False),
        (3, False, 0.3, 0.54, 4, 4.6, 5, False),
        (3, 0.3, 0.3, 0.54, 4, 4.6, 5, False),
        (3, 3, "invalid", 0.54, 4, 4.6, 5, False),
        (3, 3, 3, "invalid", 4, 4.6, 5, False),
        (3, 3, 3, 'tanh', 4, 4.6, 5, False),
        (3, 3, 3, 'tanh', 4, 4.6, 5, False),
        (3, 3, 3, 'tanh', 4.2, 4.6, 5, False),
        (3, 3, 3, 'tanh', False, 4.6, 5, False),
        (3, 3, 3, 'tanh', True, False, 5, False),
        (3, 3, 3, False, False, 1, 5, False),
        (3, 3, 3, False, False, 1, True, False),
        (3, 3, 3, False, False, 1, 5, ""),
    ]
)
def test_gru_should_throw_value_error(
    input_size, hidden_size, num_layers,
    bias, batch_first, dropout, bidirectional,name):
        with pytest.raises(ValueError) as ex:
            x = GRU(
                input_size=input_size, hidden_size=hidden_size,
                num_layers=num_layers, bias=bias,
                batch_first=batch_first, dropout=dropout,
                bidirectional=bidirectional, name=name)

# Possible values
input_sizes = [1, 2]
hidden_sizes = [2, 2]
num_layerses = [1,  4]
biases = [False, True]
batch_firsts = [False, True]
dropouts = [1, 2]
bidirectionals = [False, True]
names = ['Test', None]

@pytest.mark.parametrize(
    "input_size, hidden_size, num_layers,\
    bias, batch_first, dropout, bidirectional,name",
    [(input_size, hidden_size, num_layers,\
    bias, batch_first, dropout, bidirectional,name)
    for input_size in input_sizes
    for hidden_size in hidden_sizes
    for num_layers in num_layerses
    for bias in biases
    for batch_first in batch_firsts
    for dropout in dropouts
    for bidirectional in bidirectionals
    for name in names]
)
def test_gru_layer_get_method(
    input_size, hidden_size, num_layers,
    bias, batch_first, dropout, bidirectional,name):

        x = GRU(
                input_size=input_size, hidden_size=hidden_size,
                num_layers=num_layers, bias=bias,
                batch_first=batch_first, dropout=dropout,
                bidirectional=bidirectional, name=name)

        prev_dim = (6,1,3)

        if input_size is None:
            x.get_input_dim(prev_dim, "GRU")

        details = x.get_layer()

        assert isinstance(details, dict) == True

        assert details['layer_details'] == num_layers

        assert details['name'] == name

        assert issubclass(details['layer'], _GRU) == True

        assert isinstance(details['keyword_arguments'], dict) == True

        if input_size:
            assert details['keyword_arguments']['input_size'] == input_size
        else:
            assert details['keyword_arguments']['input_size'] == prev_dim[0]

        assert details['keyword_arguments']['hidden_size'] == hidden_size

        assert details['keyword_arguments']['num_layers'] == num_layers

        assert details['keyword_arguments']['hidden_size'] == hidden_size

        assert details['keyword_arguments']['num_layers'] == num_layers

        assert details['keyword_arguments']['bias'] == bias

        assert details['keyword_arguments']['batch_first'] == batch_first

        assert details['keyword_arguments']['dropout'] == dropout

        assert details['keyword_arguments']['bidirectional'] == bidirectional

