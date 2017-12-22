SELECT C.FirstName, C.MiddleName, C.LastName 
FROM Person.Contact as C
WHERE C.ContactID IN
(Select VC.ContactID
FROM Purchasing.VendorContact as VC
join
Purchasing.VendorContact as VC1
ON
VC.VendorID=VC1.VendorID
Where C.ContactID=VC.ContactID)


--2)	�������� ������ � ����� (���), ������� �������� �� ���������� ����������� 
--156 � ��� ������ ������� Purchasing .VendorID , ��� ���� �� 1 ContactID ���������� 1 VendorID