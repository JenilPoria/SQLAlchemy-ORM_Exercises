from sem3sqlalchemy import Customer, Orders, Salesperson, engine, Base
from newentries import session
from sqlalchemy import create_engine, Integer, String, Column, ForeignKey, Float, Date, update, insert, delete, select, or_, and_,Table, inspect, func,desc, any_,not_, case, literal
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Mapped, mapped_column, aliased
from datetime import date
from sqlalchemy import tuple_,text
from sqlalchemy.sql.expression import true

Base.metadata.create_all(engine)



## 1st question -- "SELECT * from "order";"
# select_statment = select(Salesperson.snum,Salesperson.sname,Salesperson.city, Salesperson.comm)
# select_statment = select(Salesperson)

# result = session.execute(select_statment)
# for i in result.scalars():
#     print(i)


## 2nd question --  select  Distinct snum from "order";

# select_statment = select(Orders.snum).distinct()
# result = session.execute(select_statment)
# for i in result.scalars():
#     print(i)

## 3rd question -- select sname, comm from salespeople where city = "London";

# select_statment = select(Salesperson.sname, Salesperson.comm).where(Salesperson.city == "London")
# result = session.execute(select_statment)
# for i in result.all():
#     print(i)

## 4th question -- select * from customer where rating = 100;

# select_statment = select(Customer).where(Customer.rating == 100)
# result = session.execute(select_statment)
# for i in result.scalars().all():
#     print(i)

## 5th question -- select onum, amount, odate from "order";

# select_statement = select(Orders.onum, Orders.amount, Orders.odate)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 6th question -- select * from customer where city = "San Jose" and rating > 200;

# select_statement = select(Customer).where(Customer.city == "San Jose" and Customer.rating > 200)
# result = session.execute(select_statement)
# for i in result.scalars().all():
#     print(i)

## 7th question -- select * from customer where city = "San Jose" or rating > 200;

# select_statement = select(Customer).where(Customer.city == "San Jose" or Customer.rating > 200)
# result = session.execute(select_statement)
# for i in result.scalars().all():
#     print(i)

## 8th question -- select * from "order" where amount > 1000;

# select_statement = select(Orders).where(Orders.amount > 1000)
# result = session.execute(select_statement)
# for i in result.scalars().all():
#     print(i)

## 9th question -- select sname, city from salespeople where city = "London" and comm > 0.10;

# select_statement = select(Salesperson.sname, Salesperson.city).where(Salesperson.city == "London" and Salesperson.comm > 0.10)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 10th question --  select * from customer where rating > 100 or city = "Rome";

# select_statement = select(Customer).where(or_(Customer.rating > 100, Customer.city == "Rome"))
# result = session.execute(select_statement)
# for i in result.scalars().all():
#     print(i)

## 11th question --  select * from salespeople where city = "Barcelona" or city = "London";

# select_statement = select(Salesperson).where(or_(Salesperson.city == "Barcelona", Salesperson.city == "London"))
# result = session.execute(select_statement)
# for i in result.scalars().all():
#     print(i)

## 12th question --  select * from salespeople where comm > 0.10 and comm < 0.12;

# select_statement = select(Salesperson).where(and_(Salesperson.comm > 0.10, Salesperson.comm < 0.12))
# result = session.execute(select_statement)
# for i in result.scalars().all():
#     print(i)

## 13th question -- select * from customer where city = NULL;

# select_statement = select(Customer).where(Customer.city == None)
# result = session.execute(select_statement)
# for i in result.scalars().all():
#     print(i)


## 14th question -- select * from "order"where odate = '2016-03-10' or odate = '2016-04-10';

# select_statement = select(Orders).where(or_(Orders.odate == date(2016, 3 ,10), Orders.odate == date(2016, 4, 10)))
# result = session.execute(select_statement)
# for i in result.scalars().all():
#     print(i)

## 15th question -- sqlite> select * from customer where snum in  (select snum from salespeople where sname = "Peel" or sname = "Motika");

# 1st way
# select_statement = select(Customer).where(Customer.snum.in_(select(Salesperson.snum).where(or_(Salesperson.sname == "Peel", Salesperson.sname == "Motika"))))

# 2nd way
# select_statement = select(Customer).where(Customer.snum.in_(select(Salesperson.snum).where(Salesperson.sname.in_(["Peel", "Motika"]))))


# result = session.execute(select_statement)
# for i in result.scalars().all():
#     print(i)


## 16th question -- select * from customer where cname like 'G%' or cname like 'H%';

# select_statement = select(Customer).where(or_(Customer.cname.like("G%"), Customer.cname.like("H%")))
# result = session.execute(select_statement)
# for i in result.scalars().all():
#     print(i)

## 17th question -- select * from "order" where amount = 0 or amount = NULL;

# select_statement = select(Orders).where(or_(Orders.amount == 0, Orders.amount == None))
# result = session.execute(select_statement)
# for i in result.scalars().all():
#     print(i)

## 18th question -- select count(distinct snum) from "order";

# select_statement = select(func.count(func.distinct(Orders.snum)))
# result = session.execute(select_statement)
# for i in result.scalars().all():
#     print(i)


## 19th question -- select odate, snum, max(amount) from "order" group by odate, snum order by odate, snum;

# select_statement = select(Orders.odate, Orders.snum, func.max(Orders.amount)).group_by(Orders.odate, Orders.snum).order_by(Orders.odate, Orders.snum)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 20th question --  select odate, snum, max(amount) from "order" where amount > 5000 group by odate, snum order by odate, snum;

# select_statement = select(Orders.odate, Orders.snum, func.max(Orders.amount)).where(Orders.amount > 5000).group_by(Orders.odate, Orders.snum).order_by(Orders.odate, Orders.snum)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 21th question -- select odate, sum(amount) as total_Amount from "order" group by odate order by total_Amount desc limit 1;
 
# select_statement = select(Orders.odate, func.sum(Orders.amount).label("total_Amount")).group_by(Orders.odate).order_by(desc("total_Amount")).limit(1)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 22th question -- select count(*) from "order"  where odate = '2016-03-10';

# select_statement = select(func.count(Orders.onum)).where(Orders.odate == date(2016, 3, 10))
# result = session.execute(select_statement)
# for i in result.scalars().all():
#     print(i)

## 23th question --  select count(distinct city) from customer;

# select_statement = select(func.count(func.distinct(Customer.city)))
# result  = session.execute(select_statement)
# for i in result.scalars().all():
#     print(i)

## 24th question -- select cnum, min(amount) from "order" group  by cnum;

# select_statement = select(Orders.cnum, func.min(Orders.amount)).group_by(Orders.cnum)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 25th question --  select * from customer where cname like 'G%' order by cname asc limit 1;

# select_statement = select(Customer).where(Customer.cname.like("G%")).order_by(Customer.cname.asc()).limit(1)
# result = session.execute(select_statement)
# for i in result.scalars().all():
#     print(i)

## 26th question -- select 'For ' || odate || ', there are ' || count(onum) || ' orders' from "order" group by odate;

# select_statement = select(Orders.odate, func.count(Orders.onum)).group_by(Orders.odate)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 27th question -- select onum, snum, amount, amount*0.12 from "order" order by snum; 

# select_statement = select(Orders.onum, Orders.snum, Orders.amount, Orders.amount*0.12).order_by(Orders.snum)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 28th question --  select 'For the city ' || city || ', the highest rating is ' ||  max(rating) from customer group by city;    

# select_statement = select(Customer.city, func.max(Customer.rating)).group_by(Customer.city)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 29th question -- select odate, sum(amount) as total_amount from "order" group by odate order by total_amount desc;

# select_statement = select(Orders.odate,func.sum(Orders.amount).label("total_amount")).group_by(Orders.odate).order_by(desc("total_amount"))
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 30th question --  select cname, sname from salespeople, customer where salespeople.city = customer.city; 

# select_statement = select(Customer.cname, Salesperson.sname).join(Salesperson,Customer.city == Salesperson.city)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 31st question -- select cname, sname from customer, salespeople where customer.snum = salespeople.snum;

# select_statement = select(Customer.cname, Salesperson.sname).join(Salesperson, Customer.snum == Salesperson.snum)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 32nd question -- select onum, cname from "order", customer where "order".cnum = customer.cnum;

# select_statement = select(Orders.onum, Customer.cname).join(Customer, Orders.cnum == Customer.cnum)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 33rd question -- select onum, cname, sname from "order", customer, salespeople where "order".cnum = customer.cnum and "order".snum = salespeople.snum;

# select_statement = select(Orders.onum, Customer.cname, Salesperson.sname).join(Customer, Orders.cnum == Customer.cnum).join(Salesperson, Orders.snum == Salesperson.snum)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 34th question -- select cname, sname, comm  from customer, salespeople where customer.snum = salespeople.snum and salespeople.comm > 0.12;

# select_statement = select(Customer.cname, Salesperson.sname, Salesperson.comm).join(Salesperson, Customer.snum == Salesperson.snum).where(Salesperson.comm > 0.12)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 35th question --  select sname, amount*comm, rating  from salespeople join "order" on salespeople.snum = "order".snum join "customer" on salespeople.snum = customer.snum where customer.rating > 100;

# select_statement = select(Salesperson.sname, Orders.amount*Salesperson.comm, Customer.rating).join(Orders, Salesperson.snum == Orders.snum).join(Customer, Salesperson.snum == Customer.snum).where(Customer.rating > 100)
# result = session.execute(select_statement)
# for i in result:        
#     print(i)

## 36th question -- select a.cname, b.cname, a.rating from customer a join customer b on a.rating = b.rating and a.cnum != b.cnum;

# a = aliased(Customer)
# b = aliased(Customer)
# select_statement = select(a.cname, b.cname, a.rating).join(b, and_(a.rating == b.rating, a.cnum != b.cnum))
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 37th question -- select a.cname, b.cname, a.rating from customer a join customer b on a.rating = b.rating and a.cnum < b.cnum;

# a = aliased(Customer)
# b = aliased(Customer)
# select_statement = select(a.cname, b.cname, a.rating).join(b, and_(a.rating == b.rating, a.cnum < b.cnum))
# result = session.execute(select_statement)
# for i in result:
#     print(i)   

## 38th question --

# s1 = aliased(Salesperson)
# s2 = aliased(Salesperson)
# s3 = aliased(Salesperson)

# Query: cross join salespeople 3 times with customer


# query = select(
#     Customer.cname.label("customer"),
#     s1.sname.label("salesperson1"),
#     s2.sname.label("salesperson2"),
#     s3.sname.label("salesperson3")
# ).select_from(
#     Customer
# ).join(s1, true()).join(s2, true()).join(s3, true())

# result = session.execute(query)
# for row in result:
#     print(row)


## 39th question -- select cname from customer where customer.city in (select c.city from customer c join salespeople s on c.snum = s.snum where s.sname = "Serres");

# select_statement = select(Customer.cname).where(Customer.city.in_(select(Customer.city).join(Salesperson, Customer.snum == Salesperson.snum).where(Salesperson.sname == "Serres")))
# result = session.execute(select_statement)
# for i in result.scalars().all():
#     print(i) 

## 40th question -- SELECT c1.cname AS customer1, c2.cname AS customer2, c1.snum AS salesperson FROM customer c1 JOIN customer c2 ON c1.snum = c2.snum AND c1.cnum < c2.cnum;

# a = aliased(Customer)
# b = aliased(Customer)
# select_statement = select(a.cname.label("customer1"), b.cname.label("customer2"), a.snum.label("salesperson")).join(b, and_(a.snum == b.snum, a.cnum < b.cnum))
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 41th question --  select s1.sname, s2.sname, s1.city from salespeople s1 join salespeople s2 on s1.city = s2.city where s1.snum < s2.snum;

