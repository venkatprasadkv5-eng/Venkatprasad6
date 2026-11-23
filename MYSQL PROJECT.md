drop database if exists Hospital_Management_System;
create database Hospital_Management_System;
use Hospital_Management_System;

-- 1. TABLES
create table Departments (department_id int primary key, department_name varchar(50) not null);

create table Doctors (doctor_id int primary key, department_id int,
 doctor_name varchar(80), specialization varchar(80),
 phone varchar(15), consultation_fee decimal(8,2),
 foreign key (department_id) references Departments(department_id));

create table Patients (patient_id INT PRIMARY KEY, patient_name varchar(80), date_of_birth DATE,
 gender varchar(10), phone varchar(15), city varchar(50));

create table Appointments (appointment_id int primary key, patient_id int, doctor_id int,
 appointment_date date, appointment_status varchar(20),
foreign key  (patient_id) references Patients(patient_id), 
 foreign key  (doctor_id) references Doctors(doctor_id));

create table Prescriptions (prescription_id int primary key, appointment_id int,
 medicine_name varchar(80), dosage varchar(80), duration_days int,
 foreign key  (appointment_id) references Appointments(appointment_id));

create table Billing (bill_id int primary key, patient_id int, appointment_id int,
 bill_amount decimal(8,2), payment_method varchar(20),
 payment_status varchar(20), bill_date date,
 foreign key (patient_id) references Patients(patient_id),
 foreign key (appointment_id) references Appointments(appointment_id));

-- 2. SAMPLE DATA
insert into Departments values
(101,'Cardiology'),(102,'Neurology'),(103,'Orthopedics'),
(104,'Pediatrics'),(105,'Dermatology'),(106,'ENT');

insert into Doctors values
(201,101,'Dr. Anil Kumar','General Cardiology','9876501001',800),
(202,101,'Dr. Priya Sharma','Interventional Cardiology','9876501002',1200),
(203,101,'Dr. Ravi Teja','General Cardiology','9876501003',700),
(204,102,'Dr. Sneha Reddy','Neurology','9876501004',1000),
(205,102,'Dr. Kiran Rao','Neurosurgery','9876501005',1500),
(206,103,'Dr. Meena Patel','Orthopedic Surgery','9876501006',900),
(207,103,'Dr. Arjun Singh','General Orthopedics','9876501007',750),
(208,104,'Dr. Lakshmi Devi','Pediatrics','9876501008',600),
(209,105,'Dr. Varun Reddy','Dermatology','9876501009',650),
(210,105,'Dr. Neha Kapoor','Clinical Dermatology','9876501010',850);

insert into Patients values
(301,'Aarav','1995-04-12','Male','9876510001','Hyderabad'),
(302,'Bhavya','1998-07-25','Female','9876510002','Vijayawada'),
(303,'Charan','1987-11-18','Male','9876510003','Visakhapatnam'),
(304,'Divya','2001-02-10','Female','9876510004','Bengaluru'),
(305,'Esha','1992-09-05','Female','9876510005','Chennai'),
(306,'Farhan','1985-06-20','Male','9876510006','Mumbai'),
(307,'Gopi','1978-12-15','Male','9876510007','Warangal'),
(308,'Harini','2003-03-22','Female','9876510008','Guntur'),
(309,'Ishaan','1990-08-30','Male','9876510009','Pune'),
(310,'Kavya','1997-01-14','Female','9876510010','Kochi'),
(311,'Manoj','1982-05-27','Male','9876510011','Hyderabad'),
(312,'Nandini','2010-10-08','Female','9876510012','Bengaluru');

insert into Appointments values
(401,301,201,'2026-08-01','Completed'),(402,302,202,'2026-08-02','Completed'),
(403,303,204,'2026-08-03','Scheduled'),(404,304,206,'2026-08-04','Completed'),
(405,305,209,'2026-08-05','Cancelled'),(406,306,205,'2026-08-06','Completed'),
(407,307,203,'2026-08-07','Completed'),(408,308,208,'2026-08-08','Scheduled'),
(409,309,207,'2026-08-09','Completed'),(410,310,210,'2026-08-10','Completed'),
(411,301,202,'2026-08-11','Scheduled'),(412,303,201,'2026-08-12','Completed'),
(413,311,204,'2026-08-13','Scheduled'),(414,312,208,'2026-08-14','Completed'),
(415,305,210,'2026-08-15','Scheduled');

insert into Prescriptions values
(501,401,'Aspirin','75 mg once daily',30),(502,402,'Atorvastatin','20 mg once daily',30),
(503,403,'Levetiracetam','500 mg twice daily',15),(504,404,'Calcium Tablets','500 mg once daily',30),
(505,406,'Pantoprazole','40 mg once daily',10),(506,407,'Aspirin','75 mg once daily',20),
(507,408,'Paracetamol','500 mg twice daily',5),(508,409,'Ibuprofen','400 mg twice daily',7),
(509,410,'Cetirizine','10 mg once daily',5),(510,412,'Clopidogrel','75 mg once daily',30),
(511,414,'Paracetamol','500 mg twice daily',5),(512,415,'Clindamycin','300 mg twice daily',7);

