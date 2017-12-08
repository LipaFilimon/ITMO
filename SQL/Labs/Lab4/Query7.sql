SELECT 
        FirstCustomer.CustomerID AS FirstCustomerID,
		SecondCustomer.CustomerID AS SecondCustomer,
		FirstAddress.City 
From 
        Sales.CustomerAddress AS FirstCustomer
JOIN 
		Sales.CustomerAddress AS SecondCustomer
ON
		FirstCustomer.CustomerID <> SecondCustomer.CustomerID
JOIN
        Person.Address AS FirstAddress
ON
        FirstAddress.AddressID = FirstCustomer.AddressID
JOIN
        Person.Address AS SecondAddress
ON
        SecondAddress.AddressID = SecondCustomer.AddressID
WHERE 
        FirstAddress.City = SecondAddress.City