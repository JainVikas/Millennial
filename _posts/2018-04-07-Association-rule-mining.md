---
layout: post
title: "Associative Rule Mining/ Frequent Patterns Mining"
author: "Vikas Jain"
categories: deeplearning 
tags: [Machine learning, ML, deeplearning, Deep Learning]
image: cuba-4.jpg
---




A rule based Machine learning technique to find the associativeness of one variable with other and also which variables occurs more frequently compared to other.


## Steps 

* Find frequent Itemset, 
* Prune the Itemset based on minimum support threshold.
* Find support for each itemset i.e. support of all element, support is defined as percentage of records which contains the itemset in whole data. 
* Find confidence for itemset, it is defined as percentage of records which contains the single itemset as well as both itemset as a combination.

In the end we select the rule with high support and confidence value. However, note that there other methods as well which can be  utilized in combination with support and confidence. You can check those [here.](https://en.wikipedia.org/wiki/Association_rule_learning#Useful_Concepts)

## Let's try these step on an example 
```
order 1: apple, egg, milk  
order 2: carrot, milk  
order 3: apple, egg, carrot
order 4: apple, egg
order 5: apple, carrot


Iteration 1:  Count the number of times each item occurs   
itemset      occurrence count    
{apple}              4   
{egg}                3   
{milk}               2   
{carrot}             2   

{milk} and {carrot} are eliminated because they do not meet the minimum occurrence threshold.

Iteration 2: Build item sets of size 2 using the remaining items from Iteration 1 
             (ie: apple, egg)  
itemset           occurencecount  
{apple, egg}             3  

Only {apple, egg} remains and the algorithm stops since there are no more items to add.
```

## Key metrics in Associative rule minning

There are 3 key Metrics to consider while evaluating association rules

1. <strong>Support:</strong>
	As mentioned earlier it is defined as the percentage of orders contains the itemset
    ```
    Support{A} = count(A)/count(total orders)
    
    ```
2. <strong>Confidence:</strong>
	This is defined as percentage of time a 2nd item is bought, given the 1st item is purchased. Note that the confidence value varies based on association direction, i.e. whether it is purchasing B given A is already purchased (A->B), or it is A give B is bought already (B->A).
    ```
    confidence{A->B} = support{A,B}/ support{A}
    confidence{B->A} = support{A,B}/ support{B}
    ```
3. <strong>Lift:</strong>
	Given items A and B, Lift indicates whether there is a relationship between the occurence of those items or it is simply by chance that they occured together(i.e. Random). And unlike *Confidence* which depends on the direction of the rule, *Lift* has no direction.
    
    ```
    Lift{A,B} = support{A,B}/ support{A}*support{B}
    Lift{B,A} = support{A,B}/ support{A}*support{B}
	
    How do you interpret Lift?
    Lift = 1, implies no relationship between A and B
    (i.e. A and B occur together by random)
    
	Lift > 1, implies a positive relationship between them,
    (i.e. A and B occur together more often than random)
    
    Lift < 1, implies a negative relationship between them,
    (i.e. A and B occur together less often than random)
    
    ```

## Applications
* [Market basket Analysis](https://towardsdatascience.com/a-gentle-introduction-on-market-basket-analysis-association-rules-fa4b986a40ce)
* [Topic identification/Text classification using Co-Occurence of words](https://pdfs.semanticscholar.org/b416/449c127997a688c5642363737fdda4dfc0fe.pdf)
* [Palagiarism Detection](http://research.ijais.org/volume5/number2/ijais12-450846.pdf)
* [BioMarkers- Gene/proteins vs disease](https://c-path.org/wp-content/uploads/2013/05/camd_biomarkers_israel_may_2013.pdf)
* [Time series Analysis](https://pdfs.semanticscholar.org/4fec/01de28a635ac0bb440b31545203f93483e78.pdf)


## Python Implentation

You can find the python implementation for the same on here on [github](https://github.com/JainVikas/Studyml/blob/gh-pages/Code/MarketBasketAnalysis.py)