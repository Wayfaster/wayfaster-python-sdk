"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import TypedDict
from wayfaster.types import BaseModel


class ReadSessionsRequestBodyTypedDict(TypedDict):
    interview_config_id: str


class ReadSessionsRequestBody(BaseModel):
    interview_config_id: str
