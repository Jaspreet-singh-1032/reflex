"""Common rx.State subclasses for use in tests."""
import reflex as rx

from .mutation import DictMutationTestState, ListMutationTestState, MutableTestState
from .upload import (
    ChildFileUploadState,
    FileStateBase1,
    FileUploadState,
    GrandChildFileUploadState,
    SubUploadState,
    UploadState,
)


class GenState(rx.State):
    """A state with event handlers that generate multiple updates."""

    value: int

    def go(self, c: int):
        """Increment the value c times and update each time.

        Args:
            c: The number of times to increment.

        Yields:
            After each increment.
        """
        for _ in range(c):
            self.value += 1
            yield
