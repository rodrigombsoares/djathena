import records
from urllib.parse import quote_plus


class AthenaClient():


    def __init__(self, access_key, secret_key, region_name, s3_staging_dir, schema_name='default'):
        self.conn_str = 'awsathena+jdbc://{_access_key}:{_secret_key}@athena.{_region_name}.amazonaws.com:443/'\
            '{_schema_name}?s3_staging_dir={_s3_staging_dir}'
        self.db = records.Database(self.conn_str.format(
            _access_key=quote_plus(access_key),
            _secret_key=quote_plus(secret_key),
            _region_name=region_name,
            _schema_name=schema_name,
            _s3_staging_dir=quote_plus(s3_staging_dir)))
        print('\nconnected to Athena')


    def run_query(self, query, PrimaryModel, *nested_models):
        """
        Parameters: query, the model class being queried, 
        a list for each nested model containing:
            [nested model class, nested model foreing key, nested model primary key]
        """
        rows = self.db.query(query)
        print('queried \n')
        primaries = []
        
        for primary in rows:
            primary_dict = dict(primary)
            
            for nested_model in nested_models:
                nested_model = nested_models[0]

                nm_class = nested_model[0]
                nm_fk = nested_model[1]
                nm_pk = nested_model[2]
                aux_dict = {nm_pk: primary_dict[nm_fk]}

                if primary_dict[nm_fk]:
                    primary_dict[nm_fk] = nm_class.objects.get(**aux_dict)
                
            primary_object = PrimaryModel(**primary_dict)
            primaries.append(primary_object)

        return primaries