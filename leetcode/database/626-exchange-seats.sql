select if(id%2=0,id-1,if(id!=max_id,id+1,id)) as id, student
from   ( select id, student, (select max(id) from seat) as max_id
         from   seat
	   ) t1
order by id asc
;
