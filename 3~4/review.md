RGB, BGR, HSV
===============
**RGB**   
- Red, green, and blue, the three primary colors of light, are used as basic colors.   
   빛의 삼원색인 빨간색, 초록색, 파란색을 기본 색으로 사용한다.    
- PIL (RGB)
---
**BGR**   
- BLue, Green,Red   
-  OpenCV (BGR)   
if you want to change BGR->RGB in OpenCV
<pre>
<code>
new_image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
</code>
</pre>   
---
**HSV**
- Hue (color, 색상, range: 0~ 179)   
- Saturation (채도, range: 0 ~ 255)   
- Value (brightness, 명도, range: 0 ~ 255)    
---
ThreHold
=========
