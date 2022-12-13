import cv2

try:
    version = cv2.__version__
    print(f'OpenCv version {version} installed.')
except:
    print('Error loading OpenCv.')