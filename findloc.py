import cv2 as cv
class find:
    niddle_img=None
    w=0
    h=0
    method=None
    confidence=0.0
    def __init__(self, look_for_img_path, confidence=0.5):
        self.niddle_img = cv.imread(look_for_img_path,cv.IMREAD_UNCHANGED)
        self.w=self.niddle_img.shape[1]
        self.h=self.niddle_img.shape[0]
        self.method=cv.TM_CCOEFF_NORMED
        self.confidence=confidence
    def Img(self,haystack_img):
        result=cv.matchTemplate(haystack_img, self.niddle_img, self.method)
        min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
        if max_val >= self.confidence:
            x,y=max_loc
            center_x = x + self.w/2
            center_y = y + self.h/2
            points=(center_x,center_y)
            return points
        else:
            return 0
        