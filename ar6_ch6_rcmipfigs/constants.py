import os
import ar6_ch6_rcmipfigs
BASE_DIR = os.path.dirname(ar6_ch6_rcmipfigs.__file__)
print(BASE_DIR)

INPUT_DATA_DIR = os.path.join(BASE_DIR, 'data_in')#  pathBASE_DIR + ''
OUTPUT_DATA_DIR = os.path.join(BASE_DIR, 'data_postproc')#  pathBASE_DIR + ''
print(INPUT_DATA_DIR)