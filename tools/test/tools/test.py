from kubiya_sdk.tools.models import Arg, Tool, ImageProvider, Auth
from kubiya_sdk.tools.registry import tool_registry


class BaseTestTool(Tool):
    def __init__(self, name: str, description: str, args: list[Arg], content: str):
        super().__init__(
            name=name,
            type="docker",
            image="michaelkubiya/registry-test:latest",  # You might want to update this to your actual image name
            image_provider=ImageProvider(
                kind="dockerhub",
                auth=[
                    Auth(name="username", value="michaelkubiya"),
                    Auth(name="password", value_from={"secret": "DOCKER_HUB_PASSWORD"})
                ],
            ),
            description=description,
            args=args,
            content=content,
            secrets=["DOCKER_HUB_PASSWORD"]
        )


# Hello World tool
hello_world = BaseTestTool(
    name="hello",
    description="Say hello to someone",
    args=[
        Arg(name="name", description="Name of the person to greet")
    ],
    content="""
python /app/main.py {name}
""",
)

# Register the tool
tool_registry.register("test", hello_world)