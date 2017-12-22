Select Name, AccountNumber
FROM Purchasing.Vendor
WHERE VendorID IN
(SELECT VendorID
FROM Purchasing.ProductVendor
WHERE ProductID IN 
(Select ProductID FROM Production.Product
WHERE Name='Minipump'));


--1 строка International Track Center (844, 65)
--3)	Получить названия и номер учётной записи поставщика, 
--который поставляет товар Minipump (не используя объединения таблиц)