# s1 = aliased(Salesperson)
# s2 = aliased(Salesperson)
# select_statement = select(s1.sname, s2.sname, s1.city).join(s2, s1.city == s2.city).where(s1.snum < s2.snum)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 42th question --  select c.cname, o1.onum, o2.onum from customer c join "order" o1 on c.cnum = o1.cnum join "order"  o2 on c.cnum = o2.cnum where o1.onum < o2.onum order by c.cname, o1.onum, o2.onum; 

# c = aliased(Customer)
# o1 = aliased(Orders)
# o2 = aliased(Orders)
# select_statement = select(c.cname, o1.onum, o2.onum).join(o1, c.cnum == o1.cnum).join(o2, c.cnum ==o2.cnum).where(o1.onum < o2.onum).order_by(c.cname,o1.onum,o2.onum)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 43th question -- select cname, city from customer where rating = (select rating from customer where cname = "Hoffman");

# select_statement = select(Customer.cname,Customer.city).where(Customer.rating == (select(Customer.rating).where(Customer.cname=="Hoffman")))
# result = session.execute(select_statement)
# for i in result:
#     print(i)


## 44th question -- select * from "order" where snum = (select snum from salespeople where sname = "Motika"); 

# select_statement = select(Orders).where(Orders.snum == (select(Salesperson.snum).where(Salesperson.sname =="Motika").scalar_subquery()))
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)


## 45th question -- select * from "order" where snum = (select snum from customer where cname = "Hoffman");

# select_statement = select(Orders).where(Orders.snum == (select(Customer.snum).where(Customer.cname == "Hoffman")))
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 46th question -- select * from "order" where amount > (select avg(amount) from "order" where odate = '2016-04-10');

# select_statement = select(Orders).where(Orders.amount > (select(func.avg(Orders.amount)).where(Orders.odate == date(2016, 4, 10))))
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 47th question -- select avg(comm) from salespeople where city = "London";

# select_statement = select(func.avg(Salesperson.comm)).where(Salesperson.city == "London")
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 48th question -- select * from "order" where snum in (select snum from salespeople where city = "London");

# select_statement = select(Orders).where(Orders.snum.in_(select(Salesperson.snum).where(Salesperson.city == "London")))
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 49th question --  select comm from salespeople where snum in (select snum from customer where city = "London");

# select_statement = select(Salesperson.comm).where(Salesperson.snum.in_(select(Customer.snum).where(Customer.city == "London")))
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 50th question -- select * from customer where cnum  = (select snum + 1000 from salespeople where sname = "Serres");

# select_statement = select(Customer).where(Customer.cnum == (select(Salesperson.snum + 1000).where(Salesperson.sname == "Serres")).scalar_subquery())
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 51th question -- select count(cnum) from customer where rating > (select avg(rating) from customer where city = "San Jose");

# select_statement = select(func.count(Customer.cnum)).where(Customer.rating > (select(func.avg(Customer.rating)).where(Customer.city == "San Jose")).scalar_subquery())
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 52th question -- select * from "order" where cnum = (select cnum from customer where cname = "Cisnerous");

# select_statement = select(Orders).where(Orders.cnum == (select(Customer.cnum).where(Customer.cname == "Cisnerous")).scalar_subquery())
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 53th question --  select cname, rating from customer where cnum in (select cnum from "order" where amount > (select avg(amount) from "order"));

# sub_subquery = select(func.avg(Orders.amount)).scalar_subquery()
# sub_query = select(Orders.cnum).where(Orders.amount > sub_subquery)
# select_statement = select(Customer.cname, Customer.rating).where(Customer.cnum.in_(sub_query))
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 54th question -- select snum, sum(amount) from "order" group by snum having sum(amount) > (select max(amount) from "order");

# sub_query = select(func.max(Orders.amount)).scalar_subquery()
# select_statement = select(Orders.snum, func.sum(Orders.amount)).group_by(Orders.snum).having(func.sum(Orders.amount) > sub_query)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 55th question -- select cname from customer where cnum in (select cnum from "order" where odate = '2016-03-10');

# sub_query = select(Orders.cnum).where(Orders.odate == date(2016, 3, 10))
# select_statement = select(Customer.cname).where(Customer.cnum.in_(sub_query))
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 56th question -- select s.sname, s.snum from salespeople s join customer c on s.snum = c.snum group by s.sname, s.snum having  count(c.cnum) > 1;

# select_statement = select(Salesperson.snum, Salesperson.sname).join(Customer, Salesperson.snum == Customer.snum).group_by(Salesperson.snum,Salesperson.sname).having(func.count(Customer.cnum) > 1)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 57th question -- select * from "order" o join customer c on o.cnum = c.cnum where o.snum != c.snum; 

# select_statement = select(Orders).join(Customer, Orders.cnum == Customer.cnum).where(Orders.snum != Customer.snum)
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 58th question -- select * from "order" o where amount > (select avg(amount) from "order" where cnum = o.cnum);

# sub_query = select(func.avg(Orders.amount)).where(Orders.cnum == Orders.cnum)
# select_statement = select(Orders).where(Orders.amount > sub_query.scalar_subquery())
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)


## 59th question -- SELECT o.snum FROM "order" o WHERE o.odate IN (SELECT odate FROM "order" GROUP BY odate HAVING SUM(amount) >= (SELECT MAX(amount) + 2000 FROM "order"));

# sub_sub_query = select(func.max(Orders.amount) + 2000)
# sub_query = select(Orders.odate).group_by(Orders.odate).having(func.sum(Orders.amount) >= sub_sub_query.scalar_subquery())
# select_statement = select(Orders.snum).where(Orders.odate.in_(sub_query))
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)


## 60th question --  select c.cname,c.cnum from customer c where c.rating = (select max(c1.rating) from customer c1 where c1.rating = c.rating);

# c = aliased(Customer)
# c1 = aliased(Customer)
# sub_query = select(func.max(c1.rating)).where(c1.rating == c.rating)
# select_statement = select(c.cname,c.cnum).where(c.rating == sub_query.scalar_subquery())
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 61th question -- 1) select distinct s.snum, s.sname from salespeople s join customer c on s.city = c.city and s.snum <> c.snum;

# s = aliased(Salesperson)
# c = aliased(Customer)
# select_statement = select(s.snum, s.sname).distinct().join(c, and_(s.city == c.city, s.snum != c.snum))
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 2) select s.snum, s.sname from salespeople s where exists (select 1 from customer c where s.city = c.city and s.snum <> c.snum);

# s = aliased(Salesperson)
# c = aliased(Customer)
# sub_query = select(1).where(and_(s.city == c.city,s.snum != c.snum))
# select_statement = select(s.snum, s.sname).where(sub_query.exists())
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 62th question -- select cnum, cname, city from customer where exists (select 1 from customer where city = "San Jose");

# sub_query = select(1).where(Customer.city == "San Jose")
# select_statement = select(Customer.cnum, Customer.cname, Customer.city).where(sub_query.exists())
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 63th question --  select snum from customer group by snum having count(cnum) > 1;

# select_statement = select(Customer.snum,Customer.cname).group_by(Customer.snum).having(func.count(Customer.cnum) > 1)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 64th question --  select *  from customer group by snum having count(cnum) > 1;  

# select_statement = select(Customer).group_by(Customer.snum).having(func.count(Customer.cnum) > 1)
# result = session.execute(select_statement)
# for i in result:
#     print(i)


## 65th question --  select *  from customer group by snum having count(cnum) =  1;

# select_statement = select(Customer).group_by(Customer.snum).having(func.count(Customer.cnum) == 1)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 66th question --  select  s.* from salespeople s where s.snum in (select snum from "order" group by snum having count(onum) > 1);

# sub_query = select(Orders.snum).group_by(Orders.snum).having(func.count(Orders.onum) > 1)
# select_statement = select(Salesperson).where(Salesperson.snum.in_(sub_query))
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 67th question --  select * from salespeople s where exists  (select 1 from customer c where c.snum = s.snum and c.rating = 300);

# sub_query = select(1).where(and_(Customer.snum == Salesperson.snum, Customer.rating == 300))
# select_statement = select(Salesperson).where(sub_query.exists())
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 68th question -- select s.* from salespeople s join customer c on s.snum = c.snum where rating = 300;

# s = aliased(Salesperson)
# c = aliased(Customer)
# select_statement = select(s).join(c, s.snum == c.snum).where(c.rating == 300)
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 69th question -- select * from salespeople s where exists (select 1 from customer c where s.city = c.city and  s.snum != c.snum );

# s = aliased(Salesperson)
# c = aliased(Customer)
# sub_query = select(1).where(and_(s.city == c.city, s.snum != c.snum))
# select_statement = select(s).where(sub_query.exists())
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 70th question --  select * from customer c where exists (select 1 from customer c1 join "order" o on c1.cnum = o.cnum where c1.snum = c.snum and c1.cnum != c.cnum);

# c = aliased(Customer)
# c1 = aliased(Customer)
# o = aliased(Orders)
# sub_query = select(1).select_from(c1).join(o , c1.cnum == o.cnum).where(and_(c1.snum == c.snum, c1.cnum != c.cnum))
# select_statement = select(c).where(sub_query.exists())
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)


## 71th question -- 1) select * from salespeople s where city in (select city from customer);

# sub_query = select(Customer.city)
# select_statement = select(Salesperson).where(Salesperson.city.in_(sub_query))
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

# 2)  select s.* from salespeople s where s.city = any (select city from customer);

# s = aliased(Salesperson)
# c = aliased(Customer)
# sub_query = select(c.city)
# select_statement = select(s).where(s.city.any(sub_query))
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 72th question -- 1) select * from salespeople s where exists (select 1 from customer c where c.cname > s.sname);

# s = aliased(Salesperson)
# c = aliased(Customer)
# sub_query = select(1).where(c.cname > s.sname)
# select_statement = select(s).where(sub_query.exists())
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

# 2) SELECT * FROM salespeople s WHERE s.sname < ANY (SELECT cname FROM customer);
 
# s = aliased(Salesperson)
# c = aliased(Customer)
# sub_query = select(c.cname)
# select_statement = select(s).where(s.sname < any_(sub_query))
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 73th question -- sqlite> select * from customer where rating > (select min(rating) from customer where city = "Rome");

# sub_query = select(func.min(Customer.rating)).where(Customer.city == "Rome")
# select_statement = select(Customer).where(Customer.rating > sub_query.scalar_subquery())
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 74th question -- sqlite> select * from "order" where amount > (select min(amount) from "order" where odate = '2016-06-10');

# sub_query = select(func.min(Orders.amount)).where(Orders.odate == date(2016, 6, 10))
# select_statement = select(Orders).where(Orders.amount > sub_query.scalar_subquery())
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 75th question -- select * from "order" where amount < (select max(amount) from "order" o join customer c on o.cnum = c.cnum where c.city = "San Jose");

# o = aliased(Orders)
# c = aliased(Customer)
# sub_query = select(func.max(o.amount)).join(c, o.cnum == c.cnum).where(c.city == "San Jose")
# select_statement = select(Orders).where(Orders.amount < sub_query.scalar_subquery())
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

#2) select * from "order" where amount < any (select max(amount) from "order" o join customer c on o.cnum = c.cnum where c.city = "San Jose");

# o = aliased(Orders)
# c = aliased(Customer)
# sub_query = select(func.max(o.amount)).join(c, o.cnum == c.cnum).where(c.city == "San Jose")
# select_statement = select(Orders).where(Orders.amount < any_(sub_query))
# result = session.execute(select_statement)
# for i in result.scalars().all():
#     print(i)

