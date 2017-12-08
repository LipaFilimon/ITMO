SELECT 
       FirstVendor.VendorID AS FirstVendorID,
	   SecondVendor.VendorID AS SecondVendorID,
	   FirstAddress.AddressLine1 AS Address
From 
       Purchasing.VendorAddress AS FirstVendor
JOIN 
       Purchasing.VendorAddress AS SecondVendor
ON 
       FirstVendor.VendorID <> SecondVendor.VendorID
JOIN
       Person.Address AS FirstAddress
ON
       FirstVendor.AddressID = FirstAddress.AddressID
JOIN
       Person.Address AS SecondAddress
ON
       SecondVendor.AddressID = SecondAddress.AddressID
WHERE
       FirstAddress.AddressLine1 = SecondAddress.AddressLine1