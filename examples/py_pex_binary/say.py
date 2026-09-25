import cowsay
import os

cowsay.cow(os.environ.get("BAZEL_WORKSPACE"))
