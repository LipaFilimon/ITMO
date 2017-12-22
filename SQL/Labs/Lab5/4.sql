SELECT VendorID, COUNT (ProductID)
FROM Purchasing.ProductVendor
GROUP BY VendorID
HAVING COUNT (ProductID)>
(Select COUNT (ProductID)
FROM Purchasing.ProductVendor
Where MaxOrderQty IN
(Select Max (MinOrderQty)
From Purchasing.ProductVendor))

--SELECT VendorID
--FROM Purchasing.ProductVendor
--WHERE OnOrderQty > all (
--  SELECT max(MinOrderQty)
--  FROM Purchasing.ProductVendor
--)


--����� 16 �����
--4)	�������� ������ ����������� (id), ������������ ������� ������,
-- ��� ��������� � ������������ ��������� ���������� ���������� ���������
-- � ������ � ������
--//������� : min ���??? Max �����������
