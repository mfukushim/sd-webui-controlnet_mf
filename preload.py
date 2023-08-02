def preload(parser):
    parser.add_argument(
        "--controlnet-dir-mf",
        type=str,
        help="Path to directory with ControlNet models",
        default=None,
    )
    parser.add_argument(
        "--controlnet-annotator-models-path-mf",
        type=str,
        help="Path to directory with annotator model directories",
        default=None,
    )
    parser.add_argument(
        "--no-half-controlnet-mf",
        action="store_true",
        help="do not switch the ControlNet models to 16-bit floats (only needed without --no-half)",
        default=None,
    )
    # Setting default max_size=16 as each cache entry contains image as both key
    # and value (Very costly).
    parser.add_argument(
        "--controlnet-preprocessor-cache-size-mf",
        type=int,
        help="Cache size for controlnet preprocessor results",
        default=16,
    )
    parser.add_argument(
        "--controlnet-loglevel-mf",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)",
    )
