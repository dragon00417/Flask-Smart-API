"""Utility functions for activation function"""

# pylint: disable=too-many-arguments
def get_activation_details(n_inputs, n_nodes, name, layer_type, layer, keyword_arguments):
    """
    	Creates the layer details data for the activation function
    """
    return {
        'n_inputs': n_inputs,
        'n_nodes': n_nodes,
        'name': name,
        'type': layer_type,
        'layer': layer,
        "keyword_arguments": keyword_arguments
    }

def validate_name_field(name):
    """
        A function that validates the name field
    """
    if name is not None:
        if isinstance(name, str):
            if len(name) <= 0:
                raise ValueError("Please provide a valid name")
        else:
            raise ValueError("Please provide a valid name")
