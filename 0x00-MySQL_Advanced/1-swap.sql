UPDATE users
SET 
    name = @temp := name,
    name = email,
    email = @temp;