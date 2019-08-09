from .AthenaServices import AthenaClient

from ..models.StoreModel import Store
from ..models.CompanyModel import Company

# Connecting using defaul schema
athena = AthenaClient('your_access_key', 'your_secret_key', 'us-west-1', 'your_s3_staging_dir')
# Simple query string
query_string = """
    SELECT * FROM db_name.stores 
    WHERE company='{}' LIMIT 3
""".format(self.company)
stores = athena.run_query(query_string, Store, [Company,'company','name'])