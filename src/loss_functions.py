from keras import backend
from keras.models import load_model
from keras.utils.generic_utils import get_custom_objects
from keras.backend import binary_crossentropy

def jaccard_coef(y_true, y_pred, smooth=1e-12):
    """
    Computes the jaccard coefficient.
    
    """
    
    intersection = backend.sum(y_true * y_pred, axis=[0, -1, -2])
    total = backend.sum(y_true + y_pred, axis=[0, -1, -2])
    
    return backend.mean((intersection + smooth) / (total - intersection + smooth))

def jaccard_coef_int(y_true, y_pred, smooth=1e-12):
    """
    """

    y_pred_pos = backend.round(backend.clip(y_pred, 0, 1))
    intersection = backend.sum(y_true * y_pred_pos, axis=[0, -1, -2])
    total = backend.sum(y_true + y_pred_pos, axis=[0, -1, -2])

    return backend.mean((intersection + smooth) / (total - intersection + smooth))


def jaccard_coef_loss(y_true, y_pred):
    """
    """

    return -backend.log(jaccard_coef(y_true, y_pred)) + binary_crossentropy(y_pred, y_true)