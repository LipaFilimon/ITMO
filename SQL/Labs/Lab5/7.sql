SELECT ProductID
FROM Production.Product
WHERE Style NOT IN (
  SELECT Style
  FROM Production.Product
  WHERE ProductSubcategoryID = 1
)

--Select ProductID
--FROM Production.Product
--WHERE Style <> ALL
--(SELECT Style
--FROM Production.Product
--WHERE ProductSubcategoryID=1)

--7)�������� ID ���������, ����� ������� �� ��������� � ������������ 1
--��� �������, ��� ����� ������� �� = 1 � ������� 1
--7 �����
