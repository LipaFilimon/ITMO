Select MAX (P1.DaysToManufacture), P1.ProductLine
FROM Production.Product P1
GROUP BY P1.ProductLine
HAVING MIN (P1.DaysToManufacture)<
(SELECT MAX (P2.DaysToManufacture)
FROM Production.Product P2
Where Style='U')

--10)	���������� ������������ ���������� ���� �� ������������
-- �������� �� �������� ��������� �����, ����� ��� ���� ������ 
-- ������������� ���������� ���� �� ������������ ��������� �������������� �����
--��� ������ �������
--���� ��� ������ ������� 5 �����
--����. 4
