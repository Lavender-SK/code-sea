select t1.Email
from ( select Email, count(*) as cnt
       from   Person
       group by Email
       having cnt >= 2
     ) t1 
;


