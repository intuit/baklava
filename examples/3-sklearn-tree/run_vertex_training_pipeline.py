from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value
from google.cloud.aiplatform_v1.types import InputDataConfig, GcsDestination
def create_training_job(
    container_image: str,
    instance: str,
    region: str,
    project: str,
    job_name: str,
    output_data: str,
    input_data: str
):
    client = aiplatform.gapic.PipelineServiceClient(client_options= {"api_endpoint": f"{region}-aiplatform.googleapis.com"})
    training_task_inputs_dict = {
        "workerPoolSpecs": [
            {
                "replicaCount": 1,
                "machineSpec": {"machineType": instance},
                "containerSpec": {
                    # A working docker image can be found at gs://cloud-samples-data/ai-platform/mnist_tfrecord/custom_job
                    "imageUri": container_image,
                    "env": [{"name": "sriracha_provider", "value": "gcpvertex"}
                    ],
                },
            }
        ],
        "baseOutputDirectory": {
            # The GCS location for outputs must be accessible by the project's AI Platform service account.
            "output_uri_prefix": output_data
        },
    }
    training_task_inputs = json_format.ParseDict(training_task_inputs_dict, Value())

    # Accessible at https://console.cloud.google.com/storage/browser/google-cloud-aiplatform/schema/trainingjob/definition;tab=objects?prefix=&forceOnObjectsSortingFiltering=false
    training_task_definition = "gs://google-cloud-aiplatform/schema/trainingjob/definition/custom_task_1.0.0.yaml"

    input_data_config = {
            "dataset_id": '1889198471030767616',
            "gcs_destination": {"output_uri_prefix": input_data}
        }

# when file is passed in, GCP does it's own test/valid/train data split

    training_pipeline = {
        "display_name": job_name,
        "training_task_definition": training_task_definition,
        "training_task_inputs": training_task_inputs,
        "input_data_config": input_data_config,
        # "model_to_upload": {
        #     "display_name": f"{job_name}-model",
        #     "container_spec": {"image_uri": serving_image_uri},
        # },
    }

    parent = f"projects/{project}/locations/{region}"
    response = client.create_training_pipeline(
        parent=parent, training_pipeline=training_pipeline
    )
    return response

region = 'us-central1'

aiplatform.init(
    # your Google Cloud Project ID or number
    # environment default used is not set
    project='spry-firefly-317822',

    # the Vertex AI region you will use
    # defaults to us-central1
    location='',

    # Googlge Cloud Stoage bucket in same region as location
    # used to stage artifacts
    staging_bucket='gs://vertex-staging',

    # custom google.auth.credentials.Credentials
    # environment default creds used if not set
    # credentials=my_credentials,

    # customer managed encryption key resource name
    # will be applied to all Vertex AI resources if set
    # encryption_spec_key_name=my_encryption_key_name,

    # the name of the experiment to use to track
    # logged metrics and parameters
    experiment='experiment-1',

    # description of the experiment above
    experiment_description='my experiment description'
)

print(create_training_job(
    region='us-central1',
    instance="n1-standard-4",
    project="spry-firefly-317822", 
    job_name="sk_learn_example",
    container_image="gcr.io/spry-firefly-317822/train-image",
    input_data='gs://mlctl-data/',
    output_data="gs://mlctl-model/vertex/"
))