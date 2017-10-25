Feature Detection
detect_features.py takes at least one arguement which is the image. it can also take two optional arguments which are nonmaxsupptsRadius and nonmaxsupptsThreshold. Different nonmaxsupptsRadius and nonmaxsupptsThreshold gives different number of features for each image. since we want to match these features, it is better to adjust these parameters so that the number of features from each image pair is roughly the same. if they are not given when the function is called, the default value is 20 and 0.08.

Here are the nonmaxsupptsRadius and nonmaxsupptsThreshold values for each pair I used in the driver function:

bikes1 ↔ bikes2: 
20, 0.1  20, 0.04

bikes1 ↔ bikes3
20, 0.1  20, 0.04

graf1 ↔ graf2
20, 0.01  20, 0.01

graf1 ↔ graf3
20, 0.3  20, 0.3

leuven1 ↔ leuven2
20, 0.1  20, 0.07

leuven1 ↔ leuven3
20, 0.05  20, 0.15

wall1 ↔ wall2
20, 0.27  20, 0.3

wall1 ↔ wall3
20, 0.2  20, 0.15


Feature Match
match_features.py takes two feature lists and two imgaes as input. I implemented another optional argument which is the window size for feature matching. I tried both NCC and SSD for the distance and NCC gives better result. Mutual matches are returned.
The results are good for most pairs except for graf1 ↔ graf3, and walls.
For graf1 ↔ graf3, there is a huge viewing angle difference and therefore many strong features are weakend and the matches are wrong.
For walls, there are too many similiar features and it is hard even for human to distinguish them and match them. therefore the result is bad.



Alignment and Stitching
Using the matched feature pairs from previous question, I am able to align and stitch most pairs successfully. The results for bikes and leuvens are extremely accurate because the feature pairs are accurate. Again, the result for graf1 ↔ graf3, and walls are bad because the feature pairs we used are mostly wrong. graf1 ↔ graf2 generate slightly blur image sometimes. This is because RANSAC is a completely random process, although increasing the number of loop can converege the result, it is a little bit off sometimes. 

bikes1 ↔ bikes2 : perfect, almost 0 outliners
bikes1 ↔ bikes3 : perfect, almost 0 outliners
graf1 ↔ graf2 : good, a few outliners 
graf1 ↔ graf3 : very bad
leuven1 ↔ leuven2 : perfect, 1 or 2 outliners
leuven1 ↔ leuven3 : perfect,, 1 or 2 outliners
wall1 ↔ wall2 : poor
wall1 ↔ wall3 : very bad

One thing to note about the inliner and outliner plot, since I set the threshold of counting inliners extremely strict (x'- x'_from_calculation < 1), there are some inliners marked as outliners (red lines are outliners and blue lines are inliners). 

Projection transformation generally gives better result compared to affine transformation since there are more degree of freedom involved. 

SSIFT:
I implemented this algorithm according to the question. The ratio test part is writen in ratio_test.py for easy usage and it needs to be included to use. 
SSIFT does not use mutual marriage scheme and it tends to give LESS but more accurate pairs since most will be removed during ratio test.

bikes1 ↔ bikes2 : 100% right matches
bikes1 ↔ bikes3 : 100% right matches
graf1 ↔ graf2 : only one wrong match out of 4
graf1 ↔ graf3 : 100% right matches (but only 1 match)
leuven1 ↔ leuven2 : 100% right matches
leuven1 ↔ leuven3 : only one wrong match out of 3
walls: does not work:

using affine model gives much better results since features are matched more accurately.