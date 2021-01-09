-- -- Keep a log of any SQL queries you execute as you solve the mystery.
select * from crime_scene_reports where year = 2020 and month = 7 and day = 28 and street = 'Chamberlin Street';

select * from interviews where year = 2020 and month = 7 and day = 28 ;

select * from atm_transactions where month = 7 and day = 28 and transaction_type = 'withdraw' and atm_location = 'Fifer Street';

select * from bank_accounts as a
join people as b on a.person_id = b.id;
select * from phone_calls as a
join people as b on a.caller = b.phone_number
where a.year = 2020 and a.month = 7 and a.day = 28 and duration <= 60;

select b.name, c.name from phone_calls as a
join people as b on a.caller = b.phone_number
join people as c on a.receiver = c.phone_number
where a.year = 2020 and a.month = 7 and a.day = 28 and duration <= 60;

select name from courthouse_security_logs as a
join people as b on a.license_plate = b.license_plate
where year = 2020 and month = 7 and day = 28
and activity = 'exit' and hour >= 10 and minute < 26;

select name from atm_transactions as a
join bank_accounts as b on a.account_number = b.account_number
join people as c on b.person_id = c.id
where atm_location = 'Fifer Street' and month = 7 and day = 28 and transaction_type = 'withdraw';


select * from passengers as a
join flights as b on a.flight_id = b.id
join people as c on c.passport_number = a.passport_number
where year = 2020 and month = 7 and day in (29) and origin_airport_id = 8 order by hour;