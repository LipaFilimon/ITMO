SELECT SalesOrderID
FROM Sales.SalesOrderHeader
WHERE OrderDate>ALL
(Select OrderDate
FROM 
Sales.SalesOrderHeader OH
JOIN
Sales.SalesOrderDetail OD
ON
OH.SalesOrderID=OD.SalesOrderID
WHERE OD.LineTotal>1000)

--11)�������� ������ �������, ��������� �����, 
--��� ��� ������ � �������������� ������� �� ������� ������ 1000
--����� 976 �����
