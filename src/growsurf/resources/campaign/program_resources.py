# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.campaign.program_resource import ProgramResource
from ...types.campaign.program_resource_list_response import ProgramResourceListResponse
from ...types.campaign.program_resource_upload_result import ProgramResourceUploadResult
from ...types.campaign.program_resource_upload_ticket import ProgramResourceUploadTicket
from ...types.campaign.delete_program_resource_response import DeleteProgramResourceResponse

__all__ = ["ProgramResourcesResource", "AsyncProgramResourcesResource"]


def _body(**values: object) -> Dict[str, object]:
    return {key: value for key, value in values.items() if value is not omit}


def _validate_program_resource_write(values: Dict[str, object], *, creating: bool) -> None:
    """Reject Resource field combinations excluded by the public REST contract."""
    if not creating and not values:
        raise ValueError("Program Resource update requires at least one field")

    if "position" in values:
        position = values["position"]
        if isinstance(position, bool) or not isinstance(position, int) or position < 0 or position > 99:
            raise ValueError("Program Resource position must be an integer from 0 through 99")

    has_upload_ticket = "uploadTicket" in values
    has_upload_result = "uploadResult" in values
    if has_upload_ticket != has_upload_result:
        raise ValueError("`upload_ticket` and `upload_result` must be supplied together")

    supplied_content_types: list[str] = []
    if "url" in values:
        supplied_content_types.append("LINK")
    if "text" in values:
        supplied_content_types.append("TEXT")
    if has_upload_ticket:
        supplied_content_types.append("FILE")
    if len(supplied_content_types) > 1:
        raise ValueError("Send content fields for only one Program Resource type")

    resource_type = values.get("type")
    if supplied_content_types and resource_type is not None and supplied_content_types[0] != resource_type:
        raise ValueError("Content fields must match the selected Program Resource type")
    if creating and (not supplied_content_types or supplied_content_types[0] != resource_type):
        raise ValueError("Create requires the content fields for the selected Program Resource type")


def _validate_program_resource_upload_ticket(file_name: str) -> None:
    """Reject file names outside the public upload-ticket contract."""
    if len(file_name) < 1 or len(file_name) > 120:
        raise ValueError("Program Resource file_name must contain 1 through 120 characters")


