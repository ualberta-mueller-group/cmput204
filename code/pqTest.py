import pq

q = [(4,'a'), (5, 'b'), (3, 'c')]

print ("Queue", q)
m = pq.deletemin(q)
print ("Deletemin:", m, "Remaining queue", q)
pq.decreasekey(q, 'b', 2)
print ("Decrease key b by 2, resulting queue",q)
m = pq.deletemin(q)
print ("Deletemin:", m, "Remaining queue", q)
m = pq.deletemin(q)
print ("Deletemin:", m, "Remaining queue", q)
