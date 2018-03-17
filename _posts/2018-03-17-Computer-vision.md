---
layout: post
title: "Computer Vision"
author: "Vikas Jain"
categories: deeplearning 
tags: [Machine learning, ML, deeplearning, Deep Learning]
image: computer-vision.jpg
---

# Computer Vision

In the field of AI, computer vision is one of the most important subfield with many others such as Natural language understanding, robotics.

As per Wikipedia, 
> Computer vision is an interdisciplinary field that deals with how computers can be made for gaining high-level understanding from digital images or videos. From the perspective of engineering, it seeks to automate tasks that the human visual system can do.

> Computer vision tasks include methods for acquiring, processing, analyzing and understanding digital images, and extraction of high-dimensional data from the real world in order to produce numerical or symbolic information, e.g., in the forms of decisions. 


## Why is it important you ask?

Think about it, one of the way the five sense that we humans have is sight and so does the most of the species, that is one integral part of our evolution (check [this video](https://youtu.be/vT1JzLTH4G4?t=7m25s) to understand how sight/vision was an important factor in evolution) It is by this sense of sight distinguish objects, and in an instant of time, even with change of place or situation.

For example, you can easily identify between different fruits just by looking at them at the same time you can identify which type of car is it in the picture and just not that you do it so fast it looks so simple to us. and not just that, we are so good at this that by looking at a picture for about only 1 sec, we can identify what is happening in that. 

Example 1: 
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTjIj0nQQc5jzngDpUpgPaaIG5Oh--14R8Cmfh5a49M6arbYM)

Here just by looking at this image, within less than even a sec, you can tell that there are 4 children, 2 are wearing cap, they are playing.

Example 2: ![](https://cdn.pixabay.com/photo/2017/09/16/14/09/children-2755601_960_720.jpg)

The same goes for this pic as well. You can tell that they are in park, 1 boy, 2 girls, 1 girl is walking away, and they are making bubbles during game.

Example 3: ![](http://themediaonline.co.za/wp-content/uploads/2018/01/2010_Malaysian_GP_opening_lap.jpg)

This is my favourite example I guess, just like other if you even look for just 1 sec, you can tell the following things very easily.

1. It is a racing event
2. The car in the front is the car in lead
3. They all are going in same direction
4. If the direction was to be reversed but not car position, the last car in the image will become the lead car.


And to think about it, from the moment you wake up in morning, you interact with world as you see it, you are working as camera recording everything around you, how our brain able to make sense out of all of it?
Try to locate any object in your surroundings, all you are getting as input for your brain to process is ray in different frames and frequencies.

## But, how do we make a computer understand all this?

When you look at an image your brain receives rays of light as input and process that information to make sense, the same way when a computer looks at an image all it receives pixel value associated with that

And this is a challenging problem, because given that everything remains same, even you change the angle on camera those values will change quite rapidly and in near world scenario not only the camera angle but light, colours and many other factors makes it even hard to build a generalized system.

some of the challenges are listed below:
* Illumination: Different lighting condition will change the pixel values.
* Deformation: What if something is broken, you can still identify a broken car to be a car.
* Occlusion: In case you can't see the whole object, say you saw a fin while swimming in ocean, you didn't see any shark, but you still identify the shark and run away from there.
* Background clutter: We can still do a pretty good job, even if the object in discussion is somewhat mixed up with background.
* Intraclass variation: Are you buying a chair? Not all chairs are same though.

## Solutions
If you are following the news, you know that despite these challenges in some limited situation the current technology outperforms human and takes very less time once we have trained a system.

### Rule based
Studies in the 1970s formed the early foundations for many of the computer vision algorithms that exist today, including extraction of edges from images, labelling of lines etc. Later we saw more rigorous mathematical analysis and quantitative aspects in this field some of the concept included which paved path to extract rules which identify these objects. And while this method works sometime the main disadvantage of this is  for another object, you must start all over again.

To overcome that we must think of a more suitable and generalized approach which can be scaled to any object category.
And here enter the Machine learning methods to do this which instead of depending on these abstract rules to identify object is dependent on the data. 

### Data Driven

A very basic pipeline for this task will look as follows.
1. Collect dataset of images and labels
2. Use Machine learning to train a classifier
3. Evaluate trained classifier using new images.

### How does this work, you ask?
We will be exploring both a simple method and deep learning as well.

##### Using K-NN 
K- nearest neighbour algorithms which can easily be understand by "you become who you surround yourself with". let's take the example and we will come back to this.

Let say you have 10 images of 2 classes, one has you in the picture and in other picture you are missing, this is your training data. And we decide that to classify any image to either of that classes we need at least 3 images of same class near to test image to assign that class to test image.

So basically, you model will learn all the data (store all the image files) during training file and during prediction it will check the distance between test image with respect to each image in training set and store the distance to check what are the 3 nearest i.e. least distance images labels to the test image and classify it accordingly.
But how to we find the distance between images, well this is just a heuristic here I consider that we do an absolute difference of pixel by pixel value and sum it to get a distance.

Please note: K-NN is not the only method, there are other algorithms as well, e.g. SVM classification, Linear classification etc.

#### Using Deep Learning
In the recent few years, we have seen a boom of many Deep Learning networks, convolutional networks in case of computer vision. The most important advancement has happened in 2012 in [ImageNet challenge](http://www.image-net.org/challenges/LSVRC/).

![](https://cdn-images-1.medium.com/max/624/1*bGTawFxQwzc5yV1_szDrwQ.png)

In starting 2010, the error rate was about 28% but in 2012 Alex [Krizhevsky, Geoff Hinton, and Ilya Sutskever won ImageNet and introduced Convolutional Neural Networks(CNNs)](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks) to the whole world by achieving a 16% error rate (almost 40% drop)

The one that won ImageNet wasn't very different from what 
professor [Yann LeCun](http://yann.lecun.com/) had introduced in 1980 by successfully applying [Gradient based learning for document classification](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf), it was only more deeper and faster (thanks to Moore's law).


To read more about CNNs, check out the following resources.

1. [A Beginner's Guide To Understanding Convolutional Neural Networks](https://adeshpande3.github.io/adeshpande3.github.io/A-Beginner's-Guide-To-Understanding-Convolutional-Neural-Networks/)
2. [Convolutional Neural Networks](https://www.youtube.com/watch?v=bNb2fEVKeEo)

If you are interested in Computer vision using Deep Learning check out Stanford's Course [Convolutional Neural Networks for Visual Recognition](http://cs231n.stanford.edu/)

Next post: How to build a CNN network using Keras?

Note: All images are accessed through google search to use in this blog, in case of any copyright issue, do let me know so that image can be replaced, and blog can be updated accordingly.
