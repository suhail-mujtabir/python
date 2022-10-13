import cv2 as cv
import pyautogui as auto
import numpy as np
def points(niddle_img, confidence=0.5, region=None):
    screenshot = auto.screenshot()
    screenshot = np.array(screenshot)
    haystack_img = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
    if region:
        haystack_img = haystack_img[region[1]:region[1]+region[3],region[0]:region[0]+region[2]]
    else :
        region = (0, 0)                           
    niddle_img = cv.imread(niddle_img, cv.IMREAD_UNCHANGED)

    w = niddle_img.shape[1]
    h = niddle_img.shape[0]

    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(haystack_img, niddle_img, method)
    min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)
    if max_val >= confidence:
        x, y = max_loc
        center_x = region[0] + x + w/2
        center_y = region[1] + y + h/2
        points=(center_x, center_y)
        return points
    else:
        return 0