-- 1.
SELECT Score, 
       ( SELECT COUNT(DISTINCT Score) 
         FROM   Scores 
         WHERE  Score >= s.Score
       ) as Rank 
FROM   Scores s 
ORDER BY Score DESC;


-- 2.
select t1.Score, 
       @i:= @i + if(@pre!=(@pre:=Score),1,0) as rank
from   Scores as t1, (select @i:=0, @pre:=-1) as t2
order by Score desc
;


