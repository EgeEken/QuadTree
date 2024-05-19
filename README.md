# QuadTree
QuadTree Image Compression algorithm

I got the idea for this in the shower, and then i looked into it to find out that quadtrees were invented in 1974 by Raphael Finkel and J.L. Bentley, and the idea of using them in image compression dates back to at least 1992 with [this paper](https://users.cs.duke.edu/~reif/paper/markas/pub.quad.pdf) from Tassos Markas and John Reif. 

I decided to code it as a quick little project anyways, here is a video of the web interface i made that uses this algorithm:

https://github.com/EgeEken/QuadTree/assets/96302110/41600c5d-175f-452f-8045-38e243138c26


The base version of this algorithm calculates loss based on the average color of the section, which is what i've seen in all the applications of this for image processing. But i thought of 2 main variants, so i'll explain them here:

## Max

This variant calculates loss based on the most different pixel from the average, rather than the average distance from the average like in the default "mean" version.

This verifies that if a section that passes a threshold check, every single pixel in that section is below the threshold, which prevents stuff like this from happening:

![image](https://github.com/EgeEken/QuadTree/assets/96302110/cc1779cb-ddd9-499d-b9bb-9cfd18ff718e)

## This variant overall retains more information for the same amount of size compression

![image](https://github.com/EgeEken/QuadTree/assets/96302110/a908f46a-7342-4544-bbc7-553693ab838c)


## Percentile

This variant calculates loss based on what percentage of the pixels in a given section fall below the threshold.

This can be helpful in images with a lot of noise, it would in theory prevent cases where the max variant of the algorithm would spend too much depth on parts of the image that aren't actually important but have a few pixels of random noise. But in practice, it ends up losing more time to calculating percentiles than it does gaining from depth, and just ends up being a worse version of mean in most cases.


# More results

https://github.com/EgeEken/QuadTree/assets/96302110/4f887e67-d3e3-43b6-9375-cd9f37d2a9d9


