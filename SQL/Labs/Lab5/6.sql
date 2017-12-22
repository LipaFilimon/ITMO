SELECT ProductID
FROM Production.Product
WHERE Size > ANY (
  SELECT Size
  FROM Production.Product
    JOIN Purchasing.ProductVendor
      ON Product.ProductID = ProductVendor.ProductID
  WHERE ProductVendor.VendorID = 90
)

--SELECT ProductID
--FROM Production.Product
--Where Size> ANY
--(Select Size
--FROM
--Production.Product P
--JOIN 
--Purchasing.ProductVendor PV
--ON
--P.ProductID=PV.ProductID
--WHERE VendorID=95)

--6)	�������� ����������������� ������ ���������, ��� ������� ������,
-- ��� � ������ �� ���������, ������������ ����������� ID=90

--� ���� ��� ������� NULL => ����� 0 �����
--23 ������ ��� Vendor ID95
--����� select ProductionNumber � ������� ������������ 35 ���-�� ���������, �� ����� Null,
-- � �������� Null ������������� ��� �������� � ID=90
