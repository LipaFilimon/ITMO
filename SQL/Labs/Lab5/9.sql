SELECT VendorID
FROM Purchasing.Vendor
WHERE VendorID NOT IN (
  SELECT VendorID
  FROM Purchasing.ProductVendor
)

--Select VendorID
--FROM Purchasing.Vendor
--Where NOT EXISTS
--(Select *
--FROM Purchasing.ProductVendor
--WHERE VendorID=Purchasing.Vendor.VendorID)

--9)Ќайти поставщиков (ID), дл€ которых не указаны поставл€емые товары
--ответ 18 строк
