import cv2


def resize(fp: str, scale: Union[float, int]) -> np.ndarray:
    """ Resize an image maintaining its proportions

    Args:
        fp (str): Path argument to image file
        scale (Union[float, int]): Percent as whole number of original image. eg. 53

    Returns:
        image (np.ndarray): Scaled image
    """
    def _scale(dim, s): return int(dim * s / 100)
    im: np.ndarray = cv2.imread(fp)
    width, height, channels = im.shape
    new_width: int = _scale(width, scale)
    new_height: int = _scale(height, scale)
    new_dim: tuple = (new_width, new_height)
    return cv2.resize(src=im, dsize=new_dim, interpolation=cv2.INTER_LINEAR)
