# generated by datamodel-codegen:
#   filename:  schema.yaml
#   timestamp: 2023-06-05T20:38:01+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import (
    AnyUrl,
    BaseModel,
    EmailStr,
    Extra,
    Field,
    PositiveFloat,
    conint,
    conlist,
    constr,
)
from typing_extensions import Literal


class Reference(BaseModel):
    __root__: Dict[constr(regex=r"^\$ref$"), str]


class Contact(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None
    email: Optional[EmailStr] = None


class License(BaseModel):
    name: str
    url: Optional[str] = None


class ServerVariable(BaseModel):
    enum: Optional[List[str]] = None
    default: str
    description: Optional[str] = None


class Type(Enum):
    array = "array"
    boolean = "boolean"
    integer = "integer"
    number = "number"
    object = "object"
    string = "string"


class Discriminator(BaseModel):
    propertyName: str
    mapping: Optional[Dict[str, str]] = None


class XML(BaseModel):
    name: Optional[str] = None
    namespace: Optional[AnyUrl] = None
    prefix: Optional[str] = None
    attribute: bool = False
    wrapped: bool = False


class Example(BaseModel):
    summary: Optional[str] = None
    description: Optional[str] = None
    value: Optional[Any] = None
    externalValue: Optional[str] = None


class SecurityRequirement(BaseModel):
    __root__: Optional[Dict[str, List[str]]] = None


class ExternalDocumentation(BaseModel):
    description: Optional[str] = None
    url: str


class ExampleXORExamples(BaseModel):
    __root__: Any = Field(
        ..., description="Example and examples are mutually exclusive"
    )


class SchemaXORContentItem(BaseModel):
    pass


class SchemaXORContent(BaseModel):
    __root__: Union[Any, SchemaXORContentItem] = Field(
        ...,
        description="Schema and content are mutually exclusive, at least one is required",
    )


class Style(Enum):
    matrix = "matrix"
    label = "label"
    simple = "simple"


class ParameterLocationItem(BaseModel):
    in_: Optional[Literal["path"]] = Field(None, alias="in")
    style: Style = "simple"
    required: Literal[True]


class Style1(Enum):
    form = "form"
    spaceDelimited = "spaceDelimited"
    pipeDelimited = "pipeDelimited"
    deepObject = "deepObject"


class ParameterLocationItem1(BaseModel):
    in_: Optional[Literal["query"]] = Field(None, alias="in")
    style: Style1 = "form"


class ParameterLocationItem2(BaseModel):
    in_: Optional[Literal["header"]] = Field(None, alias="in")
    style: Literal["simple"] = "simple"


class ParameterLocationItem3(BaseModel):
    in_: Optional[Literal["cookie"]] = Field(None, alias="in")
    style: Literal["form"] = "form"


class ParameterLocation(BaseModel):
    __root__: Union[
        ParameterLocationItem,
        ParameterLocationItem1,
        ParameterLocationItem2,
        ParameterLocationItem3,
    ] = Field(..., description="Parameter location")


class In(Enum):
    header = "header"
    query = "query"
    cookie = "cookie"


class APIKeySecurityScheme(BaseModel):
    type: Literal["apiKey"]
    name: str
    in_: In = Field(..., alias="in")
    description: Optional[str] = None


class HTTPSecuritySchemeItem(BaseModel):
    scheme: Optional[constr(regex=r"^[Bb][Ee][Aa][Rr][Ee][Rr]$")] = None


class HTTPSecuritySchemeItem1(BaseModel):
    scheme: Optional[Any] = None


class HTTPSecurityScheme1(HTTPSecuritySchemeItem):
    scheme: str
    bearerFormat: Optional[str] = None
    description: Optional[str] = None
    type: Literal["http"]


class HTTPSecurityScheme2(HTTPSecuritySchemeItem1):
    scheme: str
    bearerFormat: Optional[str] = None
    description: Optional[str] = None
    type: Literal["http"]


class HTTPSecurityScheme(BaseModel):
    __root__: Union[HTTPSecurityScheme1, HTTPSecurityScheme2]


class OpenIdConnectSecurityScheme(BaseModel):
    type: Literal["openIdConnect"]
    openIdConnectUrl: str
    description: Optional[str] = None


class ImplicitOAuthFlow(BaseModel):
    authorizationUrl: str
    refreshUrl: Optional[str] = None
    scopes: Dict[str, str]


class PasswordOAuthFlow(BaseModel):
    tokenUrl: str
    refreshUrl: Optional[str] = None
    scopes: Dict[str, str]


class ClientCredentialsFlow(BaseModel):
    tokenUrl: str
    refreshUrl: Optional[str] = None
    scopes: Dict[str, str]


class AuthorizationCodeOAuthFlow(BaseModel):
    authorizationUrl: str
    tokenUrl: str
    refreshUrl: Optional[str] = None
    scopes: Dict[str, str]


class Callback(BaseModel):
    __root__: Dict[constr(regex=r"^x-"), Any]


class Info(BaseModel):
    title: str
    description: Optional[str] = None
    termsOfService: Optional[str] = None
    contact: Optional[Contact] = None
    license: Optional[License] = None
    version: str


class Server(BaseModel):
    url: str
    description: Optional[str] = None
    variables: Optional[Dict[str, ServerVariable]] = None


class Schema(BaseModel):
    title: Optional[str] = None
    multipleOf: Optional[PositiveFloat] = None
    maximum: Optional[float] = None
    exclusiveMaximum: bool = False
    minimum: Optional[float] = None
    exclusiveMinimum: bool = False
    maxLength: Optional[conint(ge=0)] = None
    minLength: conint(ge=0) = 0
    pattern: Optional[str] = None
    maxItems: Optional[conint(ge=0)] = None
    minItems: conint(ge=0) = 0
    uniqueItems: bool = False
    maxProperties: Optional[conint(ge=0)] = None
    minProperties: conint(ge=0) = 0
    required: Optional[List[str]] = Field(None, min_items=1, unique_items=True)
    enum: Optional[List] = Field(None, min_items=1, unique_items=False)
    type: Optional[Type] = None
    not_: Optional[Union[Schema, Reference]] = Field(None, alias="not")
    allOf: Optional[List[Union[Schema, Reference]]] = None
    oneOf: Optional[List[Union[Schema, Reference]]] = None
    anyOf: Optional[List[Union[Schema, Reference]]] = None
    items: Optional[Union[Schema, Reference]] = None
    properties: Optional[Dict[str, Union[Schema, Reference]]] = None
    additionalProperties: Union[Schema, Reference, bool] = True
    description: Optional[str] = None
    format: Optional[str] = None
    default: Optional[Any] = None
    nullable: bool = False
    discriminator: Optional[Discriminator] = None
    readOnly: bool = False
    writeOnly: bool = False
    example: Optional[Any] = None
    externalDocs: Optional[ExternalDocumentation] = None
    deprecated: bool = False
    xml: Optional[XML] = None


class Tag(BaseModel):
    name: str
    description: Optional[str] = None
    externalDocs: Optional[ExternalDocumentation] = None


class OAuthFlows(BaseModel):
    implicit: Optional[ImplicitOAuthFlow] = None
    password: Optional[PasswordOAuthFlow] = None
    clientCredentials: Optional[ClientCredentialsFlow] = None
    authorizationCode: Optional[AuthorizationCodeOAuthFlow] = None


class Link(BaseModel):
    operationId: Optional[str] = None
    operationRef: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None
    requestBody: Optional[Any] = None
    description: Optional[str] = None
    server: Optional[Server] = None


class OAuth2SecurityScheme(BaseModel):
    type: Literal["oauth2"]
    flows: OAuthFlows
    description: Optional[str] = None


class SecurityScheme(BaseModel):
    __root__: Union[
        APIKeySecurityScheme,
        HTTPSecurityScheme,
        OAuth2SecurityScheme,
        OpenIdConnectSecurityScheme,
    ]


class Model(BaseModel):
    openapi: constr(regex=r"^3\.0\.\d(-.+)?$")
    info: Info
    externalDocs: Optional[ExternalDocumentation] = None
    servers: Optional[List[Server]] = None
    security: Optional[List[SecurityRequirement]] = None
    tags: Optional[List[Tag]] = Field(None, unique_items=True)
    paths: Paths
    components: Optional[Components] = None


class Components(BaseModel):
    schemas: Optional[
        Dict[constr(regex=r"^[a-zA-Z0-9\.\-_]+$"), Union[Schema, Reference]]
    ] = None
    responses: Optional[
        Dict[constr(regex=r"^[a-zA-Z0-9\.\-_]+$"), Union[Reference, Response]]
    ] = None
    parameters: Optional[
        Dict[constr(regex=r"^[a-zA-Z0-9\.\-_]+$"), Union[Reference, Parameter]]
    ] = None
    examples: Optional[
        Dict[constr(regex=r"^[a-zA-Z0-9\.\-_]+$"), Union[Reference, Example]]
    ] = None
    requestBodies: Optional[
        Dict[constr(regex=r"^[a-zA-Z0-9\.\-_]+$"), Union[Reference, RequestBody]]
    ] = None
    headers: Optional[
        Dict[constr(regex=r"^[a-zA-Z0-9\.\-_]+$"), Union[Reference, Header]]
    ] = None
    securitySchemes: Optional[
        Dict[constr(regex=r"^[a-zA-Z0-9\.\-_]+$"), Union[Reference, SecurityScheme]]
    ] = None
    links: Optional[
        Dict[constr(regex=r"^[a-zA-Z0-9\.\-_]+$"), Union[Reference, Link]]
    ] = None
    callbacks: Optional[
        Dict[constr(regex=r"^[a-zA-Z0-9\.\-_]+$"), Union[Reference, Callback]]
    ] = None


class Response(BaseModel):
    description: str
    headers: Optional[Dict[str, Union[Header, Reference]]] = None
    content: Optional[Dict[str, MediaType]] = None
    links: Optional[Dict[str, Union[Link, Reference]]] = None


class MediaType(BaseModel):
    schema_: Optional[Union[Schema, Reference]] = Field(None, alias="schema")
    example: Optional[Any] = None
    examples: Optional[Dict[str, Union[Example, Reference]]] = None
    encoding: Optional[Dict[str, Encoding]] = None


class Header(BaseModel):
    description: Optional[str] = None
    required: bool = False
    deprecated: bool = False
    allowEmptyValue: bool = False
    style: Literal["simple"] = "simple"
    explode: Optional[bool] = None
    allowReserved: bool = False
    schema_: Optional[Union[Schema, Reference]] = Field(None, alias="schema")
    content: Optional[Dict[str, MediaType]] = None
    example: Optional[Any] = None
    examples: Optional[Dict[str, Union[Example, Reference]]] = None


class Paths(BaseModel):
    __root__: Union[
        Dict[constr(regex=r"^\/"), PathItem], Dict[constr(regex=r"^x-"), Any]
    ]


class PathItem(BaseModel):
    field_ref: Optional[str] = Field(None, alias="$ref")
    summary: Optional[str] = None
    description: Optional[str] = None
    get: Optional[Operation] = None
    put: Optional[Operation] = None
    post: Optional[Operation] = None
    delete: Optional[Operation] = None
    options: Optional[Operation] = None
    head: Optional[Operation] = None
    patch: Optional[Operation] = None
    trace: Optional[Operation] = None
    servers: Optional[List[Server]] = None
    parameters: Optional[
        conlist(Union[Parameter, Reference], unique_items=True)
    ] = Field(None)


class Operation(BaseModel):
    tags: Optional[List[str]] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    externalDocs: Optional[ExternalDocumentation] = None
    operationId: Optional[str] = None
    parameters: Optional[
        conlist(Union[Parameter, Reference], unique_items=True)
    ] = Field(None)
    requestBody: Optional[Union[RequestBody, Reference]] = None
    responses: Responses
    callbacks: Optional[Dict[str, Union[Callback, Reference]]] = None
    deprecated: bool = False
    security: Optional[List[SecurityRequirement]] = None
    servers: Optional[List[Server]] = None


class Responses(BaseModel):
    default: Optional[Union[Response, Reference]] = None


class Parameter(BaseModel):
    name: str
    in_: str = Field(..., alias="in")
    description: Optional[str] = None
    required: bool = False
    deprecated: bool = False
    allowEmptyValue: bool = False
    style: Optional[str] = None
    explode: Optional[bool] = None
    allowReserved: bool = False
    schema_: Optional[Union[Schema, Reference]] = Field(None, alias="schema")
    content: Optional[Dict[str, MediaType]] = None
    example: Optional[Any] = None
    examples: Optional[Dict[str, Union[Example, Reference]]] = None


class RequestBody(BaseModel):
    description: Optional[str] = None
    content: Dict[str, MediaType]
    required: bool = False


class Encoding(BaseModel):
    contentType: Optional[str] = None
    headers: Optional[Dict[str, Union[Header, Reference]]] = None
    style: Optional[Style1] = "form"
    explode: Optional[bool] = None
    allowReserved: bool = False


Schema.update_forward_refs()
Model.update_forward_refs()
Components.update_forward_refs()
Response.update_forward_refs()
MediaType.update_forward_refs()
Paths.update_forward_refs()
PathItem.update_forward_refs()
Operation.update_forward_refs()
