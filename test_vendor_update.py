import os
import unittest
import tempfile

import vendor_update

class VendorUpdateTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, vendor_update.app.config['DATABASE'] = tempfile.mkstemp()
        vendor_update.app.testing = True
        self.app = vendor_update.app.test_client()
        # with vendor_update.app.app_context():
        #     vendor_update.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(vendor_update.app.config['DATABASE'])


    def test_get_response(self):
        response = self.app.get('/')
        # self.assertIsNotNone(response.text)
        assert response.status_code is 200


if __name__ == '__main__':
    unittest.main()
