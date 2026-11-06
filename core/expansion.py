"""Async entry points for the private native expansion module."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ._relationship_native import ExpansionHandle as _NativeExpansionHandle

if TYPE_CHECKING:
    from aiocqhttp import CQHttp


class ExpansionHandle:
    """Keep the plugin's public coroutine interface stable."""

    @staticmethod
    async def add_group(client: CQHttp, target_gid: int, answer: str) -> str:
        """Run a native group application on the caller's event loop.

        Args:
            client: Existing asynchronous OneBot client.
            target_gid: Target group identifier.
            answer: Application answer.

        Returns:
            The application's display text.
        """
        operation = _NativeExpansionHandle.add_group(client, target_gid, answer)
        result = None
        while True:
            done, result = operation.advance(result)
            if done:
                return result
            result = await result

    @staticmethod
    async def add_friend(
        client: CQHttp,
        target_uin: int,
        self_id: int,
        verify: str = "",
        remark: str = "",
        answer: str = "",
    ) -> str:
        """Run a native friend application on the caller's event loop.

        Args:
            client: Existing asynchronous OneBot client.
            target_uin: Target user identifier.
            self_id: Current bot identifier.
            verify: Verification message.
            remark: Friend remark.
            answer: Verification answer.

        Returns:
            The application's display text.
        """
        operation = _NativeExpansionHandle.add_friend(
            client, target_uin, self_id, verify, remark, answer
        )
        result = None
        while True:
            done, result = operation.advance(result)
            if done:
                return result
            result = await result
