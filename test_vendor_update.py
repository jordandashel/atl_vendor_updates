import os
import unittest
import tempfile

import vendor_update

class VendorUpdateTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, vendor_update.app.config['DATABASE'] = tempfile.mkstemp()
        vendor_update.app.testing = True
        self.app = vendor_update.app.test_client()
        with vendor_update.app.app_context():
            vendor_update.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(vendor_update.app.config['DATABASE'])


    def test_get_response(self):
        response = self.app.get('/')
        # self.assertIsNotNone(response.text)
        assert response.status_code is 200


    def test_parse_file_contents(self):
        sample_input = """
1	Snake	Plisken	123 Fake St.	AZ	12345	new	432	Masthead	100.12	2007-04-05T14:30Z
1	Snake	Plisken	123 Fake St.	AZ	12345	canceled	432	Masthead	100.12	2007-04-06T10:30Z
2	Clark	Kent	456 Fake St.	CA	54321	new	431	Print Magazine	50.12	2007-04-07T10:30Z
3	Johnny	Johnson	789 Not Real St.	OH	45321	new	431	Print Magazine	50.12	2007-04-08T10:30Z
3	Johnny	Johnson	789 Not Real St.	OH	45321	canceled	431	Print Magazine	50.12	2007-04-08T11:30Z
"""
        records = vendor_update.parse_file_contents(sample_input)
        assert len(records) == 5
        assert records[0]["first_name"] == "Snake"
        assert int(records[4]["id"]) == 3


    def test_parse_single_record_data(self):
        sample_input = "1	Snake	Plisken	123 Fake St.	AZ	12345	new	432	Masthead	100.12	2007-04-05T14:30Z"

        data = vendor_update.parse_record_data(sample_input)
        assert "first_name" in data
        assert data["first_name"] == "Snake"
        assert all(field in data for field in ['id', 'first_name', 
            'last_name', 'street_address', 'state', 'zip_code', 
            'purchase_status', 'product_id', 'product_name', 
            'item_price', 'date_time'])



if __name__ == '__main__':
    unittest.main()
