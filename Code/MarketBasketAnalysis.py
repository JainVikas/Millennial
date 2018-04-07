# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 23:14:21 2018

@author: vikas.e.jain
"""
#import libraries as required.
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import matplotlib.pyplot as plt

#dataset used is from UCI ML    

df = pd.read_excel('http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx')
df.head()

#Preprocessing
#we would now need to clean up the data,
#1. remove extra spaces in description
df['Description'] = df['Description'].str.strip()

#2. drop the rows  with no invoices number
df.dropna(axis=0, subset=['InvoiceNo'], inplace=True)

#3. remove returned order which has C in front of order ID
df['InvoiceNo']= df['InvoiceNo'].astype('str')
df = df[~df['InvoiceNo'].str.contains('C')]

# now consolidate all items such that there is 1 transaction per row, index being the invoiceNo, and features be the products
#basket = (df[df['Country']=="France"].groupby(['InvoiceNo', 'Description'])['Quantity'].sum().unstack().reset_index().fillna(0).set_index('InvoiceNo'))
basket = (df[df['Country'] =="France"].pivot_table(index="InvoiceNo", columns="Description", values="Quantity", aggfunc="sum",fill_value=0 ))
len(basket.columns)

#now thatall na's are Zero, we simply have to convert all positive records to one, inorder to proceed with encoding
def encode_units(x):
    if x<= 0:
        return 0
    if x >= 1:
        return 1
    
basket_set = basket.applymap(encode_units)
basket_set.drop("POSTAGE", inplace= True, axis=1)

#now that preprocessing is complete. lets find frequentItemset
frequent_itemsets = apriori(basket_set, min_support = 0.07, use_colnames= True)
# frequent itemset can also be used as recommendation option for a person who doesn't have anything on the list. kind of collaborative filtering. but for new customer with no purchase history.

# final step is to find association rules
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1)
rules.head()

def draw_graph(rules, rules_to_show):
  import networkx as nx  
  G1 = nx.DiGraph()  
  color_map=[]
  N = 50
  colors = np.random.rand(N)    
  strs=['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'R11']      
  for i in range (rules_to_show):      
    G1.add_nodes_from(["R"+str(i)])
    
     
    for a in rules.iloc[i]['antecedants']:
                
        G1.add_nodes_from([a])
        
        G1.add_edge(a, "R"+str(i), color=colors[i] , weight = 2)
       
    for c in rules.iloc[i]['consequents']:
             
            G1.add_nodes_from([c])
            
            G1.add_edge("R"+str(i), c, color=colors[i],  weight=2)
 
  for node in G1:
       found_a_string = False
       for item in strs: 
           if node==item:
                found_a_string = True
       if found_a_string:
            color_map.append('yellow')
       else:
            color_map.append('green')       
  edges = G1.edges()
  colors = [G1[u][v]['color'] for u,v in edges]
  weights = [G1[u][v]['weight'] for u,v in edges]
 
  pos = nx.spring_layout(G1, k=16, scale=1)
  nx.draw(G1, pos, edges=edges, node_color = color_map, edge_color=colors, width=weights, font_size=16, with_labels=False)            
   
  for p in pos:  # raise text positions
           pos[p][1] += 0.07
  nx.draw_networkx_labels(G1, pos)
  plt.show()
  
plt.gcf().clear()
draw_graph (rules, 10)
