class Names:
    compress = "Compress"
    watermark = "Watermark"
    merge = "Merge"
    softmux = "SoftMux"
    softremux = "SoftReMux"
    convert = "Convert"
    hardmux = "Hardmux"
    aria = "Aria"
    ffmpeg = "FFMPEG"
    telethon = "Telethon"
    pyrogram = "Pyrogram"
    rclone = "Rclone"
    gensample = "VideoSample"
    STATUS = {compress: "🏮Compressing", 
                        watermark: "🛺Adding Watermark",
                        merge: "🍧Merging", 
                        softmux: "🎮SoftMuxing Subtitles", 
                        softremux: "🛩SoftReMuxing Subtitles",
                        convert: "🚜Converting Video", 
                        hardmux: "🚍HardMuxing Subtitle"}
    FFMPEG_PROCESSES = [compress, 
                                                        watermark, 
                                                        merge, 
                                                        softmux, 
                                                        softremux, 
                                                        convert, 
                                                        hardmux]
    STATUS_UPLOADING = "🔼Uploading"
    STATUS_CLONING= "🧬Cloning"
    STATUS_DOWNLOADING = "🔽Downloading"
    STATUS_COPYING= "🔁Copying"
    STATUS_ARCHIVING = "🔐Archiving"
    STATUS_EXTRACTING = "📂Extracting"
    STATUS_SPLITTING = "✂️Splitting"
    STATUS_SYNCING= "Syncing"
    STATUS_WAITING = "Queue"
    STATUS_PAUSED = "Pause"
    STATUS_CHECKING = "CheckUp"
    STATUS_SEEDING = "Seed"