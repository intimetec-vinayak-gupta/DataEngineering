CREATE DATABASE pythonAssignments;
USE pythonAssignments;

CREATE TABLE Vehicles(
    VehicleID INT PRIMARY KEY,
    VehicleName VARCHAR(100) NOT NULL,
    SellingPrice DECIMAL(12,2) NOT NULL
);

CREATE TABLE Customers(
    CustomerID INT PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    Email VARCHAR(100)
);

-- Create Sales Table
CREATE TABLE VehicleSales(
    SaleID INT PRIMARY KEY,
    VehicleID INT NOT NULL,
    CustomerID INT NOT NULL,
    SaleDate DATE NOT NULL,
    Quantity INT NOT NULL DEFAULT 1,
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

START TRANSACTION;

INSERT INTO Customers (CustomerID, FullName, Email)
VALUES (1, 'Rahul Sharma', 'rahul@example.com');
INSERT INTO Customers (CustomerID, FullName, Email)
VALUES (2, 'Priya Verma', 'priya@example.com');

INSERT INTO Vehicles (VehicleID, VehicleName, SellingPrice)
VALUES (101, 'Honda City', 950000);
INSERT INTO Vehicles (VehicleID, VehicleName, SellingPrice)
VALUES (102, 'Hyundai Creta', 1100000);

INSERT INTO VehicleSales (SaleID, VehicleID, CustomerID, SaleDate, Quantity)
VALUES (1, 101, 1, '2024-04-15', 1);
INSERT INTO VehicleSales (SaleID, VehicleID, CustomerID, SaleDate, Quantity)
VALUES (2, 102, 2, '2024-08-20', 2);

#ROLLBACK;
COMMIT;


CREATE USER 'Rahul'@'localhost' IDENTIFIED BY 'Rahul@123';
GRANT SELECT ON pythonAssginments.* TO 'Rahul'@'localhost';
REVOKE SELECT ON pythonAssginments.* FROM 'Rahul'@'localhost';


ALTER TABLE Customers
ADD CONSTRAINT UQ_Customers_Email UNIQUE (Email);

CREATE INDEX IX_VehicleSales_SaleDate
ON VehicleSales (SaleDate);

CREATE INDEX IX_VehicleSales_VehicleID
ON VehicleSales (VehicleID);

SELECT 
    v.VehicleName,
    SUM(s.Quantity) AS TotalSold,
    SUM(s.Quantity * v.SellingPrice) AS TotalRevenue,
    SUM(s.Quantity * (v.SellingPrice * 0.40)) AS ProfitMade   -- Assume 40% as profit margin
FROM VehicleSales s
JOIN Vehicles v ON s.VehicleID = v.VehicleID
WHERE YEAR(s.SaleDate) = YEAR(CURDATE()) - 1
GROUP BY v.VehicleName
ORDER BY TotalSold DESC
LIMIT 1;




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