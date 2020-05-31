"""BCE Loss"""

import torch
from torch.nn import BCEWithLogitsLoss as _BCEWithLogitsLoss

# pylint: disable=too-few-public-methods
class BCELoss:
    """
        Applies a BCE Loss function to the model.

        BCE Loss automatically applies a Sigmoid Layer
        at the end of the model, so there is no need to add
        a Sigmoid layer.

        Supported Arguments
            weight=None : (Numpy Array | List) Manual rescaling of classes
            reduction='mean' : (String) Specifies the reduction
                that is to be applied to the output.
            post_weight=None : (Numpy Array | List) A weight of positive examples
    """
    def __init__(self, weight=None, reduction='mean', pos_weight=None):
        """
            __init__ method for BCELoss

            Supported Arguments
                weight=None : (Numpy Array | List) Manual rescaling of classes
                reduction='mean' : (String) Specifies the reduction
                    that is to be applied to the output.
                post_weight=None : (Numpy Array | List) A weight of positive examples
        """
        if weight is not None and not weight:
            raise ValueError("Invalid weight")

        if not isinstance(reduction, str) and reduction not in ["none", "mean", "sum"]:
            raise ValueError("Invalid reduction")

        if pos_weight is not None and not pos_weight:
            raise ValueError("Invalid pos_weight")

        self.__weight = weight
        self.__reduction = reduction
        self.__pos_weight = pos_weight

    def get_loss_function(self):
        """
            Returns the details of the loss function

            There is no need to call this method as this is used by the
            Sequential model to build the model
        """
        return {
            'loss_function': _BCEWithLogitsLoss,
            'keyword_arguments': {
                # pylint: disable=not-callable
                'weight': torch.tensor(self.__weight).float(),
                'reduction': self.__reduction,
                # pylint: disable=not-callable
                'pos_weight': torch.tensor(self.__pos_weight).float()
            }
        }
