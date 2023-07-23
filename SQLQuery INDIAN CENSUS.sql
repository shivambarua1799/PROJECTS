select * from project.dbo.sheet1

select * from project.dbo.sheet2

Q1-- NUMBER OF ROWS INTO OUR DATASET?


SELECT COUNT(*) FROM PROJECT..Sheet1

SELECT COUNT(*) FROM PROJECT..Sheet2


Q2--DATASET FOR JHARKHAND AND BIHAR.


SELECT * FROM PROJECT..Sheet1 WHERE STATE IN ('JHARKHAND', 'BIHAR')


Q3-- population of India


SELECT SUM(POPULATION) AS SUM_POPULATION FROM PROJECT..SHEET2


Q4-- avg growth


SELECT AVG(GROWTH) AS AVG_GROWTH FROM PROJECT..SHEET1


Q5-- avg sex ratio


SELECT AVG(SEX_RATIO) AS AVG_SEX_RATIO FROM PROJECT..SHEET1


Q6-- avg literacy 


SELECT AVG(LITERACY) AS AVG_LITERACY FROM PROJECT..SHEET1


Q7-- top 3 state showing highest growth ratio


select TOP 10 state,Growth  from project..SHEET1 ORDER BY GROWTH DESC


Q8--bottom 5 state showing lowest sex ratio


select TOP 10 state,SEX_RATIO  from project..SHEET1 ORDER BY SEX_RATIO ASC


Q9-- top and bottom 10 states in literacy Rate


SELECT TOP 10 STATE, LITERACY AS TOP_3STATES  from project..SHEET1 ORDER BY LITERACY ASC

SELECT TOP 10 STATE, LITERACY AS TOP_3STATES  from project..SHEET1 ORDER BY LITERACY DESC


Q10--union opertor

select * from (
select top 3 * from #topstates order by #topstates.topstate desc) a

union

select * from (
select top 3 * from #bottomstates order by #bottomstates.bottomstate asc) b;


Q11-- states starting with letter a


SELECT DISTINCT STATE FROM PROJECT..Sheet1 WHERE LOWER(STATE) LIKE 'a%'


Q13-- joining both table


Q13(1)--total males and females


select d.state,sum(d.males) total_males,sum(d.females) total_females from
(select c.district,c.state state,round(c.population/(c.sex_ratio+1),0) males, round((c.population*c.sex_ratio)/(c.sex_ratio+1),0) females from
(select a.district,a.state,a.sex_ratio/1000 sex_ratio,b.population from project..Sheet1 a inner join project..Sheet2 b on a.district=b.district ) c) d
group by d.state;


Q13(2)-- total literacy rate


select c.state,sum(literate_people) total_literate_pop,sum(illiterate_people) total_lliterate_pop from 
(select d.district,d.state,round(d.literacy_ratio*d.population,0) literate_people,
round((1-d.literacy_ratio)* d.population,0) illiterate_people from
(select a.district,a.state,a.literacy/100 literacy_ratio,b.population from project..data1 a 
inner join project..data2 b on a.district=b.district) d) c
group by c.state


Q13(3)-- population in previous census

select sum(m.previous_census_population) previous_census_population,sum(m.current_census_population) current_census_population from(
select e.state,sum(e.previous_census_population) previous_census_population,sum(e.current_census_population) current_census_population from
(select d.district,d.state,round(d.population/(1+d.growth),0) previous_census_population,d.population current_census_population from
(select a.district,a.state,a.growth growth,b.population from project..data1 a inner join project..data2 b on a.district=b.district) d) e
group by e.state)m


Q14-- population vs area


SELECT
  (g.total_area / g.previous_census_population) AS previous_census_population_vs_area,
  (g.total_area / g.current_census_population) AS current_census_population_vs_area
FROM
  (SELECT
   q.*,
   r.total_area
  FROM
    (SELECT
      '1' AS keyy,
      n.*
    FROM
      (SELECT
        SUM(m.previous_census_population) AS previous_census_population,
        SUM(m.current_census_population) AS current_census_population
      FROM
        (SELECT
          e.state,
          SUM(e.previous_census_population) AS previous_census_population,
          SUM(e.current_census_population) AS current_census_population
        FROM
          (SELECT
            d.district,
            d.state,
            ROUND(d.population / (1 + d.growth), 0) AS previous_census_population,
            d.population AS current_census_population
          FROM
            (SELECT
              a.district,
              a.state,
              a.growth,
              b.population
            FROM
              project..sheet1 a
              INNER JOIN project..sheet2 b ON a.district = b.district
            ) d
          ) e
        GROUP BY
          e.state
      ) m
    ) n
  ) q
  INNER JOIN
  (
    SELECT
      '1' AS keyy,
      z.*
    FROM
      (
        SELECT
          SUM(area_km2) AS total_area
        FROM
          project..sheet2
      ) z
  ) r ON q.keyy = r.keyy
) g;
