import pyautogui as auto
import cv2 as cv
import numpy as np
class find:
    def findImg(self, main_img_path, look_for_img_path, confidence=0.5, debu_mode=None):
        haystack_img = cv.imread(main_img_path,cv.IMREAD_UNCHANGED)
        niddle_img = cv.imread(look_for_img_path,cv.IMREAD_UNCHANGED)
        niddle_w=niddle_img.shape[1]
        niddle_h=niddle_img.shape[0]
        method=cv.TM_CCOEFF_NORMED
        result=cv.matchTemplate(haystack_img,niddle_img,method)
        min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
        locations=np.where(result>=confidence)
        locations=list(zip(*locations[::-1]))
        rectangles=[]
        for loc in locations:
            rect=[int(loc[0]),int(loc[1]),niddle_w,niddle_h]
            rectangles.append(rect)
            rectangles.append(rect)
        rectangles, weights = cv.groupRectangles(rectangles,2,0.5)
        points=[]
        if len(rectangles):
            line_type = cv.LINE_4
            line_color = (0,255,0)
            marker_color = (255,0,0)
            marker_type = cv.MARKER_CROSS
            for (x,y,w,h) in rectangles:
                center_x = x + int(w/2)
                center_y = y + int(h/2)
                points.append((center_x,center_y))
                if debu_mode == 'rectangles':
                    top_left = (x,y)
                    bottom_right = (x+w,y+h)
                    cv.rectangle(haystack_img,top_left,bottom_right,line_color,line_type)
                elif debu_mode == 'points':
                    cv.drawMarker(haystack_img,(center_x,center_y),marker_color,marker_type)
            if debu_mode:
                cv.imshow('Matches',haystack_img)
                cv.waitKey()
        return points #returns all positive locations
    # point=findImg('ss.png','win.png')
    # print(point)
    # for p in point:
    #     auto.moveTo(p,None,1)