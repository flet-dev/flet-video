import 'dart:convert';
import 'dart:io';

import 'package:collection/collection.dart';
import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:media_kit/media_kit.dart';
import 'package:media_kit_video/media_kit_video.dart';

Media? parseVideoMedia(dynamic value, [Media? defaultValue]) {
  if (value == null) return defaultValue;
  if (value["resource"] != null) {
    var extras = value["extras"] != null
        ? (value["extras"] as Map)
            .map((key, value) => MapEntry(key.toString(), value.toString()))
        : null;
    var httpHeaders = value["http_headers"] != null
        ? (value["http_headers"] as Map)
            .map((key, value) => MapEntry(key.toString(), value.toString()))
        : null;
    return Media(value["resource"], extras: extras, httpHeaders: httpHeaders);
  }
  return defaultValue;
}

List<Media>? parseVideoMedias(dynamic value, [List<Media>? defaultValue]) {
  if (value == null) return defaultValue;

  List<Media> m = [];
  if (value is List) {
    m = value.map((e) => parseVideoMedia(e)).nonNulls.toList();
  } else {
    if (parseVideoMedia(value) != null) {
      m.add(parseVideoMedia(value)!);
    }
  }
  return m;
}

Map<String, dynamic>? parseSubtitleConfiguration(dynamic value, ThemeData theme,
    [Map<String, dynamic>? defaultValue]) {
  if (value == null) return defaultValue;

  SubtitleViewConfiguration configuration = SubtitleViewConfiguration(
    style: parseTextStyle(
        value["text_style"],
        theme,
        const TextStyle(
            height: 1.4,
            fontSize: 32.0,
            letterSpacing: 0.0,
            wordSpacing: 0.0,
            color: Color(0xffffffff),
            fontWeight: FontWeight.normal,
            backgroundColor: Color(0xaa000000)))!,
    visible: parseBool(value["visible"], true)!,
    textScaleFactor: parseDouble(value["text_scale_factor"]),
    textAlign: parseTextAlign(value["text_align"], TextAlign.center)!,
    padding: parsePadding(
        value["padding"], const EdgeInsets.fromLTRB(16.0, 0.0, 16.0, 24.0))!,
  );

  return <String, dynamic>{
    "src": value["src"],
    "title": value["title"],
    "language": value["language"],
    "subtitleViewConfiguration": configuration
  };
}

SubtitleTrack parseSubtitleTrack(
    AssetSrc assetSrc, String? title, String? language) {
  if (assetSrc.isFile) {
    String filePath = assetSrc.path;
    File file = File(filePath);
    String content = file.readAsStringSync();
    return SubtitleTrack.data(content, title: title, language: language);
  } else {
    return SubtitleTrack.uri(assetSrc.path, title: title, language: language);
  }
}

VideoControllerConfiguration? parseControllerConfiguration(dynamic value,
    [VideoControllerConfiguration? defaultValue]) {
  if (value == null) return defaultValue;
  return VideoControllerConfiguration(
    vo: value["output_driver"],
    hwdec: value["hardware_decoding_api"],
    enableHardwareAcceleration:
        parseBool(value["enable_hardware_acceleration"], true)!,
    width: value["width"],
    height: value["height"],
    scale: value["scale"],
  );
}

PlaylistMode? parsePlaylistMode(String? value, [PlaylistMode? defaultValue]) {
  if (value == null) return defaultValue;
  return PlaylistMode.values.firstWhereOrNull(
          (e) => e.name.toLowerCase() == value.toLowerCase()) ??
      defaultValue;
}
