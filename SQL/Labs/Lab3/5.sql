SELECT Purchasing.Vendor.Name, COUNT(Person.Contact.LastName)
FROM Person.Contact LEFT OUTER JOIN Purchasing.VendorContact
ON Person.Contact.ContactID=Purchasing.VendorContact.ContactID INNER JOIN Purchasing.Vendor
ON Purchasing.VendorContact.VendorID=Purchasing.Vendor.VendorID
WHERE Purchasing.Vendor.AccountNumber <> 'NULL'
GROUP BY Purchasing.Vendor.Name