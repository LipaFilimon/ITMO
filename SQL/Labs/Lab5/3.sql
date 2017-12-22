Select Name, AccountNumber
FROM Purchasing.Vendor
WHERE VendorID IN
(SELECT VendorID
FROM Purchasing.ProductVendor
WHERE ProductID IN 
(Select ProductID FROM Production.Product
WHERE Name='Minipump'));


--1 ������ International Track Center (844, 65)
--3)	�������� �������� � ����� ������� ������ ����������, 
--������� ���������� ����� Minipump (�� ��������� ����������� ������)