## 76th question -- select * from customer where rating > all (select rating from customer where city = "Paris");

# sub_query = select(Customer.rating).where(Customer.city == "Paris")
# selet_statement = select(Customer).where(Customer.rating > func.all(sub_query))
# result = session.execute(selet_statement)
# for i in result.scalars().all():    
#     print(i)

# 2) select * from customr c1 where not exists (select 1 from customer c2 where c2.city = "Paris" and c2.rating >= c1.rating);
# 
# c1 = aliased(Customer)
# c2 = aliased(Customer)
# sub_query = select(1).where(and_(c2.city == "Paris", c2.rating >= c1.rating)) 
# select_statement = select(c1).where((not_(sub_query.exists())))
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 77th question -- 1) select * from customer where rating >= any (select rating from customer where snum = (select snum from salespeople where sname = "Serres");

# sub_sub_query = select(Salesperson.snum).where(Salesperson.sname == "Serres")
# sub_query = select(Customer.rating).where(Customer.snum == sub_sub_query.scalar_subquery())
# select_statement = select(Customer).where(Customer.rating >= any_(sub_query))
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

# 2) select * from customer where rating >= (select min(rating) from customer where snum = (select snum from salespeople where sname = "Serres"));

# sub_sub_query = select(Salesperson.snum).where(Salesperson.sname == "Serres")
# sub_query = select(func.min(Customer.rating)).where(Customer.snum == sub_sub_query.scalar_subquery())
# select_statement = select(Customer).where(Customer.rating >= sub_query.scalar_subquery())
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 78th question -- 1) SELECT * FROM salespeople s WHERE s.city != ANY (SELECT c.city FROM customer c WHERE c.snum = s.snum);
#                      SELECT * FROM salespeople s WHERE NOT EXISTS (SELECT 1 FROM customer c WHERE c.city = s.city);

# s = aliased(Salesperson)
# c = aliased(Customer)
# sub_query = select(c.city).where(c.snum == s.snum)
# select_statement = select(s).where(s.city != any_(sub_query))
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

# s = aliased(Salesperson)
# c = aliased(Customer)
# sub_query = select(1).where(c.city == s.city)
# select_statement = select(s).where(not_(sub_query.exists()))
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)


# 2) SELECT * FROM salespeople s WHERE s.city <> ALL (SELECT city FROM customer);
#    SELECT * FROM salespeople s WHERE NOT EXISTS (SELECT 1  FROM customer c WHERE c.city = s.city);

# s = aliased(Salesperson)
# c = aliased(Customer)
# sub_query = select(c.city)
# select_statement = select(s).where(s.city != func.all(sub_query))
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

# s = aliased(Salesperson)
# c = aliased(Customer)
# sub_query = select(1).where(c.city == s.city)
# select_statement = select(s).where(not_(sub_query.exists()))
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

## 79th question -- sqlite> select * from "order" o where o.amount > any (select amount from "order".o1 join customer c where c.city = "London");

# o = aliased(Orders)
# o1 = aliased(Orders)
# c = aliased(Customer)
# sub_query = select(o1.amount).join(c, o1.cnum == c.cnum).where(c.city == "London")
# select_statement = select(o).where(o.amount > any_(sub_query))
# result = session.execute(select_statement)
# for i in result.scalars().all():  
#     print(i)

# 2) SELECT * FROM "order" o WHERE o.amount > (SELECT MIN(o2.amount) FROM "order" o2 JOIN customer c ON o2.cnum = c.cnum WHERE c.city = 'London');

# o = aliased(Orders)
# o2 = aliased(Orders)
# c = aliased(Customer)
# sub_query = select(func.min(o2.amount)).join(c, o2.cnum == c.cnum).where(c.city == "London")
# select_statement = select(o).where(o.amount > sub_query.scalar_subquery())
# result = session.execute(select_statement)  
# for i in result.scalars().all():  
#     print(i)

## 80th question -- select s.sname as name from salespeople s where s.city = "London" union select c.cname as name from customer c where c.city = "London";

# s = aliased(Salesperson)
# c = aliased(Customer)
# query1 = select(s.sname.label("name"), s.city).where(s.city == "London")
# query2 = select(c.cname.label("name"), c.city).where(c.city == "London")
# select_statement = query1.union(query2)
# result = session.execute(select_statement)
# for i in result:  
#     print(i)

## 81th question -- select o.snum, o.odate, o.amount from "order" o where o.amount  = (select max(amount) from "order" where snum = o.snum) or o.amount = ( select min(amount) from "order" where snum = o.snum) order by o.snum, o.amount;

# o = aliased(Orders)
# sub_query1 = select(func.max(Orders.amount)).where(Orders.snum == o.snum)
# sub_query2 = select(func.min(Orders.amount)).where(Orders.snum == o.snum)
# select_statement = select(o.snum, o.odate, o.amount).where(or_(o.amount == sub_query1.scalar_subquery(), o.amount == sub_query2.scalar_subquery())).order_by(o.snum, o.amount)
# result = session.execute(select_statement)  
# for i in result:  
#     print(i)

## 82th question -- SELECT  s.snum, s.sname, s.city, CASE WHEN EXISTS (SELECT 1 FROM customer c WHERE c.city = s.city) THEN 'Has Customer in City' ELSE 'No Customer in City' END AS status FROM salespeople s;

# s = aliased(Salesperson)
# c = aliased(Customer)
# case_query = case(
#     (select(1).where(c.city == s.city).exists(), 'Has Customer in City'),
#     else_='No Customer in City'
# ).label("status")

# select_statement = select(s.snum, s.sname, s.city, case_query)
# result = session.execute(select_statement)  
# for i in result:  
#     print(i)

## 83th question -- select s.snum, s.sname || '(' || case when exists (select 1 from customer c where s.city = c.city) then "has customer in city" else "no customer in city" end || ')' as status from salespeople s; 

# s = aliased(Salesperson)
# c = aliased(Customer)
# case_query = case(
#     (select(1).where(c.city == s.city).exists(), 'has customer in city'),
#     else_='no customer in city'
# ).label("status")
# select_statement = select(s.snum, (s.sname + '(' + case_query + ')').label("status"))
# result = session.execute(select_statement)  
# for i in result:  
#     print(i)

## 84th question -- select cname, city ,rating, "highest rating" from customer where rating >= 200 union select cname, city, rating, "lowest rating" from customer where rating < 200;

# c = aliased(Customer)
# query1 = select(c.cname, c.city, c.rating, literal("highest rating")).where(c.rating >= 200)
# query2 = select(c.cname, c.city, c.rating, literal("lowest rating")).where(c.rating < 200)
# select_statement = query1.union(query2)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 85th question --  select c.cname as name, c.cnum as number from customer c join "order" o on c.cnum = o.cnum group by c.cnum, c.cname having count(o.onum) > 1 union select s.sname as name, s.snum as number from salespeople s join "order" o on s.snum = o.snum group by s.snum, s.sname having count(o.onum) >1;

# o = aliased(Orders)
# c = aliased(Customer)
# s = aliased(Salesperson)
# query1 = select(c.cname.label("name"),c.cnum.label("number")).join(o, c.cnum == o.cnum).group_by(c.cnum, c.cname).having(func.count(o.onum) > 1)
# query2 = select(s.sname.label("name"), s.snum.label("number")).join(o, s.snum == o.snum).group_by(s.snum, s.sname).having(func.count(o.onum) > 1)
# select_statement = query1.union(query2)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 86th question -- SELECT s.snum AS number FROM salespeople s WHERE s.city = 'San Jose' UNION SELECT FROM ( SELECT c.cnum AS number FROM customer c WHERE c.city = 'San Jose' UNION ALL SELECT o.onum AS number FROM "order" o WHERE o.odate = '2016-10-03');


# s = aliased(Salesperson)
# c = aliased(Customer)
# o = aliased(Orders)
# query1 = select(s.snum.label("number")).where(s.city =="San Jose")
# query2 = select(c.cnum.label("number")).where(c.city == "San Jose")
# query3 = select(o.onum.label("number")).where(o.odate == date(2016,10,3))


# inner_join = query2.union_all(query3).subquery()
# select_statement = query1.union(select(inner_join.c.number))
# result = session.execute(select_statement)
# for i in result:    
#     print(i)

## 87th question -- sqlite> insert into customer (cname, cnum, city, rating, snum) values ("Hoffman", 2001, "London",200,9999) ;

# new_customer = Customer(cname="Hoffman", cnum=2001, city="London", rating=200, snum=9999)
# session.add(new_customer)
# session.commit()

## 88th question sqlite> insert into Londonstaff select * from salespeople where city = "London";


# insector = inspect(engine)
# print(insector.get_table_names())

# londonstaff = Table("LondonStaff", Base.metadata, autoload_with=engine)

# select_statement = select(Salesperson).where(Salesperson.city == "London")
# insert_query = insert(londonstaff).from_select(["snum","sname","city","comm"],select_statement)
# session.execute(insert_query)
# session.commit()

# select_statement1 = select(londonstaff)
# result = session.execute(select_statement1)
# for i in result:
#     print(i)


## 89th question 

# daytotals = Table("DayTotals", Base.metadata, autoload_with=engine)
# select_query = select(Orders.odate,Orders.amount)
# insert_query = insert(daytotals).from_select(["data","total_sales"],select_query)
# session.execute(insert_query)
# session.commit()

# select_statement = select(daytotals)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 90th question -- delete from salespeope;

# delete_query = delete(Salesperson)
# session.execute(delete_query)
## session.commit()


## 91th question -- delete from customer where cname = "Clemens";

# delete_query = delete(Customer).where(Customer.cname == "Clemens")
# session.execute(delete_query)
# # session.commit()


## 92th question -- update customer set rating = rating + 100 where city = "Rome";

# update_query = update(Customer).where(Customer.city == "Rome").values(rating = Customer.rating + 100)
# session.execute(update_query)
# session.commit()

## 93th question -- 

# selet_statement = select(Salesperson).where(or_(Salesperson.sname == "Serres", Salesperson.sname == "Motika"))
# result = session.execute(selet_statement)
# for i in result.scalars().all():    
#     print(i)

# update_query = update(Customer).where(Customer.snum == (select(Salesperson.snum).where(Salesperson.sname == "Serres")).scalar_subquery()).values(snum = (select(Salesperson.snum).where(Salesperson.sname == "Motika")).scalar_subquery())
# session.execute(update_query)
# session.commit()

## 94th question-- 

# inspector = inspect(engine)
# print(inspector.get_table_names())

# sjpeople = Table("SJpeople", Base.metadata, autoload_with=engine)

# select_query = select(Salesperson).join(Customer, Salesperson.snum == Customer.snum).where(Customer.city == "San Jose")
# insert_query = insert(sjpeople).from_select(["snum","sname","city","comm"],select_query)
# session.execute(insert_query)
# session.commit()


# select_statement = select(sjpeople)
# result = session.execute(select_statement)
# for i in result:    
#     print(i)

## 95th question 

# samecity = Table("samecity", Base.metadata, autoload_with=engine)
# select_query = select(Salesperson).join(Customer, and_(Salesperson.city == Customer.city, Salesperson.snum == Customer.snum))

# insert_query = insert(samecity).from_select(["snum","sname","city","comm"],select_query)
# session.execute(insert_query)
# session.commit()

# select_statement = select(samecity)
# result = session.execute(select_statement)
# for i in result:    
#     print(i)

## 96th question

# inspector = inspect(engine)
# print(inspector.get_table_names())

# join_query = select(Orders.odate, func.max(Orders.amount).label("max_amount")).group_by(Orders.odate)
# m = aliased(join_query.subquery(), name="m")
# o = aliased(Orders)
# select_query = select(o.snum, o.odate, o.amount).join(m, and_(o.odate == m.c.odate, o.amount == m.c.max_amount))
# # result = session.execute(select_query)


# bonus = Table("bonus", Base.metadata, autoload_with=engine)
# insert_query = insert(bonus).from_select(["snum","odate","amount"],select_query)
# session.execute(insert_query)
# session.commit()


# select_statement = select(bonus)
# result = session.execute(select_statement)
# for i in result:    
#     print(i)

## 97th question

# select_statement = select(Customer).where(Customer.snum.in_(select(Salesperson.snum).where(Salesperson.city == "London")))
# result = session.execute(select_statement)

# delete_query = delete(Customer).where(Customer.snum.in_(select(Salesperson.snum).where(Salesperson.city == "London")))
# session.execute(delete_query)
# session.commit()

## 98th question 

# select_query = select(Salesperson).where(Salesperson.snum.in_(select(Customer.snum).where(Customer.rating == 100))) 

# delete_query = delete(Salesperson).where(Salesperson.snum.in_(select(Customer.snum).where(Customer.rating == 100))) 
# session.execute(delete_query)
# session.commit()

# result = session.execute(select_query)
# for i in result.scalars().all():    
#     print(i)

## 99th question
# sub_sub_query = select(Orders.odate, func.min(Orders.amount)).group_by(Orders.odate)
# sub_query = select(Orders.snum).where(tuple_(Orders.odate, Orders.amount).in_(sub_sub_query))
# delete_query = delete(Salesperson).where(Salesperson.snum.in_(sub_query))   
# session.execute(delete_query)
# session.commit()

# select_statement = select(Salesperson)
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)


## 100th question 
# sub_sub_query = select(Orders.odate, func.min(Orders.amount)).group_by(Orders.odate)
# sub_query = select(Orders.snum).where(tuple_(Orders.odate, Orders.amount).in_(sub_sub_query))
# delete_query = delete(Salesperson).where((Salesperson.snum.in_(sub_query)), Salesperson.sname != "Peel")  
# session.execute(delete_query)
# # session.commit()

# # select_statement = select(Salesperson)
# result = session.execute(select_statement)
# for i in result.scalars().all():    
#     print(i)

 

## 101th question

# select_query = select(Customer.snum).group_by(Customer.snum).having(func.count(Customer.cnum) >= 2)
# update_query = update(Salesperson).where(Salesperson.snum.in_(select_query)).values(comm = Salesperson.comm + 0.01)
# session.execute(update_query)
# session.commit()

## 102th question

# sub_sub_query = select(func.min(Orders.amount))
# sub_query = select(Orders.snum).where(Orders.amount == sub_sub_query.scalar_subquery())
# update_query = update(Salesperson).where(Salesperson.snum.in_(sub_query)).values(comm = Salesperson.comm - 0.01)
# session.execute(update_query)
# session.commit()

## 103th question

# inspector = inspect(engine)
# print(inspector.get_table_names())
# multicast = Table("multicast", Base.metadata,autoload_with=engine )
# select_query = select(Salesperson).where(Salesperson.snum.in_(select(Customer.snum).group_by(Customer.snum).having(func.count(Customer.cnum) > 1)))

# insert_query = insert(multicast).from_select(["snum","sname","city","comm"],select_query)
# session.execute(insert_query)
# session.commit()

# select_statement = select(multicast)
# result = session.execute(select_statement)
# for i in result:
#     print(i)

## 104th question

# delete_query = delete(Customer).where(~Customer.cnum.in_(select(Orders.cnum)))
# session.execute(delete_query)
# session.commit()

## 105th question

# sub_query = select(Orders.snum, func.sum(Orders.amount).label("total_amt")).group_by(Orders.snum).having(func.sum(Orders.amount) > 3000)
# sub_query_sum = select(sub_query.c.snum)
# update_query = update(Salesperson).where(Salesperson.snum.in_(sub_query_sum)).values(comm = Salesperson.comm * 1.20)
# session.execute(update_query)
# session.commit()

## 106th question

# view_query = text("""
#             create view ordersbydate as
#             select odate, count(*) as total_orders, sum(amount) as total_amount, avg(amount) as avg_amount
#             from  "order" group by odate; 
# """) 

# session.execute(view_query)
# session.commit()

# result = session.execute(text("select * from ordersbydate"))
# for i in result:
#     print(i)

## 107th question -- add this in Order table class

    # __table_args__ = (
    #     Index("idx_orders_snum_odate", "snum", "odate"),
    # )

## 108th question

    # __table_args__ = (
    #     UniqueConstraint("snum", "rating", name="uq_snum_rating"),
    # )

## 109th question

# view_query = text("""
#                     create view LondonStaffView as 
#                   select * from salespeople where city = "London";
# """)
# session.execute(view_query)
# session.commit()

# inspector = inspect(engine)
# print(inspector.get_table_names())

# result = session.execute(text("select * from LondonStaffView"))
# for i in result:
#     print(i)


## 110th question

# view_query = text("""
#             create view if not exists ratingcounts as 
#                   select rating, count(*) as countcol from customer group by rating;
# """)
# session.execute(view_query)
# session.commit()

# select_query = session.execute(text("select * from ratingcounts"))
# for i in select_query:
#     print(i)


## 111th question

# view_query = text("""
#         create view if not exists dailyordersummary as 
#                   select odate, count(distinct snum) as num_salespeople, count(*) as num_orders,
#                   avg(amount) as avg_amount, sum(amount) as total_amount from "order" group by odate;
# """)
# session.execute(view_query)
# session.commit()

# result = session.execute(text("select * from dailyordersummary;"))
# for i in result:
#     print(i)

