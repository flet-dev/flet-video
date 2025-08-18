# flet-video

[![pypi](https://img.shields.io/pypi/v/flet-video.svg)](https://pypi.python.org/pypi/flet-video)
[![downloads](https://static.pepy.tech/badge/flet-video/month)](https://pepy.tech/project/flet-video)
[![license](https://img.shields.io/github/license/flet-dev/flet-video.svg)](https://github.com/flet-dev/flet-video/blob/main/LICENSE)

A cross-platform video player for [Flet](https://flet.dev) apps.

It is based on the [media_kit](https://pub.dev/packages/media_kit) Flutter package.

## Platform Support

This package supports the following platforms:

| Platform | Supported |
|----------|:---------:|
| Windows  |     ✅     |
| macOS    |     ✅     |
| Linux    |     ✅     |
| iOS      |     ✅     |
| Android  |     ✅     |
| Web      |     ✅     |

## Usage

### Installation

To install the `flet-video` package and add it to your project dependencies:

=== "uv"
    ```bash
    uv add flet-video
    ```

=== "pip"
    ```bash
    pip install flet-video  # (1)!
    ```

    1. After this, you will have to manually add this package to your `requirements.txt` or `pyproject.toml`.

=== "poetry"
    ```bash
    poetry add flet-video
    ```

??? note "Windows Subsystem for Linux (WSL)"
    On WSL, you need to additionally install the [`libmpv`](https://github.com/mpv-player/mpv) library.

    If you receive `error while loading shared libraries: libmpv.so.1: cannot open shared object file: No such file or directory`,
    it means `libmpv` library is not installed in your WSL environment.

    To install it, run the following commands:

    ```bash
    sudo apt update
    sudo apt install libmpv-dev libmpv2
    sudo ln -s /usr/lib/x86_64-linux-gnu/libmpv.so /usr/lib/libmpv.so.1
    ```

### Examples

See [these](video.md#examples).
