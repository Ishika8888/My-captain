#!/usr/bin/env python
# coding: utf-8

# In[ ]:


E= {100, 500, 750, 400, 850, 900, 390}
N= {500, 850, 320, 100, 520, 900, 700}

print(E.union(N))
print(E.intersection(N))
print(E.difference(N))
print(E.symmetric_difference(N))

