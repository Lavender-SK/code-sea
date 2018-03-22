select t1.Name as Employee
from   `Employee` t1
        inner join 
        `Employee` t2 on t2.Id = t1.ManagerId
where  t1.Salary > t2.Salary
;

