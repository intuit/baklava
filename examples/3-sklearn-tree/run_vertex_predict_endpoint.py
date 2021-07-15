
from typing import Dict, Optional, Sequence, Tuple

from google.cloud import aiplatform

def create_endpoint(
    project: str,
    instance: str,
    model: str,
    job_name: str,
    service_account: str,
    region: str
):
    aiplatform.init(project=project, location=region)

    # create model
    # container_image="gcr.io/spry-firefly-317822/predict-image",

    endpoint = aiplatform.Endpoint.create(
        display_name=job_name, project=project, location=region,
    )
    model_uri = f'{model}'
    print(f'model_uri: {model_uri}')
    model_object = aiplatform.Model(model_uri)

    endpoint.deploy(
        model=model_object,
        deployed_model_display_name = f'{job_name}-{model}',
        machine_type = instance,
        service_account = service_account

    )

print(create_endpoint(
    region='us-central1',
    instance="n1-standard-4",
    project="spry-firefly-317822", 
    job_name="sk_learn_example",
    model='5101602011485306880',
    service_account='alex-mbp@spry-firefly-317822.iam.gserviceaccount.com'
))