import cv2


class FaceDetector(object):
    def __init__(self, face_cascade_path):
        """
        Class constructor.
        :param face_cascade_path: Path to the XML file with the parameters used by OpenCV's underlying implementation
        of Haar Cascades.
        """
        self.face_cascade = cv2.CascadeClassifier(face_cascade_path)

    def detect(self, image, scale_factor=1.1, min_neighbors=5, min_size=(30, 3)):
        """
        Performs a detection on an input image. The results will vary depending on the input parameters configuration.
        :param image: Image to detect a face.
        :param scale_factor: How much the image will be reduced in each scale. This value helps create a scale pyramid
        in order to detect faces of different sizes (for instance, a face closer to the camera lens will occupy more
        space in the image than the face of a person in the background). Therefore, for example, a value 1.05 means
        we’ll reduce the image size by 5% on each level of the pyramid
        :param min_neighbors: Minimum of neighbors used to consider a rectangle or region a face.
        :param min_size: A tuple of width and height (expressed in pixels) that establishes the minimum size a window
        must have to be taken into consideration. Windows that fail this size test will be discarded.
        :return: A list of rectangles of possible detections.
        """
        rectangles = self.face_cascade.detectMultiScale(image, scaleFactor=scale_factor, minNeighbors=min_neighbors,
                                                        minSize=min_size, flags=cv2.CASCADE_SCALE_IMAGE)

        return rectangles
