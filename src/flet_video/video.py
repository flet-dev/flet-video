import asyncio
from dataclasses import field
from typing import Optional

import flet as ft

from .types import (
    PlaylistMode,
    VideoConfiguration,
    VideoMedia,
    VideoSubtitleConfiguration,
    VideoSubtitleTrack,
)

__all__ = ["Video"]


@ft.control("Video")
class Video(ft.ConstrainedControl):
    """
    A control that displays a video from a playlist.

    Raises:
        AssertionError: If the [`volume`][(c).] is not between `0.0` and `100.0` (inclusive).
    """

    playlist: list[VideoMedia] = field(default_factory=list)
    """
    A list of `VideoMedia`s representing the video files to be played.
    """

    title: str = "flet-video"
    """
    Defines the name of the underlying window & process for native backend. 
    This is visible inside the windows' volume mixer.
    """

    fit: ft.BoxFit = ft.BoxFit.CONTAIN
    """
    The box fit to use for the video.
    """

    fill_color: ft.ColorValue = ft.Colors.BLACK
    """
    Defines the color used to fill the video background.
    """

    wakelock: bool = True
    """
    Whether to acquire wake lock while playing the video. 
    When `True`, device's display will not go to standby/sleep while the video is playing.
    """

    autoplay: bool = False
    """
    Whether the video should start playing automatically.
    """

    show_controls: bool = True
    """
    Whether to show the video player controls.
    """

    muted: bool = False
    """
    Defines whether the video player should be started in muted state.
    """

    playlist_mode: Optional[PlaylistMode] = None
    """
    Represents the mode of playback for the playlist.
    """

    shuffle_playlist: bool = False
    """
    Defines whether the playlist should be shuffled.
    """

    volume: ft.Number = 100.0
    """
    Defines the volume of the video player.
    
    Note:
        It's value ranges between `0.0` to `100.0` (inclusive), where `0.0` is muted and `100.0` is the maximum volume.
        An exception will be raised if the value is outside this range.
    """

    playback_rate: ft.Number = 1.0
    """
    Defines the playback rate of the video player.
    """

    alignment: ft.Alignment = field(default_factory=lambda: ft.Alignment.center())
    """
    Defines the Alignment of the viewport.
    """

    filter_quality: ft.FilterQuality = ft.FilterQuality.LOW
    """
    Filter quality of the texture used to render the video output.
    
    Note: 
        Android was reported to show blurry images when using `ft.FilterQuality.HIGH`. 
        Prefer the usage of `ft.FilterQuality.MEDIUM` on this platform.
    """

    pause_upon_entering_background_mode: bool = True
    """
    Whether to pause the video when application enters background mode.
    """

    resume_upon_entering_foreground_mode: bool = False
    """
    Whether to resume the video when application enters foreground mode. 
    Has effect only if `pause_upon_entering_background_mode` is also set to `True`.
    """

    pitch: ft.Number = 1.0
    """
    Defines the relative pitch of the video player.
    """

    configuration: VideoConfiguration = field(
        default_factory=lambda: VideoConfiguration()
    )
    """
    Additional configuration for the video player.
    """

    subtitle_configuration: VideoSubtitleConfiguration = field(
        default_factory=lambda: VideoSubtitleConfiguration()
    )
    """
    Defines the subtitle configuration for the video player.
    """

    subtitle_track: Optional[VideoSubtitleTrack] = None
    """
    Defines the subtitle track for the video player.
    """

    on_load: ft.OptionalControlEventHandler["Video"] = None
    """Fires when the video player is initialized and ready for playback."""

    on_enter_fullscreen: ft.OptionalControlEventHandler["Video"] = None
    """Fires when the video player enters fullscreen."""

    on_exit_fullscreen: ft.OptionalControlEventHandler["Video"] = None
    """Fires when the video player exits fullscreen"""

    on_error: ft.OptionalControlEventHandler["Video"] = None
    """
    Fires when an error occurs.
    
    Event handler argument's `data` property contains information about the error.
    """

    on_complete: ft.OptionalControlEventHandler["Video"] = None
    """Fires when a video player completes."""

    on_track_change: ft.OptionalControlEventHandler["Video"] = None
    """
    Fires when a video track changes.
    
    Event handler argument's `data` property contains the index of the new track.
    """

    def before_update(self):
        super().before_update()
        assert 0 <= self.volume <= 100, "volume must be between 0 and 100 inclusive"

    def play(self):
        """Starts playing the video."""
        asyncio.create_task(self.play_async())

    def play_async(self):
        """Starts playing the video."""
        return self._invoke_method_async("play")

    def pause(self):
        """Pauses the video player."""
        asyncio.create_task(self.pause_async())

    def pause_async(self):
        """Pauses the video player."""
        return self._invoke_method_async("pause")

    def play_or_pause(self):
        """
        Cycles between play and pause states of the video player,
        i.e., plays if paused and pauses if playing.
        """
        asyncio.create_task(self.play_or_pause_async())

    def play_or_pause_async(self):
        """
        Cycles between play and pause states of the video player,
        i.e., plays if paused and pauses if playing.
        """
        return self._invoke_method_async("play_or_pause")

    def stop(self):
        """Stops the video player."""
        asyncio.create_task(self.stop_async())

    def stop_async(self):
        """Stops the video player."""
        return self._invoke_method_async("stop")

    def next(self):
        """Jumps to the next `VideoMedia` in the `playlist`."""
        asyncio.create_task(self.next_async())

    def next_async(self):
        """Jumps to the next `VideoMedia` in the `playlist`."""
        return self._invoke_method_async("next")

    def previous(self):
        """Jumps to the previous `VideoMedia` in the `playlist`."""
        asyncio.create_task(self.previous_async())

    def previous_async(self):
        """Jumps to the previous `VideoMedia` in the `playlist`."""
        return self._invoke_method_async("previous")

    def seek(self, position: ft.DurationValue):
        """
        Seeks the currently playing `VideoMedia` from the `playlist` at the specified `position`.
        """
        asyncio.create_task(self.seek_async(position))

    def seek_async(self, position: ft.DurationValue):
        """
        Seeks the currently playing `VideoMedia` from the `playlist` at the specified `position`.
        """
        return self._invoke_method_async("seek", {"position": position})

    def jump_to(self, media_index: int):
        """
        Jumps to the `VideoMedia` at the specified `media_index` in the `playlist`.
        """
        asyncio.create_task(self.jump_to_async(media_index))

    async def jump_to_async(self, media_index: int):
        """
        Jumps to the `VideoMedia` at the specified `media_index` in the `playlist`.
        """
        assert self.playlist[media_index], "media_index is out of range"
        if media_index < 0:
            # dart doesn't support negative indexes
            media_index = len(self.playlist) + media_index
        await self._invoke_method_async("jump_to", {"media_index": media_index})

    def playlist_add(self, media: VideoMedia):
        """Appends/Adds the provided `media` to the `playlist`."""
        asyncio.create_task(self.playlist_add_async(media))

    async def playlist_add_async(self, media: VideoMedia):
        """Appends/Adds the provided `media` to the `playlist`."""
        assert media.resource, "media has no resource"
        await self._invoke_method_async("playlist_add", {"media": media})
        self.playlist.append(media)

    def playlist_remove(self, media_index: int):
        """Removes the provided `media` from the `playlist`."""
        asyncio.create_task(self.playlist_remove_async(media_index))

    async def playlist_remove_async(self, media_index: int):
        """Removes the provided `media` from the `playlist`."""
        assert self.playlist[media_index], "index out of range"
        await self._invoke_method_async("playlist_remove", {"media_index": media_index})
        self.playlist.pop(media_index)

    async def is_playing_async(self) -> bool:
        """
        Returns:
            `True` if the video player is currently playing, `False` otherwise.
        """
        return await self._invoke_method_async("is_playing")

    async def is_completed_async(self) -> bool:
        """
        Returns:
            `True` if video player has reached the end of
            the currently playing media, `False` otherwise.
        """
        return await self._invoke_method_async("is_completed")

    async def get_duration_async(self) -> ft.Duration:
        """
        Returns:
            The duration of the currently playing media.
        """
        return await self._invoke_method_async("get_duration")

    async def get_current_position_async(self) -> ft.Duration:
        """
        Returns:
            The current position of the currently playing media.
        """
        return await self._invoke_method_async("get_current_position")
