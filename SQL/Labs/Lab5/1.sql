SELECT EmployeeID
FROM HumanResources.Employee
Where BirthDate > ANY
(Select BirthDate
FROM HumanResources.Employee
WHERE ContactID IN
(Select ContactID
FROM Person.Contact
Where AdditionalContactInfo IS  NULL)) 


--1)	�������� ������ ����������� (����������������� �����), ������� ������, 
--��� �����-���� ���������, �� ���������� � ���� ���������� ���������� 
--(�� ��������� ����������� ������)

--SELECT EmployeeID
--FROM HumanResources.Employee
--WHERE BirthDate > ANY (
--  SELECT BirthDate
--  FROM HumanResources.Employee
--  WHERE ContactID IN (
--    SELECT ContactID
--    FROM Person.Contact
--    WHERE Phone IS NULL AND EmailAddress IS NULL
--  )
--)