# Fortinet Assignment
Fortinet assignment of data archival service

### Data Archival Service Logical Architecture

![image](https://github.com/user-attachments/assets/2771f160-784b-41b0-a150-7f90d56e5213)

### Data Archival Service Technical Architecture

![image](https://github.com/user-attachments/assets/bdf41558-240c-4f81-8d0f-465c524f638b)


### Commands to RUN Docker and internal components:

> docker-compose up --build

### Sample Data to be inserted on primery DB for Student and Teacher Table

```
INSERT INTO `fortinet_primary_db`.`student`
(`id`, `name`, `email`, `created_on`)
VALUES
(1, 'Student 1', 'student1@example.com', DATE_SUB(NOW(), INTERVAL 190 DAY)),
(2, 'Student 2', 'student2@example.com', DATE_SUB(NOW(), INTERVAL 190 DAY)),
(3, 'Student 3', 'student3@example.com', DATE_SUB(NOW(), INTERVAL 750 DAY)),
(4, 'Student 4', 'student4@example.com', DATE_SUB(NOW(), INTERVAL 750 DAY)),
(5, 'Student 5', 'student5@example.com', DATE_SUB(NOW(), INTERVAL 60 DAY)),
(6, 'Student 6', 'student6@example.com', DATE_SUB(NOW(), INTERVAL 60 DAY)),
(7, 'Student 7', 'student7@example.com', DATE_SUB(NOW(), INTERVAL 2 MONTH)),
(8, 'Student 8', 'student8@example.com', DATE_SUB(NOW(), INTERVAL 2 MONTH)),
(9, 'Student 9', 'student9@example.com', DATE_SUB(NOW(), INTERVAL 60 DAY)),
(10, 'Student 10', 'student10@example.com', DATE_SUB(NOW(), INTERVAL 750 DAY)),
(11, 'Student 11', 'student11@example.com', DATE_SUB(NOW(), INTERVAL 1000 DAY)),
(12, 'Student 12', 'student12@example.com', DATE_SUB(NOW(), INTERVAL 200 DAY)),
(13, 'Student 13', 'student13@example.com', DATE_SUB(NOW(), INTERVAL 950 DAY));
```

```
INSERT INTO `fortinet_primary_db`.`teacher`
(`created_on`, `id`, `name`, `email`, `subject`)
VALUES
(DATE_SUB(NOW(), INTERVAL 11 DAY), 1, 'Alice Johnson', 'alice.johnson@example.com', 'Mathematics'),
(DATE_SUB(NOW(), INTERVAL 14 DAY), 2, 'Bob Smith', 'bob.smith@example.com', 'Science'),
(DATE_SUB(NOW(), INTERVAL 10 DAY), 3, 'Charlie Brown', 'charlie.brown@example.com', 'English'),
(DATE_SUB(NOW(), INTERVAL 150 DAY), 4, 'David White', 'david.white@example.com', 'History'),
(DATE_SUB(NOW(), INTERVAL 300 DAY), 5, 'Eva Green', 'eva.green@example.com', 'Mathematics'),
(DATE_SUB(NOW(), INTERVAL 330 DAY), 6, 'Frank Harris', 'frank.harris@example.com', 'Science'),
(DATE_SUB(NOW(), INTERVAL 30 DAY), 7, 'Grace Lee', 'grace.lee@example.com', 'History'),
(DATE_SUB(NOW(), INTERVAL 61 DAY), 8, 'Hannah King', 'hannah.king@example.com', 'Mathematics'),
(DATE_SUB(NOW(), INTERVAL 60 DAY), 9, 'Ivy Turner', 'ivy.turner@example.com', 'Science'),
(DATE_SUB(NOW(), INTERVAL 50 DAY), 10, 'Jack Martin', 'jack.martin@example.com', 'English'),
(DATE_SUB(NOW(), INTERVAL 200 DAY), 11, 'Karen Adams', 'karen.adams@example.com', 'Mathematics'),
(DATE_SUB(NOW(), INTERVAL 10 DAY), 12, 'Leo Scott', 'leo.scott@example.com', 'History'),
(DATE_SUB(NOW(), INTERVAL 19 DAY), 13, 'Mona Thomas', 'mona.thomas@example.com', 'Science'),
(DATE_SUB(NOW(), INTERVAL 196 DAY), 14, 'Nina Roberts', 'nina.roberts@example.com', 'English'),
(DATE_SUB(NOW(), INTERVAL 90 DAY), 15, 'Oscar Blake', 'oscar.blake@example.com', 'Mathematics');
```
