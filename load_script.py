source_schema = [ {'name':'objectid','type':'integer','mode':'required'},{'name':'story_id','type':'integer'},{'name':'parent_id','type':'integer'},{'name':'comment_text','type':'string'},{'name':'num_points','type':'integer'},{'name':'author','type':'string'},{'name':'created_at','type':'integer'} ]
project_id = 'hn-comments'
dataset_id = hn

job_data = {
        'jobReference': {
            'projectId': 'hn-comments',
            'job_id': str(uuid.uuid4())
        },
        'configuration': {
            'load': {
                'sourceUris': 'gs://comments_bucket/2015comments.csv',
                'schema': {
                    'fields': source_schema
                },
                'destinationTable': {
                    'projectId': project_id,
                    'datasetId': dataset_id,
                    'tableId': table_name
                }
            }
        }
    }

return bigquery.jobs().insert(
    projectId=project_id,
    body=job_data).execute(num_retries=num_retries)