insert into Billing values
(601,301,401,1500,'UPI','Paid','2026-08-01'),(602,302,402,2200,'Card','Paid','2026-08-02'),
(603,303,403,1800,'UPI','Pending','2026-08-03'),(604,304,404,1700,'Cash','Paid','2026-08-04'),
(605,305,405,900,'Card','Refunded','2026-08-05'),(606,306,406,2500,'UPI','Paid','2026-08-06'),
(607,307,407,1400,'Cash','Paid','2026-08-07'),(608,308,408,1000,'UPI','Pending','2026-08-08'),
(609,309,409,1600,'Card','Paid','2026-08-09'),(610,310,410,1900,'UPI','Paid','2026-08-10'),
(611,301,411,2200,'Card','Pending','2026-08-11'),(612,303,412,1500,'Cash','Paid','2026-08-12'),
(613,311,413,1800,'UPI','Paid','2026-08-13'),(614,312,414,1200,'Cash','Paid','2026-08-14'),
(615,305,415,1700,'Card','Pending','2026-08-15');

-- 3. BASIC QUERIES (1-10)
-- 1 Doctors and specialization
select doctor_name,specialization from Doctors;
-- 2 Patients from Hyderabad (change city as needed)
select patient_name from Patients where city='Hyderabad';
-- 3 Increase Cardiology doctors' fee by 15%
update Doctors set consultation_fee=consultation_fee*1.15 where department_id=101;
-- 4 Update appointment status for a chosen date
update Appointments set appointment_status='Completed'
where appointment_date='2026-08-03' and appointment_status='Scheduled';
set sql_safe_updates=0;
-- 5 Delete cancelled appointment and its dependent records
delete from Billing where appointment_id in
(select appointment_id from Appointments where appointment_status='Cancelled');
delete from Prescriptions where appointment_id in
(select appointment_id from Appointments where appointment_status='Cancelled');
delete from Appointments where appointment_status='Cancelled';
-- 6-10 String functions
select upper(doctor_name) from Doctors;
select lower(patient_name) from Patients;
select patient_name,left(patient_name,3) from Patients;
select concat(doctor_name,' - ',specialization)as doctor_details from Doctors;
select doctor_name,replace(specialization,'General','Specialist') as specialization
from Doctors;

-- 4. DATE QUERIES (11-15)
-- 11 Appointments in current month
select * from Appointments where month(appointment_date)=month(CURDATE()) and year(appointment_date)=year(CURDATE());
-- 12 Day of week
select appointment_id,appointment_date,dayname(appointment_date) as day_name from Appointments;
-- 13 Patient age
select patient_name,timestampdiff(YEAR,date_of_birth,CURDATE()) as age from Patients;
-- 14 Date format
select appointment_id,date_format(appointment_date,'%d-%M-%Y') as formatted_date from Appointments;
-- 15 Bill month and year
select bill_id,date_format(bill_date,'%M %Y') as bill_month from Billing;

-- 5. GROUP FUNCTIONS (16-22)
-- 16 Doctors in each department
select d.department_name,count(doc.doctor_id) as total_doctors
from Departments d left join Doctors doc on d.department_id=doc.department_id
group by d.department_id,d.department_name;
-- 17 Average fee by department
select d.department_name,avg(doc.consultation_fee) as average_fee
FROM Departments d left join Doctors doc on d.department_id=doc.department_id
group by d.department_id,d.department_name;
-- 18 Highest bill
select max(bill_amount) AS highest_bill FROM Billing;
-- 19 Total bill by payment method
select payment_method,sum(bill_amount) as total_amount from Billing group by payment_method;
-- 20 Appointments per doctor
select doc.doctor_name,count(a.appointment_id) as total_appointments
from Doctors doc left join Appointments a on doc.doctor_id=a.doctor_id
group by doc.doctor_id,doc.doctor_name;
-- 21 Departments with more than two doctors
select d.department_name,COUNT(doc.doctor_id) as total_doctors
from Departments d join Doctors doc on d.department_id=doc.department_id
group by d.department_id,d.department_name having count(doc.doctor_id)>2;
-- 22 Appointment count by status
select appointment_status,COUNT(*) as total from Appointments group by appointment_status;

