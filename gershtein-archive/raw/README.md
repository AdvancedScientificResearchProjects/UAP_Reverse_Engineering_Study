# `raw/` — large-binary staging (gitignored)

This directory is intentionally empty in git. The original `mp4` files (62 videos,
≈ 24 GB total) live on a separate disk:

```
/mnt/data/uap-gershtein-raw/videos/
```

Their absolute paths and `sha256` checksums are recorded in `../manifest.json`
under `files.videos`. The mirror pattern is the same one used by
`dubna-element-115-analysis/raw/` in this repo.

To re-fetch from YouTube, see `../catalog/youtube_catalog.json` for `webpage_url`
of each item; the original yt-dlp command line is preserved in
`/mnt/data/uap-gershtein-raw/scripts/download_videos.sh`.
