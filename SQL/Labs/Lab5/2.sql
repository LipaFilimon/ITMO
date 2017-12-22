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


--2)	Получить данные о людях (ФИО), которые работают на нескольких поставщиков 
--156 – это полная таблица Purchasing .VendorID , при этом на 1 ContactID приходится 1 VendorID