## 112th question
# session.execute(text("DROP VIEW IF EXISTS orderswithnames;"))

# view_query = text("""
#                 create view if not exists orderswithnames as
#                   select o.onum, s.sname as salesperson_name, c.cname as customer_name, o.odate, o.amount 
#                   from "order" o join salespeople s on o.snum = s.snum
#                   join customer c on o.cnum = c.cnum; 
# """)
# session.execute(view_query)
# session.commit()

# result = session.execute(text("SELECT *  from orderswithnames;"))
# for i in result:
#     print(i)

## 113th question

# view_query = text("""
#             create view if not exists axelrods_data as
#                   select o.*, s.comm from "order" o join salespeople s on o.snum = s.snum where s.sname = "Axelrod"; 

# """)

# session.execute(view_query)
# session.commit()

# result = session.execute(text("select * from axelrods_data"))
# for i in result:
#     print(i)


## 114th question
# session.execute(text("DROP VIEW IF EXISTS bonus_salespeople;"))

# view_query = text("""
#             create view if not exists bonus_salespeople as
#                   select o.onum, o.odate, o.amount, s.sname as salespeople_name, c.cname as customer_name
#                   from "order" o join salespeople s on o.snum = s.snum join customer c on o.cnum = c.cnum 
#                   where o.amount = (select max(o2.amount) from "order" o2 where o2.odate = o.odate);
#                   """)
# session.execute(view_query)
# session.commit()

# result = session.execute(text("select * from bonus_salespeople;"))
# for i in result:
#     print(i)


## 115th question

# view_query = text("""
# CREATE VIEW IF NOT EXISTS bonus_after_10_times AS
# WITH highest_each_day AS (
#     SELECT o.odate, o.snum, o.cnum, o.amount
#     FROM "order" o
#     WHERE o.amount = (
#         SELECT MAX(o2.amount)
#         FROM "order" o2
#         WHERE o2.odate = o.odate
#     )
# ),
# counts AS (
#     SELECT snum, COUNT(*) AS times_highest
#     FROM highest_each_day
#     GROUP BY snum
#     HAVING COUNT(*) >= 10
# )
# SELECT s.snum, s.sname, c.times_highest
# FROM counts c
# JOIN salespeople s ON s.snum = c.snum;
# """)

# session.execute(view_query)
# session.commit()

# result = session.execute(text("SELECT * FROM bonus_after_10_times;"))
# for row in result:
#     print(row)


## 116th question

# view_query = text("""
#                 create view if not exists HighRatingCustomers as
#                   select * from customer where rating = (select max(rating) from customer);
# """)
# session.execute(view_query)
# session.commit()

# result = session.execute(text("select * from HighRatingCustomers;"))
# for i in result:
#     print(i)

## 117th question

# view_query = text("""
#                 create view if not exists SalespeoplePerCity as
#                   select snum, count(*) as num_salespeople from salespeople group by city;
# """)
# session.execute(view_query)
# session.commit()

# result = session.execute(text("select * from SalespeoplePerCity;"))
# for i in result:
#     print(i)

## 118th question
# session.execute(text("DROP VIEW IF EXISTS SalespersonOrderStats;"))

# view_query = text("""
#                 create view if not exists SalespersonOrderStats as
#                   select s.sname as salespeople_name, avg(o.amount) as avg_order_amt, sum(o.amount) as total_order_amt
#                   from salespeople s left join "order" o on s.snum = o.snum group by s.sname;
# """)
# session.execute(view_query)
# session.commit()

# result = session.execute(text("select * from SalespersonOrderStats;"))
# for i in result:
#     print(i)

## 119th question
# session.execute(text("DROP VIEW IF EXISTS SalespeopleWithMultipleCustomers;"))

# view_query = text("""
#                     create view if not exists SalespeopleWithMultipleCustomers  as
#                   select s.snum, s.sname, count(c.cnum) as customer_count from  salespeople s join customer c
#                   on s.snum = c.snum group by s.snum, s.sname having count(c.cnum) > 1;
# """)
# session.execute(view_query)
# session.commit()

# result = session.execute(text("select * from SalespeopleWithMultipleCustomers;"))
# for i in result:
#     print(i)


## 120th question

# view_query = text("""
#                     create view if not exists DailyOrderStats as 
#                   select o.odate, count(*) as order_count, avg(o.amount) as avg_order_amount, sum(o.amount) as total_order_amount
#                   from "order" o group by o.odate;
# """)
# session.execute(view_query)
# session.commit()

# result = session.execute(text("select * from DailyOrderStats;"))
# for i in result:
#     print(i)


## 121th question

# select_query = text("""
#                     select s.sname from salespeople s where s.city = "London"
#                     intersect 
#                     select s.sname from salespeople s join customer c on s.snum = c.snum where c.city = "London";
# """)
# result = session.execute(select_query)
# for i in result:
#     print(i)


## 122th question

# s = aliased(Salesperson)
# c = aliased(Customer)
# select_query = select(s.sname).where(and_(s.city == "London", ~select(1).where(and_(c.snum == s.snum, c.city == "London")).exists()))
# result = session.execute(select_query)
# for i in result:
#     print(i)

## 123th question

# s = aliased(Salesperson)
# c = aliased(Customer)
# select_query = select(s.sname, c.cname).join(c, s.snum == c.snum, isouter= True)

# result = session.execute(select_query)
# for i in result:
#     print(i)

## 124th question

# view_query = text("""
#     CREATE VIEW IF NOT EXISTS LowRatingCustomers AS
#     SELECT *
#     FROM customer
#     WHERE rating = (SELECT MIN(rating) FROM customer);
# """)
# session.execute(view_query)
# session.commit()

# GRANT SELECT ON LowRatingCustomers TO janet;

# result = session.execute(text("SELECT * FROM LowRatingCustomers;"))
# for row in result:
#     print(row)
