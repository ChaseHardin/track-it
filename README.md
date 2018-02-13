# Track It

*A time managing micro service that provides a summary of wasted time.*

## Testing
*The testing examples are here to provide some basic documentation on testing the application. Take a look at the spec file for more examples.*

### GET Example:

**Controller**
```
@app.route('/summary', methods=['GET'])
def get_summary():
    data = [{
        'id': 1,
        'category': 'merge request'
    }]

    return jsonify(data)
```
 
**Spec**

*Verify the response and status code. Note that we have to load the object into a json object before verifying.*

```
from flask import json
from app import app
import unittest


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_summary__when_multiple_times_have_been_entered(self):
        expected_response = [{
            'id': 1,
            'category': 'merge request'
        }]

        actual_response = self.app.get('/summary')
        data = json.loads(actual_response.get_data())

        self.assertEqual(actual_response.status_code, 200)
        self.assertEqual(data, expected_response)
```
