func = lambda x:x%3==0
I=filter(func,range(10))
I=list(I)
print(len(I)+sum(I)+max(I))

"""range дает список от 0 до 10, лямда поставлят все значения по порядку, что бы делилось без
остатка(остаток 0), получаем (list) 0,3,6,9  делее len(4) + sum(18)+ max(9) = 31 """