-- 6. JOINS (23-29)
-- 23 Patient and doctor names
select p.patient_name,doc.doctor_name from Patients p
join Appointments a on p.patient_id=a.patient_id
join Doctors doc on a.doctor_id=doc.doctor_id;
-- 24 Doctor, department and specialization
select doc.doctor_name,d.department_name,doc.specialization
from Doctors doc join Departments d on doc.department_id=d.department_id;
-- 25 Patient appointment details
select p.patient_name,a.appointment_date,a.appointment_status
from Patients p join Appointments a on p.patient_id=a.patient_id;
-- 26 Prescription details
select p.patient_name,doc.doctor_name,pr.medicine_name,pr.dosage,pr.duration_days
from Patients p join Appointments a on p.patient_id=a.patient_id
join Doctors doc on a.doctor_id=doc.doctor_id
join Prescriptions pr on a.appointment_id=pr.appointment_id;
-- 27 Billing details
select p.patient_name,b.bill_amount,b.payment_method,b.payment_status
from Patients p join Billing b on p.patient_id=b.patient_id;
-- 28 All doctors, including those without appointments
select doc.doctor_name,a.appointment_id,a.appointment_date
from Doctors doc left join Appointments a on doc.doctor_id=a.doctor_id;
-- 29 All patients, including those without bills
select p.patient_name,b.bill_amount,b.payment_status
from Patients p left join Billing b on p.patient_id=b.patient_id;

-- 7. SUBQUERIES (30-34)
-- 30 Doctors charging above average
select doctor_name,consultation_fee from Doctors
where consultation_fee>(select avg(consultation_fee) from Doctors);
-- 31 Patient with highest individual bill
select p.patient_name,b.bill_amount from Patients p join Billing b on p.patient_id=b.patient_id
where b.bill_amount=(select max(bill_amount) from Billing);
-- 32 Doctors with above-average appointment count
select doc.doctor_name,count(a.appointment_id) as total
from Doctors doc left join Appointments a on doc.doctor_id=a.doctor_id
group by doc.doctor_id,doc.doctor_name
having count(a.appointment_id)>(select avg(cnt) from
(select count(*) as cnt from Appointments group by doctor_id) as counts);
-- 33 Patients who visited Cardiology
select distinct p.patient_name from Patients p
join Appointments a on p.patient_id=a.patient_id
join Doctors doc on a.doctor_id=doc.doctor_id
join Departments d on doc.department_id=d.department_id
where d.department_name='Cardiology';
-- 34 Departments without doctors
select d.department_name from Departments d left join Doctors doc
on d.department_id=doc.department_id where doc.doctor_id is null;

-- 8. VIEWS (35-36)
create or replace view Patient_Appointment_Details as
select p.patient_name,doc.doctor_name,d.department_name,a.appointment_date,a.appointment_status
from Patients p join Appointments a on p.patient_id=a.patient_id
join Doctors doc on a.doctor_id=doc.doctor_id
join Departments d on doc.department_id=d.department_id;

create or replace view Hospital_Billing_Summary as
select p.patient_name,sum(b.bill_amount) as total_bill_amount,b.payment_method,b.payment_status
from Patients p join Billing b on p.patient_id=b.patient_id
group by p.patient_id,p.patient_name,b.payment_method,b.payment_status;

select * from Patient_Appointment_Details;
select * from Hospital_Billing_Summary;

-- 9. TRANSACTION (37)
START TRANSACTION;

UPDATE Doctors 
SET consultation_fee = 1000 
WHERE doctor_id = 201;

SAVEPOINT fee_updated;

UPDATE Billing 
SET payment_status = 'Paid' 
WHERE bill_id = 603;

ROLLBACK TO SAVEPOINT fee_updated;

COMMIT;

-- 10. STORED PROCEDURES (38-39)
CALL GetPatientAppointments(301);

#39
CALL GetPatientTotalBill(301);

-- 11. TRIGGERS (40-41)
CREATE TABLE IF NOT EXISTS Billing_Archive (
    bill_id INT,
    patient_id INT,
    appointment_id INT,
    bill_amount DECIMAL(10, 2),
    payment_method VARCHAR(50),
    payment_status VARCHAR(50),
    bill_date DATE,
    deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO Billing (bill_id, patient_id, appointment_id, bill_amount, payment_method, payment_status, bill_date) 
VALUES (999, 301, 401, 500.00, 'Cash', 'Pending', '2026-11-22');
SELECT * FROM Billing WHERE bill_id = 999;
DELETE FROM Billing WHERE bill_id = 999;
SELECT * FROM Billing_Archive WHERE bill_id = 999;




-- First, ensure the history table exists:
CREATE TABLE IF NOT EXISTS Appointment_Status_History (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT,
    old_status VARCHAR(50),
    new_status VARCHAR(50),
    change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT appointment_id, appointment_status 
FROM Appointments 
WHERE appointment_id = 403;

SELECT * FROM Appointments WHERE appointment_id = 403;

UPDATE Appointments 
SET appointment_status = 'Completed' 
WHERE appointment_id = 403;

SELECT * FROM Appointment_Status_History 
WHERE appointment_id = 403;
