# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import pytest
from pydantic import ValidationError

from growsurf import Growsurf, AsyncGrowsurf
from growsurf._compat import parse_obj
from growsurf.types.campaign.program_resource import ProgramResource
from growsurf.types.campaign.program_resource_upload_ticket import ProgramResourceUploadTicket


class TestProgramResources:
    def test_resource_is_attached(self, client: Growsurf) -> None:
        assert client.campaign.resources is not None

    def test_rejects_empty_program_id(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match="Expected a non-empty value"):
            client.campaign.resources.list("")

    def test_models_use_epoch_milliseconds_and_opaque_scalar_upload_fields(self) -> None:
        resource = parse_obj(
            ProgramResource,
            {
                "id": "resource_abc123",
                "type": "TEXT",
                "title": "Launch notes",
                "description": None,
                "category": None,
                "url": None,
                "text": "Welcome to Pied Piper.",
                "file": None,
                "isPublished": False,
                "position": 0,
                "createdAt": 1767225600000,
                "updatedAt": 1767225600001,
            },
        )
        ticket = parse_obj(
            ProgramResourceUploadTicket,
            {
                "ticket": "one-time-ticket",
                "expiresIn": 600,
                "uploadUrl": "https://upload.example.com/file",
                "uploadParameters": {"signature": "signed", "timestamp": 1767225600, "overwrite": False},
            },
        )

        assert resource.created_at == 1767225600000
        assert ticket.upload_parameters == {"signature": "signed", "timestamp": 1767225600, "overwrite": False}
        assert not hasattr(ticket, "cloud_name")

        scalar_ticket = parse_obj(
            ProgramResourceUploadTicket,
            {
                "ticket": "one-time-ticket",
                "expiresIn": 600,
                "uploadUrl": "https://upload.example.com/file",
                "uploadParameters": {
                    "one": 1,
                    "zero": 0,
                    "truth": "true",
                    "digits": "123",
                    "fraction": 1.25,
                    "enabled": False,
                },
            },
        )
        assert scalar_ticket.upload_parameters == {
            "one": 1,
            "zero": 0,
            "truth": "true",
            "digits": "123",
            "fraction": 1.25,
            "enabled": False,
        }
        assert type(scalar_ticket.upload_parameters["one"]) is int
        assert type(scalar_ticket.upload_parameters["truth"]) is str
        assert type(scalar_ticket.upload_parameters["fraction"]) is float
        assert type(scalar_ticket.upload_parameters["enabled"]) is bool

        with pytest.raises(ValidationError):
            parse_obj(
                ProgramResourceUploadTicket,
                {
                    "ticket": "one-time-ticket",
                    "expiresIn": 600,
                    "uploadUrl": "https://upload.example.com/file",
                    "uploadParameters": {"nested": {"objects": "are not allowed"}},
                },
            )

    def test_resource_requires_nullable_content_fields(self) -> None:
        with pytest.raises(ValidationError):
            parse_obj(
                ProgramResource,
                {
                    "id": "resource_abc123",
                    "type": "TEXT",
                    "title": "Launch notes",
                    "category": None,
                    "url": None,
                    "text": "Welcome to Pied Piper.",
                    "file": None,
                    "isPublished": False,
                    "position": 0,
                    "createdAt": 1767225600000,
                    "updatedAt": 1767225600001,
                },
            )

    @pytest.mark.parametrize(
        "params",
        [
            {
                "type": "FILE",
                "title": "Media kit",
                "url": "https://example.com/guide",
                "upload_ticket": "one-time-ticket",
                "upload_result": {},
            },
            {
                "type": "LINK",
                "title": "Guide",
                "url": "https://example.com/guide",
                "text": "Guide",
            },
            {
                "type": "TEXT",
                "title": "Guide",
                "text": "Guide",
                "upload_ticket": "one-time-ticket",
                "upload_result": {},
            },
        ],
    )
    def test_create_rejects_cross_type_fields(self, client: Growsurf, params: dict[str, object]) -> None:
        with pytest.raises(ValueError, match="content fields"):
            client.campaign.resources.create("program-id", **params)  # type: ignore[arg-type]

    def test_update_requires_the_upload_pair(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match="must be supplied together"):
            client.campaign.resources.update(
                "resource-id",
                id="program-id",
                upload_ticket="one-time-ticket",
            )

    @pytest.mark.parametrize("resource_type", ["FILE", "LINK", "TEXT"])
    def test_update_type_requires_replacement_content(self, client: Growsurf, resource_type: str) -> None:
        with pytest.raises(ValueError, match="requires its replacement content"):
            client.campaign.resources.update(
                "resource-id",
                id="program-id",
                type=resource_type,  # type: ignore[arg-type]
            )

    def test_update_and_upload_ticket_enforce_public_bounds(self, client: Growsurf) -> None:
        with pytest.raises(ValueError, match="requires at least one field"):
            client.campaign.resources.update("resource-id", id="program-id")
        with pytest.raises(ValueError, match="position must be an integer from 0 through 99"):
            client.campaign.resources.update("resource-id", id="program-id", position=100)
        with pytest.raises(ValueError, match="file_name must contain 1 through 120 characters"):
            client.campaign.resources.create_upload_ticket(
                "program-id",
                file_name=f"{'a' * 117}.pdf",
                mime_type="application/pdf",
                bytes=42,
            )


class TestAsyncProgramResources:
    def test_resource_is_attached(self, async_client: AsyncGrowsurf) -> None:
        assert async_client.campaign.resources is not None

    @pytest.mark.asyncio
    async def test_rejects_empty_program_id(self, async_client: AsyncGrowsurf) -> None:
        with pytest.raises(ValueError, match="Expected a non-empty value"):
            await async_client.campaign.resources.list("")
