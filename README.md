## Djathena
###A python module based on PyAthena and Records which gives you the power to query into Athena and recieve Django objects

####How it works:
So far there are no django backends that support Athena connections, however we can connect any Python projects to it by using a beautyfull library called PyAthena.<br>But the only ORM you can use with PyAthena is SQLAlchemy (so, no Django ORM yet :pensive: )<br>What we can do with Djathena is let you still use your Django Models by making your queries using Records (which uses SQLAlchemy under the hood) and converting directly into your beloved model.
####Installation:
Soon on pip, by now just copy the file  :stuck_out_tongue_winking_eye:

####Sample usage:
Supose you have a model called `Store` and a table in Athena containing the same column names as you models attributes.

Lets get the first three lines of that table and convert our `Store`  model:

```Python
from Djathena import AthenaClient

from ..models.StoreModel import Store

# Connecting using defaul schema
athena = AthenaClient('your_access_key', 'your_secret_key', 'us-west-1', 'your_s3_staging_dir')
# Simple query string
query_string = """
    SELECT * FROM db_name.stores 
    WHERE company='{}' LIMIT 3
""".format(self.company)
# Run your query passing the model you want your lines to be converted to
stores = athena.run_query(query_string, Store)
```

####Models with foreign fields:
Now, suppose that your `Store` has a foreing field called `Company` where it's name is unique and used in Athena.
Having a Athena table like that:

####What if my columns in Athena and Django have different names?

