SELECT
  SalesOrderDetail.SalesOrderID? FROM Sales.SalesOrderDetail? JOIN Sales.SalesOrderHeader ON SalesOrderDetail.SalesOrderID = SalesOrderHeader.SalesOrderID? WHERE OrderDate < ALL (? SELECT DISTINCT OrderDate? FROM Sales.SalesOrderDetail? JOIN Sales.SalesOrderHeader ON SalesOrderDetail.SalesOrderID = SalesOrderDetail.SalesOrderID? WHERE LineTotal > 20000);
 
--Select SalesOrderID
--From Sales.SalesOrderHeader
--Where OrderDate<ALL
--(Select OrderDate
--FROM
--Sales.SalesOrderHeader OH
--JOIN
--Sales.SalesOrderDetail OD
--ON
--OH.SalesOrderID=OD.SalesOrderID
--Where OD.LineTotal>20000) 

--12)�������� ������ �������, ��������� ������,
-- ��� ������ ����� � �������������� ������� �� ������� ������ 20000
--��������� �� �����, � �� ������
--����� 19460, �� 184 ����������
