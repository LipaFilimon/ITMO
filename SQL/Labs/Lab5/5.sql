Select O1.CustomerID, O1.OrderDate, O1.SalesOrderID
FROM Sales.SalesOrderHeader O1
WHERE OrderDate = 
(Select MAX (OrderDate)
From Sales.SalesOrderHeader
WHERE CustomerID=O1.CustomerID)
ORDER BY O1.CustomerID, O1.SalesOrderID

--5)	���������� ��� ������� ���������� ��� ������ (ID),
-- �������������� � ���� ���������� ���������� ������, ������������� 
-- �� ������������������ ������ ����������

--19127 � ��� ���� ����������� �����
--��������� �����, ���������� ���. = 40
--��� ������ �� ��������� ���� � 103
