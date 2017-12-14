SELECT 
       'Customer' AS Type,
	   CustomerID AS ID
FROM
       Sales.CustomerAddress AS CustomerAddress
JOIN
       Person.Address AS Address1
ON
       CustomerAddress.AddressID=Address1.AddressID
WHERE
       Address1.City = 'New York'

UNION

SELECT 
       'Vendor' AS Type,
	   VendorID AS ID
FROM
       Purchasing.VendorAddress AS VendorAddress
JOIN
       Person.Address AS Address2
ON
       VendorAddress.AddressID=Address2.AddressID
WHERE
       Address2.City = 'New York'