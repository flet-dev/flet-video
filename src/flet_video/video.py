import asyncio
from dataclasses import field
from typing import List, Optional

import flet as ft

from .types import (
    PlaylistMode,
    VideoConfiguration,
    VideoMedia,
    VideoSubtitleConfiguration,
)

__all__ = ["Video"]


@ft.control("Video")
class Video(ft.ConstrainedControl):
    """
    A control that displays a video from a playlist.

    -----

    Online docs: https://flet.dev/docs/controls/video
    """

    playlist: List[VideoMedia] = field(default_factory=list)
    title: str = "Flet Video"
    fit: ft.BoxFit = ft.BoxFit.CONTAIN
    fill_color: ft.ColorValue = ft.Colors.BLACK
    wakelock: bool = True
    autoplay: bool = False
    show_controls: bool = True
    muted: bool = False
    playlist_mode: Optional[PlaylistMode] = None
    shuffle_playlist: Optional[bool] = None
    volume: ft.OptionalNumber = None
    playback_rate: ft.OptionalNumber = None
    alignment: ft.Alignment = field(default_factory=lambda: ft.Alignment.center())
    filter_quality: ft.FilterQuality = ft.FilterQuality.LOW
    pause_upon_entering_background_mode: bool = True
    resume_upon_entering_foreground_mode: bool = False
    aspect_ratio: ft.OptionalNumber = None
    pitch: ft.OptionalNumber = None
    configuration: VideoConfiguration = field(default_factory=VideoConfiguration)
    subtitle_configuration: VideoSubtitleConfiguration = field(
        default_factory=VideoSubtitleConfiguration
    )
    on_loaded: ft.OptionalControlEventCallable = None
    on_enter_fullscreen: ft.OptionalControlEventCallable = None
    on_exit_fullscreen: ft.OptionalControlEventCallable = None
    on_error: ft.OptionalControlEventCallable = None
    on_completed: ft.OptionalControlEventCallable = None
    on_track_changed: ft.OptionalControlEventCallable = None

    def play(self):
        asyncio.create_task(self.play_async())

    def play_async(self):
        return self._invoke_method_async("play")

    def pause(self):
        asyncio.create_task(self.pause_async())

    def pause_async(self):
        return self._invoke_method_async("pause")

    def play_or_pause(self):
        asyncio.create_task(self.play_or_pause_async())

    def play_or_pause_async(self):
        return self._invoke_method_async("play_or_pause")

    def stop(self):
        asyncio.create_task(self.stop_async())

    def stop_async(self):
        return self._invoke_method_async("stop")

    def next(self):
        asyncio.create_task(self.next_async())

    def next_async(self):
        return self._invoke_method_async("next")

    def previous(self):
        asyncio.create_task(self.previous_async())

    def previous_async(self):
        return self._invoke_method_async("previous")

    def seek(self, position: ft.DurationValue):
        asyncio.create_task(self.seek_async(position))

    def seek_async(self, position: ft.DurationValue):
        return self._invoke_method_async("seek", {"position": position})

    def jump_to(self, media_index: int):
        asyncio.create_task(self.jump_to_async(media_index))

    async def jump_to_async(self, media_index: int):
        assert self.playlist[media_index], "media_index is out of range"
        if media_index < 0:
            # dart doesn't support negative indexes
            media_index = len(self.playlist) + media_index
        await self._invoke_method_async("jump_to", {"media_index": media_index})

    def playlist_add(self, media: VideoMedia):
        asyncio.create_task(self.playlist_add_async(media))

    async def playlist_add_async(self, media: VideoMedia):
        assert media.resource, "media has no resource"
        await self._invoke_method_async("playlist_add", {"media": media})
        self.playlist.append(media)

    def playlist_remove(self, media_index: int):
        asyncio.create_task(self.playlist_remove_async(media_index))

    async def playlist_remove_async(self, media_index: int):
        assert self.playlist[media_index], "index out of range"
        await self._invoke_method_async(
            "playlist_remove", {"media_index": str(media_index)}
        )
        self.playlist.pop(media_index)

    async def is_playing_async(self) -> bool:
        return await self._invoke_method_async("is_playing")

    async def is_completed_async(self) -> bool:
        return await self._invoke_method_async("is_completed")

    async def get_duration_async(self) -> Optional[int]:
        return await self._invoke_method_async("get_duration")

    async def get_current_position_async(self) -> Optional[int]:
        return await self._invoke_method_async("get_current_position")