class ProgramResourcesResource(SyncAPIResource):
    """Program Resources configuration and secure FILE upload operations."""

    @cached_property
    def with_raw_response(self) -> ProgramResourcesResourceWithRawResponse:
        return ProgramResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProgramResourcesResourceWithStreamingResponse:
        return ProgramResourcesResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProgramResourceListResponse:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/campaign/{id}/resources", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProgramResourceListResponse,
        )

    def create(
        self,
        id: str,
        *,
        type: Literal["FILE", "LINK", "TEXT"],
        title: str,
        description: Optional[str] | Omit = omit,
        category: Optional[str] | Omit = omit,
        is_published: bool | Omit = omit,
        url: str | Omit = omit,
        text: str | Omit = omit,
        upload_ticket: str | Omit = omit,
        upload_result: ProgramResourceUploadResult | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProgramResource:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        body = _body(
            type=type,
            title=title,
            description=description,
            category=category,
            isPublished=is_published,
            url=url,
            text=text,
            uploadTicket=upload_ticket,
            uploadResult=upload_result,
        )
        _validate_program_resource_write(body, creating=True)
        return self._post(
            path_template("/campaign/{id}/resources", id=id),
            body=body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProgramResource,
        )

    def update(
        self,
        resource_id: str,
        *,
        id: str,
        type: Literal["FILE", "LINK", "TEXT"] | Omit = omit,
        title: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        category: Optional[str] | Omit = omit,
        is_published: bool | Omit = omit,
        position: int | Omit = omit,
        url: str | Omit = omit,
        text: str | Omit = omit,
        upload_ticket: str | Omit = omit,
        upload_result: ProgramResourceUploadResult | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProgramResource:
        if not id or not resource_id:
            raise ValueError("Expected non-empty `id` and `resource_id` values")
        body = _body(
            type=type,
            title=title,
            description=description,
            category=category,
            isPublished=is_published,
            position=position,
            url=url,
            text=text,
            uploadTicket=upload_ticket,
            uploadResult=upload_result,
        )
        _validate_program_resource_write(body, creating=False)
        return self._patch(
            path_template("/campaign/{id}/resources/{resource_id}", id=id, resource_id=resource_id),
            body=body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProgramResource,
        )

    def delete(
        self,
        resource_id: str,
        *,
        id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteProgramResourceResponse:
        if not id or not resource_id:
            raise ValueError("Expected non-empty `id` and `resource_id` values")
        return self._delete(
            path_template("/campaign/{id}/resources/{resource_id}", id=id, resource_id=resource_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteProgramResourceResponse,
        )

    def create_upload_ticket(
        self,
        id: str,
        *,
        file_name: str,
        mime_type: str,
        bytes: int,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProgramResourceUploadTicket:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        _validate_program_resource_upload_ticket(file_name)
        return self._post(
            path_template("/campaign/{id}/resource-upload-tickets", id=id),
            body={"fileName": file_name, "mimeType": mime_type, "bytes": bytes},
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProgramResourceUploadTicket,
        )


class AsyncProgramResourcesResource(AsyncAPIResource):
    """Program Resources configuration and secure FILE upload operations."""

    @cached_property
    def with_raw_response(self) -> AsyncProgramResourcesResourceWithRawResponse:
        return AsyncProgramResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProgramResourcesResourceWithStreamingResponse:
        return AsyncProgramResourcesResourceWithStreamingResponse(self)

    async def list(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProgramResourceListResponse:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/campaign/{id}/resources", id=id),
            cast_to=ProgramResourceListResponse,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
        )

    async def create(
        self,
        id: str,
        *,
        type: Literal["FILE", "LINK", "TEXT"],
        title: str,
        description: Optional[str] | Omit = omit,
        category: Optional[str] | Omit = omit,
        is_published: bool | Omit = omit,
        url: str | Omit = omit,
        text: str | Omit = omit,
        upload_ticket: str | Omit = omit,
        upload_result: ProgramResourceUploadResult | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProgramResource:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        body = _body(
            type=type,
            title=title,
            description=description,
            category=category,
            isPublished=is_published,
            url=url,
            text=text,
            uploadTicket=upload_ticket,
            uploadResult=upload_result,
        )
        _validate_program_resource_write(body, creating=True)
        return await self._post(
            path_template("/campaign/{id}/resources", id=id),
            body=body,
            cast_to=ProgramResource,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
        )

    async def update(
        self,
        resource_id: str,
        *,
        id: str,
        type: Literal["FILE", "LINK", "TEXT"] | Omit = omit,
        title: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        category: Optional[str] | Omit = omit,
        is_published: bool | Omit = omit,
        position: int | Omit = omit,
        url: str | Omit = omit,
        text: str | Omit = omit,
        upload_ticket: str | Omit = omit,
        upload_result: ProgramResourceUploadResult | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProgramResource:
        if not id or not resource_id:
            raise ValueError("Expected non-empty `id` and `resource_id` values")
        body = _body(
            type=type,
            title=title,
            description=description,
            category=category,
            isPublished=is_published,
            position=position,
            url=url,
            text=text,
            uploadTicket=upload_ticket,
            uploadResult=upload_result,
        )
        _validate_program_resource_write(body, creating=False)
        return await self._patch(
            path_template("/campaign/{id}/resources/{resource_id}", id=id, resource_id=resource_id),
            body=body,
            cast_to=ProgramResource,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
        )

    async def delete(
        self,
        resource_id: str,
        *,
        id: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteProgramResourceResponse:
        if not id or not resource_id:
            raise ValueError("Expected non-empty `id` and `resource_id` values")
        return await self._delete(
            path_template("/campaign/{id}/resources/{resource_id}", id=id, resource_id=resource_id),
            cast_to=DeleteProgramResourceResponse,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
        )

    async def create_upload_ticket(
        self,
        id: str,
        *,
        file_name: str,
        mime_type: str,
        bytes: int,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProgramResourceUploadTicket:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        _validate_program_resource_upload_ticket(file_name)
        return await self._post(
            path_template("/campaign/{id}/resource-upload-tickets", id=id),
            body={"fileName": file_name, "mimeType": mime_type, "bytes": bytes},
            cast_to=ProgramResourceUploadTicket,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
        )


class ProgramResourcesResourceWithRawResponse:
    def __init__(self, resources: ProgramResourcesResource) -> None:
        self.list = to_raw_response_wrapper(resources.list)
        self.create = to_raw_response_wrapper(resources.create)
        self.update = to_raw_response_wrapper(resources.update)
        self.delete = to_raw_response_wrapper(resources.delete)
        self.create_upload_ticket = to_raw_response_wrapper(resources.create_upload_ticket)


class AsyncProgramResourcesResourceWithRawResponse:
    def __init__(self, resources: AsyncProgramResourcesResource) -> None:
        self.list = async_to_raw_response_wrapper(resources.list)
        self.create = async_to_raw_response_wrapper(resources.create)
        self.update = async_to_raw_response_wrapper(resources.update)
        self.delete = async_to_raw_response_wrapper(resources.delete)
        self.create_upload_ticket = async_to_raw_response_wrapper(resources.create_upload_ticket)


class ProgramResourcesResourceWithStreamingResponse:
    def __init__(self, resources: ProgramResourcesResource) -> None:
        self.list = to_streamed_response_wrapper(resources.list)
        self.create = to_streamed_response_wrapper(resources.create)
        self.update = to_streamed_response_wrapper(resources.update)
        self.delete = to_streamed_response_wrapper(resources.delete)
        self.create_upload_ticket = to_streamed_response_wrapper(resources.create_upload_ticket)


class AsyncProgramResourcesResourceWithStreamingResponse:
    def __init__(self, resources: AsyncProgramResourcesResource) -> None:
        self.list = async_to_streamed_response_wrapper(resources.list)
        self.create = async_to_streamed_response_wrapper(resources.create)
        self.update = async_to_streamed_response_wrapper(resources.update)
        self.delete = async_to_streamed_response_wrapper(resources.delete)
        self.create_upload_ticket = async_to_streamed_response_wrapper(resources.create_upload_ticket)
