---
layout: post
title: "Types of Machine Learning"
author: "Vikas Jain"
categories: ML
tags: [Machine learning, ML]
image: machine-learning.jpg
---

In last post we talked about what is machine learning? And as mentioned in this post we will be talking about different types of Machine learning.

There are 3 types of Machine learning:
  1. supervised learning
  2. unsupervised learning
  3. Reinforcement learning

## Supervised learning

In supervised learning we have labelled data set. for example, let's say you have been given the task to sort the coins that you have. Now since each of the coin is labelled you can understand that a coin of 1 rupees is smaller in size than that of 2 and similarly the design pattern is different too and while 1 and 5 rupees coins roughly has same size the width of 5 rupees coin is more. So, you learn about these features based on the observation that you made during initial sorting of these coins. now if I had to give you a coin and ask whether it is 1,2 or 5 without looking at the labels you can easily do that.

Same process goes when you have to decide whether a fruit is Orange or apple, from our past experiences in our childhood we all have learnt that oranges are orange is colour and have a bumpy texture on outer layer and are squishy while at the same time an apple has red colour (generally, there are different type of apples too, we are talking about red apples), the outer layer skin is quite smooth and they are quit firm compared to oranges.


## Unsupervised learning

Now we noticed how supervised learning worked, but think for a moment, if those coins were not labelled when you were initially sorting them and learning about their features, would you still be able to sort them out with correct labels (note: this is considering you have no prior knowledge on how 1,2 or 5 rupees coin looks or what is it size, as a system you have ever seen them). Or lets you have never seen apples or oranges and I give you a bucket full of both, would you be able to identify which one is apple or orange.
Possibly not, but you would certainly be able to divide them into 2 groups in case of fruits and in 3 groups for coins by looking at their features, while we still don't know whether group 1 is orange or not. we can see that the machine is able to learn the features and divide them in separate groups without any supervision or labelled dataset.

## Reinforcement Learning
Reinforcement learning is how we learn from our experiences, where we act in an environment and receive rewards or punishments based on our actions which helps us to determine what should we do.
Let's say you have a dog and if you have one you know how you train him to shake hands or do a roll. Every time you ask dog to do something you give him a treat as reward which suggest that what he did was correct and helps him determine that he should do the roll when you say "roll". Now what if your dog does a roll when you ask him to sit, you won't give him punishment, I mean who punishes pet, but you certainly won't give him that treat right which sends a signal to him that what he did what in fact not correct and he should not be doing roll when you asked him to sit and he will try different actions and when he will sit on your command you will give him a treat which will do the same effect and will help him determine the right action for right words.
Even we learn the same way, that maths test results tell you whether you need to focus more, or your level is competence enough. Or think about it, do we behave the same way in public as we do in our house, why?

In next part we will explore each of these in more details.
