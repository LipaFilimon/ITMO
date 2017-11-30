SELECT Person.Contact.LastName, Person.Contact.MiddleName, Person.Contact.FirstName, 
       Person.Contact.Phone
FROM Person.Contact LEFT OUTER JOIN Purchasing.VendorContact
ON Person.Contact.ContactID=Purchasing.VendorContact.ContactID INNER JOIN Purchasing.Vendor
ON Purchasing.VendorContact.VendorID=Purchasing.Vendor.VendorID LEFT OUTER JOIN Purchasing.ProductVendor
ON Purchasing.Vendor.VendorID=Purchasing.ProductVendor.VendorID INNER JOIN Production.Product
ON Purchasing.ProductVendor.ProductID=Production.Product.ProductID
WHERE Production.Product.ProductLine = 'T' AND Person.Contact.Phone LIKE '439%'