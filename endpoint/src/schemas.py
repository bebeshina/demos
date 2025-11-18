from pydantic import BaseModel


class Config(BaseModel):
    embedding_model: str = "llama3.2"
    completion_model: str = "mxbai-embed-large"
    vectorstore_path: str = "vectors"


class Input(BaseModel):
    input_str: str | None = None

 # https://jonathanserrano.medium.com/deploy-a-fastapi-app-to-production-using-docker-and-aws-ecr-928e17312445
 # need to create ec2, connect to ecr
 # https://fastapi.tiangolo.com/tutorial/body/
 # https://www.datacamp.com/tutorial/serving-an-llm-application-as-an-api-endpoint-using-fastapi-in-python




