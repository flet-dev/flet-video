from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Dict

import flet as ft

__all__ = [
    "PlaylistMode",
    "VideoMedia",
    "VideoConfiguration",
    "VideoSubtitleConfiguration",
]


class PlaylistMode(Enum):
    NONE = "none"
    SINGLE = "single"
    LOOP = "loop"


@dataclass
class VideoMedia:
    resource: str
    http_headers: Optional[Dict[str, str]] = None
    extras: Optional[Dict[str, str]] = None


@dataclass
class VideoConfiguration:
    output_driver: ft.OptionalString = None
    hardware_decoding_api: ft.OptionalString = None
    enable_hardware_acceleration: bool = True
    width: ft.OptionalNumber = None
    height: ft.OptionalNumber = None
    scale: ft.OptionalNumber = None


@dataclass
class VideoSubtitleConfiguration:
    src: ft.OptionalString = None
    title: ft.OptionalString = None
    language: ft.OptionalString = None
    text_style: ft.TextStyle = field(
        default_factory=lambda: ft.TextStyle(
            height=1.4,
            size=32.0,
            letter_spacing=0.0,
            word_spacing=0.0,
            color=ft.Colors.WHITE,
            weight=ft.FontWeight.NORMAL,
            bgcolor=ft.Colors.BLACK54,
        )
    )
    text_scale_factor: ft.OptionalNumber = None
    text_align: ft.TextAlign = ft.TextAlign.CENTER
    padding: ft.PaddingValue = field(
        default_factory=lambda: ft.Padding(left=16.0, top=0.0, right=16.0, bottom=24.0)
    )
    visible: bool = True
