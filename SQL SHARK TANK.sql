select * from projects..data


--total episodes


select max ([Ep# No#]) from projects..data
select count(distinct [Ep# No#]) from projects..data



--pitches 

select count ( distinct [brand]) from projects..data


--pitches that got investment


select cast(sum(a.converted_not_converted) as float)/ cast(count(*)as float ) total_pitches from(
select Amount_Invested_lakhs, case when Amount_Invested_lakhs> 0  then 1 else 0 end as converted_not_converted from projects..data) a



-- total male

select sum (male) from projects..data


--total female


select sum (female) from projects..data



-- gender ratio


select sum(female)/ sum(male) from projects..data



--total invested amount


select sum(amount_invested_lakhs) from projects..data



--highest deal taken


select max(amount_invested_lakhs) from data

--highest amount asked 

select max(amout_asked) from data



-- startups having at least women


select sum(a.female_count) as total_female_count from (select case when female>0 then 1 else 0 end as female_count from data) a where a.female_count>0


-- pitches converted having atleast n0 women

select * from data


SELECT SUM(b.female_count)
FROM (
    SELECT CASE WHEN a.female > 0 THEN 1 ELSE 0 END AS female_count, a.*
    FROM (
        SELECT * FROM data WHERE deal != 'No Deal'
    ) a
) b;



-- avg team members



select avg(team_members) from projects..data


-- amount invested per deal


SELECT AVG(a.amount_invested_lakhs) AS amount_invested_per_deal
FROM (
    SELECT * FROM data WHERE deal != 'No Deal'
) a;



-- avg age group of contestants

select avg_age,count(avg_age) cnt from data group by avg_age order by cnt desc

-- location group of contestants

select location,count(location) cnt from data group by location order by cnt desc

-- sector group of contestants

select sector,count(sector) cnt from data group by sector order by cnt desc


--partner deals

select partners,count(partners) cnt from data  where partners!='-' group by partners order by cnt desc


-- making the matrix



SELECT m.keyy,
       m.total_deals_present,
       m.total_deals,
       n.total_amount_invested,
       n.avg_equity_taken 
FROM (
    SELECT a.keyy,
           a.total_deals_present,
           b.total_deals 
    FROM (
        SELECT 'Ashneer' AS keyy,
               COUNT(ashneer_amount_invested) AS total_deals_present 
        FROM projects..data 
        WHERE ashneer_amount_invested IS NOT NULL
    ) a
    INNER JOIN (
        SELECT 'Ashneer' AS keyy,
               COUNT(ashneer_amount_invested) AS total_deals 
        FROM projects..data 
        WHERE ashneer_amount_invested IS NOT NULL AND ashneer_amount_invested = 0
    ) b ON a.keyy = b.keyy
) m

INNER JOIN (
    SELECT 'Ashneer' AS keyy,
           SUM(ASHNEER_AMOUNT_INVESTED) AS total_amount_invested,
           AVG(ASHNEER_EQUITY_TAKEN) AS avg_equity_taken
    FROM projects..data 
    WHERE Ashneer_Equity_Taken = 0 AND ASHNEER_EQUITY_TAKEN IS NOT NULL
) n ON m.keyy = n.keyy;


-- which is the startup in which the highest amount has been invested in each domain/sector




select c.* from 
(select brand,sector,amount_invested_lakhs,rank() over(partition by sector order by amount_invested_lakhs desc) rnk 

from projectS..data) c


