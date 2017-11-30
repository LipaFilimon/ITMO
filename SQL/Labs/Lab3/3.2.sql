SELECT Purchasing.Vendor.Name, COUNT(Production.Product.Name)
FROM Purchasing.Vendor LEFT OUTER JOIN Purchasing.ProductVendor
ON Purchasing.Vendor.VendorID=Purchasing.ProductVendor.VendorID INNER JOIN Production.Product
ON Purchasing.ProductVendor.ProductID=Production.Product.ProductID
WHERE Production.Product.MakeFlag = '0'
GROUP BY Purchasing.Vendor.Name