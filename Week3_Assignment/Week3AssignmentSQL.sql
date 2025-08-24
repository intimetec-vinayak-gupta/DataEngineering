USE pythonAssignments;
CREATE TABLE Departments (
    Id INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL
);

#DROP TABLE Employees
CREATE TABLE Employees (
    Id INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    ManagerId INT NULL,
    DepartmentId INT NOT NULL,
    Score INT CHECK (Score BETWEEN 1 AND 5),
    Ratings CHAR(1) DEFAULT NULL,
    FOREIGN KEY (DepartmentId) REFERENCES Departments(Id),
    FOREIGN KEY (ManagerId) REFERENCES Employees(Id)
);

INSERT INTO Departments (Id, Name) VALUES
(1, 'Data Engineers'),
(2, 'Front End Developer'),
(3, 'Back End Developer'),
(4, 'QA Engineers'),
(5, 'DevOps Engineers'),
(6, 'Data Science');

INSERT INTO Employees (Id, Name, ManagerId, DepartmentId, Score) VALUES
(1, 'Alice', NULL, 1, 5),   
(2, 'Bob', 1, 1, 4),        
(3, 'Charlie', 1, 2, 3),    
(4, 'David', 1, 3, 2),      
(5, 'Eva', 2, 4, 5),        
(6, 'Frank', 3, 5, 4),      
(7, 'Grace', 4, 2, 1);      


ALTER TABLE Employees
ADD Ratings VARCHAR(1) AS 
   (CASE 
        WHEN Score = 3 THEN 'M'
        WHEN Score = 4 THEN 'E'
        WHEN Score = 5 THEN 'S'
        ELSE NULL
    END);
  
UPDATE Employees
SET DepartmentId = 6
WHERE DepartmentId = 1 AND Ratings = 'S';


SELECT * FROM Departments