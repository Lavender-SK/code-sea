select distinct(t1.Num) as ConsecutiveNums
from   ( select t.Num, 
	            if (@pre=(@pre:=Num),@i:=@i+1,@i:=1) as cc
		 from   Logs as t, (select @i:=1, @pre:=-1) as cnt
	   ) t1
where  t1.cc >= 3
;

