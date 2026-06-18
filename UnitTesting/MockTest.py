from unittest.mock import Mock

db = Mock()

db.getData.return_value = "Success"

print(db.getData())