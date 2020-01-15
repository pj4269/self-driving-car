Finding Lane Lines on the Road


Reflection
1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.
My pipeline consisted of 5 steps. 

First, I converted the images to grayscale. To do that, I've used cvtColor() function. Alternatively I could also use BGR2GRAY had I read an image with cv2.imread(). 

Next, I blurred the image using a Gaussian Noise kernel.

After that, I applied canny edge detection using canny transformation.

Then I drew my region of interest by defining a blank mask to start with. Then I converted the rest of the image to black. 

Finally I applied Hough trnasformation to detect lines in an image.

 As for draw_lines() function, at first I defined it simply as: 
     def draw_lines(img, lines, color=[255, 0, 0], thickness=2):
        for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(img, (x1, y1), (x2, y2), color, thickness)

After that I improved it in order to draw a single line on the left and right lanes, by filtering and processing those lines to determine which belong to the left and right lane lines. Next I use the average slope, the highest point on the image, and the values from the previous frame to draw the lane lines on top of the original image.



2. Identify potential shortcomings with your current pipeline
One potential shortcoming would be what would happen when the slope of the angle changes fast in the event of sudden angle turn. 

Another shortcoming could be draw lines function is at risk of not capturing lines when the width of the lines changes. 

3. Suggest possible improvements to your pipeline

A possible improvement would be to incorporate hyper parameter tuning to find the best possible values. 


