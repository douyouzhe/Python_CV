Youzhe Dou

Programming Assignment
1(a)
The threshold value used is 125.

1(c)
The attributes I pick is position, orientation and object roundness.

1(d)
Object roundness is used to detect the objects and the result is satisfying.
The threshold for roundness is 0.03
abs(roundness for current object – roundness for object in database) < 0.03

2(a)
I used 3*3 Sobel mask. It has good localization and easy to implement.
I also tried 5*5 Sobel mask, there is no significant improvement and the localization become worse so I used 3*3 mask. (5*5 code is commented, can try)

2(b)
I choose lowest “appropriate” edge thresh value so that all edges are clear and visible.
Theta is in range from -2/pi to 2/pi, to make the resolution higher, I use 0.5 degree as step size so the column size is 360
Rho is same as the image diagonal length so it is sqrt(640^2+480^2)= 800
For the sake of the following questions, rho is between -400 to 400
Therefore, the accumulator size is 800*360. It is accurate and the program is not too slow.

2(c)
I pick 250 for the first two images and 150 for the last image.
So that appropriate amount of lines is shown and the result is not too messy. 

2(d)
The algorithm I used is:
•	Get the equation of the infinite line from Hough accumulator (same as previous question)
•	Trim the line so that the line is only inside the image (that is the only part we are interested in)
•	Divide the line into 40+ segments
•	In the threshed edged image, make the start point and the end point and check whether that pixel is background. If it is, drop the segment and go to the next one.
•	Repeat the process for all segments in all lines
•	This algorithm perform better when the thresh value for Hough accumulator is lower because most segments will be dropped but none will appear between the squares in the test image.


 
