from unittest.mock import Mock

database=Mock()

database.getUser.return_value="Barani"

print(

database.getUser()

)