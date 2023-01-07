import cv2

class Region :
    def __init__(self):
        self.childrem = []
        self.validity = False
        self.roi = Rectange(0,0,0,0)#(x,y,w,h)
        self.m = None
        self.label = 0
        
class Rectange :
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.xf = x+w
        self.yf = y+h

    def overlap_x (self,other):
        if self.xf <= other.x: return False 
        if other.xf <= self.x: return False
        return True

    def overlap_y (self,other):
        if self.yf <= other.y: return False 
        if other.yf <= self.y: return False
        return True

    def intercept (self,other):
        ox = self.overlap_x(other)
        oy = self.overlap_y(other)
        
        if not (ox and oy):return None
        
        x0 = max(self.x, other.x)
        xf = min(other.xf, self.xf)

        y0 = max(self.y, other.y)
        yf = min(other.yf, self.yf)

        return Rectange(x0, y0,  xf - x0, yf - y0) 
    def combine (self,other):
        x0 = min(self.x, other.x)
        xf = max(other.xf, self.xf)

        y0 = min(self.y, other.y)
        yf = max(other.yf, self.yf)
        return Rectange(x0, y0,  xf - x0, yf - y0) 


def segmentacion(grises):
    _,th =  cv2.threshold(grises, 150, 255, cv2.THRESH_BINARY_INV)

    cnts,_ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return cnts

def split (img,roi,predicate):
    r = Region()
    r.roi = roi
    r.m = src
    r.validity = True

    b = predicate(src)

    if b:
        mean = np.mean(src)
        #  std = np.std(src)
        r.label = mean
    else:
        h,w = img.shape
        h //=2
        w //=2
        r1 = split(img[0:w,0:h], Rectange(roi[0]  ,roi[1]  ,w,h), predicate)
        r2 = split(img[w: ,0:h], Rectange(roi[0]+w,roi[1]  ,w,h), predicate)
        r3 = split(img[0:w,h: ], Rectange(roi[0]  ,roi[1]+h,w,h), predicate)
        r4 = split(img[w: ,h: ], Rectange(roi[0]+w,roi[1]+h,w,h), predicate)

        r.childrem = [r1,r2,r3,r4]
    return r;


def merge_two_region(parent,img,r1:Region,r2:Region,predicate):
    r_inter:Rectange = r1.roi.combine(r2.roi)
    if predicate(img[r_inter.x : r_inter.xf,r_inter.y:r_inter.yf]):
        r1.roi  = r_inter
        r2.validity = False
        return True

    return False
def merge():pass

if __name__ == "__main__":
    r1 = Rectange(0,0,20,20)
    r2 = Rectange(3,3,30,30)
    print(r1.intercept(r2).__dict__)
